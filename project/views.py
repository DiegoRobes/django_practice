from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template import loader

job_title = [
    "FIRST JOB",
    "SECOND JOB"
]

job_description = [
    "description 1. muthafaicka",
    "description 2"
]


class Object:
    x = 5


# Create your views here.
# the context dictionary is used to feed the jinja templates. each key is a keyword. in the render function,
# you pass the whole dict as an arg and then in the template you choose which keys to use.
# these keys can be many types of objects
# render function takes 3 args, the request, the name of the template to render and the context.
# context can be empty, but be careful to specify the route to the template properly, and to register
# this route on the config of your project
def home(request):
    list_of_words = ["1", "2", "3"]
    tem = Object()
    context = {"name": "Itzel",
               "assume": "how you doing?",
               "list": list_of_words,
               "object": tem
               }
    return render(request, "app_folder/index.html", context=context)


def job(request, job_id):
    try:
        context = {
            "job_title": job_title[job_id],
        }
        # return reverse("job_by_id", args=job_id, context=context)
        # this one if to get the url by name, as defined in urls.py
        return render(request, "app_folder/job_detail.html", context=context)
    except IndexError as e:
        return HttpResponseNotFound("You lost, fren?")


def all_jobs(request):
    context = {
        "all_jobs": job_title,
        "all_descriptions": job_description
    }
    return render(request, "app_folder/all_jobs.html", context=context)
