from django.shortcuts import render_to_response
from schedules.models import *

#Las materias deben ser creadas seguidas para cada grupo.

# Create your views here.
def home(request):
	subjects = Subject.objects.all()
	matriz = []
	groups = Group.objects.all()
	elemento = 0

	for i in xrange(len(groups)):
		tmp = []
		for j in xrange(4):
			elemento += 1
			tmp.append(elemento)
		matriz.append(tmp)

	for i in xrange(len(groups)):
		for j in subjects:
			if groups[i].pk == j.Teaching.pk:
				matriz[i][(j.pk-1)%4] = j.Teach_by

	
	for i in xrange(len(groups)):
		for j in xrange(4):
			tmp = 0
			if matriz[(i)%len(groups)][(j)%4] == matriz[(i+1)%len(groups)][(j)%4]:
				tmp = matriz[(i)%len(groups)][(j+1)%4]
				matriz[(i)%len(groups)][(j+1)%4] = matriz[(i)%len(groups)][(j)%4]
				matriz[(i)%len(groups)][(j)%4] = tmp

	return render_to_response(
		'home.html',
		{
			'matriz':matriz,
		}
	)