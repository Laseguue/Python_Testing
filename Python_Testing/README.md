README.md pour le dépôt Python_Testing (Branche : QA)
Aperçu
Le dépôt Python_Testing, spécifiquement dans la branche QA, est une application web basée sur Flask. Elle est conçue pour gérer et réserver des places dans des compétitions sportives. L'application permet aux utilisateurs de voir, réserver et gérer les points des clubs et les places des compétitions.

Fonctionnalités Clés
Authentification des Utilisateurs : Les utilisateurs peuvent se connecter en utilisant leur email.
Voir les Compétitions : Lister et voir les détails des compétitions sportives à venir.
Réserver des Places : Réserver des places pour les compétitions.
Gérer les Points des Clubs : Voir et gérer les points pour différents clubs.
Modèles Réactifs : L'application utilise des modèles Flask pour une interface utilisateur dynamique et réactive.
Composants Principaux
Serveur (server.py) : Le fichier principal de l'application Flask. Il inclut des routes pour gérer différentes fonctionnalités comme voir les compétitions, réserver des places et gérer les points.
Voir le Fichier Serveur
Fichiers de Données : Fichiers JSON pour stocker les données des clubs et des compétitions.
Données des Clubs (clubs.json) : Contient des informations sur les clubs.
Voir les Données des Clubs
Données des Compétitions (competitions.json) : Contient les détails des compétitions.
Voir les Données des Compétitions
Modèles : Modèles HTML pour le rendu des pages web.
Réservation (booking.html) : Modèle pour la réservation de places pour les compétitions.
Accueil (index.html) : Le modèle de la page d'accueil.
Affichage des Points (points.html) : Modèle pour afficher les points des clubs.
Bienvenue (welcome.html) : Modèle affiché après la connexion.
Voir le Répertoire des Modèles
Installation et Configuration
Cloner le Dépôt :
bash
Copy code
git clone -b QA https://github.com/Laseguue/Python_Testing.git
Installer les Dépendances :
Copy code
pip install -r requirements.txt
Voir le Fichier des Prérequis
Exécuter l'Application :
Copy code
python server.py
Utilisation
Démarrez le serveur Flask et naviguez vers l'URL locale fournie (habituellement http://127.0.0.1:5000/).
Utilisez l'application pour voir les compétitions, réserver des places et gérer les points des clubs.
Contribuer
Les contributions au projet sont les bienvenues. Veuillez suivre les procédures standard pour contribuer aux projets open-source sur GitHub.

Licence
Le projet est open-source sous la Licence MIT.