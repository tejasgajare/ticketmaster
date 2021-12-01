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
    assert value['tickets'] == [{'id': 1}, {'id': 2}]
    value = list_tickets.fetch_all_tickets(None)
    assert value['tickets'] == [{'id': 1}, {'id': 2}]
    value = list_tickets.fetch_all_tickets('string')
    assert value['tickets'] == [{'id': 1}, {'id': 2}]
    value = list_tickets.fetch_all_tickets('')
    assert value['tickets'] == [{'id': 1}, {'id': 2}]

@mock.patch('app.list_tickets.fetch_all_tickets')
def test_show_tickets(fetch_all_tickets_mock, client):
    fetch_all_tickets_mock.return_value = {'tickets': [
        {'id': 1, 'status': 'random_status', 'priority': 'random_priority'}]}
    rv = client.get('/')
    assert b'random_status' in rv.data
    assert b'random_priority' in rv.data