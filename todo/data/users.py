import sqlalchemy as sa

from todo.data.modelbase import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'user'

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String)
    hash_pass = sa.Column(sa.String)
    last_logon = sa.Column(sa.DateTime)

    def __repr__(self):
        return f'<User {self.id}>'
