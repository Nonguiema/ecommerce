# ecommerce
# Projet Ecommerce Django

Ce projet est une application ecommerce développée avec **Django**.  
Il permet aux utilisateurs de consulter les produits, créer un compte, gérer leur panier et effectuer des achats.  
Une interface dédiée au **gérant** permet également de gérer l’activité du site.

---

##  Fonctionnalités principales

### 🔹 Côté client
- Consultation des produits par catégorie
- Recherche de produits
- Détails d’un produit
- Ajout au panier
- Gestion du panier
- Création de compte / Connexion
- Commande et validation d'achat
- Gestion du profil utilisateur

---

##  Fonctionnalités du gérant

L’interface du gérant permet de suivre et gérer tout le site ecommerce :

### 🔸 Tableau de bord du gérant
- Vue globale de l’activité du site
- Récapitulatif des commandes récentes
- Statistiques (ventes du mois, nombre de clients, etc.)

### 🔸 Gestion des produits
- Ajouter un produit
- Modifier un produit
- Supprimer un produit
- Gestion des images des produits
- Gestion des catégories

### 🔸 Gestion des commandes
- Voir toutes les commandes
- Suivre le statut d’une commande (en attente, en livraison, terminée)
- Détails d’une commande

### 🔸 Gestion des utilisateurs
- Voir la liste des clients
- Accéder aux informations de chaque client
- Filtrage / recherche d’utilisateur

### 🔸 Options avancées
- Gestion des promotions ou réductions
- Rapports téléchargeables (PDF/Excel)
- Configuration du site (logo, nom, devise, etc.)

---

##  Technologies utilisées
- **Django 4+**
- **Python 3**
- **HTML / CSS / Bootstrap**
- **SQLite** 
- **Git / GitHub**

---

##  Installation

### 1. Cloner le projet
git clone https://github.com/Nonguiema/ecommerce.git

### 2. Créer un environnement virtuel

python3 -m venv env
source env/bin/activate


### 3. Installer les dépendances

pip install -r requirements.txt


### 4. Appliquer les migrations

python manage.py migrate


### 5. Lancer le serveur

python manage.py runserver


---

## Structure du projet

ecommerce/
│── ecommerce/ # Configuration principale Django
│── core/ # Pages principales & dashboard gérant
│── store/ # Gestion des produits
│── orders/ # Gestion des commandes
│── users/ # Authentification & profils
│── static/ # Fichiers CSS / JS / images
│── templates/ # Templates HTML
│── manage.py


---

##  Contact
Projet développé par **Romaric Nonguierma**  
Pour toute suggestion ou amélioration, n'hésitez pas à contribuer via GitHub.

