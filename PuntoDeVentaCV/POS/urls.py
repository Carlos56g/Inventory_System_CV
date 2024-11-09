from django.urls import path

from . import views


app_name="pos"
urlpatterns = [
    path("", views.indexPOS, name="homePOS"),
    path("product", views.indexProduct, name="indexProduct"),
    path("Brand", views.indexBrand, name="indexBrand"),
    path("Supplier", views.indexSupplier, name="indexSupplier"),
    path("Category", views.indexCategory, name="indexCategory"),
    path("newBrand", views.BrandCreateView.as_view(), name="newBrand"),
    path("newSupplier", views.SupplierCreateView.as_view(), name="newSupplier"),
    path("newCategory", views.CategoryCreateView.as_view(), name="newCategory"),
    path("newProduct", views.ProductCreateView.as_view(), name="newProduct"),
    path("product/detail/<int:pk>", views.DetailView.as_view(), name="detailProduct"),
    path("product/put/<int:productID>", views.putProduct, name="putProduct"),
    path("product/delete/<int:productID>", views.deleteProduct, name="deleteProduct"),

]

