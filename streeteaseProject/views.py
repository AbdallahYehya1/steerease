from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Size, Session, Cart, images
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
    return render(request,"hello/home.html")
# your_app/views.py


from django.contrib.sessions.models import Session

def add_to_cart(request, product_id):
    # Get the product
    product = get_object_or_404(Product, id=product_id)

    # Get the session (You might need to customize this depending on how you manage sessions)
    session_id = request.session.session_key
    if not session_id:
        request.session.create()
        session_id = request.session.session_key
    
    session = get_object_or_404(Session, session_key=session_id)
    
    if request.method == 'POST':
        size_id = request.POST.get('size_id')
        
        # Get the size object
        size = get_object_or_404(Size, id=size_id, product=product)
        
        # Get the first image for the product
        first_image = images.objects.filter(product=product).first()
        image_url = first_image.url if first_image else 'http://example.com/default.jpg'
        
        # Check if the cart item already exists
        cart_item, created = Cart.objects.get_or_create(
            product=product,
            session=session,
            size=size,
            defaults={'imageUrl': image_url, 'quantity': 1}
        )
        
        if not created:
            # If the item already exists, increase the quantity
            cart_item.quantity += 1
            cart_item.save()
        
        return redirect('cart_view')  # Replace 'cart_view' with your cart view name

    return HttpResponse(status=400)



def cart_view(request):
    session_id = request.session.session_key
    if not session_id:
        request.session.create()  # Create a new session if it doesn't exist
        session_id = request.session.session_key

    # Get the cart items for the current session
    cart_items = Cart.objects.filter(session_id=session_id)

    # Convert cart items to a list of dictionaries
    cart_data = []
    for item in cart_items:
        cart_data.append({
            'id': item.product.id,
            'name': item.product.name,
            'quantity': item.quantity,
            'price': float(item.product.price),
            'imagepath': item.imageUrl,  # Update with correct image field
            'size_name': item.size.size_name,  # Assuming you want size_name
        })
    print(cart_data)
    context = {
        'cart': json.dumps(cart_data),
    }

    return render(request, 'products/cart.html', context)


def product_list(request):
    products_with_images = []
    
    for product in Product.objects.all():
        first_image = images.objects.filter(product_id=product.id).first()  # Get the first image for the product
        products_with_images.append({
            'product': product,
            'image_url': first_image.url if first_image else None  # Use the first URL (url1) if it exists
        })

    return render(request, 'products/products.html', {'products_with_images': products_with_images})

def product_detail(request, product_id):
    # Get the product with the given id
    product = get_object_or_404(Product, id=product_id)
    
    # Get the images for this product
    image = images.objects.filter(product_id=product_id)
    first_image_url = image.first().url if image.exists() else None
    
    # Get the sizes for this product
    sizes = Size.objects.filter(product_id=product_id)
    
    context = {
        'product': product,
        'first_image_url':first_image_url,
        'images': image,
        'sizes': sizes,
    }
    
    return render(request, 'products/product_details.html', context)