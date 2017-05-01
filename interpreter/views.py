import json
import os
import copy

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .ascendantAnalysis.setupGrammar import Grammar

def setup(request):
	data = {
		"js" : ["setup.js"]
	}
	return render(request, "setup/table.html", data)

def getRules(request):
	grammar = Grammar()
	return HttpResponse(json.dumps(grammar.getRules()), content_type ='application/json')

@require_POST
def setMatrix(request):
	grammar = Grammar()
	matrixStringKeys = json.loads(request.POST['json'])
	matrix = {}
	for key in matrixStringKeys:
		matrix[int(key)] = copy.copy(matrixStringKeys[key])
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'ascendantAnalysis\\matrix.py')
	f = open(file_path, 'w')
	f.write('matrix = ' + repr(matrix) + '\n')
	f.close()

	return HttpResponse(json.dumps(matrix), content_type='application/json')

def getGrammar(request):
	grammar = Grammar()
	return HttpResponse(json.dumps(grammar.getRules()), content_type ='application/json')