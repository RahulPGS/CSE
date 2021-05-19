from django.shortcuts import render, redirect
import django
from .models import Faculty, Staff, Publication, Gallery, News, Slide, Award, Timetablenacedemics, Events, Batch, Placement, Internship, Collaboration, Message
from .forms import Faculty_form, Staff_form, Event_form, A_cal_form, publication_form, gallery_form, news_form, slide_form, award_form, batch_form, placement_form, internship_form, collaboration_form, message_form
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.


def main(res):
    form = message_form()
    if res.method == 'POST':
        form = message_form(res.POST)
        if form.is_valid():
            form.save()
            messages.success(res, "Message sent successfully")
            return redirect('/')
    announcements = News.objects.filter(category='Announcement')[:2]
    updates = News.objects.filter(category='Update')[:2]
    placements = News.objects.filter(category='Placement drive')[:2]
    time_table = Timetablenacedemics.objects.get(is_time=True)
    academic_cal = Timetablenacedemics.objects.get(is_time=False)
    print(announcements, updates, placements)
    return render(res, 'index.html', {'announcements':announcements, 'updates':updates, 'placements': placements, 'slides': Slide.objects.all(), 'time_table': time_table, 'academic_cal': academic_cal, 'form': form})


@login_required
def faculty_form(res, id=None):
    if res.method == 'POST':
        if id:
            form = Faculty_form(res.POST, res.FILES, instance=Faculty.objects.get(id=id))
        else:
            form = Faculty_form(res.POST, res.FILES)
        if form.is_valid():
            o = form.save(commit=False)
            o.approved = True
            o.save()
            messages.success(res, "Successfully submitted")
            return redirect('faculty')
        print(form.errors)
        return render(res, '/admin/faculty.html', {'form': form})
    return render(res, 'admin/faculty.html', {'form': Faculty_form(instance=Faculty.objects.get(id=id)) if id else Faculty_form(), 'faculty': Faculty.objects.all(), 'id': id if id else None})

@login_required
def admin_events(res, id=None):
    if res.method == 'POST':
        if id:
            form = Event_form(res.POST, res.FILES, instance=Events.objects.get(id=id))
        else:
            form = Event_form(res.POST, res.FILES)
        if form.is_valid():
            form.save()
            messages.success(res, "Successfully submitted")
            return redirect('/admin/events')
        print(form.errors)
        return render(res, 'admin/events.html', {'form': form})
    return render(res, 'admin/events.html', {'form': Event_form(instance=Events.objects.get(id=id)) if id else Event_form(), 'events': Events.objects.all(), 'id': id if id else None})


@login_required
def admin_staff(res, id=None):
    if res.method == 'POST':
        if id:
            form = Staff_form(res.POST, res.FILES, instance=Staff.objects.get(id=id))
        else:
            form = Staff_form(res.POST, res.FILES)
        if form.is_valid():
            o = form.save(commit=False)
            o.approved = True
            o.save()
            messages.success(res, "Successfully submitted")
            return redirect('/admin/staff')
        print(form.errors)
        return render(res, 'admin/staff.html', {'form': form})
    return render(res, 'admin/staff.html', {'form': Staff_form(instance=Staff.objects.get(id=id)) if id else Staff_form(), 'staff': Staff.objects.all(), 'id': id if id else None})


@login_required
def admin_a_cal(res):
    if res.method == 'POST':
        form = A_cal_form(res.POST, instance=Timetablenacedemics.objects.get(is_time=False))
        if form.is_valid():
            acad = form.save(commit=False)
            acad.is_time = False
            acad.save()
            messages.success(res, "Successfully submitted")
            return redirect('/admin/academic_calender')
        print(form.errors)
        return render(res, 'admin/academic.html', {'form': form})
    return render(res, 'admin/academic.html', {'form': A_cal_form(instance=Timetablenacedemics.objects.get(is_time=False))})

