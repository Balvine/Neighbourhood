
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import UserProfile,Post,Neighborhood,Company,Comment
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm,CompanyForm,PostForm,CommentForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import CompanySerializer
from .email import send_a_email

# Create your views here.
@login_required
def index(request):
    current_user = request.user
    # try:
    #     profile = UserProfile.objects.get(user = current_user)
    # except:
    #     return redirect('edit_profile',username = current_user.username)

    try:
        posts = Post.objects.filter(neighborhood = profile.neighborhood)
    except:
        posts = None

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.neighborhood = profile.neighborhood
            post.type = request.POST['type']
            post.save()

            if post.type == '1':
                recipients = UserProfile.objects.filter(neighborhood=post.neighborhood)
                for recipient in recipients:
                    send_a_email(post.title,post.content,recipient.email)

        return redirect('index')
    else:
        form = PostForm()
    return render(request,'index.html',{"posts":posts,"form":form})

@login_required
def edit_profile(request,username):
    current_user = request.user
    if request.method == 'POST':
        try:
            profile = UserProfile.objects.get(user=current_user)
            form = UserProfileForm(request.POST,instance=profile)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = current_user
                profile.save()
            return redirect('index')
        except:
            form = UserProfileForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = current_user
                profile.save()
            return redirect('index')
    else:
        if UserProfile.objects.filter(user=current_user):
            profile = UserProfile.objects.get(user=current_user)
            form = UserProfileForm(instance=profile)
        else:
            form = UserProfileForm()
    return render(request,'edit_profile.html',{"form":form})

@login_required
def companies(request):
    current_user = request.user
    neighborhood = UserProfile.objects.get(user = current_user).neighborhood
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = current_user
            company.neighborhood = neighborhood
            company.save()
            return redirect('companies')
    else:
        form = CompanyForm()

    try:
        companies = Company.objects.filter(neighborhood = neighborhood)
    except:
        companies = None

    return render(request,'companies.html',{"companies":companies,"form":form})
@login_required
def post(request,id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
        return redirect('post',id = post.id)
    else:
        form = CommentForm()
    return render(request,'post.html',{"post":post,"comments":comments,"form":form})

class CompanyList(APIView):
    def get(self, request, format=None):
        all_companies = Company.objects.all()
        serializers = CompanySerializer(all_companies, many=True)
        return Response(serializers.data)

@login_required
def search(request):
    current_user = request.user
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        companies = Company.objects.filter(name__icontains=search_term)
        return render(request,'search.html',{'companies':companies})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})