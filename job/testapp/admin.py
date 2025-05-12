from django.contrib import admin
from testapp.models import Hydjobs
from testapp.models import Bengjobs
from testapp.models import Deljobs


# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligiblity', 'address', 'email', 'phonenumber']

admin.site.register(Hydjobs, HydjobsAdmin)

class BengjobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligiblity', 'address', 'email', 'phonenumber']

admin.site.register(Bengjobs, BengjobsAdmin)

class DeljobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligiblity', 'address', 'email', 'phonenumber']

admin.site.register(Deljobs, DeljobsAdmin)