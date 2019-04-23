import json
import requests
host = 'https://pms.kmm-vsu.ru/'


class API:
    def __init__(self):
        self.token = ''
        self.user = ''
        self.pwd = ''

    def check_connect(self):
        try:
            requests.get(host)
            return True
        except requests.exceptions.ConnectionError:
            return False

    def authorization(self, email, pwd):
        data = json.dumps({"requests": {"authorization": {"email": email, "pwd": pwd}}, 'token': ''})
        try:
            response = requests.post(host, data=data).json()
        except requests.exceptions.ConnectionError:
            return False
        self.token = response['content']['authorization']['content']
        return response

    def send_query(self, args):
        data = json.dumps({"requests": args, 'token': self.token})
        try:
            response = requests.post(host, data=data).json()
        except requests.exceptions.ConnectionError:
            return False
        try:
            if response['error_code'] == 403:
                self.authorization(self.user, self.pwd)
                data = json.dumps({"requests": args, 'token': self.token})
                response = requests.post(host, data=data).json()
        except (KeyError, requests.exceptions.ConnectionError) as e:
            if e == requests.exceptions.ConnectionError:
                return False
        if not (len(args) == 1):
            pass
        elif response['ok']:
            try:
                return tuple(response['content'].values())[0]['content']
            except Exception:
                pass
        return response

    def get_all_users(self, args):
        return self.send_query({"get_all_users": args})

    def get_all_projects(self, args):
        return self.send_query({"get_all_projects": args})

    def add_users(self, users):
        return self.send_query({"add_users": users})

    def edit_users(self, users):
        return self.send_query({"edit_users": users})

    def del_users(self, emails):
        return self.send_query({"del_users": emails})

    def add_projects(self, projects):
        return self.send_query({"add_projects": projects})

    def edit_projects(self, projects):
        return self.send_query({"edit_projects": projects})

    def del_projects(self, projects):
        return self.send_query({"del_projects": projects})

    def change_password(self, args):
        return self.send_query({"change_password": args})

    def get_users_count(self):
        return self.send_query({"get_users_count": {}})

    def assign_to_projects(self, args):
        return self.send_query({"assign_to_projects": args})

    def remove_from_projects(self, args):
        return self.send_query({"remove_from_projects": args})

    # def get_users_projects(self, ):
    #     return self.send_query({}, 'get_users_projects')

    # def get_all_projects(self):
    #     return self.send_query({}, 'get_all_projects')