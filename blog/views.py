from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F, Q
from blog.models import posts
from . import data
import operator
# Create your views here.

def index(req):
    # post = posts.objects.all().values()
    post = posts.objects.filter(Q(author="Josh")| Q(author="Kunle")| Q(author="Isaac"))   
    return render(req,"blog/index.html", {
      "posts": data.post_data  
    })

def latest(req):
    latest_post = posts.objects.all().order_by("-date")  
    
    return render(req, "blog/index.html", {
      'posts': latest_post  
    })
def top(req):
    top_post = posts.objects.all().order_by("-views")

    print(top_post)
    return render(req, "blog/index.html", {
      'posts': top_post  
    })

def post(req, slug):
    
    current_post = posts.objects.get(slug = slug)

    posts.objects.filter(slug= slug).update(views= F('views') + 1 )
    
    return render(req,"blog/post.html" ,{
        "post": current_post
        
    })
    
    
def create_post(req):
    current_post = data.post_date[0]
    post1 = posts(title =current_post['title'], slug = current_post['slug'],author = current_post['author'], author_img = current_post['author_img'], views=0,content = current_post['content'])
    post1.save()
    return HttpResponse("SAVED") 