from app import list_tickets
from unittest import mock
import json
from tests import client, example_tickets

@mock.patch('app.list_tickets.utils.set_namefields')
@mock.patch('app.list_tickets.requests.get')
def test_fetch_all_tickets_valid_json(mock_request, mock_namefields, example_tickets):
    _response = mock.Mock()
    _response.text = json.dumps(example_tickets)
    mock_request.return_value = _response

    _namefields = mock.Mock()
    _namefields = example_tickets
    mock_namefields.return_value = _namefields
    
    value = list_tickets.fetch_all_tickets()
    assert len(value['tickets']) > 0
    assert value['tickets'][0]['id'] == example_tickets['tickets'][0]['id']
    assert value['tickets'][0]['subject'] == example_tickets['tickets'][0]['subject']
    assert value['tickets'][0]['status'] == example_tickets['tickets'][0]['status']
    assert value['tickets'][0]['priority'] == example_tickets['tickets'][0]['priority']
    assert value['tickets'][0]['requester_id'] == example_tickets['tickets'][0]['requester_id']
    assert value['tickets'][0]['organization_id'] == example_tickets['tickets'][0]['organization_id']


@mock.patch('app.list_tickets.utils.set_namefields')
@mock.patch('app.list_tickets.requests.get')
def test_fetch_all_tickets_invalid_json(mock_request, mock_namefields):
    _response = mock.Mock()
    _response.text = json.dumps({})
    _response.status_code = 200
    mock_request.return_value = _response

    _namefields = mock.Mock()
    _namefields = {}
    mock_namefields.return_value = _namefields
    
    value = list_tickets.fetch_all_tickets()
    assert len(value['tickets']) == 0

@mock.patch('app.list_tickets.fetch_all_tickets')
def test_show_tickets_valid_json(fetch_all_tickets_mock, client, example_tickets):
    fetch_all_tickets_mock.return_value = example_tickets
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Example Ticket 2' in rv.data
    assert b'random_nextpage_url' in rv.data
    assert b'random_previouspage_url' in rv.data

@mock.patch('app.list_tickets.fetch_all_tickets')
def test_show_tickets_nodata(fetch_all_tickets_mock, client):
    fetch_all_tickets_mock.return_value = {}
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'No data found' in rv.data