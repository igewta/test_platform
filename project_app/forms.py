from django import forms


class projectForm(forms.Form):
	name = forms.CharField(label='项目名称')
	description = forms.CharField(label='项目描述',widget=forms.Textarea)
	status = forms.BooleanField(label='状态',required=False)