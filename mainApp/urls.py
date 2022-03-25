from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('forms/<fid>/', views.tforms, name="tform"),
    path('toTdetails/<fid>/', views.toTdetails, name="toTdetails"),
    path('traineeDetails/', views.tdetails, name='tdetails'),
    path('delTrainee/<temail>/', views.delTrainee, name='delTrainee'),
    path('setSession/<fid>/', views.setSession, name='setSession'),
    path('sendEmail/', views.sendEmail, name='sendEmail'),
    path('toogleUrlStatus/<fid>/', views.urlStatusToogle, name='urlStatusToogle'),
    path('gcsv/', views.download_csv, name='gcsv'),
    path('delForm/<fid>/', views.delForm, name='delForm'),
    path('generateCertificate/', views.generateCertificate, name='generateCertificate'),
    path('generateOfferLetter/', views.generateOfferLetter, name='generateOfferLetter'),
]
