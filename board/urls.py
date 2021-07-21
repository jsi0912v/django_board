from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='board'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/',views.posting, name='posting'),
    path('new_post/', views.new_post, name='new_post'),
    path('remove_post/<int:pk>/', views.remove_post, name='remove_post'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)