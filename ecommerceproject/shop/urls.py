from django.urls import path
from.import views
app_name='shop'

urlpatterns = [

    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProDetail,name='prodCatdetail'),
    # path('<slug:c_slug>/', views.products_by_category, name='products_by_category'),
]