from unittest import skip
from django.http.request import HttpRequest

from django.contrib.auth.models import User

from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase # Para simular la prueba más avanzada 
from django.urls import reverse

from store.models import Category, Product

from .views import all_products
# from store.views import all_products

@skip("demonstrating skipping")
class TestSkip(TestCase):
    def test_skip_example(self):
        pass

    # def test_homepage_url(self):
    #    """
    #    Test homepage response status
    #    """
    #    response = self.Client.get('/')

class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()

        # Se crea datos para probar
        user = User.objects.create(username='admin')
        print('User: ', user.id, user)

        # Verificamos el valor de categoria
        cat = Category.objects.create(name='django', slug='django')
        print('Categoria: ', cat.id, cat)
        
        # Importante: Aunque en el modelo se usa category, en la base de datos se crea el campo como
        #           category_id. Lo mismo ocurre con created_by; es created_by_id en la base de datos.
        self.data1 = Product.objects.create(category_id=cat.id, title='django beginners', created_by_id=user.id,
                                            slug='django-beginners', price='20.00', image='django')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test Product response status
        """
        response = self.c.get(reverse('store:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test Category response status
        """
        response = self.c.get(reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        print(html)
        self.assertIn('<title>Home</title>', html) # Probamos si el html devuelto tiene, por ejemplo el titulo segun lo programamos
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get('/item/django-beginners')
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html) # Probamos si el html devuelto tiene, por ejemplo el titulo segun lo programamos
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
