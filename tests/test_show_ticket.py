from app import show_ticket
from unittest import mock
import json
from tests import client, example_single_ticket

@mock.patch('app.show_ticket.utils.set_namefields')
@mock.patch('app.show_ticket.requests.get')
def test_fetch_ticket_valid_json(mock_request, mock_namefields, example_single_ticket):
    _response = mock.Mock()
    _response.text = json.dumps(example_single_ticket)
    _response.status_code = 200
    mock_request.return_value = _response

    _namefields = mock.Mock()
    _namefields = example_single_ticket
    mock_namefields.return_value = _namefields
    
    id = example_single_ticket['ticket']['id']
    value = show_ticket.fetch_ticket(id)

    assert value['subject'] == example_single_ticket['ticket']['subject']
    assert value['status'] == example_single_ticket['ticket']['status']
    assert value['description'] == example_single_ticket['ticket']['description']
    assert value['priority'] == example_single_ticket['ticket']['priority'] 
    assert value['requester_id'] == example_single_ticket['ticket']['requester_id']
    assert value['organization_id'] == example_single_ticket['ticket']['organization_id']

@mock.patch('app.show_ticket.utils.set_namefields')
@mock.patch('app.show_ticket.requests.get')
def test_fetch_ticket_invalid_json(mock_request, mock_namefields):
    _response = mock.Mock()
    _response.text = json.dumps({})
    _response.status_code = 200
    mock_request.return_value = _response

    _namefields = mock.Mock()
    _namefields = {}
    mock_namefields.return_value = _namefields
    
    value = show_ticket.fetch_ticket()

    assert value is None

@mock.patch('app.show_ticket.fetch_ticket')
def test_show_ticket_valid_json(fetch_ticket_mock, client, example_single_ticket):
    fetch_ticket_mock.return_value = example_single_ticket['ticket']
    id = example_single_ticket['ticket']['id']
    rv = client.get(f'/ticket/1')
    assert rv.status_code == 200
    assert b'Example Ticket 1' in rv.data
    assert b'Example Ticket 1 Description' in rv.data

@mock.patch('app.show_ticket.fetch_ticket')
def test_show_ticket_nodata(fetch_ticket_mock, client):
    fetch_ticket_mock.return_value = {}
    rv = client.get('/ticket/none')
    assert rv.status_code == 200
    assert b'No data found' in rv.data