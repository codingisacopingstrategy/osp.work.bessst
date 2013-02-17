from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Image(models.Model):
    description = models.CharField(max_length=255, verbose_name=_("Caption"))
    image = models.ImageField(upload_to="images", max_length=100, verbose_name=_("Image file"))
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()

    def __unicode__(self):
        return self.description

class Document(models.Model):
    description = models.CharField(max_length=255, verbose_name=_("Caption"))
    document = models.FileField(upload_to="documents", max_length=100, verbose_name=_("Document File"))
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()

    def __unicode__(self):
        return self.description

