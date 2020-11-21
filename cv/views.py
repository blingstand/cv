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

class PuzzleView(View):
	def get(self, request):
		projects = get_projects(13)
		print(projects) 		
		context={
			'puzzle_parts': projects
		}
		return render(request, "cv/puzzle.html", context)