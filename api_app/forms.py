from django.forms import ModelForm
from api_app.models import case

class caseForm(ModelForm):
	class meta:
		model = case
		fields = ['module']