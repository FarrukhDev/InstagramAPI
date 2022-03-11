
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
from users.views import AccountListCreateAPIView
from feed.views import MediaListCreateAPIView,CommentListCreateAPIView,PostListCreateAPIView,PostRetrieveUpdateDestroyAPIView,CommentRetrieveUpdateDestroyAPIView,MediaRetrieveUpdateDestroyAPIView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Instagram API",
      default_version='v1',
      description="Clone of the most popular social media Instagram",
       terms_of_service="https://www.google.com/policies/terms/",
       contact=openapi.Contact(email="farruxbekergashaliev@gmail.com"),
   ),
   public=True,
)
urlpatterns = [
    path('',PostListCreateAPIView.as_view(),name='posts'),
    path('admin/', admin.site.urls),
    path('token/',TokenObtainPairView.as_view(),name = 'token'),
    path('token/refresh',TokenRefreshView.as_view(),name ='refresh_token'),
    path('users/',AccountListCreateAPIView.as_view(),name = 'userslist'),
    path('users/create',AccountListCreateAPIView.as_view(),name = 'userscreate'),
    path('media/',MediaListCreateAPIView.as_view(),name='media_list'),
    path('comment/',CommentListCreateAPIView.as_view(),name='comment_list'),
    path('post/',PostListCreateAPIView.as_view(),name='post_list'),
    path('post/<int:pk>',PostRetrieveUpdateDestroyAPIView.as_view(),name='post_rud'),
    path('comment/<int:pk>',CommentRetrieveUpdateDestroyAPIView.as_view(),name='comment_rud'),
    path('media/<int:pk>',MediaRetrieveUpdateDestroyAPIView.as_view(),name='media_rud'),
    path('docs/',schema_view.with_ui('swagger',cache_timeout=0),name="swagger_doc"),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout=0),name="redoc_doc"),
]
