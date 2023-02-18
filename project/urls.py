from django.urls import path
import app_folder.views as v

urlpatterns = [
    path('', v.home, name="home"),
    path('job/<int:job_id>', v.job, name="job_by_id"),
    path('all_jobs', v.all_jobs, name="all_jobs")
]
