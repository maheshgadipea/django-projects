from django.contrib import admin

# Register your models here.
from usersapp.models import UserAccount

admin.site.register(UserAccount)