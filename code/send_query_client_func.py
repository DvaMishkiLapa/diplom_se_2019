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