from django.urls import path
from . import views
from.views import PatchAddress, PatchEmail, PatchHomeVideo, PatchMission, PatchPhone, PatchSocial, PatchTeam, PatchTestimonial, PatchVision

urlpatterns = [
    path('', views.getRoutes),
    path('testimonials', views.getTestimonials, name='testimonials'),
    path('add-testimonials', views.addTestimonial, name='add-testimonials'),
    path('delete-testimonial/<str:pk>', views.deleteTestimonial,
         name='delete-testimonials'),
    path('patch-testimonial/<str:pk>',
         PatchTestimonial.as_view(), name='patch-testimonial'),

    path('addresses', views.getAddresses, name='addresses'),
    path('add-address', views.addAddress, name='add-address'),
    path('delete-address/<str:pk>', views.deleteAddress,
         name='delete-address'),
    path('patch-address/<str:pk>',
         PatchAddress.as_view(), name='patch-address'),

    path('phone', views.getPhone, name='phone'),
    path('add-phone', views.addPhone, name='add-phone'),
    path('delete-phone/<str:pk>', views.deletePhone,
         name='delete-phone'),
    path('patch-phone/<str:pk>',
         PatchPhone.as_view(), name='patch-phone'),

    path('email', views.getEmail, name='email'),
    path('add-email', views.addEmail, name='add-email'),
    path('delete-email/<str:pk>', views.deleteEmail,
         name='delete-email'),
    path('patch-email/<str:pk>',
         PatchEmail.as_view(), name='patch-email'),

    # This is Team as n Team Member
    path('team', views.getTeam, name='team'),
    path('add-team', views.addTeam, name='add-team'),
    path('delete-team/<str:pk>', views.deleteTeam,
         name='delete-team'),  # This is deleting just a team member specific not the whole team
    path('patch-team/<str:pk>',
         PatchTeam.as_view(), name='patch-team'),

    path('socials', views.getSocial, name='socials'),
    path('add-social', views.addSocial, name='add-social'),
    path('delete-social/<str:pk>', views.deleteSocial,
         name='delete-social'),
    path('patch-social/<str:pk>',
         PatchSocial.as_view(), name='patch-social'),

    path('mission', views.getMission, name='mission'),
    path('add-mission', views.addMission, name='add-mission'),
    path('delete-mission/<str:pk>', views.deleteMission,
         name='delete-mission'),
    path('patch-mission/<str:pk>',
         PatchMission.as_view(), name='patch-mission'),

    path('vision', views.getVision, name='vision'),
    path('add-vision', views.addVision, name='add-vision'),
    path('delete-vision/<str:pk>', views.deleteVision,
         name='delete-vision'),
    path('patch-vision/<str:pk>',
         PatchVision.as_view(), name='patch-vision'),

    path('homevideo', views.getHomeVideo, name='homevideo'),
    path('add-homevideo', views.addHomeVideo, name='add-homevideo'),
    path('delete-homevideo/<str:pk>', views.deleteHomeVideo,
         name='delete-homevideo'),
    path('patch-homevideo/<str:pk>',
         PatchHomeVideo.as_view(), name='patch-homevideo'),

    path('clientemails', views.getClientEmails, name='clientemails'),
    path('add-clientemail', views.addClientEmail, name='add-clientemail'),
    path('delete-clientemail/<str:pk>', views.deleteClientEmail,
         name='delete-clientemail'),



]
