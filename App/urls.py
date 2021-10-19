from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logoutView/', views.logoutView, name='logoutView'),
    path('upisi/<int:pk>/',views.view_subjects,name='upisi'),
    path('upisiPredmet/<int:pid>/<int:pk>', views.upisiPredmet, name='upisiPredmet'),
    path('ispisiPredmet/<str:pname>/<int:pk>', views.ispisiPredmet, name='ispisiPredmet'),
    path('promijeniPredmet/<str:pname>/<int:pk>', views.promijeniPredmet, name='promijeniPredmet'),
    path('predmeti/', views.sviPredmeti, name='predmeti'),
    path('editPredmet/<int:pk>/', views.editPredmet, name='editPredmet'),
    path('createPredmet/', views.createPredmet, name='createPredmet'),
    path('predmetDetails/<int:pk>/', views.predmetDetails, name='predmetDetails'),
    path('sviStudenti/', views.sviStudenti, name='sviStudenti'),
    path('deletePredmet/<int:pk>/', views.deletePredmet, name='deletePredmet'),
]