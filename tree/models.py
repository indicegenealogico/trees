from unicodedata import name
from django.db import models

# Create your models here.


#=======================================================================
class Tree(models.Model):
  common_name = models.CharField(max_length=30, blank=False, null=False )
  photo_link = models.URLField( blank=True, null=True)

  class Meta:
    ordering = ['common_name']

  def __str__(self) :
    return (self.common_name)


#=======================================================================
class Disease(models.Model):
  name = models.CharField(max_length=30, blank=False, null=False  )
  description = models.TextField(null=True, blank=True)
  photo_link = models.URLField( blank=True, null=True)


  class Meta:
    ordering = ['name']

  def __str__(self) :
    return (self.name)