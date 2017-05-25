#####################################################################
#
# File: urls.py
# Auth: Gerik Peterson
#
#####################################################################

from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

#from StoreManager.controllers import index,store
from StoreManager import views

app_name = 'storemanager'

schema_view = get_schema_view(title='Store Manager API')

router = DefaultRouter()
router.register(r'stores',views.StoreViewSet,base_name='Store')
router.register(r'products',views.ProductViewSet)
router.register(r'inventories',views.InventoryViewSet)

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
]


"""
urlpatterns = [
    url(r'^$',
        index.StoreManagerIndexView.as_view(),
        name='index'
        ),
    url(r'^store/$',
        store.CreateStoreView.as_view(),
        name='createstore'
        ),
    url(r'^store/(?P<pk>[0-9]+)/$',
        store.DetailedStoreView.as_view(),
        name='detailedstore'
        ),
]
"""
