from django.urls import path

from web_magazine.common.views import Index, ErrorPage, AboutPage

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('error/', ErrorPage.as_view(), name='error page'),
    path('about/',AboutPage.as_view(), name='about page'),
]