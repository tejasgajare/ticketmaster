from app import utils
from unittest import mock
from tests import client, example_tickets, example_single_ticket

def test_get_user_valid(example_tickets):
    assert utils.get_user(example_tickets, 1) == "Example User 1"
    assert utils.get_user(example_tickets, 2) == "Example User 2"

def test_get_organization_valid(example_tickets):
    assert utils.get_organization(example_tickets, 1) == "Example Organization 1"
    assert utils.get_organization(example_tickets, 2) == "Example Organization 2"

def test_get_user_invalid_data():
    assert utils.get_user({}, None) == "null"

def test_get_organization_invalid_data():
    assert utils.get_organization({}, None) == "null"


@mock.patch('app.utils.get_organization')
@mock.patch('app.utils.get_user')
def test_set_namefields_valid_json(mock_user, mock_organization, example_tickets):
    _user = mock.Mock()
    _user = "random_user"
    mock_user.return_value = _user

    _organization = mock.Mock()
    _organization = "random_organization"
    mock_organization.return_value = _organization
    
    value = utils.set_namefields(example_tickets)
    assert value['tickets'][0]['organization'] == "random_organization" 
    assert value['tickets'][0]['requester'] == "random_user"
    assert value['tickets'][0]['assignee'] == "random_user"

@mock.patch('app.utils.get_organization')
@mock.patch('app.utils.get_user')
def test_set_namefields_blank_json(mock_user, mock_organization):
    _user = mock.Mock()
    _user = "random_user"
    mock_user.return_value = _user

    _organization = mock.Mock()
    _organization = "random_organization"
    mock_organization.return_value = _organization
    
    value = utils.set_namefields({})
    len(value['tickets']) == 0

@mock.patch('app.utils.get_organization')
@mock.patch('app.utils.get_user')
def test_set_namefields_fields_not_present(mock_user, mock_organization):
    _user = mock.Mock()
    _user = "random_user"
    mock_user.return_value = _user

    _organization = mock.Mock()
    _organization = "random_organization"
    mock_organization.return_value = _organization
    
    value = utils.set_namefields({})
    len(value['tickets']) == 0
