from django.forms import (
    Form,
    ModelForm,
    CharField,
    EmailField,
    FileField,
)

from .models import User

class UserForm(ModelForm):

    class Meta:
        model = User
        fields = '__all__'

class UserNameForm(Form):

    user_name = CharField()

class UploadCsvForm(Form):

    csv_file = FileField()

