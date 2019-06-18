import sqlalchemy as sa

from todo.data.modelbase import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String)
    hashed_pass = sa.Column(sa.String)
    last_login = sa.Column(sa.DateTime)

    def __repr__(self):
        return f'<User {self.id}>'
