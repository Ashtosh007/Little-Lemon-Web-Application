from django.test import TestCase

from .models import MenuItem

class MenuItemTestCase(TestCase):
    def setUp(self):
        MenuItem.objects.create(name="Pizza", price=12.99, description="Delicious")

    def test_menu_item(self):
        pizza = MenuItem.objects.get(name="Pizza")
        self.assertEqual(pizza.price, 12.99)
