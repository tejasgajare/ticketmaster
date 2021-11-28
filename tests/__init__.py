import os
import tempfile

import pytest

from app import create_app
from dotenv import load_dotenv
from app import tickets

load_dotenv()

@pytest.fixture
def client():
    app = create_app()

    with app.test_client() as client:
        with app.app_context():
            yield client