@login_required
def admin_tt(res):
    if res.method == 'POST':
        form = A_cal_form(res.POST, instance=Timetablenacedemics.objects.get(is_time=True))
        if form.is_valid():
            form.save()
            messages.success(res, "Successfully submitted")
            return redirect('admin/timetable')
        print(form.errors)
        return render(res, '/admin/timetable.html', {'form': form})
    return render(res, 'admin/timetable.html', {'form': A_cal_form(instance=Timetablenacedemics.objects.get(is_time=True))})

def new_faculty_form(res):
    if res.method == 'POST':
        form = Faculty_form(res.POST, res.FILES)
        if form.is_valid():
            form.save()
            messages.success(res, "Successfully submitted")
            return redirect('faculty')
        print(form.errors)
        return render(res, 'faculty_form.html', {'form': form})
    return render(res, 'faculty_form.html', {'form': Faculty_form()})


def new_staff_form(res):
    if res.method == 'POST':
        form = Staff_form(res.POST, res.FILES)
        if form.is_valid():
            form.save()
            messages.success(res, "Successfully submitted")
            return redirect('faculty')
        print(form.errors)
        return render(res, 'staff_form.html', {'form': form})
    return render(res, 'staff_form.html', {'form': Staff_form()})


def new_publication_form(res):
    if res.method == 'POST':
        form = publication_form(res.POST, res.FILES)
        if form.is_valid():
            form.save()
            messages.success(res, "Successfully submitted")
            return redirect('publications')
        print(form.errors)
        return render(res, 'publication_form.html', {'form': form})
    return render(res, 'publication_form.html', {'form': publication_form()})


def new_awards_form(res):
    if res.method == 'POST':
        form = award_form(res.POST, res.FILES)
        if form.is_valid():
            form.save()
            messages.success(res, "Successfully submitted")
            return redirect('awards_honours')
        print(form.errors)
        return render(res, 'publication_form.html', {'form': form})
    return render(res, 'publication_form.html', {'form': award_form()})

def new_placement_form(res):
    if res.method == 'POST':
        form = placement_form(res.POST, res.FILES)
        if form.is_valid():
            form.save()
            messages.success(res, "Successfully submitted")
            return redirect('placements')
        print(form.errors)
        return render(res, 'placement_form.html', {'form': form})
    return render(res, 'placement_form.html', {'form': placement_form()})

def new_internship_form(res):
    if res.method == 'POST':
        form = internship_form(res.POST, res.FILES)
        if form.is_valid():
            form.save()
            messages.success(res, "Successfully submitted")
            return redirect('internships')
        print(form.errors)
        return render(res, 'internship_form.html', {'form': form})
    return render(res, 'internship_form.html', {'form': internship_form()})

@login_required
def admin_publication(res, id=None):
    if res.method == 'POST':
        if id:
            form = publication_form(res.POST, res.FILES, instance=Publication.objects.get(id=id))
        else:
            form = publication_form(res.POST, res.FILES)
        if form.is_valid():
            o = form.save(commit=False)
            o.approved = True
            o.save()
            messages.success(res, "Successfully submitted")
            return redirect('/admin/publications')
        print(form.errors)
        return render(res, 'admin/publication.html', {'form': form})
    return render(res, 'admin/publication.html', {'form': publication_form(instance=Publication.objects.get(id=id)) if id else publication_form(), 'objects': Publication.objects.all(), 'id': id if id else None})

@login_required
def admin_awards(res, id=None):
    if res.method == 'POST':
        if id:
            form = award_form(res.POST, res.FILES, instance=Award.objects.get(id=id))
        else:
            form = award_form(res.POST, res.FILES)
        if form.is_valid():
            o = form.save(commit=False)
            o.approved = True
            o.save()
            messages.success(res, "Successfully submitted")
            return redirect('/admin/awards_honours')
        print(form.errors)
        return render(res, 'admin/awards.html', {'form': form})
    return render(res, 'admin/awards.html', {'form': award_form(instance=Award.objects.get(id=id)) if id else award_form(), 'awards': Award.objects.all(), 'id': id if id else None})


