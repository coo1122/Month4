from django import forms
from posts.models import Post

class PostCreateform(forms.Form):
    image=forms.ImageField()
    title=forms.CharField()
    content=forms.CharField()

    def clean_title(self):
        cleaned_data = super().clean()
        title = self.cleaned_data.get('title')
        if title and title.lower() == "python":
            raise forms.ValidationError("title python is not allowed")
        return title

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        title = cleaned_data.get('title')
        if title and content and title.lower() == content.lower():
            raise forms.ValidationError("title and content should not be same")
        return cleaned_data


class PostCreateform2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

    def clean_title(self):
        cleaned_data = super().clean()
        title = self.cleaned_data.get('title')
        if title and title.lower() == "python":
            raise forms.ValidationError("title python is not allowed")
        return title

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        title = cleaned_data.get('title')
        if title and content and title.lower() == content.lower():
            raise forms.ValidationError("title and content should not be same")
        return cleaned_data


