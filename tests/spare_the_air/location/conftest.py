import mock
import pytest
import requests


@pytest.fixture(autouse=True)
def mock_requests():
    with mock.patch.dict('sys.modules', **{
        'botocore.vendored': mock.Mock(requests=requests),
    }):
        yield
