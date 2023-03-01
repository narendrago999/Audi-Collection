from django.contrib import admin
from userContactUs.models import userContacted

class adminuserContacted(admin.ModelAdmin):
    list_display = ["fullname","email","question"]
admin.site.register(userContacted, adminuserContacted)    