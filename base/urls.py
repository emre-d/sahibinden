from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
   path('ilan/<str:pk>',views.listing,name='ilan'),
   path('ilanac/',views.createListing,name='create-listing'),
   path('kayit/',views.registerPage,name='kayit'),
   path('profil/',views.userProfile,name='profile'),
   path('profile/<str:pk>',views.profileCheck,name='check'),
   path('giris/',views.loginPage,name='giris'),
   path('logout/',views.logoutUser,name = "logout"),
   path('update-listing/<str:pk>/',views.updateListing, name="update-listing"),
   path('delete-listing/<str:pk>/',views.deleteListing, name="delete-listing"),
   path('delete-comment/<str:pk>/',views.deleteComment, name="delete-comment"),
   path('favori/<str:pk>',views.favori,name='favori'),
   path('sil/<str:pk>',views.favoriSil,name='sil')
]