import datetime
from typing import Optional

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from auth import create_login_manager
from config import DATABASE_PARAMETERS, SECRET_KEY
from connector import mariadb_connection
from models import Spectacle, Token
from queries import select_query

app = FastAPI()

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")
LoginManager = create_login_manager(
    oauth_scheme=oauth_scheme,
)
login_manager = LoginManager(
    default_expiration_interval=datetime.timedelta(hours=4),
    algorithm="HS256",
    secret_key=SECRET_KEY
)
get_current_user = login_manager.get_current_user


class Application:
    def __init__(self, secret_key):
        self._oauth2_scheme = oauth_scheme
        self._app = FastAPI()

    @app.get("/spectacles")
    async def get_spectacles(self, user=Depends(get_current_user)):
        print(user)
        with mariadb_connection(DATABASE_PARAMETERS) as connection:
            records = select_query(
                connection,
                "spectacles",
                ("id", "name", "description"),
                Spectacle,
            )
            return records


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    user = login_manager.authenticate(form_data)
    access_token = await login_manager.create_access_token(
        {
            "user": form_data.username,
            "valid": True,
        })
    return Token(
        access_token=access_token,
        token_type="bearer"
    )


