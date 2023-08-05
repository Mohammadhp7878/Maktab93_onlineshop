from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products_api', views.ProductViewSet, basename='products_list')

product_router = routers.NestedDefaultRouter(router, 'products_api', lookup='product')
product_router.register('comments_api', views.CommentViewSet, basename='comments_api')


urlpatterns = [
    path('products', views.ProductsPage.as_view(), name='products_page'),
    path('categories_list/', views.CategoryView.as_view(), name='categories_list'),
    path('', include(product_router.urls)),
    path('', include(router.urls)),
]