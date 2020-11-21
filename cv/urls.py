from django.urls import path
from . import views as v

urlpatterns = [
    path(r'', v.IndexView.as_view(), name="index"),
    path(r'puzzle', v.PuzzleView.as_view(), name="puzzle"),
    ]
