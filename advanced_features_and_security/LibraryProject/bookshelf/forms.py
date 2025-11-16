from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    age = forms.IntegerField(label="Your Age")
