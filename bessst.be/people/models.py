from django.db import models
from django.utils.translation import ugettext_lazy as _

class People(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    prefix = models.CharField(max_length=255, verbose_name=_("Prefix"), null=True, blank=True)
    slug = models.SlugField(_("Slug"), unique=True, help_text=_("Unique identifier. Allows a constant targeting of this event."))
    #country = 
    address = models.CharField(max_length=100, verbose_name=_("Address"), null=True, blank=True)
    city = models.CharField(max_length=80, verbose_name=_("Postal code + City"), null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name=_("Phone number"), null=True, blank=True)
    email = models.EmailField(max_length=100, verbose_name=_("Email"), null=True, blank=True)
    link = models.URLField(_("Link URL"), null=True, blank=True)
    biography = models.TextField(_("Short biography"), blank=True)

    def __unicode__(self):
        return self.name

class Individual(People):
    firstname = models.CharField(max_length=255, verbose_name=_("First Name"), null=True, blank=True)
    
class Organization(People):
    contact_person = models.ForeignKey(Individual, verbose_name=_("Contact Person"), related_name="contact_person", null=True, blank=True)
