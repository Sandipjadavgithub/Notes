from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import*
from .forms import*
from django.views import generic
from django.urls import reverse_lazy



class Home(generic.ListView):
    template_name = 'home.html'
    model = Note
    Queryset = Note.objects.all()
class Createnote(generic.CreateView):
    model = Note
    template_name = 'create-note.html'
    form_class = Noteform
    success_url=reverse_lazy('home')
class UpdateNote(generic.UpdateView):
    model = Note
    template_name = 'update.html'
    form_class = Noteform
    success_url=reverse_lazy('home')
class DeleteNote(generic.View):
    def post(self, *args, **kwargs):
        note = get_object_or_404(Note, pk=kwargs.get('pk'))
        note.delete()
        return redirect('home')
def register(request):
 if request.user.is_authenticated:
     return redirect('home')
 if request.method == 'POST':
      username = request.POST.get('username')
      email = request.POST.get('email')
      password = request.POST.get('password')

      all_user = User.objects.filter(username=username)

      if all_user:
          messages.error(request,"Username is already Exists !")
          return redirect('register')


      new_user =User.objects.create_user(username=username, email=email, password=password)
      new_user.save()
      messages.success(request,"User Created Successfully! Login Now")
      return redirect('login')
 return render(request, 'register.html',{})
def loginpage(request):
  
    if request.user.is_authenticated:
     return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        valid_user =authenticate(username=username,password=password)

        if valid_user is not None:
            login(request,valid_user)
            return redirect('home')
        else:
            messages.error(request,"Username and password is Incorrect !")
            return redirect('login')
    return render(request, 'login.html',{})
def logoutpage(request):
    logout(request)
    return redirect('login')