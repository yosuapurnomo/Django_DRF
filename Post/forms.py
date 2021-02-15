from django import forms
from .models import PostModel

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = '__all__'

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('caption', 'image', 'slug')

    def save(self, commit=True):
    	posts_model = self.instance
    	posts_model.caption = self.cleaned_data['caption']

    	if self.cleaned_data['image']:
    		posts_model.image = self.cleaned_data['image']

    	if commit:
    		posts_model.save()

    	return posts_model