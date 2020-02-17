from django.shortcuts import render
import django.views.generic


# Create your views here.
def home(request):
    par = {
        'header': 'Home'
    }
    return render(request, 'home.html', context=par)


class DepartmentsView(django.views.generic.View):
    def get(self, request):
        data = {
            'departments': [
                {'title': 'Отдел маркентинга','id': 1},
                {'title': 'Бухгалтерия','id': 2}
            ]
        }
        return render(request, 'departments.html', data)


class DepartmentView(django.views.generic.View):
    def get(self, request, id):
        data = {
            'department':
                {
                    'id': id
                }
        }
        return render(request, 'department.html', data)
