from django.shortcuts import get_object_or_404, render, redirect
from .models import Flan
from .forms import ContactFormForm
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth.decorators import login_required #para que solo los usuarios logueados puedan ver la pagina welcome



from django.shortcuts import render, redirect
from .models import Flan, Comment
from .forms import CommentForm

def add_comment(request, flan_id):
    flan = Flan.objects.get(id=flan_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.flan = flan
            comment.save()
            return redirect('flan_detail', flan_id=flan_id)
    else:
        form = CommentForm()
    
    return render(request, 'add_comment.html', {'form': form, 'flan': flan})


# Create your views here.
def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html',{'flanes': flanes_publicos})

def about(request):
    return render(request, 'about.html')

def exito(request):
    return render(request, 'exito.html')

def flan_detail(request, flan_id):
    flan = get_object_or_404(Flan, pk=flan_id)
    comments = Comment.objects.filter(flan=flan)
    return render(request, 'flan_detail.html', {'flan': flan, 'comments': comments})

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    
    return render(request, 'welcome.html', {'flanes':flanes_privados})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else: 
        form = ContactFormForm()

    return render(request, 'contacto.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registrationlogin.html'

class CustomLogoutView(LogoutView):
    next_page = '/'





    