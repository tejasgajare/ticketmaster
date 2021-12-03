import pytest

from app import create_app
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def client():
    app = create_app()

    with app.test_client() as client:
        with app.app_context():
            yield client

@pytest.fixture
def example_tickets():
    return {
        'tickets': [
            {   
                'id': 1,    
                'subject': 'Example Ticket 1',    
                'description': 'Example Ticket 1 Description',    
                'status': 'open',    
                'priority': 'normal',    
                'assignee_id': 1,    
                'requester_id': 1,  
                'organization_id': 1,  
                'created_at': '2020-01-01 00:00:00',    
                'updated_at': '2020-01-01 00:00:00'
            },
            {   
                'id': 2,    
                'subject': 'Example Ticket 2',    
                'description': 'Example Ticket 2 Description',    
                'status': 'open',    
                'priority': 'normal',    
                'assignee_id': 2,    
                'requester_id': 2,  
                'organization_id': 2,  
                'created_at': '2020-01-01 00:00:00',    
                'updated_at': '2020-01-01 00:00:00'
            },
        ],
        'users': [
            {
                'id': 1,
                'name': 'Example User 1',
            },
            {
                'id': 2,
                'name': 'Example User 2',
            },
        ],
        'organizations': [
            {
                'id': 1,
                'name': 'Example Organization 1',
            },
            {
                'id': 2,
                'name': 'Example Organization 2',
            },
        ],
        'next_page': "random_nextpage_url",
        'previous_page': "random_previouspage_url",
        'count': 2
    }

@pytest.fixture
def example_single_ticket():
    return {
        'ticket':  {   
                'id': 1,    
                'subject': 'Example Ticket 1',    
                'description': 'Example Ticket 1 Description',    
                'status': 'open',    
                'priority': 'normal',    
                'assignee_id': 1,    
                'requester_id': 1,  
                'organization_id': 1,  
                'created_at': '2020-01-01 00:00:00',    
                'updated_at': '2020-01-01 00:00:00'
            },
        'users': [
            {
                'id': 1,
                'name': 'Example User 1',
            },
        ],
        'organizations': [
            {
                'id': 1,
                'name': 'Example Organization 1',
            },
        ]
    }