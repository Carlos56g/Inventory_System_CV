#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Producto
from .models import Marca
from .models import Categoria
from .models import Distribuidor
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.views import generic
from django.http import HttpResponseRedirect

def indexProduct(request):
    current_user = request.user
    product_list=Producto.objects.order_by("Producto").filter(Usuario=current_user)
    return render(request, 'POS/indexProduct.html', {'product_list': product_list})

def indexBrand(request):
    current_user = request.user
    brand_list=Marca.objects.order_by("Marca").filter(Usuario=current_user)
    return render(request, 'POS/indexBrand.html', {'brand_list': brand_list})

def indexCategory(request):
    current_user = request.user
    category_list=Categoria.objects.order_by("Categoria").filter(Usuario=current_user)
    return render(request, 'POS/indexCategory.html', {'category_list': category_list})

def indexSupplier(request):
    current_user = request.user
    supplier_list=Distribuidor.objects.order_by("Distribuidor").filter(Usuario=current_user)
    return render(request, 'POS/indexSupplier.html', {'supplier_list': supplier_list})

def indexPOS(request):
    current_user = request.user
    return render(request, 'POS/indexPOS.html',{'user': current_user})

class BrandCreateView(CreateView):
    model = Marca
    fields = ["Marca"]
    template_name = "POS/addBrand.html"
    success_url=reverse_lazy("POS:indexBrand")

    def form_valid(self, form):
        marca=form.save(commit=False)
        current_user = self.request.user
        marca.Usuario=current_user
        marca.save()
        return super().form_valid(form)
    
class CategoryCreateView(CreateView):
    model = Categoria
    fields = ["Categoria"]
    template_name = "POS/addCategory.html"
    success_url=reverse_lazy("POS:indexCategory")
    def form_valid(self, form):
        categoria=form.save(commit=False)
        current_user = self.request.user
        categoria.Usuario=current_user
        categoria.save()
        return super().form_valid(form)
    
class SupplierCreateView(CreateView):
    model = Distribuidor
    fields = ["Distribuidor","Correo","Telefono","Descripcion","Direccion"]
    template_name = "POS/addSupplier.html"
    success_url=reverse_lazy("POS:indexSupplier")

    def form_valid(self, form):
        distribuidor=form.save(commit=False)
        current_user = self.request.user
        distribuidor.Usuario=current_user       
        distribuidor.save()
        return super().form_valid(form)
    
class ProductCreateView(CreateView):
    model = Producto
    fields = ["Producto","Cantidad","PVenta","PCompra","Descripcion","IdDistribuidor","IdCategoria","IdMarca","Imagen"]
    template_name = "POS/addProduct.html"
    success_url=reverse_lazy("POS:indexProduct")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add the lists to the context
        current_user = self.request.user
        context["distribuidores_list"] = Distribuidor.objects.order_by("Distribuidor").filter(Usuario=current_user)
        context["categorias_list"] = Categoria.objects.order_by("Categoria").filter(Usuario=current_user)
        context["marcas_list"] = Marca.objects.order_by("Marca").all().filter(Usuario=current_user)
        return context

    def form_valid(self, form):
        producto=form.save(commit=False)
        producto.Imagen = self.request.FILES.get("Imagen")
        if self.request.FILES.get("Imagen"):
            producto.Imagen = self.request.FILES.get("Imagen")
        else:
            producto.Imagen='images/default.png'
        current_user = self.request.user
        producto.Usuario=current_user
        producto.save()
        return super().form_valid(form)
    
class DetailProductView(generic.DetailView):
    model=Producto
    template_name="POS/detailProduct.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add the lists to the context
        current_user = self.request.user
        context["distribuidores_list"] = Distribuidor.objects.order_by("Distribuidor").filter(Usuario=current_user)
        context["categorias_list"] = Categoria.objects.order_by("Categoria").filter(Usuario=current_user)
        context["marcas_list"] = Marca.objects.order_by("Marca").filter(Usuario=current_user)
        return context
    
class DetailBrandView(generic.DetailView):
    model=Marca
    template_name="POS/detailBrand.html"

class DetailSupplierView(generic.DetailView):
    model=Distribuidor
    template_name="POS/detailSupplier.html"

class DetailCategoryView(generic.DetailView):
    model=Categoria
    template_name="POS/detailCategory.html"
    
def deleteProduct(request, productID):
    Dproduct = get_object_or_404(Producto, pk=productID)
    Dproduct.delete()
    return HttpResponseRedirect(reverse('POS:indexProduct'))

def deleteBrand(request, brandID):
    Dproduct = get_object_or_404(Marca, pk=brandID)
    Dproduct.delete()
    return HttpResponseRedirect(reverse('POS:indexBrand'))

def deleteSupplier(request, supplierID):
    Dproduct = get_object_or_404(Distribuidor, pk=supplierID)
    Dproduct.delete()
    return HttpResponseRedirect(reverse('POS:indexSupplier'))

def deleteCategory(request,categoryID):
    Dproduct = get_object_or_404(Categoria, pk=categoryID)
    Dproduct.delete()
    return HttpResponseRedirect(reverse('POS:indexCategory'))

def putProduct(request, productID):
    selection=request.POST.get('action')
    Dproduct = get_object_or_404(Producto, pk=productID)
    if (selection=="cambiar"):
        Dproduct.Producto = request.POST.get('Producto')
        Dproduct.Cantidad = request.POST.get('Cantidad')
        Dproduct.PVenta = request.POST.get('PVenta')
        Dproduct.PCompra = request.POST.get('PCompra')
        Dproduct.Descripcion = request.POST.get('Descripcion')
        Dproduct.IdCategoria = Categoria.objects.get(id=request.POST.get('IdCategoria'))
        #Dproduct.IdCategoria.id = request.POST.get('IdCategoria')
        Dproduct.IdDistribuidor = Distribuidor.objects.get(id=request.POST.get('IdDistribuidor'))
        #Dproduct.IdDistribuidor.id = request.POST.get('IdDistribuidor')
        Dproduct.IdMarca = Marca.objects.get(id=request.POST.get('IdMarca'))
        #Dproduct.IdMarca.id = request.POST.get('IdMarca')
        if (request.FILES.get("Imagen")):
            Dproduct.Imagen = request.FILES.get("Imagen")
        Dproduct.save()
    if (selection=="eliminarImagen"):
        Dproduct.Imagen='images/default.png'
        Dproduct.save()
    return HttpResponseRedirect(reverse('POS:detailProduct', args=[Dproduct.id]))

def putBrand(request, brandID):
    Dbrand = get_object_or_404(Marca, pk=brandID)
    Dbrand.Marca = request.POST.get('Marca')
    Dbrand.save()
    return HttpResponseRedirect(reverse('POS:detailBrand', args=[Dbrand.id]))

def putCategory(request, categoryID):
    DCategory = get_object_or_404(Categoria, pk=categoryID)
    DCategory.Categoria = request.POST.get('Categoria')
    DCategory.save()
    return HttpResponseRedirect(reverse('POS:detailCategory', args=[DCategory.id]))

def putSupplier(request, supplierID):
    Dsupplier = get_object_or_404(Distribuidor, pk=supplierID)
    Dsupplier.Distribuidor = request.POST.get('Distribuidor')
    Dsupplier.Correo = request.POST.get('Correo')
    Dsupplier.Telefono = request.POST.get('Telefono')
    Dsupplier.Descripcion = request.POST.get('Descripcion')
    Dsupplier.Direccion = request.POST.get('Direccion')
    Dsupplier.save()
    return HttpResponseRedirect(reverse('POS:detailSupplier', args=[Dsupplier.id]))

