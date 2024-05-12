from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products
from .forms import ProductForm

apple_products = [
    {"id": "1", "product_name": "iPhone 13", "description": "The iPhone 13 is the latest iteration of Apple's iconic smartphone lineup. It features a stunning Super Retina XDR display, powerful A15 Bionic chip, and advanced dual-camera system with improved low-light performance and computational photography capabilities. With its sleek design and all-day battery life, the iPhone 13 is designed to elevate your everyday experiences."},
    {"id": "2", "product_name": "MacBook Air", "description": "The MacBook Air is an ultra-thin and lightweight laptop that redefines portability. It boasts a brilliant Retina display, blazing-fast performance thanks to the Apple M1 chip, and exceptional battery life that lasts up to 18 hours on a single charge. Whether you're a student, professional, or creative, the MacBook Air is the perfect companion for getting things done on the go."},
    {"id": "3", "product_name": "iPad Pro", "description": "The iPad Pro is the ultimate tablet for power users and creatives. It features a stunning Liquid Retina XDR display with ProMotion technology, the blazing-fast Apple M1 chip, and support for the Apple Pencil and Magic Keyboard. With its versatility and performance, the iPad Pro lets you tackle any task, from editing 4K videos to creating intricate digital artwork, with ease."},
    {"id": "4", "product_name": "Apple Watch Series 7", "description": "The Apple Watch Series 7 is the most advanced smartwatch yet. It features a larger and more durable display, faster charging, and new health and fitness features like fall detection and blood oxygen monitoring. With its sleek design and customizable watch faces, the Apple Watch Series 7 lets you stay connected, motivated, and in control of your health and fitness."},
    {"id": "5", "product_name": "AirPods Pro", "description": "AirPods Pro are wireless earbuds that deliver immersive sound and active noise cancellation for an unparalleled listening experience. They feature a customizable fit with three sizes of soft, silicone tips, and are sweat and water resistant, making them perfect for workouts and outdoor activities. With transparency mode, you can hear what's happening around you without taking your AirPods Pro out, and with Adaptive EQ, the music automatically tunes to the shape of your ear for a rich, consistent listening experience."}
]


def product(request, pk):
    data = Products.objects.get(id=pk)
    tags = data.tag.all()
    return render(request, "project/product.html", {"data" : data, "tags" : tags})

def products(request):
    data = Products.objects.all()
    return render(request, "project/products.html", {"data" : data})

def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    return render(request, "project/create.html", {"form" : form })

def updateProduct(request, pk):
    product = Products.objects.get(id=pk)
    form = ProductForm(instance = product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    return render(request, "project/create.html", {"form" : form })

def deleteProduct(request, pk):
    product = Products.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    return render(request, "project/delete.html", {"object" : product })


