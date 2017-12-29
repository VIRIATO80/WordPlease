from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, DateTimeInput

from blogs.models import Post


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        del self.fields['password2']


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        exclude = ['user']
        widgets = {"intro": Textarea(attrs={'cols': 40, 'rows': 5}),
                   'publish_date': DateTimeInput(attrs={'class': 'datepicker'})
                   }
