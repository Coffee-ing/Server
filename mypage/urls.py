from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "mypage"

urlpatterns = [
    path('myclub/', get_my_apply, name='myapply'),
    path('myclub/<int:post_id>/', delete_my_apply, name='delete-myapply'),
    path('mylike/', get_my_like, name='myapply'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)