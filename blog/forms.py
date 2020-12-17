from .models import Post
from django import forms
from django.forms.models import ModelForm
from djrichtextfield.widgets import RichTextWidget


class CreateForm(forms.ModelForm):
	content = forms.CharField(widget=RichTextWidget())

	class Meta:
		model = Post
		fields = ('title','content','image','status')

class UpdateForm(forms.ModelForm):
	content = forms.CharField(widget=RichTextWidget())

	class Meta:
		model = Post
		fields = ('title', 'content','image','status')
