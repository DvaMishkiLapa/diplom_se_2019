def authorization(self, user_data):
    email = user_data['email']
    pwd = user_data['pwd']
    user = self.users.find_one({'email': email})
    if not user:
        return False, 'User not found!', 404
    if user['pwd'] == sha256(pwd.encode()).hexdigest():
        return True, self.create_token(email), 200
    return False, 'Wrong password!', 400