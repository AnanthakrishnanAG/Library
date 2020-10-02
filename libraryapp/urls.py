from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('users',views.UserView, basename='users')
router.register('library',views.LibraryView, basename='Library')




urlpatterns=[
    
    path('login/view/',include(router.urls)),
    path('',views.signupview),
    path('login/',views.login)
  
]