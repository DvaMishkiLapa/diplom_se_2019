def assign_to_projects(self, data):
    result = []
    for x in data:
        user = self.users.find_one({'email': x['email']})
        if not user:
            result.append((False, 'User not found!', 404))
            continue
        project = self.projects.find_one({'name': x['project']})
        if not project:
            result.append((False, 'Project not found!', 404))
            continue
        connection = self.connections.find_one({'user': user['_id'], 'project': project['_id']})
        if connection:
            result.append((False, 'Project already assigned!', 400))
            continue
        self.connections.insert_one({'user': user['_id'], 'project': project['_id']})
        result.append((True, 'Project has been assigned!', 200))
    return result