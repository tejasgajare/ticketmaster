def get_user(data, user_id):
    if user_id is None:
        return 'null'
    if 'users' not in data:
        return 'null'
    for item in data['users']:
        if item['id'] == user_id:
            return item['name']
    return 'null'

def get_organization(data, organization_id):
    if organization_id is None:
        return 'null'
    if 'organizations' not in data:
        return 'null'
    for item in data['organizations']:
        if item['id'] == organization_id:
            return item['name']
    return 'null'

def set_namefields(data):
    if 'tickets' not in data:
        data['tickets'] = []
        return data

    for ticket in data['tickets']:

        if 'requester_id' not in ticket:
            ticket['requester'] = 'null'
        else:
            ticket['requester'] = get_user(data, ticket['requester_id'])

        if 'assignee_id' not in ticket:
            ticket['assignee'] = 'null'
        else:
            ticket['assignee'] = get_user(data, ticket['assignee_id'])

        if 'organization_id' not in ticket:
            ticket['organization'] = 'null'
        else:
            ticket['organization'] = get_organization(data, ticket['organization_id'])
        
    return data

def set_namevalues(data):
    if 'error' in data:
        return data
        
    if 'ticket' not in data:
        data['ticket'] = {}
        return data

    if 'requester_id' not in data['ticket']:
        data['ticket']['requester'] = 'null'
    else:
        data['ticket']['requester'] = get_user(data, data['ticket']['requester_id'])

    if 'assignee_id' not in data['ticket']:
        data['ticket']['assignee'] = 'null'
    else:
        data['ticket']['assignee'] = get_user(data, data['ticket']['assignee_id'])

    if 'organization_id' not in data['ticket']:
        data['ticket']['organization'] = 'null'
    else:
        data['ticket']['organization'] = get_organization(data, data['ticket']['organization_id'])
        
    return data