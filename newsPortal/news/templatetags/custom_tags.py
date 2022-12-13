from datetime import datetime
from django import template

register = template.Library()


@register.simple_tag()
def current_time(format_string='%b %d %Y'):
    return datetime.utcnow().strftime(format_string)


# создаем тег для работы поиска и пагинации
@register.simple_tag(takes_context=True)  # сообщает Django, что для работы тега требуется передать контекст
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()  # позволяет скопировать все параметры текущего запроса
    for k, v in kwargs.items():  # Далее по указанным полям мы просто устанавливаем новые значения,
        d[k] = v  # которые нам передали при использовании тега
    return d.urlencode()  # Кодируем параметры в формат, который может быть указан в строке браузера
