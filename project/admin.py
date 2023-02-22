from django.contrib import admin
import app_folder.models as m


# this class here is used to add some fields to the presentation of your objects in the list view from the admin panel
# this is similar to the __str__ method that returns the title in the models.py file, but this one is a little stronger
# bc you can use it to customize the list view further. only valid headers can be added
# notice the class has to be passed as an argument in the
# registration of the model down bellow
# if needed, you can also use the __str__ representation method, like this:
# list_display = ("__str__", "title", "salary", "date")
# then you have the filter that adds precisely that to your list view
# a search field is also included, it allows user to search by title, as specified
# fieldsets allows you to group your sections in a more orderly manner. NOTE: you can only add editable
# fields to its sections. careful with grouping them in a tuple. in the second section, the "classes" key refers to a
# css property that will collapse the section. this is in case you have a very lengthy section
class JobAdmin(admin.ModelAdmin):
    list_display = ("__str__", "title", "salary", "date")
    list_filter = ("date", "title")
    search_fields = ("title", "description")
    # fields = (("title", "description"), "salary")
    # exclude = ("date",)
    fieldsets = (("Basics", {"fields": ("title", "salary")}),
                 ("About", {"classes": ("collapse",),
                            "fields": ("description", )}))

# according to this class, you should get 4 headers; 2 filters and 1 search field in the list view of the admin panel,
# everything presented in 2 sections, one for "basics", and other for "about"


# MODELS
admin.site.register(m.JobPost, JobAdmin)
