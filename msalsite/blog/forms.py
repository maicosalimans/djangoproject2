from django import forms
from .models import Post

class PostForm(forms.ModelForm):   
    class Meta:
        model = Post
        fields = ('title', 'text',)

        from django import forms

class PollForm(forms.Form):   
    CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('dont_know', "Don't know"),

    ]
    question = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Do you mlike working with Django?")
