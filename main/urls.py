from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "clubs"

urlpatterns = [
    path('search/', search_clubs, name='search'),
    path('list/<int:post_id>/', get_detail, name="detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)