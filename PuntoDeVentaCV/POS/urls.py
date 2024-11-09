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
    path("product/detail/<int:pk>", views.DetailProductView.as_view(), name="detailProduct"),
    path("brand/detail/<int:pk>", views.DetailBrandView.as_view(), name="detailBrand"),
    path("supplier/detail/<int:pk>", views.DetailSupplierView.as_view(), name="detailSupplier"),
    path("category/detail/<int:pk>", views.DetailCategoryView.as_view(), name="detailCategory"),
    path("brand/put/<int:brandID>", views.putBrand, name="putBrand"),
    path("category/put/<int:categoryID>", views.putCategory, name="putCategory"),
    path("product/put/<int:productID>", views.putProduct, name="putProduct"),
    path("supplier/put/<int:supplierID>", views.putSupplier, name="putSupplier"),
    path("product/delete/<int:productID>", views.deleteProduct, name="deleteProduct"),
    path("brand/delete/<int:brandID>", views.deleteBrand, name="deleteBrand"),
    path("supplier/delete/<int:supplierID>", views.deleteSupplier, name="deleteSupplier"),
    path("category/delete/<int:categoryID>", views.deleteCategory, name="deleteCategory"),

]



