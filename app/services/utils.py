import datetime
from sqlalchemy.orm import scoped_session


def add_arguments(**_kwargs):
    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            return func(*args, **_kwargs, **kwargs)

        return wrapper

    return out_wrapper


class BaseORMHandler:
    def __init__(self, cls, handler: scoped_session):
        self.cls = cls
        self.handler = handler

    @add_arguments(
        create_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        modify_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    def add(self, **kwargs) -> None:
        if self.handler is None:
            raise Exception("has no active db handler")
        self.handler.add(self.cls.to_model(**kwargs))
        self.handler.commit()

    def delete(self, **kwargs) -> None:
        if self.handler is None:
            raise Exception("has no active db handler")
        self.handler.query(self.cls).filter_by(**kwargs).delete()
        self.handler.commit()

    def get(self, **kwargs):
        if self.handler is None:
            raise Exception("has no active db handler")
        print(type(self.handler.query(self.cls).filter_by(**kwargs).one_or_none()))
        return self.handler.query(self.cls).filter_by(**kwargs).one_or_none()

    def get_all(self):
        if self.handler is None:
            raise Exception("has no active db handler")
        return self.handler.query(self.cls).filter_by().all()

    @add_arguments(
        modify_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    def update(self, _, /, **kwargs) -> None:
        if self.handler is None:
            raise Exception("has no active db handler")
        self.handler.query(self.cls).filter_by(**{self.cls.__tablename__ + "_id": _}).update(kwargs)
        self.handler.commit()
