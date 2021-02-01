from django.shortcuts import render, HttpResponse, get_object_or_404, Http404
from .models import photo
from .models import wedding
from .models import Contact
from .models import Article
from django.shortcuts import redirect
from collections import Counter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

           
def index(request):

  dests = photo.objects.all()
  context = {'dests':dests}

  return render(request, "index.html", context)

def gallery(request):
  
  gals = wedding.objects.all()
  context = {'gals' :gals}

  return render(request, "gallery.html", context)    

def about(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone'] 
        message = request.POST['message']
  
        about = Contact(name=name, phone=phone, email=email, message=message)
        about.save();
        print('Thank You')
        return redirect('about')
    else:   
      return render(request, "about.html")

def services(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone'] 
        message = request.POST['message']
  
        services = Contact(name=name, phone=phone, email=email, message=message)
        services.save();
        print('Thank You')
        return redirect('services')
    else: 
      return render(request, "services.html") 


def blog(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']

        blog = Contact(name=name, email=email)
        blog.save();
        print('Thank You')
        return redirect('blog')
    else:
      act_list = Article.objects.all() #.order_by("-id")
    
      paginator = Paginator(act_list, 3) # Show 25 contacts per page.
      page = request.GET.get('page')
      acts = paginator.get_page(page)     
      try:
        acts = paginator.page(page)
      except PageNotAnInteger:
        acts = paginator.page(1)
      except EmptyPage:
        acts = paginator.page(paginator.num_pages)
      context = {'acts':acts}
    return render(request, "blog.html", context) 

def contact(request):
  
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone'] 
        message = request.POST['message']
  
        contact = Contact(name=name, phone=phone, email=email, message=message)
        contact.save();
        print('Thank You')
        return redirect('contact')
    else: 
      return render(request, "contact.html") 

def blogpost(request, slug):
  

    try:
     page = get_object_or_404(Article, slug=slug)
     acts = Article.objects.filter(slug=slug)
     context = {'acts':acts}
     return render(request, "blogpost.html", context)
    
    except Article.DoesNoExist:
      raise Http404
   
  
