import pytest

from fist.client import Fist


@pytest.fixture(scope="session", autouse=True)
def client(request):
    return Fist(host="localhost", port=5575)
