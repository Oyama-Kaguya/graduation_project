from sqlalchemy.orm import scoped_session

from .utils import BaseORMHandler
from ..models import User, UserDetail


class UserORMHandler(BaseORMHandler):
    def __init__(self, handler: scoped_session):
        super().__init__(User, handler)

    def login(self, **kwargs):
        user = self.get(user_id=kwargs["user_id"])
        if user and user.password_hash == kwargs["password_hash"]:
            return True
        return False


class UserDetailORMHandler(BaseORMHandler):
    def __init__(self, handler: scoped_session):
        super().__init__(UserDetail, handler)
