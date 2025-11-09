from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Product, Cart, CartItem, Order
from .forms import ProductForm


# ------------------------------
# Vérifie si l'utilisateur est un gérant
# ------------------------------
def is_manager(user):
    return user.is_staff or user.is_superuser  # Autorise les administrateurs et gérants


# ------------------------------
# PRODUITS
# ------------------------------
def product_list(request):
    """Afficher la liste des produits."""
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def product_detail(request, pk):
    """Afficher les détails d’un produit."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})


# ------------------------------
# PANIER
# ------------------------------
@login_required
def add_to_cart(request, product_id):
    """Ajouter un produit au panier."""
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        item.quantity += 1
        item.save()

    messages.success(request, f"{product.name} a été ajouté au panier.")
    return redirect('cart_view')


@login_required
def remove_from_cart(request, item_id):
    """Supprimer un produit du panier."""
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    messages.info(request, f"{item.product.name} a été retiré du panier.")
    item.delete()
    return redirect('cart_view')


@login_required
def cart_view(request):
    """Afficher le contenu du panier."""
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total = cart.total_price()

    return render(request, 'products/cart.html', {
        'cart': cart,
        'items': items,
        'total': total,
    })


@login_required
def checkout_view(request):
    """Page de paiement."""
    cart = get_object_or_404(Cart, user=request.user)
    total = cart.total_price()

    return render(request, 'products/checkout.html', {
        'cart': cart,
        'total': total,
    })


# ------------------------------
# TABLEAU DE BORD DU GÉRANT
# ------------------------------
@login_required
@user_passes_test(is_manager)
def dashboard(request):
    """Tableau de bord du gérant : produits, commandes, statistiques."""
    products = Product.objects.all().order_by('-created_at')
    orders = Order.objects.all().order_by('-created_at')

    # ✅ Calcul des statistiques globales
    total_ventes = sum(order.total for order in orders)
    nombre_commandes = orders.count()
    nombre_clients = User.objects.count()
    produits_vendus = sum(item.quantity for order in orders for item in order.items.all())

    # ✅ Formulaire d’ajout de produit
    if request.method == 'POST' and 'add_product' in request.POST:
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit ajouté avec succès ✅")
            return redirect('dashboard')
    else:
        form = ProductForm()

    context = {
        'products': products,
        'orders': orders,
        'form': form,
        'total_ventes': total_ventes,
        'nombre_commandes': nombre_commandes,
        'nombre_clients': nombre_clients,
        'produits_vendus': produits_vendus,
    }
    return render(request, 'products/dashboard.html', context)


# ------------------------------
# GESTION DES PRODUITS PAR LE GÉRANT
# ------------------------------
@login_required
@user_passes_test(is_manager)
def edit_product(request, product_id):
    """Modifier un produit existant."""
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit modifié avec succès ✅")
            return redirect('dashboard')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'products/edit_product.html', {'form': form, 'product': product})


@login_required
@user_passes_test(is_manager)
def delete_product(request, product_id):
    """Supprimer un produit."""
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.warning(request, "Produit supprimé avec succès 🗑️")
    return redirect('dashboard')


# ------------------------------
# TABLEAUX DÉTAILLÉS DU GÉRANT
# ------------------------------
@login_required
@user_passes_test(is_manager)
def dashboard_users(request):
    """Liste de tous les utilisateurs inscrits."""
    users = User.objects.all().order_by('username')
    return render(request, 'products/dashboard_users.html', {'users': users})


@login_required
@user_passes_test(is_manager)
def dashboard_orders(request):
    """Liste complète des commandes."""
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'products/dashboard_orders.html', {'orders': orders})


@login_required
@user_passes_test(is_manager)
def dashboard_products(request):
    """Produits vendus."""
    products = Product.objects.all()
    return render(request, 'products/dashboard_products.html', {'products': products})


@login_required
@user_passes_test(is_manager)
def dashboard_sales(request):
    """Statistiques des ventes."""
    orders = Order.objects.all()
    total_ventes = sum(order.total for order in orders)
    return render(request, 'products/dashboard_sales.html', {'total_ventes': total_ventes})
