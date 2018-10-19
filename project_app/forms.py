from django.forms import ModelForm
from project_app.models import project,module


class projectForm(ModelForm):
	class Meta:
		model = project
		exclude = ['create_time']


class moduleForm(ModelForm):
	class Meta:
		model = module
		fields = ['project','name','description']
		#exclude = ['create_time']

