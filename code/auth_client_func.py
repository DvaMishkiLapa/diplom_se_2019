def authorization(self, email, pwd):
    data = json.dumps({"requests": {"authorization": {"email": email, "pwd": pwd}}, 'token': ''})
    try:
        response = requests.post(host, data=data).json()
    except requests.exceptions.ConnectionError:
        return False
    self.token = response['content']['authorization']['content']
    return response