# from django.shortcuts import render,redirect
# from django.http import HttpResponse,Http404,HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
# # Create your views here.
# @login_required
# def index(request):
#     current_user = request.user
#     try:
#         profile = UserProfile.objects.get(user = current_user)
#     except:
#         return redirect('edit_profile',username = current_user.username)

#     try:
#         posts = Post.objects.filter(neighborhood = profile.neighborhood)
#     except:
#         posts = None

#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = current_user
#             post.neighborhood = profile.neighborhood
#             post.type = request.POST['type']
#             post.save()

#             if post.type == '1':
#                 recipients = UserProfile.objects.filter(neighborhood=post.neighborhood)
#                 for recipient in recipients:
#                     send_a_email(post.title,post.content,recipient.email)

#         return redirect('index')
#     else:
#         form = PostForm()
#     return render(request,'index.html',{"posts":posts,"profile":profile,"form":form})

