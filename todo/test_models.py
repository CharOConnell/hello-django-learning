from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        # create a new item
        self.assertFalse(item.done)
        # check it's automatically set to false

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')
        # check a string is written
