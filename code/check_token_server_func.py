def check_token(self, token):
    try:
        payload = jwt.decode(token.encode(), self.secret, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return False, 'Token expired!', 403
    except (jwt.DecodeError, AttributeError):
        return False, 'Invalid token!', 403
    return True, payload['email'], 200