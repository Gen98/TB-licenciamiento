from django import forms
from .models import Clients_Licenses

class ClientsLicensesForm(forms.ModelForm):
    """Form definition for Clients_Licenses."""
    class Meta:
        """Meta definition for ClientsLicensesForm."""
        model = Clients_Licenses
        fields = ('__all__')
        widgets = {
            'server_access': forms.Textarea()
        }
