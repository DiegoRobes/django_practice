from django.shortcuts import render, redirect
from django.urls import reverse
import subscribe.models as m
import subscribe.forms as f


# Create your views here.
# after importing the form model, you can create instances of it in your
# view function. depending on the request type, different functions can be used
# we are using the cleaned_data[] function to get the data from the form and pass it into the database
# after the process of catching the info and making a new record on the DB, we make use of the redirect and
# reverse shortcuts to send the user to a designated thank you page
def subscribe(request):
    subscribe_form = f.SubscribeForm()
    if request.POST:
        subscribe_form = f.SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            name = subscribe_form.cleaned_data["name"]
            last_name = subscribe_form.cleaned_data["last_name"]
            email = subscribe_form.cleaned_data["email"]
            to_save = m.Subscribe(name=name,
                                  last_name=last_name,
                                  email=email)
            to_save.save()
        else:
            context = {"form": subscribe_form}
            return render(request, 'subscribe/subscribe.html', context)

        return redirect(reverse("thank_you"))

    context = {"form": subscribe_form}
    return render(request, 'subscribe/subscribe.html', context)


def thank_you(request):
    context = {}
    return render(request, 'subscribe/thank_you.html', context)
