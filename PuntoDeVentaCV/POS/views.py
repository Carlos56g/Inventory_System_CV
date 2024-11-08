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

def index(request):
    product_list=Producto.objects.order_by("Producto").all()
    return render(request, 'POS/index.html', {'product_list': product_list})
    #output = ", ".join([p.product_name for p in product_list])
    #return HttpResponse(output)

class BrandCreateView(CreateView):
    model = Marca
    fields = ["Marca"]
    template_name = "POS/addBrand.html"
    success_url=reverse_lazy("pos:index")

    def form_valid(self, form):
        marca=form.save(commit=False)
        marca.save()
        return super().form_valid(form)
    
class CategoryCreateView(CreateView):
    model = Categoria
    fields = ["Categoria"]
    template_name = "POS/addCategory.html"
    success_url=reverse_lazy("pos:index")

    def form_valid(self, form):
        cagoria=form.save(commit=False)
        cagoria.save()
        return super().form_valid(form)
    
class SupplierCreateView(CreateView):
    model = Distribuidor
    fields = ["Distribuidor","Correo","Telefono","Descripcion","Direccion"]
    template_name = "POS/addSupplier.html"
    success_url=reverse_lazy("pos:index")

    def form_valid(self, form):
        distribuidor=form.save(commit=False)
        distribuidor.save()
        return super().form_valid(form)
    
class ProductCreateView(CreateView):
    model = Producto
    fields = ["Producto","Cantidad","PVenta","PCompra","Descripcion","IdDistribuidor","IdCategoria","IdMarca"]
    template_name = "POS/addProduct.html"
    success_url=reverse_lazy("pos:index")

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
        producto.save()
        return super().form_valid(form)
    

class DetailView(generic.DetailView):
    model=Producto
    template_name="pos/detail.html"

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
    return HttpResponseRedirect(reverse('pos:index'))

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
    return HttpResponseRedirect(reverse('pos:detailProduct', args=(Dproduct.id,)))




