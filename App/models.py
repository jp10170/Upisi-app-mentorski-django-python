from django.db import models
from django.utils.translation import ugettext_lazy as _
from .enums import Roles
from .enums import Statuses
from .enums import Izborni
from django.contrib.auth.models import AbstractUser
# Create your models here.

class korisnici(AbstractUser):
    role=models.CharField(_('role'),choices=Roles.choices(),max_length=(60),null=False)
    status=models.CharField(_('status'),choices=Statuses.choiceS(),max_length=(60),null=False)

class predmeti(models.Model):
    ime=models.CharField(max_length=(255),null=False)
    kod=models.CharField(unique=True,max_length=(16),null=False)
    program=models.TextField(null=False)
    bodovi=models.IntegerField(null=False)
    sem_redovni=models.IntegerField(null=False)
    sem_izvanredni=models.IntegerField(null=False)
    izborni=models.CharField(_('izborni'),choices=Izborni.Choices(),max_length=(60),null=False)

class upisi(models.Model):
    student_id = models.ForeignKey(korisnici, on_delete=models.CASCADE)
    predmet_id = models.ForeignKey(predmeti, on_delete=models.CASCADE)
    status=models.CharField(max_length=(64),null=False)
     