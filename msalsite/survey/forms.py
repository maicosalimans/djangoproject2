from django import forms

class SurveyForm(forms.form):
    CHOICES = [
        ('yes', 'Yes'),
        ( 'no', 'No'),
        ('dont_know', "Don't know")
    ]

    question = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Do you like working with Django")