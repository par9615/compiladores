import json
import os
import copy

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .createSupplies import Supplier

def setup(request):
	data = {
		"js" : ["setup.js"]
	}
	return render(request, "setup/table.html", data)

def getRules(request):
	supplier = Supplier()
	return HttpResponse(json.dumps(supplier.getRules()), content_type ='application/json')

@require_POST
def setMatrix(request):
	matrixStringKeys = json.loads(request.POST['json'])
	matrix = {}
	for key in matrixStringKeys:
		matrix[int(key)] = copy.copy(matrixStringKeys[key])
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'aParser\\matrix.py')
	f = open(file_path, 'w')
	f.write('matrix = {\n')
	for state in matrix:
		f.write('\t' + str(state) + ' : {\n')
		for key in matrix[state]:
			f.write('\t\t\'' + key + '\' : \'' + matrix[state][key] + '\',\n')
		f.write('\t},\n')
	f.write('}\n')
	f.close()

	return HttpResponse(json.dumps(matrix), content_type='application/json')