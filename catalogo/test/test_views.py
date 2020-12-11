from django.test import Client, TestCase

 

class ViewTest2(TestCase):

    def test_h(self):
        c = Client()
        resp = c.get('/qs/')
        self.assertEqual(resp.status_code, 404)