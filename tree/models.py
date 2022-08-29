from django.db import models


# Create your models here.

#=======================================================================
class Tree(models.Model):
  
  common     = models.CharField('Common Name', max_length=30, blank=False, null=False )
  scientific = models.CharField('Scientific Name', max_length=50, blank=True,  null=True)
  photo_link = models.URLField( blank=True)
  gallery    = models.URLField( blank=True)

  class Meta:
    ordering = ['common']

  def __str__(self) :
    return (self.common)


#=======================================================================
class Pest(models.Model):

  class Meta:
    # verbose_name        = 'Body'
    # verbose_name_plural = 'Bodies'
    ordering = ['name']
    
  class Categories(models.IntegerChoices):
    DISEASE = 1
    INSECT  = 2
    WEED    = 3
    
  name        = models.CharField('Pest', max_length=50, blank=False, null=False)
  category    = models.PositiveIntegerField(null=False, choices=Categories.choices, default=1)
  phatogen    = models.CharField(max_length=30, blank=True)
  description = models.TextField(blank=True)
  photo_link  = models.URLField( blank=True)
  tree        = models.ManyToManyField(Tree, through='Host')

  def __str__(self) :
    return (self.name)


#=======================================================================
class Host(models.Model):
  
  tree     = models.ForeignKey(Tree, on_delete=models.CASCADE)
  pest     = models.ForeignKey(Pest, on_delete=models.CASCADE)
  symptoms = models.TextField(blank=True)
  
  class Meta:
    unique_together = [['tree', 'pest']]


#=======================================================================
class Chemical(models.Model):

  class Categories(models.IntegerChoices):
    FUNGICIDE       = 1
    GROWN_REGULATOR = 2
    HERBICIDE       = 3
    INSECT_MITICIDE = 4
    INSECTICIDE     = 5
    NUTRIBOOSTER    = 6
    POST_EMERGENT   = 7
    PRE_EMERGENT    = 8

  name       = models.CharField('Chemical Name', max_length=30, blank=False, null=False )
  category   = models.PositiveIntegerField(null=False, choices=Categories.choices, default=1)
  brand      = models.CharField('Brand Name', max_length=50, blank=True,  null=True)
  epa        = models.CharField('EPA', max_length=20, blank=True)
  photo_link = models.URLField(blank=True)

  class Meta:
    ordering = ['name']

  def __str__(self) :
    return (self.name +' '+ self.brand)
  
  
#=======================================================================
class Ingredient(models.Model):
  
  active_ingredient = models.CharField('Active ingredient', max_length=30, blank=False, null=False)
  chemical          = models.ManyToManyField(Chemical, through='Concentration')


  class Meta:
    ordering = ['active_ingredient']

  def __str__(self) :
    return (self.active_ingredient)
  
  
#=======================================================================
class Concentration(models.Model):
  
  chemical          = models.ForeignKey(Chemical, on_delete=models.CASCADE)
  active_ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
  percentage        = models.CharField(max_length=6, blank=True)


  class Meta:
    unique_together = [['chemical', 'active_ingredient']]

  def __str__(self) :
    return ("%s %s" % (self.active_ingredient, self.percentage))