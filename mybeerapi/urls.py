from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'marcas', views.MarcaViewSet)
router.register(r'modelos', views.ModeloViewSet)
router.register(r'lojas', views.LojaViewSet)
router.register(r'bebidas', views.BebidaViewSet)
router.register(r'produtos', views.ProdutoViewSet)
router.register(r'cestas', views.CestaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]