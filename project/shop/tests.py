from django.test import TestCase, RequestFactory
from shop import views


# Create your tests here.


class IndexViewTestCase(TestCase):
    def test_index(self):
        factory = RequestFactory()
        request = factory.get('/shop')

        view = views.IndexView()
        view.setup(request)
        responce = view.get(request)
        self.assertEqual(responce.status_code, 200)
        self.assertContains(responce, 'Hello world')