@login_required
def admin_gallery(res):
    if res.method == 'POST':
        form = gallery_form(res.POST, res.FILES)
        images = res.FILES.getlist('images')
        if form.is_valid():
            category = form.cleaned_data.get("category")
            name = form.cleaned_data.get("name")
            for image in images:
                o = Gallery()
                o.image = image
                o.category = category
                o.name = name
                o.save()
            messages.success(res, "Successfully submitted")
            return redirect('/admin/gallery')
        print(form.errors)
        return render(res, 'admin/gallery.html', {'form': form})
    return render(res, 'admin/gallery.html', {'form': gallery_form(), 'gallery': Gallery.objects.all()})

@login_required
def admin_news(res, id=None):
    if res.method == 'POST':
        if id:
            form = news_form(res.POST, instance=News.objects.get(id=id))
        else:
            form = news_form(res.POST)
        if form.is_valid():
            form.save()
            messages.success(res, "Successfully submitted")
            return redirect('/admin/news')
        print(form.errors)
        return render(res, 'admin/news.html', {'form': form})
    return render(res, 'admin/news.html', {'form': news_form(instance=News.objects.get(id=id)) if id else news_form(), 'news': News.objects.all(), 'id': id if id else None})

@login_required
def admin_slider(res, id=None):
    if res.method == 'POST':
        if id:
            form = slide_form(res.POST, res.FILES, instance=Slide.objects.get(id=id))
        else:
            form = slide_form(res.POST, res.FILES)
        if form.is_valid():
            form.save()
            messages.success(res, "Successfully submitted")
            return redirect('/admin/slider')
        print(form.errors)
        return render(res, 'admin/slider.html', {'form': form})
    return render(res, 'admin/slider.html', {'form': slide_form(instance=Slide.objects.get(id=id)) if id else slide_form(), 'slides': Slide.objects.all(), 'id': id if id else None})


@login_required
def admin_students(res, id=None):
    if res.method == 'POST':
        if id:
            form = batch_form(res.POST, instance=Batch.objects.get(id=id))
        else:
            form = batch_form(res.POST)
        if form.is_valid():
            form.save()
            messages.success(res, "Successfully submitted")
            return redirect('/admin/students')
        print(form.errors)
        return render(res, 'admin/students.html', {'form': form})
    return render(res, 'admin/students.html', {'form': batch_form(instance=Batch.objects.get(id=id)) if id else batch_form(), 'batches': Batch.objects.all(), 'id': id if id else None})


@login_required
def admin_placements(res, id=None):
    if res.method == 'POST':
        if id:
            form = placement_form(res.POST, instance=Placement.objects.get(id=id))
        else:
            form = placement_form(res.POST, res.FILES)
        if form.is_valid():
            o = form.save(commit=False)
            o.approved = True
            o.save()
            messages.success(res, "Successfully submitted")
            return redirect('/admin/placements')
        print(form.errors)
        return render(res, 'admin/placements.html', {'form': form})
    return render(res, 'admin/placements.html', {'form': placement_form(instance=Placement.objects.get(id=id)) if id else placement_form(), 'placements': Placement.objects.all(), 'id': id if id else None})



@login_required
def admin_internships(res, id=None):
    if res.method == 'POST':
        if id:
            form = internship_form(res.POST, instance=Internship.objects.get(id=id))
        else:
            form = internship_form(res.POST, res.FILES)
        if form.is_valid():
            o = form.save(commit=False)
            o.approved = True
            o.save()
            messages.success(res, "Successfully submitted")
            return redirect('/admin/internships')
        print(form.errors)
        return render(res, 'admin/internships.html', {'form': form})
    return render(res, 'admin/internships.html', {'form': internship_form(instance=Internship.objects.get(id=id)) if id else internship_form(), 'internships': Internship.objects.all(), 'id': id if id else None})

