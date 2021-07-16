from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from . import views
import django


urlpatterns = [
    #dynamic pages
    path('', views.main, name='main'),
    path('faculty', views.faculty, name='faculty'),
    path('students', views.students, name='students'),
    path('publications', views.publications , name='publications'),
    path('awards_honours', views.awards_honours, name='awards_honours'),
    path('gallery', views.gallery, name='gallery'),
    path('staff', views.staff, name='staff'),
    path('news', views.news, name='news'),
    path('events', views.events, name='events'),
    path('internships', views.internships, name='internships'),
    path('placements', views.placements, name='placements'),
    path('collaborations', views.collaborations, name='collaborations'),


    #static pages
    path('web_team', TemplateView.as_view(
        template_name='web_team.html'), name='web_team'),
    path('curriculum', TemplateView.as_view(
        template_name='curriculum.html'), name='curriculum'),
    path('courses', TemplateView.as_view(
        template_name='course.html'), name='courses'),
    path('labs', TemplateView.as_view(
        template_name='labs.html'), name='labs'),
    path('research_areas', TemplateView.as_view(
        template_name='research.html'), name='reasearch_areas'),
    

    #admin
    path('admin/dashboard', views.admin_dashboard, name='admin_dashboard'),

    path('admin/faculty', views.faculty_form, name='admin_faculty'),
    path('admin/faculty/<int:id>', views.faculty_form, name='admin_faculty'),

    path('admin/events', views.admin_events, name='admin_events'),
    path('admin/events/<int:id>', views.admin_events, name='admin_events'),

    path('admin/staff', views.admin_staff, name='admin_staff'),
    path('admin/staff/<int:id>', views.admin_staff, name='admin_staff'),

    path('admin/students', views.admin_students, name='admin_students'),
    path('admin/students/<int:id>', views.admin_students, name='admin_students'),

    path('admin/academic_calender', views.admin_a_cal, name='admin_a_cal'),
    path('admin/timetable', views.admin_tt, name='admin_tt'),
    
    path('admin/publications', views.admin_publication, name='admin_publication'),
    path('admin/publications/<int:id>', views.admin_publication, name='admin_publication'),

    path('admin/awards_honours', views.admin_awards, name='admin_awards'),
    path('admin/awards_honours/<int:id>', views.admin_awards, name='admin_awards'),

    path('admin/gallery', views.admin_gallery, name='admin_gallery'),
    path('admin/messages', views.message, name='messages'),

    path('admin/news', views.admin_news, name='admin_news'),
    path('admin/news/<int:id>', views.admin_news, name='admin_news'),

    path('admin/slider', views.admin_slider, name='admin_slider'),
    path('admin/slider/<int:id>', views.admin_slider, name='admin_slider'),

    path('admin/placements', views.admin_placements, name='admin_placements'),
    path('admin/placements/<int:id>', views.admin_placements, name='admin_placements'),

    path('admin/internships', views.admin_internships, name='admin_internships'),
    path('admin/internships/<int:id>', views.admin_internships, name='admin_internships'),

    path('admin/collaborations', views.admin_collaborations, name='admin_collaborations'),
    path('admin/collaborations/<int:id>', views.admin_collaborations, name='admin_collaborations'),

    path('faculty_form', views.new_faculty_form, name='faculty_form'),
    path('staff_form', views.new_staff_form, name='staff_form'),
    path('publication_form', views.new_publication_form, name='publication_form'),
    path('award_form', views.new_awards_form, name='award_form'),
    path('placement_form', views.new_placement_form, name='placement_form'),
    path('internship_form', views.new_internship_form, name='internship_form'),

    path('admin/accept/<int:id>/<str:model>', views.admin_accept, name='admin_accept'),
    path('admin/admin_delete/<int:id>/<str:model>', views.admin_delete, name='admin_delete'),


    #to serve media and static files
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),

] + static(settings.STATIC_URL, doucument_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
