from django.contrib import admin
from account.models import account

class addaccount(admin.ModelAdmin):
    list_display = ["fullname","email","number","state","city","password"]
admin.site.register(account, addaccount)    