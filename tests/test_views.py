from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse



class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        item1= Menu.objects.create(title="chips", price=29, inventory=15)
        item2=Menu.objects.create(title='hamburger', price=44, inventory=6)
        item3 = Menu.objects.create(title='pasta', price=16, inventory=11)

    def test_getall(self):
        menu = Menu.objects.all()
        response = self.client.get(reverse('menu'))
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)