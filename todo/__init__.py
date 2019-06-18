import os
import logging

from pyramid.config import Configurator

from todo.data.db_session import DbSession

log = logging.getLogger(__name__)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    init_includes(config)
    init_db(config)
    init_routing(config)

    return config.make_wsgi_app()


def init_includes(config):
    config.include('pyramid_chameleon')


def init_db(config):
    db_file = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            'db',
            'todo.sqlite'
        )
    )
    log.debug(str(db_file))
    DbSession.global_init(db_file)


def init_routing(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
