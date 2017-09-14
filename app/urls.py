from django.conf.urls import url, include

from app.views import pdf_sample

urlpatterns = [
    url(r'^pdf_sample/?$', pdf_sample),
]