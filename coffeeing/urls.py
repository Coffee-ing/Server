from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main.views import *

router = routers.DefaultRouter()
router.register('post', PostViewSet)
router.register('list', ListViewSet)

# post list : GET method
post_list = ListViewSet.as_view({
    'get' : 'list'
})

# post detail : POST, PUT, DELETE method
post_detail = PostViewSet.as_view({
    'post' : 'create',
    'put' : 'update',
    'delete' : 'destroy'
})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('list/', post_list),
    path('list/<int:pk>', post_detail),
]
