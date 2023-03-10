from django.db import models
from django.utils.text import slugify

# list of field types https://docs.djangoproject.com/en/4.1/ref/models/fields/


# we are doing a one-to-many relationship with this model:
class Location(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=100)


# many-to-one relationships will be demonstrated with this one:
class Author(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)


# many-to-many relationships:
class Skills(models.Model):
    name = models.CharField(max_length=100)


# basic table with the key to the other tables
class JobPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    # title was the initial field, now we add others with different type fields
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()
    # a slug is a human-friendly url that can be placed on the url bar on your browser
    slug = models.SlugField(null=True, max_length=50, unique=True)
    # this one is the relationship for the first model
    # the CASCADE function is used to delete the Location object made in the other table, the one that holds the
    # relationship to this particular object in JobPost table. this is to avoid having locations without anything to
    # relate to in the other table
    location = models.OneToOneField(Location, null=True, on_delete=models.CASCADE)
    # this one is the foreign key to the Author table. same deal with cascade function
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    skills = models.ManyToManyField(Skills)

    # this messy function is responsible to create the slugs from the titles field of the model.
    # after you create the new object using the model in the console, you can see the result of this funct in the
    # database, where the slug field should have the title slugified
    # the second line in this function is used to make sure that even after the title of the object is changed, the
    # slug remains the same. this is a good practice that will prevent you from having broken urls on your app.
    # this condition only checks if the object has an id, meaning if it already exists
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)

    # once you add these new field, you need to sync them using the terminal command py manage.py makemigrations
    # follow instructions on the command line, and then you'll see the new migration file created on migrations folder
    # after that clear command line, and run py manage.py migrate to se the new fields added to the database
    # in the browser

    # this next method is helpful to fetch the information from the objects inside the django shell and in the
    # view for the app, in the form of string, so they can be actually read.
    # in this particular case we are asking the method to return the JOB TITLE
    def __str__(self):
        return self.title
