from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
# Create your models here.
department_values = (
        ('cse', 'Computer Science & Engineering'),
        ('ece', 'Electronics & Communication Engineering'),
        ('me', 'Mechanical Engineering'),
        ('ce', 'Civil Engineering'),
        ('dd', 'Design'),
        ('bsbe', 'Biosciences & Bioengineering'),
        ('cl', 'Chemical Engineering'),
        ('cst', 'Chemical Science & Technology'),
        ('eee', 'Electronics & Electrical Engineering'),
        ('ma', 'Mathematics & Computing'),
        ('ph', 'Engineering Physics'),
        ('rt', 'Rural Technology'),
        ('hss', 'Humanities & Social Sciences'),
        ('enc', 'Centre for Energy'),
        ('env', 'Centre for Environment'),
        ('nt', 'Centre for Nanotechnology'),
        ('lst', 'Centre for Linguistic Science & Technology')
    )
program_values = (
        ('btech', 'BTech'),
        ('mtech', 'MTech'),
        ('phd', 'PhD'),
        ('msc', 'MSc'),
        ('msr', 'MS-R'),
        ('ma', 'MA'),
        ('bdes', 'BDes'),
        ('mdes', 'MDes')
    )
class Event(models.Model):
    name = models.CharField(max_length=300, help_text='Enter the event name')
    slug = models.SlugField(unique=True)
    fee = models.PositiveIntegerField()
    capacity  = models.PositiveIntegerField()
    target_audience = models.CharField(max_length=300)
    date = models.DateField(null = False, blank = False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    faq = models.TextField()
    tags = models.CharField(max_length=300)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Profile(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    department = models.CharField(max_length=100,blank=False,choices=department_values)
    program = models.CharField(max_length=100,blank=False,choices=program_values)
    roll_no = models.BigIntegerField(unique=True,blank=False)
    phone_no = models.BigIntegerField(blank=False)
