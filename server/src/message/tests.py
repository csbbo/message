from test import TestCase


class MessageAPITest(TestCase):
    def setup(self):
        self.url = self.get_url('MessageAPI')
        self.user = self.create_user()
        self.message_id = ''

    def message_post_test(self):
        data = {'title': 'title1', 'content': 'content1'}
        resp = self.post(self.url, data=data)
        self.message_id = resp.json()['data']['id']
        return self.assert_success(resp.json())

    def message_get_test(self):
        resp = self.get(self.url+f'?id={self.message_id}')
        return self.assert_success(resp.json())

    def message_get_list_test(self):
        resp = self.get(self.get_url('MessageListAPI'))
        return self.assert_success(resp.json())

    def message_delete_test(self):
        data = {'id': self.message_id}
        resp = self.delete(self.url, data=data)
        return self.assert_success(resp.json())


class CommentAPITest(TestCase):
    def setup(self):
        self.url = self.get_url('CommentAPI')
        self.user = self.create_user()
        insert_result = self.db.messages.insert_one({'title': 'title1', 'content': 'content1'})
        self.message_id = str(insert_result.inserted_id)
        self.comment_id = ''

    def comment_post_test(self):
        data = {'mid': self.message_id, 'content': 'comment1'}
        resp = self.post(self.url, data=data)
        self.comment_id = resp.json()['data']['id']
        return self.assert_success(resp.json())

    def comment_get_test(self):
        resp = self.get(self.url+f'?id={self.comment_id}')
        return self.assert_success(resp.json())

    def comment_get_list_test(self):
        resp = self.get(self.get_url('CommentListAPI'))
        return self.assert_success(resp.json())