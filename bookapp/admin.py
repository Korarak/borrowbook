from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(tb_member)
admin.site.register(tb_book)
admin.site.register(tb_borrow_book)