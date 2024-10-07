from django import forms

class PollForm(forms.Form):   
    CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('dont_know', "Don't know"),

    ]
    question = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Do you mlike working with Django?")
