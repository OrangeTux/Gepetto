import os

try:
    from importlib import reload
    try:
        from imp import reload
    except:
        pass
except ImportError:
    pass

import app


def test_app():
    """ Test configuration of app in different environment. """
    assert app.app.debug is False

    os.environ['GEPETTO_ENV'] = 'dev'
    reload(app)
    assert app.app.debug is True
