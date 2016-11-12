from django.contrib import admin
from models import User, Topic, Room, Message

class UserAdmin(admin.ModelAdmin):
    pass

class TopicAdmin(admin.ModelAdmin):
    pass

class RoomAdmin(admin.ModelAdmin):
    pass

class MessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)