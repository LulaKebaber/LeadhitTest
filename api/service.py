import re

from .models import FormTemplate


class FieldService:
    @staticmethod
    def validate_field_type(value, expected_type):
        if expected_type == "email":
            return FieldService.validate_email(value)
        elif expected_type == "phone":
            return FieldService.validate_phone(value)
        elif expected_type == "date":
            return FieldService.validate_date(value)
        elif expected_type == "text":
            return isinstance(value, str)
        else:
            return False

    @staticmethod
    def validate_email(value):
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        return email_pattern.match(value) is not None

    @staticmethod
    def validate_phone(value):
        phone_pattern = re.compile(r'^\+7 \d{3} \d{3} \d{2} \d{2}$')
        return phone_pattern.match(value) is not None

    @staticmethod
    def validate_date(value):
        date_pattern = re.compile(r'^\d{2}\.\d{2}.\d{4}$|^20\d{2}-\d{2}-\d{2}$')
        return date_pattern.match(value) is not None


class FormService(FieldService):
    def __init__(self, form_template, form_data):
        super().__init__()
        self.form_template = form_template
        self.form_data = form_data

    def create_new_form(self):
        new_form = {}
        for field, info in self.form_data.items():
            if self.validate_date(info):
                new_form[field] = "date"
            elif self.validate_phone(info):
                new_form[field] = "phone"
            elif self.validate_email(info):
                new_form[field] = "email"
            else:
                new_form[field] = "text"
        return new_form

    def check_form_exists(self):
        for field, field_type in self.form_template.items():
            if field in self.form_data:
                user_input = self.form_data[field]
            else:
                return False
            if field not in self.form_data or not self.validate_field_type(user_input, field_type):  # новая форма
                return False
        return True


class TestForms:
    def create_test_forms(self):
        # Форма 1
        registration_form = FormTemplate.objects.create(
            name='registration_form',
            fields={
                "username": "text",
                "email": "email",
                "password": "text",
                "user_phone": "phone",
                "created_date": "date"
            })

        # Форма 2
        contact_form = FormTemplate.objects.create(
            name='contact_form',
            fields={
                "name": "text",
                "contact_email": "email",
                "contact_phone": "phone",
            })

        # Форма 3
        appointment_form = FormTemplate.objects.create(
            name='appointment_form',
            fields={
                "patient_name": "text",
                "patient_phone": "phone",
                "appointment_date": "date",
            })

        # Форма 4
        feedback_form = FormTemplate.objects.create(
            name='feedback_form',
            fields={
                "username": "email",
                "user_phone": "phone",
                "feedback_date": "date",
                "message": "text",
            })

        # Форма 5
        order_form = FormTemplate.objects.create(
            name='order_form',
            fields={
                "username": "text",
                "user_phone": "phone",
                "order_date": "date",
                "user_email": "email",
            })

    def delete_test_forms(self):
        FormTemplate.objects.all().delete()