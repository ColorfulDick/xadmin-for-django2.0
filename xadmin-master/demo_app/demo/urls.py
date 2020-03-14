# -*- coding: utf-8 -*-
from django.urls import path,include

# Uncomment the next two lines to enable the admin:
import xadmin
xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

#from django.contrib import admin

urlpatterns = [
    #path('admin/', include('admin.site.urls')),
    #path('', include('xadmin.site.urls'))
	path('admin/',xadmin.site.urls),
]
