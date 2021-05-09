from django.db import models
from django.core.validators import FileExtensionValidator
from datetime import date

# Create your models here.

class TimeStampable(models.Model):
    created = models.DateField(auto_now_add=True, editable=False)
    modified = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Faculty(TimeStampable):
    edu_level_choices = [('b_tech', 'B.Tech'), ('m_tech', 'M.Tech'), ('phd', 'PHD'), ('other', '(Other)')]
    name = models.CharField(max_length=100)
    edu_level = models.CharField(choices=edu_level_choices, max_length=50)
    education = models.TextField(max_length=5000)
    spec_sub = models.CharField(max_length=100)
    work_exp = models.TextField(max_length=5000, blank=True, null=True)
    publication = models.TextField(max_length=1000, blank=True, null=True)
    projects  = models.TextField(max_length=5000, blank=True, null=True)
    gender = models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    sub_dealt = models.TextField(max_length=500)
    conf_attended = models.TextField(max_length=200, blank=True, null=True)
    workshops_attended = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='faculty_images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'img'])])
    cv = models.ImageField(upload_to='faculty_cv/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'txt', 'doc', 'jpg', 'png', 'jpeg', 'img'])])
    approved = models.BooleanField(default=False)


class Staff(TimeStampable):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)
    approved = models.BooleanField(default=False)


class Publication(TimeStampable):
    name = models.CharField(max_length=100)
    id_no = models.CharField(max_length=7)
    title = models.CharField(max_length=50)
    description = models.TextField()
    link = models.TextField()
    approved = models.BooleanField(default=False)
    proof = models.FileField(upload_to='proofs/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'ppt', 'word', 'txt'])])



class Award(TimeStampable):
    name = models.CharField(max_length=100)
    id_no = models.CharField(max_length=7)
    title = models.CharField(max_length=50)
    description = models.TextField()
    link = models.TextField(blank=True, null=True)
    approved = models.BooleanField(default=False)
    proof = models.FileField(upload_to='proofs/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'ppt', 'word', 'txt'])])



class Timetablenacedemics(models.Model):
    link = models.TextField()
    is_time = models.BooleanField(default=True) #to say whether it is Timetable or acedemics


class Gallery(TimeStampable):
    categoreis = [('Workshops', 'Workshops'), ('Talks', 'Talks'), ('Events', 'Events')]
    image = models.ImageField(upload_to='gallery/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'img'])])
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=10, choices=categoreis)


class Events(TimeStampable):
    name = models.CharField(max_length=100)
    res_person = models.CharField(max_length=100) #resource person name
    covinor = models.CharField(max_length=100, null=True, blank=True)
    coordinators = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField()


class News(TimeStampable):
    categories = [('Announcement', 'Announcement'),('Update', 'Update'),('Placement drive', 'Placement drive')]
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=20, choices=categories)
    description = models.TextField()
    link = models.TextField(blank=True, null=True)

class Slide(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="slides/", validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'img'])])

class Batch(models.Model):
    batch_year = models.CharField(max_length=4)
    batch_link = models.TextField()