from django.forms import ModelForm
from .models import ProfileData
from .models import Interests
from .models import PersonalData
    
class ProfileForm(ModelForm):
    class Meta:
        model = ProfileData
        fields = '__all__'
        exclude = ['user', 'likes', 'acquaintances_available', 'current_acquaintance',
                   'couples_requests', 'interests', 'personal_data', 'birthdate', 'age']

class InterestsForm(ModelForm):
    class Meta:
        model = Interests
        fields = '__all__'


class PersonalDataForm(ModelForm):
    class Meta:
        model = PersonalData
        fields = '__all__'

