from django.test import Client, TestCase

class ViewTest(TestCase):

    def test_hello(self):
        c = Client()
        resp = c.get('/hello/')
        self.assertEqual(resp.status_code, 404)


class ViewTest2(TestCase):

    def test_h(self):
        c = Client()
        resp = c.get('/qs/')
        self.assertEqual(resp.status_code, 404)