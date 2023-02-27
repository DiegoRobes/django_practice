from django.db import models


# We are going to use this model to upload images to the server. for that
# we need to install the pillow library into the venv
class Image(models.Model):
    image = models.ImageField(upload_to="img")
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


# this model is for files other than images
class File(models.Model):
    file = models.FileField(upload_to='files')
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
