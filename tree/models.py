from django.db import models


# Create your models here.

#=======================================================================
class Tree(models.Model):
  
  common_name = models.CharField('Common Name', max_length=30, blank=False, null=False )
  photo_link  = models.URLField( blank=True)

  class Meta:
    ordering = ['common_name']

  def __str__(self) :
    return (self.common_name)


#=======================================================================
class Issue(models.Model):

  class Meta:
    # verbose_name        = 'Body'
    # verbose_name_plural = 'Bodies'
    ordering = ['name']
    
  class Type(models.IntegerChoices):
    DISEASE = 1
    INSECT  = 2
    
  name        = models.CharField('Issue', max_length=30, blank=False, null=False)
  type        = models.PositiveIntegerField(null=False, choices=Type.choices, default=1)
  description = models.TextField(blank=True)
  photo_link  = models.URLField( blank=True)
  tree        = models.ManyToManyField(Tree, through='Host')

  def __str__(self) :
    return (self.name)


#=======================================================================
class Host(models.Model):
  
  tree     = models.ForeignKey(Tree, on_delete=models.CASCADE)
  issue    = models.ForeignKey(Issue, on_delete=models.CASCADE)
  symptoms = models.TextField(blank=True)
  
  class Meta:
    unique_together = [['tree', 'issue']]
  