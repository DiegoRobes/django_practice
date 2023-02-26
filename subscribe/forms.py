from django import forms
import subscribe.models as m
from django.utils.translation import gettext_lazy as _


# this validator function is doing the same as the one that is inside the class, but this one can be used in
# multiple fields, using validators=[<name of function>]
def validate_comma(value):
    if "," in value:
        raise forms.ValidationError("Invalid Character ','")
    return value


"""# we are defining models for the forms we are going to use in the views.
# this is going to save us lots of time once we import it to the
# views.py
# required fields are the default for all fields here, to make them not required, you need to specify it
# examples: required=<bool>, label="", help_text="", check notes for link and full list
class SubscribeForm(forms.Form):
    # validators: this function checks some conditions and raises exception when needed
    # you can customize it in many ways
    def clean_name(self):
        data = self.cleaned_data["name"]
        if "," in data:
            raise forms.ValidationError("Invalid Name")
        return data
    name = forms.CharField(max_length=100, validators=[validate_comma])
    hello = forms.CharField(widget=forms.TextInput(attrs={'class': 'myfieldclass'}))
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
"""


# the next is a way to make a form using the modelforms functions of django, it can be a bit faster that the
# first approach. the first thing you do is import the model you need from models.py, and then create the class
# and the META, be careful with that one. the "__all__" is used to render every field on the model as a field on the
# form, being mapped and transformed automatically by django
# if you need to customize your labels and error messages, you can use the labels attribute after importing the
# gettext_lazy thing from utils
# an advantage of using modelforms is that the process of catching the info input by the user and creating an object
# that can be saved into the db is done in a much easier way, just using the save() method. go the
# views.py to check it out
class SubscribeForm(forms.ModelForm):
    class Meta:
        model = m.Subscribe
        fields = "__all__"
        labels = {"name": _("Please enter your First Name")}
        error_messages = {
            "name": {"required": _("You need to input your name")},
            "last_name": {"required": _("You need to enter your last name")}
        }
        # if you have a very large form, and you want to hide a field, you can use the exclude method
        # exclude = ("name",)

