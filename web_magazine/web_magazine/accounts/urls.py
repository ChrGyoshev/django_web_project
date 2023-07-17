from django.urls import path


from web_magazine.accounts.views import Index, SignUp, SignIn, SignOut, EditProfile, ProfileDetails, DeleteProfile

urlpatterns = [


    path('sign-up/', SignUp.as_view(),name='sign up'),
    path('sign-in/', SignIn.as_view(),name='sign in'),
    path('sign-out/',SignOut.as_view(),name='sign out'),
    path('details/<int:pk>/',ProfileDetails.as_view(),name='profile details'),

    path('delete/<int:pk>/',DeleteProfile.as_view(),name='delete profile'),
    path('edit/<int:pk>/', EditProfile.as_view(), name='edit profile'),


]