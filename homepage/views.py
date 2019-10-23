from django.shortcuts import render
from django.http import HttpResponseRedirect
from homepage import forms as homepage
from homepage import models as homepageModels
from django.contrib import messages

response = {'form': homepage.Biodata_Forms}
# Create your views here.
def index(request):
	return render(request, 'homepage/index.html',response)

def form_post(request):
	form = homepage.Biodata_Forms(request.POST or none)
	if(request.method=='POST' and form.is_valid()):
		response['name']=request.POST['name']
		response['email']=request.POST['email']
		data=homepageModels.biodata(name=response['name'],email=response['email'])
		data.save()
		messages.success(request, 'Data Berhasil Ditambahkan')
		return HttpResponseRedirect("/")
	else :
		return HttpResponseRedirect("/")

def data_get(request):
	data=homepageModels.biodata.objects.all().values()
	response['data']=data
	return render(request,'homepage/data.html', response)