from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

class IndexView(View): 
	""" this class displays the index get request """
	def get(self, request):
		return render(request, "cv/index.html")
