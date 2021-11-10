from django.urls import path, include
from p_api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hellov-viewset', views.HelloViewSet, base_name = 'hello-viewset')
router.register('profile', views.UserProfileViewSet) # queryset direkt bağlandı bu yüzden base_name kullanmadık.


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
