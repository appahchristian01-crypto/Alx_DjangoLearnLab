from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from taggit.forms import TagWidget   # <-- REQUIRED for tagging functionality


# -----------------------------
# Post Form (with TagWidget)
# -----------------------------
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter title here'
            }),
            'content': forms.Textarea(attrs={
                'rows': 8,
                'placeholder': 'Write your post...'
            }),
            'tags': TagWidget(attrs={
                'placeholder': 'Add tags separated by commas'
            }),  # <-- REQUIRED by the task
        }


# -----------------------------
# Comment Form
# -----------------------------
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your comment here...'
            })
        }

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content or len(content.strip()) == 0:
            raise forms.ValidationError("Comment cannot be empty.")
        return content
