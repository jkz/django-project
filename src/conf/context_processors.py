import path

from django.conf import settings

def static(request):
    "Shorthand static URLs. In debug mode, the JavaScript is not minified."
    static_url = path.path(settings.STATIC_URL)
    prefix = 'src' if settings.DEBUG else 'min'
    return {
        'CSS_URL': static_url / 'css',
        'IMG_URL': static_url / 'img',
        'JS_URL': static_url / 'js' / prefix,
    }
