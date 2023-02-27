from django.urls import path
import upload.views as v

urlpatterns = [
    path('image/', v.upload_image, name="image"),
    path('file/', v.upload_file, name="file"),

]
