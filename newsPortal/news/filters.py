from .models import Post, Category
from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter
from django.forms import DateTimeInput


# Создаем свой набор фильтров для модели Post.
class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='Любая'
    )
    time_in = DateTimeFilter(
        field_name='time_in',
        lookup_expr='gt',
        label='Дата',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'}
        )
    )

    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            'title': ['icontains'],

        }
