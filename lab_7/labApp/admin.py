from django.contrib import admin

from labApp.models import*

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username','full_name','email',)
    search_fields = ['last_name', 'first_name']

    def full_name(self, obj):
        return "{} {}".format(obj.last_name, obj.first_name)

    def username(self, obj):
        return "{}".format(obj.user.username)


@admin.register(Departments)
class DepartmentAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('department','description',)
    search_fields = ['department_name']

    def department(self, obj):
        return "{}".format(obj.prodact_name)

    def description(self, obj):
        return "{}".format(obj.description)
