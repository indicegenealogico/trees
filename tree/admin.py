from django.contrib import admin
from .models import *


# Register your models here.
#=======================================================================
@admin.register(Tree)
class MakeAdmin(admin.ModelAdmin):
  pass

#=======================================================================
@admin.register(Pest)
class MakeAdmin(admin.ModelAdmin):
  pass

#=======================================================================
@admin.register(Host)
class MakeAdmin(admin.ModelAdmin):
  pass

#=======================================================================
@admin.register(Chemical)
class MakeAdmin(admin.ModelAdmin):
  pass

#=======================================================================
@admin.register(Ingredient)
class MakeAdmin(admin.ModelAdmin):
  pass

#=======================================================================
@admin.register(Concentration)
class MakeAdmin(admin.ModelAdmin):
  pass
