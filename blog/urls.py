from . import views
from django.urls import path
from blog.models import Post

urlpatterns = [
    path('',views.indexpage),
    path('blog/', views.PostList.as_view(), name="home"),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('resume',views.resume)
]