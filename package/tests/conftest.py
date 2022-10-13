from flask.testing import FlaskClient
import pytest


def pytest_configure(config):
    config.addinivalue_line("markers", "login_as")


@pytest.fixture
def client(app, user, request):
    """The test client, optionally logged in as a user of the given role

    @pytest.mark.login_as('Admin')
    def test_while_logged_in(client):
        ....

    def test_while_anon(clinet):
        ...

    """
    marker = request.node.get_closest_marker('login_as')
    user_obj = None

    if marker:
        user_obj = user(marker.args[0])

    with app.test_client(user=user_obj) as client:
        yield client


@pytest.fixture(scope='module')
def app():
    from airflow.utils.db import initdb
    from airflow.www.app import create_app

    initdb()
    app = create_app(testing=True)
    app.test_client_class = FlaskLoginClient
    return app


@pytest.fixture()
def appbuilder(app):
    return app.appbuilder


@pytest.fixture
def user(appbuilder):
    def _user(role):
        username = role.lower()

        user = appbuilder.sm.find_user(username=username)
        if user:
            return user

        txn2 = appbuilder.session.begin_nested()
        role_obj = appbuilder.sm.find_role(role)
        if not appbuilder.sm.add_user(username, "Local", role, f'{username}@fab.org', role_obj, role.lower()):
            raise RuntimeError("Error creating test user")
        if txn2.is_active:
            # add_user calls commit(), but lets be safe and ensure it does
            txn2.commit()
        user = appbuilder.sm.find_user(username=username)

        return user

    return _user


class FlaskLoginClient(FlaskClient):
    """
    A Flask test client that knows how to log in users
    using the Flask-Login extension.

    This is taken from flask-login 0.5, but right now airflow needs <0.5
    """

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        fresh = kwargs.pop("fresh_login", True)

        super().__init__(*args, **kwargs)

        if user:
            with self.session_transaction() as sess:
                sess["user_id"] = user.id
                sess["_fresh"] = fresh
