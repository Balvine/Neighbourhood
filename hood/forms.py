
from django import forms
from .models import UserProfile,Neighborhood,Company,Post,Comment

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','bio','neighborhood','email')

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['user','neighborhood']

class PostForm(forms.ModelForm):
    CHOICES = (('1', 'Amber',), ('2', 'Normal',))
    type = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    class Meta:
        model = Post
        fields = ('title','content','type')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
