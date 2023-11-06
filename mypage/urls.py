from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main.views import PostViewSet
from .views import *
from rest_framework import routers

app_name = "mypage"

router = routers.DefaultRouter()
router.register('post', PostViewSet)

# post detail : PUT method
post_detail_put =  PostViewSet.as_view({
    'put' : 'update',
})

# post detail : DELETE method
post_detail_delete =  PostViewSet.as_view({
    'delete' : 'destroy'
})

urlpatterns = [
    path('myapply/', get_my_apply, name='myapply'),
    path('myapply/<int:post_id>/', delete_my_apply, name='delete-myapply'),
    path('mylike/', get_my_like, name='myapply'),

    path('myclub/<int:post_id>/mod', post_detail_put),
    path('myclub/<int:post_id>/del', post_detail_delete),
    path('myclub/', get_my_club), 
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)