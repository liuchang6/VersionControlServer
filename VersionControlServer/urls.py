"""VersionControlServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import SimpleRouter

from version_control.views import server,login,repository


router = SimpleRouter()
router.register('server', server.ServerInfoView)
router.register('check_server', server.CheckServiceView)
router.register('get_server', server.ConnectServiceInfoView)
router.register('repository', repository.RepositoryInfoView)
router.register('check_repository', repository.CheckRepositoryView)
router.register('get_repository', repository.ConnectRepositoryInfoView)

login_router = SimpleRouter()
login_router.register('login',login.LoginView)
login_router.register('check_token',login.CheckTokenView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(login_router.urls)),
    path(r'api/', include(router.urls)),
]
