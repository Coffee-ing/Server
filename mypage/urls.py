from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "mypage"

urlpatterns = [
    path('myclub/', get_my_clubs, name='myclub'),
    path('myclub/<int:post_id>/', delete_my_club, name='delete-myclub'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)