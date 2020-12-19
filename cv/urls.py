from django.urls import path
from . import views as v

urlpatterns = [
    path(r'', v.IndexView.as_view(), name="index"),
    path(r'description-p7', v.DP7View.as_view(), name="dp-7"),
    path(r'description-p8', v.DP8View.as_view(), name="dp-8"),
    path(r'description-p13', v.DP13View.as_view(), name="dp-13"),
    ]
