from django.urls import path
from .views import form_view

urlpatterns = [
    path('get_form', form_view.get_form, name='get_form'),
    path('add_form', form_view.add_new_form, name='add_new_form'),
    path('create_test_forms', form_view.create_test_forms, name='create_test_forms'),
    path('delete_all_forms', form_view.delete_all_forms, name='delete_all_forms')
]
