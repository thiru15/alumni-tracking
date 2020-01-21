from django.forms import ModelForm
from testapp.models import Account,colleges

# Create the form class.
class AccountForm(ModelForm):
     class Meta:
         model = Account
         fields = ['username', 'email', 'password', 'year','register_number','field','occupation','college']

# Creating a form to add an article.
class collegeform(ModelForm):
    class Meta:
        model=colleges
        fields=['college_code','password']