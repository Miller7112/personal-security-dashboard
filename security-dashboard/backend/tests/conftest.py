import pytest
from app import create_app
from database import db

@pytest.fixture
def app():
    """Create and configure a new Flask app instance for testing."""
    app = create_app(testing=True)  # Ensure your app.py supports a 'testing' mode

    with app.app_context():
        db.create_all()  # Create a temporary test database
        yield app
        db.session.remove()
        db.drop_all()  # Clean up after tests

@pytest.fixture
def client(app):
    """Return a test client for making API requests."""
    return app.test_client()
