from django.contrib import admin


from . import views
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    path('policy/', views.policy, name='policy'),
    path('contact/', views.contact,name='contact'),
    path('resources/', views.resources, name='resources'),
    path('news/', views.news, name='news'),
    path('submit-idea/', views.submit_idea, name='submit_idea'),
    path('ideas/', views.idea_list, name='idea_list'),
    path('ideas/<slug:slug>', views.idea_page, name='idea_page'),
    path('ideas/<int:idea_id>/submit_comment/', views.submit_comment, name='submit_comment'),


]


