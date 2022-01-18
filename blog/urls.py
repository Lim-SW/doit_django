from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index), # 안녕 FBV
    path('category/<str:slug>/', views.category_page),
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]