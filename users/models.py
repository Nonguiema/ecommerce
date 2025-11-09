from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Profil de {self.user.username}"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Crée un profil automatiquement lors de la création d'un utilisateur,
    ou le met à jour si l'utilisateur existe déjà.
    """
    if created:
        # Création du profil pour le nouvel utilisateur
        Profile.objects.create(user=instance)
    else:
        # Vérifie que le profil existe avant de sauvegarder
        if hasattr(instance, 'profile'):
            instance.profile.save()
