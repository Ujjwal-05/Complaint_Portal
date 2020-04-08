from django.shortcuts import render
from .models import Complaint
from django.contrib.auth.models import models
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
)
# Create your views here.
class ComplaintCreateView(LoginRequiredMixin, CreateView):
    model =Complaint
    fields = ['type','title','problem']
    template_name = 'complaint/registercomplaint.html'
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        #form.instance.stream =user.stream
        #form.instance.gender=user.gender
        return super().form_valid(form)

class ComplaintUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Complaint
    fields = ['type','title','problem']
    template_name = 'complaint/detailcomplaint.html'
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        complaint_user = self.get_object()
        if self.request.user == complaint_user.user:
            return True
        return False

class  ComplaintDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Complaint
    success_url = '/'
    template_name = 'complaint/complaint_confirm_delete.html'
    def test_func(self):
        complaint_user = self.get_object()
        if self.request.user == complaint_user.user:
            return True
        return False

def showcomplaints(request,i):
    i=int(i)
    if i>0:
        com = Complaint.objects.get(id=i)
        return render(request, 'complaint/showcomplaints.html', {'com': com})
    elif i==-1:
        comp=Complaint.objects.filter(status=True)
        return render(request,'complaint/showcomplaints.html',{'comp':comp,'status':i})
    elif i==-2:
        comp = Complaint.objects.filter(status=False)
        return render(request, 'complaint/showcomplaints.html', {'comp': comp,'status':i})
    else:
        if i==-3:
            comp = Complaint.objects.all()
            return render(request, 'complaint/showcomplaints.html', {'comp': comp,'status':i})
        return render(request,'base.html')

def user_complaints(request):
    user=request.user
    comp=Complaint.objects.filter(user=user)
    return render(request,'complaint/usercomplaints.html',{'comp':comp})

def solvecomplaint(request):
    if request.method=='POST':
       id=request.POST['id']
       comp=Complaint.objects.get(id=id)
       comp.status=True
       comp.save()
       return render(request,'complaint/showcomplaints.html')
    return render(request, 'complaint/showcomplaints.html')