from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from media_app.models import Image, Document
from random import randint

class ResourceCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    def __unicode__(self):
        return self.name

class Resource(models.Model):
    published = models.BooleanField(_("Published"), default=False)
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    category = models.ForeignKey(ResourceCategory, verbose_name=_("Category"))
    summary = models.TextField(_("Summary"), blank=True)
    link = models.URLField(_("Link URL"))
    image_set = generic.GenericRelation(Image)
    documents = generic.GenericRelation(Document)
    #preview = models.ImageField(upload_to="")

    def __unicode__(self):
        return self.title

    def size_x(self):
        return randint(8, 12)

    class Meta:
        ordering = ["-id"]
