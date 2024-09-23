# BotMail

## Description
BotMail est un projet Python qui permet d'envoyer des mails automatiquement à une liste de destinataires.

## Pré-requis
Si vous disposez d'un compte Gmail, vous devrez activer le partage pour les applications tiers.
Ensuite, vous pourrez récupérer un mot de passe à utiliser via le lien :
https://myaccount.google.com/apppasswords?

## Installation
Pour installer le projet, il suffit de cloner le dépôt et d'installer les dépendances nécessaires avec la commande suivante:
```bash
pip install -r requirements.txt
```

## Obligation
Ne surtout pas supprimer le fichier `config.json` car il est nécessaire pour le bon fonctionnement du projet.
Mais également les fichier `.xlsx` qui sont nécessaires pour l'envoi des mails ainsi que le fichier `.txt` qui est le template du mail.
Ces fichiers sont placés dans le dossier `res`.

## Utilisation
Pour utiliser le projet, il suffit de lancer le fichier `main.py` avec la commande suivante:
```bash
python main.py
```

## Compilation du projet en exécutable
Pour compiler le projet, il suffit de lancer la commande suivante:
```bash
pyinstaller main.spec
```


