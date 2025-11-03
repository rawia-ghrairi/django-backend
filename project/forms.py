from django import forms
from .models import Project,Skills, History,Contact

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'

class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'