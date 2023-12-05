from django.forms import ModelForm
from .models import PhotoPost,Category

class PhotoPostForm(ModelForm):

    class Meta:
        model = PhotoPost
        fields = ['category', 'title', 'comment', 'image1', 'image2']

class CategoryForm(ModelForm):
    class Meta:
        model =Category
        fields =["title"]
