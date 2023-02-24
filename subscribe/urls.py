from django.urls import path
import subscribe.views as v


urlpatterns = [
    path('subscribe/', v.subscribe, name="subscribe"),
    path('thank_you/', v.thank_you, name="thank_you"),

]
