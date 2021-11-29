from app import show_ticket
from unittest import mock
import json
from tests import client

@mock.patch('app.show_ticket.requests.get')
def test_fetch_ticket(request_mock):
    _resp = mock.MagicMock()
    _resp.text = json.dumps({'ticket': {'id': 102, 'url': 2}})
    _resp.status_code = 200
    request_mock.return_value = _resp
    value = show_ticket.fetch_ticket(101)
    assert value in [{'id': 102, 'url': 2}]

