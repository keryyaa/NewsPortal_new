from django import forms
from .models import Post


# Существует несколько видов создания форм
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'text',
            'category',
            'categoryType',
        ]

# Для показа что еще можно делать так
# class ProductForm(forms.Form):
#     name = forms.CharField(label='Name')
#     description = forms.CharField(label='Description')
#     quantity = forms.IntegerField(label='Quantity')
#     category = forms.ModelChoiceField(
#         label='Category', queryset=Category.objects.all(),
#     )
#     price = forms.FloatField(label='Price')
