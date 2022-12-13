# Импортируем джинерики
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Импортируем наши модели от куда будем брать данные
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy


# Создаем класс представление, наследуемся от джинерика ListView
class PostList(ListView):
    # Предаем нашу модель с данными
    model = Post
    # Если хотим подключаем сортировку
    ordering = '-time_in'
    # Прописываем путь к html файлу отображающему нашу страницу
    template_name = 'news/PostList.html'
    # Обозначаем имя по которому мы сможем обращаться в шаблонах к классу
    context_object_name = 'PostList'
    # Добавляем пагинацию для вывода определенного кол-ва новостей
    paginate_by = 8

    # # Можем переопределить получение данных и добавить туда что-нибудь или что-то еще с ними сделать
    # def get_context_data(self, **kwargs):
    #     date_context = super().get_context_data(**kwargs)
    #     # Добавляем в контекст объект фильтрации.
    #     date_context['filterset'] = self.filterset
    #     return date_context


class PostSearch(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'news/PostSearch.html'
    context_object_name = 'PostSearch'
    paginate_by = 8
    paginate_orphans = 1

    # Можем переопределить получение данных и добавить туда что-нибудь или что-то еще с ними сделать
    def get_context_data(self, **kwargs):
        date_context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        date_context['filterset'] = self.filterset
        return date_context

    # Переопределяем функцию получения списка новостей
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict,
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs


class PostDetail(DetailView):
    model = Post
    template_name = 'news/PostDetail.html'
    context_object_name = 'PostDetail'


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news/PostCreate.html'
    success_url = reverse_lazy('PostList')


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news/PostCreate.html'
    success_url = reverse_lazy('PostList')


class PostDelete(DetailView):
    model = Post
    template_name = 'news/PostDelete.html'
