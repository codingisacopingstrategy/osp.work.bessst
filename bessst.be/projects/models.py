from django.db import models
from django.utils.translation import ugettext_lazy as _
from axis.models import Axis
from people.models import People
from django.contrib.contenttypes import generic
from media_app.models import Image

from random import randint

class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    slug = models.SlugField(_("Slug"), unique=True, help_text=_("Unique identifier. Allows a constant targeting of this event."))
    archived = models.BooleanField(_("Archived"), default=False)
    producers = models.ManyToManyField(People, verbose_name=_("Stiltebemidelaars"), related_name="producer_set")
    location = models.CharField(max_length=80, verbose_name=_("Location"), null=True)
    axis = models.ForeignKey(Axis, verbose_name=_("Axis"))
    summary = models.TextField(_("Summary"))
    description = models.TextField(_("Description"))
    image_set = generic.GenericRelation(Image)

#    @property
    def size_x(self):
        return randint(4, 14)
    
#    @property
    def size_y(self):
        return randint(2, 7)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('project-detail', (), {'slug': str(self.slug)})
