from django import forms


# we are defining models for the forms we are going to use in the views.
# this is going to save us lots of time once we import it to the
# views.py
class SubscribeForm(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
