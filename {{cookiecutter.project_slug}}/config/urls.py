from django.contrib import admin
{% if cookiecutter.use_wagtail %}
from django.urls import path, include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.conf import settings
from django.conf.urls.static import static
{% else %}
from django.urls import path
from django.views.generic import TemplateView
{% endif %}

{% if cookiecutter.use_wagtail %}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('', include(wagtail_urls)),
]
{% else %}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]
{% endif%}

{% if cookiecutter.use_wagtail %}
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
{% endif %}
