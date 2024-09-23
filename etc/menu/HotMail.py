########################################################################################################################

# Description: Classe HotMail permettant de gérer les actions du menu principal
# Author: Hugo BOURDAIS
# Date: 22/09/2024

########################################################################################################################
# Importation de modules
########################################################################################################################

import pandas as pd
import os

from pandas import DataFrame
from etc.utils.Messages import Messages

########################################################################################################################
# Classe HotMail
########################################################################################################################

class HotMail:
    """
    Constructeur de la classe HotMail
    """

    def __init__(self) -> None:
        """
        Constructeur de la classe HotMail
        """
        self.__CONFIG_FILE: str = "configuration.json"
        self.__CONFIG_FOLDER: str = "res"

        self.messages: Messages = Messages()
        self.config :DataFrame = self.load_config().get('config', None)

    def show_menu(self) -> None:
        """
        Afficher le menu de configuration
        """
        os.system('cls')

        print(self.messages.LOGO)
        print(self.messages.AUTEUR, "at https://github.com/boguh/bot-mail", '\n')

        print(self.messages.MENU_TITRE, '\n')

        print(self.messages.OPTION_XLSX)
        print(self.messages.OPTION_TEMPLATE)
        print(self.messages.OPTION_PJ)
        print(self.messages.OPTION_MAIL)
        print(self.messages.OPTION_CONFIGURATION)
        print(self.messages.OPTION_QUITTER, '\n')

        option: int = self.ask_option()
        self.execute_action(option)

    def ask_option(self) -> int:
        """
        Demander une option à l'utilisateur
        :return: Option choisie
        :rtype: int
        """
        return int(input(self.messages.SELECT_OPTION))

    def execute_action(self, option :int) -> None:
        """
        Exécuter l'action correspondant à l'option choisie
        :param option: Option choisie
        :type option: int
        :return: None
        """
        if option == 1:
            # Ouverture du fichier Excel
            os.system('start excel res/' + self.config['xlsx'])
            self.show_menu()
        elif option == 2:
            # Ouverture du template
            os.system('start notepad res/' + self.config['template'])
            self.show_menu()
        elif option == 3:
            # Ouverture du pdf
            os.system('start res/' + self.config['attachment'])
            self.show_menu()
        elif option == 4:
            from etc.menu.MenuMail import MenuMail
            MenuMail(self).show_menu()
        elif option == 5:
            from etc.menu.MenuConfiguration import MenuConfiguration
            MenuConfiguration(self).show_menu()
        elif option == 6:
            os.system('cls')
        else:
            self.show_menu()

    def load_config(self) -> DataFrame:
        """
        Charger la configuration à partir du fichier de configuration avec pandas
        :return: Dictionnaire contenant la configuration
        :rtype: dict
        """
        # Obtenir le répertoire courant
        current_dir: str = os.getcwd()
        # Construire le chemin complet
        chemin_fichier: str = os.path.join(current_dir, self.__CONFIG_FOLDER, self.__CONFIG_FILE)
        # Lire le fichier de configuration
        return pd.read_json(chemin_fichier)

    def change_json_prop(self, prop :str, value :str) -> None:
        """
        Changer une propriété du fichier de configuration
        :param prop: Propriété à changer
        :type prop: str
        :param value: Nouvelle valeur
        :type value: str
        :return: None
        """
        self.config[prop] = value
        self.save_config()

    def save_config(self) -> None:
        """
        Sauvegarder la configuration dans le fichier de configuration
        au format JSON : {'config': {'email': '...', 'password': '...', 'objet': '...'}}
        :return: None
        """
        # Dictionnaire temporaire
        temp :dict = {'config': self.config}
        # Obtenir le répertoire courant
        current_dir: str = os.getcwd()
        # Construire le chemin complet
        chemin_fichier: str = os.path.join(current_dir, self.__CONFIG_FOLDER, self.__CONFIG_FILE)
        # Sauvegarder la configuration
        pd.DataFrame(temp).to_json(chemin_fichier)