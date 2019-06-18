import logging

import sqlalchemy
import sqlalchemy.orm
from todo.data.modelbase import SqlAlchemyBase
# noinspection PyUnresolvedReferences
import todo.data.__all_models

log = logging.getLogger(__name__)


class DbSession:
    factory = None
    engine = None

    @staticmethod
    def global_init(db_file: str):
        if DbSession.factory:
            return

        if not db_file or not db_file.strip():
            raise Exception("You must specify a data file.")

        conn_str = f'sqlite:///{db_file}'
        log.debug(f'Connecting to DB at: {conn_str}')

        engine = sqlalchemy.create_engine(conn_str, echo=False)
        DbSession.engine = engine
        DbSession.factory = sqlalchemy.orm.sessionmaker(bind=engine)

        SqlAlchemyBase.metadata.create_all(engine)
