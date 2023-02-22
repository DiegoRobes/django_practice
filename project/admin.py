from django.contrib import admin
import app_folder.models as m


# this class here is used to add some fields to the presentation of your objects in the list view from the admin panel
# this is similar to the __str__ method that returns the title in the models.py file, but this one is a little stronger
# bc you can use it to customize the list view further. only valid headers can be added
# notice the class has to be passed as an argument in the
# registration of the model down bellow
# if needed, you can also use the __str__ representation method, like this:
# list_display = ("__str__", "title", "salary", "date")
class JobAdmin(admin.ModelAdmin):
    list_display = ("__str__", "title", "salary", "date")

# according to this class, you should get 4 headers in the list view of the admin panel 


# MODELS
admin.site.register(m.JobPost, JobAdmin)
