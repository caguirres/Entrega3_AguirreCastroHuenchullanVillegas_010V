from django.test import TestCase
from catalogo.forms import LocalForm, UsuarioForm, UserForms

class FormTest(TestCase):
    def test_forms(self):
        form_data = {'id_local':'1'}
        form = LocalForm(data=form_data)
        self.assertFalse(form.is_valid())

class FormTest2(TestCase):
    def test_forms(self):
        form_data = {'fields':'__all__'}
        form = LocalForm(data=form_data)
        self.assertFalse(form.is_valid())


class FormTest3(TestCase):
    def test_forms(self):
        form_data = {'fields':'__all__'}
        form = UsuarioForm(data=form_data)
        self.assertFalse(form.is_valid())


class FormTest4(TestCase):
    def test_forms(self):
        form_data = {'fields':'__all__'}
        form = UserForms(data=form_data)
        self.assertFalse(form.is_valid())




