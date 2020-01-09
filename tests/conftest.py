import os.path

import pytest


@pytest.fixture()
def test_data_dir():
    yield os.path.join(os.path.dirname(__file__), "test-data")
