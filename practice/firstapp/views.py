from django.shortcuts import render

from django.http import Http404

from .models import Admission

def home(request):
	admission=Admission.objects.all()
	return render(request,'home.html', {'admission':admission})
	

def student_detail(request, student_id):
		return HttpResponse(f'<p>student_detail view with id {student_id}</p>')



def student_detail(request,student_id):
	try:
		student=Admission.objects.get(id=student_id)
	except Admission.DoesNotExist:
		raise Http404('Student does not exist')
	return render(request, 'student_detail.html', {
		'student':student
		})