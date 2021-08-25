from django import forms
from django.core.validators import RegexValidator

from .models import Post

email_softcatalyst_validator = RegexValidator(
    regex='@softcatalyst\.com$',
    message='Email is invalid. The email should be a softcatalyst email',
    code='invalid_email',
)
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
    title = forms.EmailField(label='Your email', max_length=100, required=True,validators=[email_softcatalyst_validator])

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100, required=True)
    email = forms.EmailField(label='Your email', max_length=100, required=True,validators=[email_softcatalyst_validator])
    feedback = forms.CharField(label='Your feedback', widget=forms.Textarea, required=True)