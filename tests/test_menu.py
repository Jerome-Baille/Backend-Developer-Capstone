from django.test import TestCase, RequestFactory
from restaurant.models import Menu
from restaurant.views import menu
from restaurant.serializers import MenuSerializer


# Test to get one menu item
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            name="Tiramisu",
            price=8.99,
            description="Classic Italian dessert with layers of espresso-soaked ladyfingers and creamy mascarpone. Rich, sweet, and indulgent."
        )
        self.assertEqual(item.__str__(), "Tiramisu")

# Test to get all menu items
class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        Menu.objects.create(
            name="Bruschetta",
            price=6.99,
            description="Grilled slices of rustic bread topped with fresh diced tomatoes, garlic, basil, and drizzled with extra virgin olive oil. A delightful Italian appetizer bursting with flavors."
        )
        Menu.objects.create(
            name="Lemon Dessert",
            price=7.99,
            description="Zesty lemon-infused dessert featuring a delicate sponge cake layered with lemon curd and topped with a fluffy meringue. A delightful sweet treat that provides a refreshing citrus finish to your meal."
        )

    def test_getall(self):
        menuitems = Menu.objects.all()
        serialized_menuitems = MenuSerializer(menuitems, many=True)
        request = self.factory.get('menu/')
        response = menu.as_view()(request)

        self.assertEqual(response.data, serialized_menuitems.data)
