from django.contrib import admin
from .models import Comment, Post, Friendship, Invite

class InviteAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']

admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Friendship)
admin.site.register(Invite, InviteAdmin)

