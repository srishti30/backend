from django.contrib.auth import get_user_model
from django.contrib import admin
from .models import ResetPasswordLink, EmailTemplate, SocialAccount

User = get_user_model()

admin.site.register(ResetPasswordLink)
admin.site.register(EmailTemplate)
admin.site.register(SocialAccount)
admin.site.register(User)
