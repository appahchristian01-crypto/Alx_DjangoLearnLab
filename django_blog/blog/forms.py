from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# -----------------------------
# Post Form
# -----------------------------
class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        # Use these fields ONLY if you have a Tag model added
        # If you don’t have tags, remove 'tags'
        fields = ['title', 'content']  

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title here'}),
            'content': forms.Textarea(attrs={'rows': 8, 'placeholder': 'Write your post...'}),
        }


# -----------------------------
# Comment Form
# -----------------------------
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


# -----------------------------
# User Registration Form
# -----------------------------
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
