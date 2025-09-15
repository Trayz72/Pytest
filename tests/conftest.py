import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client