from django.shortcuts import render, redirect
import django
from .models import Faculty, Staff
from .forms import Faculty_form, Staff_form, Event_form, A_cal_form, publication_form, event_form, gallery_form, news_form
from django.contrib.auth.decorators import login_required


# Create your views here.


def main(res):
    return render(res, 'index.html', {})


@login_required
def faculty_form(res):
    if res.method == 'POST':
        form = Faculty_form(res.POST, res.FILES)
        if form.is_valid():
            form.save()
            return redirect('faculty')
        return render(res, 'admin/faculty.html', {'form': form})
    return render(res, 'admin/faculty.html', {'form': Faculty_form()})

@login_required
def admin_events(res):
    if res.method == 'POST':
        form = Event_form(res.POST)
        if form.is_valid():
            form.save()
            return redirect('admin/events')
        return render(res, 'admin/events.html', {'form': form})
    return render(res, 'admin/events.html', {'form': Event_form()})


@login_required
def admin_staff(res):
    if res.method == 'POST':
        form = Staff_form(res.POST)
        if form.is_valid():
            print('vai=webhhwe')
            form.save()
            return redirect('admin/staff')
        return render(res, 'admin/staff.html', {'form': form})
    return render(res, 'admin/staff.html', {'form': Staff_form()})


@login_required
def admin_a_cal(res):
    if res.method == 'POST':
        form = A_cal_form(res.POST)
        if form.is_valid():
            acad = form.save(commit=False)
            acad.is_time = False
            acad.save()
            return redirect('admin/academic_calender')
        return render(res, 'admin/academic.html', {'form': form})
    return render(res, 'admin/academic.html', {'form': A_cal_form()})

@login_required
def admin_tt(res):
    if res.method == 'POST':
        form = A_cal_form(res.POST)
        if form.is_valid():
            form.save()
            return redirect('admin/timetable')
        return render(res, 'admin/timetable.html', {'form': form})
    return render(res, 'admin/timetable.html', {'form': A_cal_form()})

@login_required
def admin_publication(res):
    if res.method == 'POST':
        form = publication_form(res.POST)
        if form.is_valid():
            form.save()
            return redirect('admin/publications')
        return render(res, 'admin/publication.html', {'form': form})
    return render(res, 'admin/publication.html', {'form': publication_form()})

@login_required
def admin_awards(res):
    if res.method == 'POST':
        form = publication_form(res.POST)
        if form.is_valid():
            o = form.save(commit=False)
            o.is_p = False
            o.save()
            return redirect('admin/awards_honors')
        return render(res, 'admin/awards.html', {'form': form})
    return render(res, 'admin/awards.html', {'form': publication_form()})

@login_required
def admin_events(res):
    if res.method == 'POST':
        form = event_form(res.POST)
        if form.is_valid():
            form.save()
            return redirect('admin/events_talks')
        return render(res, 'admin/events.html', {'form': form})
    return render(res, 'admin/events.html', {'form': event_form()})

@login_required
def admin_gallery(res):
    if res.method == 'POST':
        form = gallery_form(res.POST)
        if form.is_valid():
            form.save()
            return redirect('admin/gallery')
        return render(res, 'admin/gallery.html', {'form': form})
    return render(res, 'admin/gallery.html', {'form': gallery_form()})

@login_required
def admin_news(res):
    if res.method == 'POST':
        form = news_form(res.POST)
        if form.is_valid():
            form.save()
            return redirect('admin/news')
        return render(res, 'admin/news.html', {'form': form})
    return render(res, 'admin/news.html', {'form': news_form()})

def faculty(res):
    return render(res, 'faculty.html', {'faculty': Faculty.objects.all()})

def staff(res):
    return render(res, 'staff.html', {'staff': Staff.objects.all()})