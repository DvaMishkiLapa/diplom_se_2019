def create_token(self, email):
    exp = datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
    token = jwt.encode({'email': email, 'exp': exp}, self.secret, algorithm='HS256')
    return token.decode()