from app import list_tickets
from unittest import mock
import json
from tests import client

@mock.patch('app.list_tickets.requests.get')
def test_fetch_all_tickets(request_mock):
    _resp = mock.MagicMock()
    _resp.text = json.dumps({'tickets': [{'id': 1}, {'id': 2}]})
    _resp.status_code = 200
    request_mock.return_value = _resp
    value = list_tickets.fetch_all_tickets()
    assert value == [{'id': 1}, {'id': 2}]

@mock.patch('app.list_tickets.fetch_all_tickets')
def test_show_tickets(fetch_all_tickets_mock, client):
    fetch_all_tickets_mock.return_value = [{'description': 'mock_decription'}]
    rv = client.get('/')
    assert b'mock_decription' in rv.data