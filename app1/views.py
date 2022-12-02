from django.shortcuts import render,HttpResponseRedirect
from app1.models import Course
from app1.forms import CourseForm
from django.views.generic.base import TemplateView,RedirectView,View

# Create your views here.

class Index(TemplateView):
    template_name = 'app1/index.html'

    def get_context_data(self, **kwargs):
        courses = Course.objects.all()
        form = CourseForm()
        context = {'courses':courses,'form':form}
        return context

    def post(self,request):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')

class Update(View):
    def get(self,request,id):
        course = Course.objects.get(pk=id)
        form = CourseForm(instance=course)
        return render(request,'app1/update.html',{'form':form})

    def post(self,request,id):
        course = Course.objects.get(pk=id)
        form = CourseForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')

class Delete(RedirectView):
    url = '/'
    def get_redirect_url(self, *args,**kwargs):
        id = kwargs['id']
        Course.objects.get(pk=id).delete()
        return super().get_redirect_url(*args,**kwargs)