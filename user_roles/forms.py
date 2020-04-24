from django import forms
from .models import Permohonan

class PermohonanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(PermohonanForm, self).__init__(*args, **kwargs)
       self.fields['contractor'].widget.attrs['readonly'] = True
    
    class Meta:
        model = Permohonan
        fields = [
            'contractor_name',
            'phone_no',
            'company_name',
            'company_address',
            'contractor',
        ]