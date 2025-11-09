from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


@csrf_protect
def register(request):
    """Inscription d’un nouvel utilisateur."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connexion automatique après inscription
            messages.success(request, "Compte créé avec succès 🎉 Bienvenue !")
            return redirect('product_list')  # Redirige vers la page produit (client)
        else:
            messages.error(request, "Erreur lors de l’inscription. Vérifiez vos informations.")
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})


@csrf_protect
def user_login(request):
    """Connexion de l’utilisateur (client ou gérant)."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # ✅ Vérifie si c’est un gérant ou un client
            if user.is_staff or user.is_superuser:
                messages.success(request, f"Bienvenue dans votre tableau de bord, {user.username} 👨‍💼")
                return redirect('dashboard')  # Gérant
            else:
                messages.success(request, f"Heureux de vous revoir, {user.username} 🎶")
                return redirect('product_list')  # Client
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, 'users/login.html')


@login_required
def profile(request):
    """Affichage et mise à jour du profil utilisateur."""
    # Crée un profil si inexistant
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    profile = request.user.profile

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "✅ Votre profil a été mis à jour avec succès.")
            return redirect('product_list')  # Redirection vers la page produits
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'users/profile.html', context)

def user_logout(request):
    """Déconnexion et redirection vers la page d’accueil."""
    logout(request)
    messages.info(request, "Vous êtes maintenant déconnecté ")
    return redirect('home')  # Redirige vers la page d’accueil
