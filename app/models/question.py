from app.extensions import db
from .utils import to_model as tm, to_dict_specific as td


class Question(db.Model):
    __tablename__ = "question"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    difficulty = db.Column(db.Enum(
        "简单", "中等", "困难"
    ), server_default="简单", nullable=False)
    description = db.Column(db.String(200), nullable=False)
    example = db.Column(db.JSON)
    answer = db.Column(db.JSON)

    modify_time = db.Column(db.DateTime, nullable=False, server_default=db.text("NOW()"))
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.text("NOW()"))

    _question_banks = db.relationship("QuestionBank", secondary="bank", back_populates="_questions",
                                      lazy="dynamic", primaryjoin="Question.id == Bank.question_id",
                                      secondaryjoin="_and(Question.id == Bank.question_id, "
                                                    "QuestionBank.id == Bank.question_bank_id)")

    @classmethod
    def to_model(cls, **kwargs):
        return tm(cls, **kwargs)

    def to_dict(self):
        return td(self)


class QuestionBank(db.Model):
    __tablename__ = "question_bank"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    modify_time = db.Column(db.DateTime, nullable=False, server_default=db.text("NOW()"))
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.text("NOW()"))

    _questions = db.relationship("Question", secondary="bank", back_populates="_questions_banks",
                                 lazy="dynamic", primaryjoin="QuestionBank.id == Bank.question_bank_id",
                                 secondaryjoin="_and(QuestionBank.id == Bank.question_bank_id, "
                                               "QuestionBank.id == Bank.question_bank_id)")

    @classmethod
    def to_model(cls, **kwargs):
        return tm(cls, **kwargs)

    def to_dict(self):
        return td(self)


class Bank(db.Model):
    __tablename__ = "bank"

    question_id = db.Column(db.Integer, db.ForeignKey("question.id", ondelete="CASCADE"), primary_key=True)
    question_bank_id = db.Column(db.Integer, db.ForeignKey("question_bank.id", ondelete="CASCADE"), primary_key=True)
