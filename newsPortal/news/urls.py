# Создали файл urls.py импортируем необходимые функции
from django.urls import path
# Импортируем наши представления
from .views import PostList, PostDetail, PostCreate, PostSearch, PostUpdate, PostDelete

# Пишем пути для наших представлений
urlpatterns = [
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('', PostList.as_view(), name='PostList'),
    # В пути можем встретить int для того что бы на данном этапе проходила
    # проверка, а не дальше так же будет работать и без int
    path('<int:pk>', PostDetail.as_view(), name='PostDetail'),
    # Путь для создания постов
    path('create/', PostCreate.as_view(), name='PostCreate'),
    # Путь для поиска
    path('search/', PostSearch.as_view(), name='PostSearch'),
    # Путь для редактирования
    path('<int:pk>/update/', PostUpdate.as_view(), name='PostUpdate'),
    # Путь для удаления
    path('<int:pk>/delete/', PostDelete.as_view(), name='PostDelete'),
]
