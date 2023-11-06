from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import *

app_name = "clubs"

router = routers.DefaultRouter()
router.register('post', PostViewSet)
router.register('list', ListViewSet)

# post list : GET method
post_list = ListViewSet.as_view({
    'get' : 'list'
})

# post detail : POST method
post_detail = PostViewSet.as_view({
    'post' : 'create',
    'put' : 'update',
    'delete' : 'destroy'
})

urlpatterns = [
    path('search/', search_clubs, name='search'),
    path('list/<int:post_id>/', get_detail, name="detail"),

    path('', include(router.urls)),
    path('list/', post_list),
    path('list/<int:pk>', post_detail),
    
    path('list/registration/<int:post_id>/', register_club, name="registration"),
    path('like/<int:post_id>/', set_wishlist, name="wishlist"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)