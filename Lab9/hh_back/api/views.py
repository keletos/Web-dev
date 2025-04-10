from django.http import JsonResponse
from .models import Company, Vacancy

def company_list(request):
    companies = Company.objects.all()
    data = [{"id": c.id, "name": c.name, "description": c.description, "city": c.city, "address": c.address} for c in companies]
    return JsonResponse(data, safe=False)

def company_detail(request, id):
    try:
        c = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company not found'}, status=404)
    data = {"id": c.id, "name": c.name, "description": c.description, "city": c.city, "address": c.address}
    return JsonResponse(data)

def company_vacancies(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company not found'}, status=404)
    vacancies = company.vacancies.all()
    data = [{"id": v.id, "name": v.name, "description": v.description, "salary": v.salary, "company": v.company.id} for v in vacancies]
    return JsonResponse(data, safe=False)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    data = [{"id": v.id, "name": v.name, "description": v.description, "salary": v.salary, "company": v.company.id} for v in vacancies]
    return JsonResponse(data, safe=False)

def vacancy_detail(request, id):
    try:
        v = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist:
        return JsonResponse({'error': 'Vacancy not found'}, status=404)
    data = {"id": v.id, "name": v.name, "description": v.description, "salary": v.salary, "company": v.company.id}
    return JsonResponse(data)

def top_ten_vacancies(request):
    top = Vacancy.objects.order_by('-salary')[:10]
    data = [{"id": v.id, "name": v.name, "description": v.description, "salary": v.salary, "company": v.company.id} for v in top]
    return JsonResponse(data, safe=False)
