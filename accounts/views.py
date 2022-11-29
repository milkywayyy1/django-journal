from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.shortcuts import render,redirect
from people.detection import FaceRecognition
from people.forms import UserCreateForm
from django.contrib import messages

from django_journal.settings import STUDENT
from people.models import User


class UserTypeRedirectView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.user_status == STUDENT:
            return reverse_lazy('student_lk')
        else:
            return reverse_lazy('group_student_list')


faceRecognition = FaceRecognition()

def home(request):
    return render(request, 'faceDetection/home.html')


def register(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            print("IN HERE")
            messages.success(request,"SuceessFully registered")
            addFace(request.POST['face_id'])
            redirect('home')
        else:
            messages.error(request,"Account registered failed")
    else:
        form = UserCreateForm()

    return render(request, 'faceDetection/register.html', {'form':form})

def addFace(face_id):
    face_id = face_id
    faceRecognition.faceDetect(face_id)
    faceRecognition.trainFace()
    return redirect('/')

def login(request):
    face_id = faceRecognition.recognizeFace()
    print(face_id)
    return redirect('greeting', str(face_id))

def Greeting(request,face_id):
    face_id = int(face_id)
    context ={
        'user' : User.objects.get(face_id = face_id)
    }
    return render(request, 'faceDetection/greeting.html', context=context)

