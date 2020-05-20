from django.urls import path
from . import views as v

urlpatterns = [
    path(r'', v.IndexView.as_view(), name="index"),
    path(r'index/', v.IndexView.as_view(), name="index"),
    ]