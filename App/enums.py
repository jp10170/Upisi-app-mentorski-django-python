from enum import Enum
from django.utils.translation import ugettext_lazy as _

class Roles(Enum):
    role_mentor='MENTOR'
    role_student='STUDENT'
    
    def __str__(self):
        return self.value
    
    @classmethod
    def choices(cls):
        return (
                (str(cls.role_mentor),_('mentor')),
                (str(cls.role_student),_('student')),
                
               )
class Statuses(Enum):
    status_none='NONE'
    status_redovni='REDOVNI'
    status_izvanredni='IZVANREDNI'
    def __str__(self):
        return self.value
    
    @classmethod
    def choiceS(cls):
        return (
                (str(cls.status_none),_('none')),
                (str(cls.status_redovni),_('redovni')),
                (str(cls.status_izvanredni),_('izvanredni')),
               )
class Izborni(Enum):
    izborni_da='DA'
    izborni_ne='NE'
    def __str__(self):
        return self.value
    @classmethod
    def Choices(cls):
        return (
                 (str(cls.izborni_da),_('da')),
                 (str(cls.izborni_ne),_('ne')),
               )
    