@login_required
def admin_collaborations(res, id=None):
    if res.method == 'POST':
        if id:
            form = collaboration_form(res.POST, instance=Collaboration.objects.get(id=id))
        else:
            form = collaboration_form(res.POST, res.FILES)
        if form.is_valid():
            o = form.save(commit=False)
            o.approved = True
            o.save()
            messages.success(res, "Successfully submitted")
            return redirect('/admin/collaborations')
        print(form.errors)
        return render(res, 'admin/collaborations.html', {'form': form})
    return render(res, 'admin/collaborations.html', {'form': collaboration_form(instance=Collaboration.objects.get(id=id)) if id else collaboration_form(), 'collaborations': Collaboration.objects.all(), 'id': id if id else None})



def faculty(res):
    return render(res, 'faculty.html', {'faculty': Faculty.objects.filter(approved=True)})

def staff(res):
    return render(res, 'staff.html', {'staff': Staff.objects.filter(approved=True)})

def students(res):
    return render(res, 'students.html', {'batches': Batch.objects.all()})

def publications(res):
    return render(res, 'publication.html', {'publications': Publication.objects.filter(approved=True).order_by('-id')})

def awards_honours(res):
    return render(res, 'awards_honours.html', {'awards_honours': Award.objects.filter(approved=True).order_by('-id')})

def events(res):
    return render(res, 'events.html', {'events': Events.objects.all().order_by('-id')})

def gallery(res):
    return render(res, 'gallery.html', {'gallery': Gallery.objects.all().order_by('-id')})

def news(res):
    return render(res, 'news.html', {'news': News.objects.all().order_by('-id')})

def internships(res):
    return render(res, 'internships.html', {'internships': Internship.objects.filter(approved=True).order_by('-id')})

def placements(res):
    return render(res, 'placements.html', {'placements': Placement.objects.filter(approved=True).order_by('-id')})

def collaborations(res):
    return render(res, 'collaborations.html', {'collaborations': Collaboration.objects.all()})

def message(res):
    return render(res, 'admin/messages.html', {'message': Message.objects.all()})

def admin_dashboard(res):
    return render(res, 'admin/dash_new.html', {'p_pendings': Publication.objects.filter(approved=False), 'a_pendings': Award.objects.filter(approved=False), 'f_pendings': Faculty.objects.filter(approved=False), 's_pendings': Staff.objects.filter(approved=False), 'pl_pendings' : Placement.objects.filter(approved=False), 'in_pendings' : Internship.objects.filter(approved=False)})

@login_required
def admin_accept(res, id, model):
    if model == 'award':
        o = Award.objects.get(id=id)
    elif model == 'faculty':
        o = Faculty.objects.get(id=id)
    elif model == 'staff':
        o = Staff.objects.get(id=id)
    elif model == 'publication':
        o = Publication.objects.get(id=id)
    elif model == 'internship':
        o = Internship.objects.get(id=id)
    elif model == 'placement':
        o = Placement.objects.get(id=id)
    o.approved = True
    o.save()
    messages.success(res, f'{model.title()} object is Approved')
    return redirect('/admin/dashboard')

@login_required
def admin_delete(res, id, model):
    if model == 'award':
        o = Award.objects.get(id=id)
    elif model == 'publication':
        o = Publication.objects.get(id=id)
    elif model == 'faculty':
        o = Faculty.objects.get(id=id)
    elif model == 'staff':
        o = Staff.objects.get(id=id)
    elif model == 'gallery':
        o = Gallery.objects.get(id=id)
    elif model == 'event':
        o = Events.objects.get(id=id)
    elif model == 'news':
        o = News.objects.get(id=id)
    elif model == 'slide':
        o = Slide.objects.get(id=id)
    elif model == 'batch':
        o = Batch.objects.get(id=id)
    elif model == 'placement':
        o = Placement.objects.get(id=id)
    elif model == 'internship':
        o = Internship.objects.get(id=id)
    elif model == 'collaboration':
        o = Collaboration.objects.get(id=id)
    elif model == 'message':
        o = Message.objects.get(id=id)
    o.delete()
    messages.warning(res, f"The {model.title()} object is deleted")
    return redirect(res.META['HTTP_REFERER'])

