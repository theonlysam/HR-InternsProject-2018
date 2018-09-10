from django.contrib import admin
from .models import personal_information
from .models import internship_history
from .models import qualifications_on_entry
from .models import past_employees
from .models import employment_history
from .models import employee_degrees
from .models import countries

admin.site.register(personal_information)
admin.site.register(internship_history)
admin.site.register(qualifications_on_entry)
admin.site.register(past_employees)
admin.site.register(employment_history)
admin.site.register(employee_degrees)
admin.site.register(countries)

