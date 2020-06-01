from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        # name it descriptively so if it fails we know exactly what fails
        form = ItemForm({'name': ''})
        # simulated instance of form without a name
        self.assertFalse(form.is_valid())
        # the form shouldn't be valid
        self.assertIn('name', form.errors.keys())
        # the errors should be sent back in the dictionary of errors
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        # make sure that the error matches what we wanted
        # it's the first entry

    def test_done_field_is_not_required(self):
        # item model auto selects it
        form = ItemForm({'name': 'Test Todo Item'})
        # only a name given to the form
        self.assertTrue(form.is_valid())
        # make sure it is a valid form

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        # instantiate empty form
        self.assertEqual(form.Meta.fields, ['name', 'done'])
        # check that the meta equals the list
        # ensures fields are defined explicitly and if someone changes
        # the item model, it won't accidentally show fields we don't want
        # protects against reordering of list
