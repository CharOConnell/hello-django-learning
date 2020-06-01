from django.test import TestCase
from .models import Item
# Create your tests here.


class TestViews(TestCase):

    def test_get_todo_list(self):
        # built in http-client
        response = self.client.get('/')
        # homepage
        self.assertEqual(response.status_code, 200)
        # successful http response
        self.assertTemplateUsed(response, 'todo/todo_list.html')
        # check it uses the correct template

    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Test Todo Item')
        # create a new instance of it
        response = self.client.get(f'/edit/{item.id}')
        # the item id will be numerical - use the f notation
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # as if we've just added something
        self.assertRedirects(response, '/')
        # check it redirects to the homepage

    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        # create a new instance of it
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        # then check if we search for it it is not in the system
        self.assertEqual(len(existing_items), 0)
        # as we know it's the only entry, it should now have nothing

    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True)
        # manually set it to be true
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
        # it should've changed back to being false by then

    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.post(
            f'/edit/{item.id}', {'name': 'Updated Name'})
        # edit the initial response
        self.assertRedirects(response, '/')
        # check it then redirects
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')
        # check the updated name is what we changed it to
