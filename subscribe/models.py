from django.db import models

# to give the user a field where they need to choose from multiple options
# we first define the options in a list of tuples and then call it in the
# model for the form. in this list of tuples, the first value is the value
# that will go into the database, while the second one is the one to be shown
# to the user in the browser
multiple_options = [
    ("W", "Weekly"),
    ("M", "Monthly"),
    ("N", "No")
]


# Create your models here.
class Subscribe(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    option = models.CharField(max_length=2, choices=multiple_options, default="N")
