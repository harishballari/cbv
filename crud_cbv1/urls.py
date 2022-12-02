from django.contrib import admin
from django.urls import path,include
from app1.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index.as_view(),name='index'),
    path('app1/',include('app1.urls',namespace='app1'))
]

