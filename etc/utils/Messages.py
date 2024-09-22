########################################################################################################################

# Description: Classe HotMail permettant de gérer les actions du menu principal
# Author: Hugo BOURDAIS
# Date: 22/09/2024

########################################################################################################################
# Classe
########################################################################################################################

class Messages:
    """
    Cette classe contient les messages de l'application
    sous la forme de constantes.
    """

    def __init__(self) -> None:
        """
        Constructeur de la classe Messages
        """
        # Messages d'erreur --------------------------------------------------------------------------------------------
        self.ERREUR_FICHIER: str = "Erreur lors de la lecture du fichier"
        self.ERREUR_TEMPLATE: str = "Erreur lors de la lecture du template"
        self.ERREUR_MAIL: str = "Erreur lors de l'envoi du mail"
        self.ERREUR_OPTION: str = "(Option invalide)"
        # --------------------------------------------------------------------------------------------------------------

        # Messages de succès -------------------------------------------------------------------------------------------
        self.SUCCES_FICHIER: str = "Fichier lu avec succès"
        self.SUCCES_TEMPLATE: str = "Template lu avec succès"
        self.SUCCES_MAIL: str = "Mail envoyé avec succès"
        # --------------------------------------------------------------------------------------------------------------

        # Messages d'information ---------------------------------------------------------------------------------------
        self.INFO_FICHIER: str = "Lecture du fichier en cours"
        self.INFO_TEMPLATE: str = "Lecture du template en cours"
        self.INFO_MAIL: str = "Envoi du mail en cours"
        # --------------------------------------------------------------------------------------------------------------

        # Messages de confirmation -------------------------------------------------------------------------------------
        self.CONFIRMATION_FICHIER: str = "Fichier lu"
        self.CONFIRMATION_TEMPLATE: str = "Template lu"
        self.CONFIRMATION_MAIL: str = "Mail envoyé"
        # --------------------------------------------------------------------------------------------------------------

        # Messages de contrôle du menu ---------------------------------------------------------------------------------
        self.MENU_TITRE: str = "~ HotMail ~"
        self.SELECT_OPTION: str = "Sélectionnez une option: "
        self.OPTION_XLSX: str = "\t1 - Ouvrir le fichier Excel"
        self.OPTION_TEMPLATE: str = "\t2 - Ouvrir le template"
        self.OPTION_MAIL: str = "\t3 - Envoyer le(s) mail(s)"
        self.OPTION_CONFIGURATION: str = "\t4 - Configuration"
        self.OPTION_QUITTER: str = "\t5 - Quitter"
        # --------------------------------------------------------------------------------------------------------------

        # Messages d'action pour le menu configuration -----------------------------------------------------------------
        self.CONFIGURATION_TITRE: str = "~ Configuration ~"
        self.CONFIGURATION_EMAIL: str = "\t1 - Changer l'email"
        self.CONFIGURATION_PASSWORD: str = "\t2 - Changer le mot de passe"
        self.CONFIGURATION_OBJET: str = "\t3 - Changer l'objet"
        self.CONFIGURATION_XLSX: str = "\t4 - Changer le nom du fichier Excel"
        self.CONFIGURATION_TEMPLATE: str = "\t5 - Changer le nom du template"
        self.CONFIGURATION_FIN: str = "\t6 - Quitter la configuration"

        # Configuration actuelle
        self.CONFIG_EMAIL: str = "Email: "
        self.CONFIG_PASSWORD: str = "Mot de passe: "
        self.CONFIG_OBJET: str = "Objet: "
        self.CONFIG_XLSX: str = "Nom du fichier Excel: "
        self.CONFIG_TEMPLATE: str = "Nom du template: "

        # Messages d'erreur pour le menu configuration
        self.ERREUR_EMAIL: str = "Erreur lors du changement de l'email"
        self.ERREUR_PASSWORD: str = "Erreur lors du changement du mot de passe"
        self.ERREUR_FIN: str = "Erreur lors de la fin de la configuration"

        # Messages d'action pour le menu d'envoi de mail ---------------------------------------------------------------
        self.MAIL_TITRE: str = "~ Envoi de mail ~"
        self.MAIL_INFO_NOMBRE: str = "Nombre de destinataires trouvés: "

        # Options
        self.MAIL_ENVOI: str = "\t1 - Envoyer le(s) mail(s)"
        self.MAIL_LISTE: str = "\t2 - Liste des destinataires"
        self.MAIL_APERCU: str = "\t3 - Aperçu du mail"
        self.MAIL_QUITTER: str = "\t4 - Quitter l'envoi de mail"

        # Messages de confirmation pour le menu d'envoi de mail
        self.MAIL_ATTENTION: str = "Attention, une fois le processus lancé, il ne peut être arrêté."
        self.MAIL_CONFIRMATION: str = "Voulez-vous vraiment envoyer le(s) mail(s) ? (o/n) "

        # Messages de fin ----------------------------------------------------------------------------------------------
        self.FIN: str = "Fin du programme"
        # --------------------------------------------------------------------------------------------------------------

        # Page de lancement --------------------------------------------------------------------------------------------
        self.LOGO: str = """
  ____        _   __  __       _ _ 
 |  _ \      | | |  \/  |     (_) |
 | |_) | ___ | |_| \  / | __ _ _| |
 |  _ < / _ \| __| |\/| |/ _` | | |
 | |_) | (_) | |_| |  | | (_| | | |
 |____/ \___/ \__|_|  |_|\__,_|_|_|                                   
"""
        self.AUTEUR: str = "by boguh"