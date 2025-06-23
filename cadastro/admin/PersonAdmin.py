# questions/admin.py
from django.contrib import admin
from cadastro.models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'enrollment_number', 'birth_date', 'gender')
    search_fields = ('full_name', 'user__username', 'enrollment_number')
    list_filter = ('gender', 'enrolled_subjects')
    raw_id_fields = ('user',) 
    filter_horizontal = ('enrolled_subjects',) 