from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/', include(('rest.urls', 'rest'))),
    path('docs/', include('rest.urls.schemes')),
    path('', RedirectView.as_view(url='/admin'))
]
