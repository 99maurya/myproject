
from django.contrib import admin
from django.urls import path, include
from app.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from django.urls import path
from app.views import ProductSearchAPIView




router = routers.DefaultRouter()

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

 
# define the router path and viewset to be used

router.register(r'user', UserViewset)
router.register(r'category', CategoryViewset)
router.register(r'subcategory', SubCategoryViewset)
router.register(r'product', ProductViewset)
router.register(r'product-images', ProductImageViewset)
router.register(r'order',OrderViewSet)
router.register(r'subcategory_by_category',SubCategoryByCategoryIdViewSet,basename='subcategory_by_category_id')
router.register(r'product_by_subcategory',ProductBySubCategoryIdViewset,basename='product_by_subcategory_id')

# router.register(r'cart', AddToCartViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', homepage, name='homepage'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    # path('', homepage, name='homepage'),


    # Category Views #
    path('create/', Create_category, name='Create_category'),
    path('category/edit/<int:id>/', Edit_cat, name='edit_category'),


    path('api/search/', ProductSearchAPIView.as_view(), name='product_search'),
    # path('api/')


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Subcategory Views #
    path('sub_category/<int:id>/', sub_category, name="sub_category"), 
    path('create_subcategory/<int:id>/', create_subcategory, name="create_subcategory"), 
    path('edit_sub_cat/<int:subcategory_id>/', edit_sub_cat, name="edit_sub_category"), 
    path('delete_sub_category/<int:subcategory_id>/', delete_sub_category, name="delete_sub_category"),
    
   
    ## product_page ##
    path('products_list_page/<int:subcategory_id>/', product_list_page, name='product_list_page'),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),
    path('create-product/<int:subcategory_id>/', create_product, name='create_product'),
    path('edit-product/<int:product_id>/', Edit_product_page, name='edit_product'),
    path('product_delete/<int:product_id>/', delete, name='delete'),
    path('delete-product/<int:product_id>/', delete, name='delete'),
    
   
    
   
   ## cart options ##
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('order/', create_order, name="create_order"),
    # path('buy-now/<int:product_id>/', Buy_Now, name="Buy_Now"),
   
    # User authentication Views #
    path('create_user/', createuser, name='create_user'),
    path('login/', userlogin, name="userlogin"),
    path('logout/', userlogout, name="userlogout"),
    path('profile/', get_profile, name='get_profile'),
    path('search/', search_bar, name="search_bar"),
    

    ## review ##
    path('product/<int:product_id>/add_review/', add_review, name='add_review'),
    path('product/<int:product_id>/edit_review/<int:review_id>/', edit_review, name='edit_review'),
    path('product/<int:product_id>/review/<int:review_id>/delete/', delete_review, name='delete_review'),


    
    # order urls
    path('order/', proceed_order, name="proceed_order"),
    path('buy-now/<int:product_id>/',Buy_Now, name='Buy_Now'),
    path('order/confirmation/<int:order_id>/', order_confirmation, name="order_confirmation"),
    path('order/cancel/<int:order_id>/', cancel_order, name='cancel_order'),
    path('history/', order_history, name="order_history"),
    # path('mark_as_delivered/<int:order_id>/', mark_as_delivered, name='mark_as_delivered'),

    path("ajax/",ajax_page)


] + static(settings.STATIC_URL, documents_root= settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
