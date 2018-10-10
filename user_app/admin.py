from django.contrib import admin
from user_app.models import project,module

# Register your models here.
class projectadmin(admin.ModelAdmin):
	list_display = ['name','description','create_time','id']

class moduleadmin(admin.ModelAdmin):
	list_display = ['name','project','description','create_time','id']

admin.site.register(project,projectadmin)
admin.site.register(module,moduleadmin)


