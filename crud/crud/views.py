from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProductForm
from .models import Product

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_product')  # redirect to same or another view
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')  # redirect to the product list or another view
    return render(request, 'delete_product.html', {'product': product})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})