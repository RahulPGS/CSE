from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from . import views
import django


urlpatterns = [
    path('', views.main, name='main'),
    path('faculty', views.faculty, name='faculty'),
    path('publications', TemplateView.as_view(
        template_name='publication.html'), name='publications'),
    path('awards_honours', TemplateView.as_view(
        template_name='awards_honours.html'), name='awards_honours'),
    path('web_team', TemplateView.as_view(
        template_name='web_team.html'), name='web_team'),
    path('curriculam', TemplateView.as_view(
        template_name='curriculam.html'), name='curriculam'),
    path('courses', TemplateView.as_view(
        template_name='course.html'), name='courses'),
    path('students', TemplateView.as_view(
        template_name='students.html'), name='students'),
    path('staff', views.staff, name='staff'),
    path('news_events', TemplateView.as_view(
        template_name='news.html'), name='news_events'),
    path('labs', TemplateView.as_view(
        template_name='labs.html'), name='labs'),
    path('research_areas', TemplateView.as_view(
        template_name='research.html'), name='reasearch_areas'),
    path('events_talks', TemplateView.as_view(
        template_name='events.html'), name='events_talks'),
    path('gallery', TemplateView.as_view(
        template_name='gallery.html'), name='gallery'),
    path('admin/faculty', views.faculty_form, name='admin_faculty'),
    path('admin/events', views.admin_events, name='admin_events'),
    path('admin/staff', views.admin_staff, name='admin_staff'),
    path('admin/academic_calender', views.admin_a_cal, name='admin_a_cal'),
    path('admin/timetable', views.admin_tt, name='admin_tt'),
    path('admin/publications', views.admin_publication, name='admin_publication'),
    path('admin/awards_honors', views.admin_awards, name='admin_awards'),
    path('admin/events_talks', views.admin_events, name='admin_events'),
    path('admin/gallery', views.admin_gallery, name='admin_gallery'),
    path('admin/news', views.admin_news, name='admin_news'),


    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),

] + static(settings.STATIC_URL, doucument_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
