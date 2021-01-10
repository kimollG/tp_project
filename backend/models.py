from datetime import datetime
from typing import Optional

from enum import Enum

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class PrivilegesGroups(Enum):
    DEFAULT = 1
    MANAGER = 2
    ADMIN = 3


class Spectacle(BaseModel):
    id: int
    name: str
    description: str


class TokenEntry(BaseModel):
    user_group: Optional[PrivilegesGroups]
    valid: bool = True
