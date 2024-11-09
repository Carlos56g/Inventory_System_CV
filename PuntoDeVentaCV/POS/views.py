#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Producto
from .models import Marca
from .models import Categoria
from .models import Distribuidor
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, DeleteView
from django.views import generic
from django.http import HttpResponseRedirect

def indexProduct(request):
    product_list=Producto.objects.order_by("Producto").all()
    return render(request, 'POS/indexProduct.html', {'product_list': product_list})

def indexBrand(request):
    brand_list=Marca.objects.order_by("Marca").all()
    return render(request, 'POS/indexBrand.html', {'brand_list': brand_list})

def indexCategory(request):
    category_list=Categoria.objects.order_by("Categoria").all()
    return render(request, 'POS/indexCategory.html', {'category_list': category_list})

def indexSupplier(request):
    supplier_list=Distribuidor.objects.order_by("Distribuidor").all()
    return render(request, 'POS/indexSupplier.html', {'supplier_list': supplier_list})

class BrandCreateView(CreateView):
    model = Marca
    fields = ["Marca"]
    template_name = "POS/addBrand.html"
    success_url=reverse_lazy("pos:indexProduct")

    def form_valid(self, form):
        marca=form.save(commit=False)
        marca.save()
        return super().form_valid(form)
    
class CategoryCreateView(CreateView):
    model = Categoria
    fields = ["Categoria"]
    template_name = "POS/addCategory.html"
    success_url=reverse_lazy("pos:indexProduct")

    def form_valid(self, form):
        categoria=form.save(commit=False)
        categoria.save()
        return super().form_valid(form)
    
class SupplierCreateView(CreateView):
    model = Distribuidor
    fields = ["Distribuidor","Correo","Telefono","Descripcion","Direccion"]
    template_name = "POS/addSupplier.html"
    success_url=reverse_lazy("pos:indexProduct")

    def form_valid(self, form):
        distribuidor=form.save(commit=False)
        distribuidor.save()
        return super().form_valid(form)
    
class ProductCreateView(CreateView):
    model = Producto
    fields = ["Producto","Cantidad","PVenta","PCompra","Descripcion","IdDistribuidor","IdCategoria","IdMarca","Imagen"]
    template_name = "POS/addProduct.html"
    success_url=reverse_lazy("pos:indexProduct")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add the lists to the context
        context["distribuidores_list"] = Distribuidor.objects.order_by("Distribuidor").all()
        context["categorias_list"] = Categoria.objects.order_by("Categoria").all()
        context["marcas_list"] = Marca.objects.order_by("Marca").all()
        return context

    def form_valid(self, form):
        producto=form.save(commit=False)
        producto.Imagen = self.request.FILES.get("Imagen")
        producto.save()
        return super().form_valid(form)
    

class DetailView(generic.DetailView):
    model=Producto
    template_name="pos/detailProduct.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add the lists to the context
        context["distribuidores_list"] = Distribuidor.objects.order_by("Distribuidor").all()
        context["categorias_list"] = Categoria.objects.order_by("Categoria").all()
        context["marcas_list"] = Marca.objects.order_by("Marca").all()
        return context
    

def deleteProduct(request, productID):
    Dproduct = get_object_or_404(Producto, pk=productID)
    Dproduct.delete()
    return HttpResponseRedirect(reverse('pos:indexProduct'))

def deleteBrand(request, brandID):
    Dproduct = get_object_or_404(Producto, pk=brandID)
    Dproduct.delete()
    return HttpResponseRedirect(reverse('pos:indexBrand'))

def deleteSupplier(request, brandID):
    Dproduct = get_object_or_404(Producto, pk=brandID)
    Dproduct.delete()
    return HttpResponseRedirect(reverse('pos:indexSupplier'))

def deleteCategory(request, brandID):
    Dproduct = get_object_or_404(Producto, pk=brandID)
    Dproduct.delete()
    return HttpResponseRedirect(reverse('pos:indexCategory'))

def putProduct(request, productID):
    Dproduct = get_object_or_404(Producto, pk=productID)
    Dproduct.Producto = request.POST.get('Producto')
    Dproduct.Cantidad = request.POST.get('Cantidad')
    Dproduct.PVenta = request.POST.get('PVenta')
    Dproduct.PCompra = request.POST.get('PCompra')
    Dproduct.Descripcion = request.POST.get('Descripcion')
    Dproduct.IdCategoria.id = request.POST.get('IdCategoria')
    Dproduct.IdDistribuidor.id = request.POST.get('IdDistribuidor')
    Dproduct.IdMarca.id = request.POST.get('IdMarca')
    Dproduct.save()
    return HttpResponseRedirect(reverse('pos:indexProduct'))


def indexPOS(request):
    current_user = request.user
    return render(request, 'POS/indexPOS.html',{'user': current_user})

