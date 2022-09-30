
from django.shortcuts import get_object_or_404, render,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from post.models import Post
from .forms import PostForm
from django.contrib import messages

def show_my_post(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    posts = list(Post.objects.filter(visibility=["1"])) + list(Post.objects.filter(user=request.user))
    posts = list(set(posts))

    
    return render(request,"post/showposts.html",{"posts":posts})

# @login_required("login")
def create_post(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    elif request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        # form.cleaned_data['user'] = request.user
        if form.is_valid():
            post_obj = Post(**form.cleaned_data)
            post_obj.user = request.user
            post_obj.save()
            print("New post Saved...")
            return HttpResponseRedirect(reverse("mypost"))
        else:
            messages.error(request,"Form is invalid")
            print("Invalid form")
            print(form.cleaned_data)
    
    
    form = PostForm()

    return render(request,"post/create.html",{"form":form})

# @login_required("login")
def edit_post(request,id):
    p = get_object_or_404(Post,pk=id)
    if (not request.user == p.user) and (not request.user.is_superuser):
        return HttpResponseRedirect(reverse("mypost"))
    elif request.method=="POST":
        form = PostForm(request.POST,request.FILES,instance=p)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("mypost"))            
    else:
        form = PostForm(instance=p)
    
    return render(request,"post/edit.html",{"form":form,"post":p})

def check(request,id):
    post = get_object_or_404(Post,pk=id)
    x = request.user == post.user
    return HttpResponse(str(x))

# @login_required("login")
def delete_post(request,id):
    p = get_object_or_404(Post,pk=id)
    if request.user==p.user or request.user.is_superuser:
        p.delete()
    return HttpResponseRedirect(reverse("mypost"))

def go_to_post(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    post = get_object_or_404(Post,pk=id)
    return render(request,"post/show_detail_post.html",{"post":post,"showactions":post.user==request.user})