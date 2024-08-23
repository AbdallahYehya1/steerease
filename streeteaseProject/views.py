from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Size, Session, Cart, images
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
    return render(request,"products/home.html")
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

def home_view(request):
     return render(request, 'home.html')
def contact(request):
     return render(request, 'products/contactUs.html')
def menwomen(request):
     return render(request, 'products/menWomen.html')
def aboutUs(request):
     return render(request, 'products/about-us.html')
def cart_view(request):
    session_id = request.session.session_key
    if not session_id:
        request.session.create()  # Create a new session if it doesn't exist
        session_id = request.session.session_key

    if request.method == 'GET':
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
    elif request.method == 'POST':
        operation = request.POST.get('operation')
        prod_id = request.POST.get('id')
        sname = request.POST.get('sName')
        session_id = request.session.session_key
        print(f"Operation: {operation}, Product ID: {prod_id}, Size Name: {sname}, Session ID: {session_id}")
        # Get the size object, or return a 404 if it doesn't exist
        sizeid = get_object_or_404(Size, size_name=sname.upper(), product_id=prod_id)
        print(f"sizeid: {sizeid}")
        # Check if the cart item exists
        cart_items = Cart.objects.filter(session_id=session_id, size=sizeid.id, product_id=prod_id)
        
        if cart_items.exists():
            cart_item = cart_items[0]
        

        if operation == '-':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
            

        elif operation == '+':
            # Check if there is enough stock available
            if sizeid.size_quantity > cart_item.quantity:
                cart_item.quantity += 1
                cart_item.save()
           
        
        elif operation == 'remove':
            cart_item.delete()
            

        return redirect('cart_view')
        

    context = {
        'cart': json.dumps(cart_data),
    }

    return render(request, 'products/cart.html', context)


def product_list(request):
    products_with_images = []
    gender = request.GET.get('gender', '')
    products = Product.objects.filter(gender=gender)
    
    for product in products:
        first_image = images.objects.filter(product_id=product.id).first()  # Get the first image for the product
        products_with_images.append({
            'product': product,
            'image_url': first_image.url if first_image else None  # Use the first URL (url1) if it exists
        })

    return render(request, 'products/products.html', {'products_with_images': products_with_images})

def checkout_view(request):
    session_id = request.session.session_key
    cart=Cart.objects.filter(session_id=session_id)
    for item in cart:
        quantity=item.quantity
        size=get_object_or_404(Size,id=item.size_id)
        size.size_quantity-=quantity
        size.save()
        
    cart.delete()    
    return render(request, 'products/Checkout.html')

def thank_you(request):

    return render(request, 'products/ThankYouPage.html')

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