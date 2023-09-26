from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import UserProfileViewSet, BlogPostViewSet, CommentViewSet, TagViewSet
from blog import views

router = DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'blog-posts', BlogPostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', views.LoginView.as_view()),
    path('profile/', views.ProfileView.as_view()),
    path('', include('Account.urls')),
]
