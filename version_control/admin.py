from django.contrib import admin
from version_control.models import UserInfo

# Register your models here.
admin.site.site_header = "后台管理系统"
admin.site.site_title = "欢迎进入后台管理~"
admin.site.index_title = "版本管理后台"

admin.site.register(UserInfo)