def test_del_users(self):
    users_list = [{'email': 'test0@test.ru'}, {'email': 'test1@test.ru'}]
    result = self.dbm.del_users(users_list)
    self.assertEqual(len(result), 2, f'Too many response! ({len(result)})')
    for r in result:
        _, content, code = r
        self.assertEqual(code, 200, f'Test users has not been removed! ({content})')
    result = self.dbm.del_users(users_list)
    for r in result:
        _, content, code = r
        self.assertEqual(code, 404, f'Removed non-existent user! ({content})')