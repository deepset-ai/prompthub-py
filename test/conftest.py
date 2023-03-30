import os
from pathlib import Path

import pytest

os.environ["PROMPTHUB_MAIN_ENDPOINT"] = "http://localhost"


@pytest.fixture()
def test_root():
    return Path(__file__).parent
