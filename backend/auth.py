from datetime import datetime
from enum import Enum

from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from models import TokenEntry
from passlib.context import CryptContext


class AuthBackend:
    def __init__(self, password_context):
        self._password_context: CryptContext = password_context

    async def get_hash_for_password(self, password):
        return self._password_context.hash(password)

    async def verify_password(self, password, hashed_password):
        return self._password_context.verify(password, hashed_password)


def create_login_manager(oauth_scheme):
    class LoginManager:
        def __init__(
                self,
                secret_key,
                algorithm,
                default_expiration_interval=None):
            self._secret_key = secret_key
            self._algorithm = algorithm
            self._default_expiration_interval = default_expiration_interval

        async def create_access_token(self, data, expiration_interval=None):
            expiration_interval = expiration_interval \
                                  or self._default_expiration_interval
            if not expiration_interval:
                raise ValueError(
                    "Neither default nor special expiration date provided"
                )
            to_encode = data.copy()
            expiration_date = expiration_interval + datetime.utcnow()
            to_encode["exp"] = expiration_date
            encoded = jwt.encode(
                to_encode,
                key=self._secret_key,
                algorithm=self._algorithm,
            )
            return encoded

        def get_current_user(self, token=Depends(oauth_scheme)):
            authentication_error = HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect password or username",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            try:
                payload = jwt.decode(
                    token,
                    self._secret_key,
                    algorithms=[self._algorithm]
                )
                print(payload)
                if not payload["valid"]:
                    raise authentication_error
                loaded = TokenEntry.parse_obj(payload)
                return loaded
            except JWTError:
                raise authentication_error

        def authenticate(self, user):
            return True
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )


    return LoginManager
