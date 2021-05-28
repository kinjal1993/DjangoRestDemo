from django.urls import path
from .views import ArticleAPIView,ArticleDetailAPIView,GenericAPIView

urlpatterns = [
#    path('article/', article_list),
#   path('detail/<int:pk>/', article_detail),
    path('article/<int:id>/', GenericAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetailAPIView.as_view()),
]
