from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index), # 안녕 FBV
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]