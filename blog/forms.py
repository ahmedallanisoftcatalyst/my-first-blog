from django import forms
from django.core.validators import RegexValidator

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

email_validator = RegexValidator(
    regex='@softcatalyst\.com$',
    message='Email is invalid. The email should be a softcatalyst email',
    code='invalid_email',
)
class FeedbackForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100, required=True)
    email = forms.CharField(label='Your email', max_length=100, required=True,validators=[email_validator])
    feedback = forms.CharField(label='Your feedback', widget=forms.Textarea, required=True)