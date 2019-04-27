from .models import Gist

def search_gists(db_connection, **kwargs):
    result = []
    query = 'SELECT * FROM gists'
    if kwargs:
        query += ' WHERE '
    if 'github_id' in kwargs.keys():
        query += ' github_id="{}" AND'.format(kwargs['github_id'])
    if 'created_at' in kwargs.keys():
        query += ' datetime(created_at) = datetime("{}")'.format(kwargs['created_at'])
    else:
        query = query.rstrip(' AND')
    cursor = db_connection.execute(query)
    for row in cursor:
        new_gist = Gist(row)
        result.append(new_gist)
    return result