import sqlalchemy as sa

from todo.data.modelbase import SqlAlchemyBase


class ToDo(SqlAlchemyBase):
    __tablename__ = 'todos'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    date_added = sa.Column(sa.Date)
    date_completed = sa.Column(sa.Date)
    completed = sa.Column(sa.Boolean)

    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))

    def __repr__(self):
        return f'<ToDo {self.id}>'
