from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('books/', include('books.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
