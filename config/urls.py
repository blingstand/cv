#python libs
import os

#django libs
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('cv/admin/', admin.site.urls),
    path('cv/', include(('cv.urls', 'cv'), namespace='cv')),
]

if os.environ["ENV"] == "local" or os.environ["ENV"] == "heroku":
	urlpatterns.append(
		path('', include(('cv.urls', 'cv'), namespace='cv')),
		)


