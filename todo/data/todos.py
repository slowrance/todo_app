import sqlalchemy as sa

from todo.data.modelbase import SqlAlchemyBase


class ToDo(SqlAlchemyBase):
    __tablename__ = 'todo'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    date_added = sa.Column(sa.Date)
    date_completed = sa.Column(sa.Date)
    completed = sa.Column(sa.Boolean)

    def __repr__(self):
        return f'<ToDo {self.id}>'
