from django.db import models


# Create your models here.
# list of field types https://docs.djangoproject.com/en/4.1/ref/models/fields/
class JobPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    # title was the initial field, now we add others with different type fields
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()
    # once you add these new field, you need to sync them using the terminal command py manage.py makemigrations
    # follow instructions on the command line, and then you'll see the new migration file created on migrations folder
    # after that clear command line, and run py manage.py migrate to se the new fields added to the database
    # in the browser

    # this next method is helpful to fetch the information from the objects inside the django shell in the form of
    # string, so they can be actually read. in this particular case we are asking the method to return the JOB TITLE
    def __str__(self):
        return self.title

