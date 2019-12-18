from rest_framework.routers import DefaultRouter
from rest_framework.renderers import CoreJSONRenderer

from . import views

router = DefaultRouter()
router.register(r'entities', views.EntityListViewSet, basename='entities')
router.register(r'entity-data', views.EntityDataListViewSet, basename='entity_data')
router.default_schema_renderers = (CoreJSONRenderer, )
urlpatterns = router.urls
