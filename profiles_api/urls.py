from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
# first "hello-viewset" is the name of the name of the url, we wish to ccreate
# base_name="hello-viewset" for retrieving URLs in our router, if we ever need
# to do that using the URL retrieving function providewd by dhango
router.register("hello-viewset", views.HelloViewSet, base_name="hello-viewset")

# we have the queryset in the views.py, so no need ot set base_name
router.register("profile", views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path("", include(router.urls))
]
