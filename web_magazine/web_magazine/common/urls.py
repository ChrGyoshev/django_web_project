from django.urls import path

from web_magazine.common.views import Index, ErrorPage

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('test', ErrorPage.as_view(), name='error page'),
]