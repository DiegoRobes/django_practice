from django import forms
import upload.models as m


class UploadImage(forms.ModelForm):
    class Meta:
        model = m.Image
        fields = "__all__"


class UploadFile(forms.ModelForm):
    class Meta:
        model = m.File
        fields = "__all__"
