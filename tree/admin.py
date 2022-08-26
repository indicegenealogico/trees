from django.contrib import admin
from .models import *


# Register your models here.
#=======================================================================
@admin.register(Tree)
class MakeAdmin(admin.ModelAdmin):
  pass

#=======================================================================
@admin.register(Issue)
class MakeAdmin(admin.ModelAdmin):
  pass

#=======================================================================
@admin.register(Host)
class MakeAdmin(admin.ModelAdmin):
  pass
