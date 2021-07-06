from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from store.models import Category, Product

class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'django')
        

class TestProductsModel(TestCase):

    def setUp(self):
        c = Category.objects.create(name='django', slug='django')
        print(c.id, c)
        User.objects.create(username='admin')
        # Importante: Aunque en el modelo se usa category, en la base de datos se crea el campo como
        #           category_id. Lo mismo ocurre con created_by; es created_by_id en la base de datos.
        self.data1 = Product.objects.create(category_id=2, title='django beginners', created_by_id=1,
                                            slug='django-beginners', price='20.00', image='django')

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')