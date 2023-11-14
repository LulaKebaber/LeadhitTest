from django.http import JsonResponse
from rest_framework.decorators import api_view
from ..models import FormTemplate
from ..service import FormService
from ..service import TestForms


@api_view(['GET'])
def get_form(request):
    form_data = request.query_params

    all_templates = FormTemplate.objects.all()
    for template in all_templates:
        template_fields = template.fields
        if FormService(form_data=form_data, form_template=template_fields).check_form_exists():
            return JsonResponse({'data': template.name}, status=200)
    new_form = FormService(form_data=form_data, form_template=1).create_new_form()
    return JsonResponse({'data': new_form}, status=200)


@api_view(['POST'])
def add_new_form(request):
    if "name" in request.data and "fields" in request.data:
        name = request.data["name"]
        fields = request.data["fields"]
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)

    if FormTemplate.objects.filter(name=name).exists():
        return JsonResponse({'message': 'Form already exists!'}, status=400)

    form_template = FormTemplate.objects.create(name=name, fields=fields)

    return JsonResponse({'message': f"{form_template.name} form created!"}, status=201)


@api_view(['POST'])
def create_test_forms(request):
    action = request.data['action']

    if action == 'create':
        TestForms().create_test_forms()
    return JsonResponse({'message': 'Test forms created!'}, status=201)


@api_view(['DELETE'])
def delete_all_forms(request):
    action = request.data['action']

    if action == 'delete':
        TestForms().delete_test_forms()
    return JsonResponse({'message': 'All forms deleted!'}, status=200)