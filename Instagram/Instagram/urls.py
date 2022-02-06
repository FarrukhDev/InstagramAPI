
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
from users.views import AccountListCreateAPIView
from feed.views import MediaListCreateAPIView,CommentListCreateAPIView,PostListCreateAPIView,PostRetrieveUpdateDestroyAPIView,CommentRetrieveUpdateDestroyAPIView,MediaRetrieveUpdateDestroyAPIView

urlpatterns = [
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

]
