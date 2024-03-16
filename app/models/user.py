from app.extensions import db
from .utils import to_model as tm, to_dict_specific as td


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.String(10), primary_key=True)

    role_type = db.Column(db.Enum(
        "未核验", "学生", "老师", "管理员", "超级管理员"
    ), server_default="未核验", nullable=False)
    password_hash = db.Column(db.String(255, "utf8mb4_0900_ai_ci"), nullable=False)
    modify_time = db.Column(db.DateTime, nullable=False, server_default=db.text("NOW()"))
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.text("NOW()"))

    # 一对一
    detail = db.relationship("UserDetail", uselist=False, back_populates="user")

    @classmethod
    def to_model(cls, **kwargs):
        return tm(cls, **kwargs)

    def to_dict(self):
        return td(self)


class UserDetail(db.Model):
    __tablename__ = "user_detail"
    user_detail_id = db.Column(db.ForeignKey("user.user_id", ondelete="CASCADE"),
                               primary_key=True, nullable=False)

    name = db.Column(db.String(10), nullable=False)
    modify_time = db.Column(db.DateTime, nullable=False, server_default=db.text("NOW()"))
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.text("NOW()"))

    # 一对一
    user = db.relationship("User", back_populates="detail", cascade="all, delete")

    @classmethod
    def to_model(cls, **kwargs):
        return tm(cls, **kwargs)

    def to_dict(self):
        return td(self)
