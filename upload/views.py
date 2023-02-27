from django.shortcuts import render
import upload.forms as f


# Create your views here.
def upload_image(request):
    upload_form = f.UploadImage()
    if request.POST:
        upload_form = f.UploadImage(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.save()
            saved_object = upload_form.instance
            print("IMG UPLOADED")
            context = {"success": saved_object}
            return render(request, 'upload/upload_img.html', context)
    else:
        context = {"form": upload_form}
        return render(request, 'upload/upload_img.html', context)


def upload_file(request):
    upload_form = f.UploadFile()
    if request.POST:
        upload_form = f.UploadFile(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.save()
            saved_object = upload_form.instance
            context = {"success": saved_object}
            return render(request, 'upload/upload_file.html', context)
    else:
        context = {"form": upload_form}
        return render(request, 'upload/upload_file.html', context)
