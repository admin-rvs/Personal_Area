# from django.contrib import admin
from django.urls import path, include


handler400 = 'adminlte_full.views.handler400'
handler403 = 'adminlte_full.views.handler403'
handler404 = 'adminlte_full.views.handler404'
handler500 = 'adminlte_full.views.handler500'


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('adminlte_full.urls')),
    path('', include('core.urls')),
]
