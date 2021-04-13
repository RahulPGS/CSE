from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class Faculty(models.Model):
    edu_level_choices = [('b_tech', 'B.Tech'), ('m_tech', 'M.Tech'), ('phd', 'PHD'), ('other', '(Other')]
    name = models.CharField(max_length=100)
    edu_level = models.CharField(choices=edu_level_choices, max_length=50)
    education = models.TextField(max_length=500)
    spec_sub = models.CharField(max_length=100)
    work_exp = models.TextField(max_length=500, blank=True, null=True)
    publication = models.TextField(max_length=1000, blank=True, null=True)
    projects  = models.TextField(max_length=500, blank=True, null=True)
    gender = models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    sub_dealt = models.TextField(max_length=500)
    conf_attended = models.TextField(max_length=500, blank=True, null=True)
    workshops_attended = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='faculty_images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'img'])])
    cv = models.ImageField(upload_to='faculty_cv/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'txt', 'doc', 'jpg', 'png', 'jpeg', 'img'])])


class Staff(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    profession = models.CharField(max_length=30)

class Publication(models.Model): # Includes both publications and awards and honnors section
    name = models.CharField(max_length=100)
    id_no = models.CharField(max_length=7)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    link = models.CharField(max_length=1000)
    is_p = models.BooleanField(default=True) #to say whether it is publication or awards and honors

class Timetablenacedemics(models.Model):
    link = models.CharField(max_length=1000)
    is_time = models.BooleanField(default=True) #to say whether it is Timetable or acedemics

class Gallery(models.Model):
    categoreis = [('Workshops', 'Workshops'), ('Talks', 'Talks'), ('Events', 'Events')]
    image = models.ImageField(upload_to='faculty_images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'img'])])
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=10, choices=categoreis)

class Events(models.Model):
    name = models.CharField(max_length=100)
    res_person = models.CharField(max_length=100) #resource person name
    covinor = models.CharField(max_length=100)
    coordinators = models.CharField(max_length=500)

class Notification(models.Model):
    categories = [('announcements', 'Announcements'),('updates', 'Updates'),('placement drives', 'Placement drives')]
    notifiation = models.CharField(max_length=500)
    category = models.CharField(max_length=20, choices=categories)