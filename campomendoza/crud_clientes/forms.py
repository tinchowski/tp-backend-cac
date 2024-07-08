from .models import VisitaModel
from django import forms


class VisitaForm(forms.ModelForm):
    plan = forms.ChoiceField(choices=VisitaModel.PLAN)
    class Meta:
        model = VisitaModel
        fields = '__all__'

