from django.urls import path


from . import views

urlpatterns = [
    # home templates
    path('', views.home, name='home'),
    path('aboutus/', views.about_us, name='aboutus'),
    path('services/', views.services, name='services'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),
    path('login/admin/', views.admin, name='admin'),
    path('login/newuser/', views.newuser, name='newuser'),
    path('login/existinguser/', views.existinguser, name='existinguser'),
    # after login user templates
    path('userui/', views.userui, name='userui'),
    path('user/website_checking/', views.website_checking, name='website_checking'),
    path('user/feedback/', views.feedback, name='feedback'),
    path('user/logout', views.ulogout, name='logout'),
    # after login admin templates
    path('adminui/', views.adminui, name='adminui'),
    path('admin/url_database', views.url_database, name='url_database'),
    path('admin/feedback_database', views.feedback_database, name='feedback_database'),
    path('admin/logout', views.alogout, name='alogout'),
    path('admin/delete_url_database/<int:id>', views.delete_url_database, name='delete_url_database'),
    path('admin/update_url_database/<int:id>', views.update_url_database, name='update_url_database'),


]

