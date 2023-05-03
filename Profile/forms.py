from django.forms import ModelForm
from .models import ProfileData

    
class ProfileForm(ModelForm):
    class Meta:
        model = ProfileData
        fields = '__all__'
        exclude = ['user', 'likes', 'acquaintances_available', 'current_acquaintance']
