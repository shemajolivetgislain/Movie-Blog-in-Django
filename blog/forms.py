from django import forms
from .models import Comment


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'author', 'intro', 'image', 'body', "date_added"]
#
#         widgets = {
#             'title': forms.CharField(attrs={'class': 'form-control'}),
#             'author': forms.TextInput(attrs={'class': 'form-control'}),
#             'intro': forms.TextInput(attrs={'class': 'form-control'}),
#             'image': forms.ImageField(attrs={'class': 'form-control'}),
#             'body': forms.TextInput(attrs={'class': 'form-control'}),
#             'date_added': forms.DateField(attrs={'class': 'form-control'}),
#         }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
