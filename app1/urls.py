from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('update/<int:id>',views.Update.as_view(),name='update'),
    path('delete/<int:id>',views.Delete.as_view(),name='delete'),
]