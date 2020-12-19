from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .datas import exp_prof, educ, all_btn, skills, ten_spans, all_success
from .utils import get_projects

class IndexView(View): 
	""" this class displays the index get request """
	def get(self, request):
		context = {
		'exp_prof': exp_prof,
		'education': educ, 
		'all_btn': all_btn, 
		'skills': skills,
		'ten_spans' : ten_spans,
		"all_success" : all_success,
		}
		return render(request, "cv/index.html", context)

class DP7View(View):
	"""this class renders description for p7"""
	def get(self, request): 
		"""renders the get request for /description-p7 path"""
		return render(request, "cv/description/p7.html")

class DP8View(View):
	"""this class renders description for p8"""
	def get(self, request): 
		"""renders the get request for /description-p8 path"""
		return render(request, "cv/description/p8.html")

class DP13View(View):
	"""this class renders description for p13"""
	def get(self, request): 
		"""renders the get request for /description-p13 path"""
		return render(request, "cv/description/p13.html")

