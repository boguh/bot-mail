########################################################################################################################

# Description: Classe HotMail permettant de gérer les actions du menu principal
# Author: Hugo BOURDAIS
# Date: 22/09/2024

########################################################################################################################
# Importation de modules
########################################################################################################################

import os

from etc.menu.HotMail import HotMail
from etc.utils.Messages import Messages

########################################################################################################################
# Classe MenuConfiguration
########################################################################################################################

class MenuConfiguration:
    """
    Classe permettant de gérer le menu de configuration
    """

    def __init__(self, app :HotMail) -> None:
        """
        Constructeur de la classe
        :param app: Instance de la classe HotMail
        :type app: HotMail
        """
        self.message = Messages()
        self.app :HotMail= app

    def __header_menu(self) -> None:
        """
        Afficher l'en-tête du menu
        """
        os.system('cls')
        print(self.message.LOGO)
        print(self.message.AUTEUR, "at https://github.com/boguh/bot-mail", '\n')
        print(self.message.CONFIGURATION_TITRE, '\n')

    def show_menu(self) -> None:
        """
        Afficher le menu de configuration
        """
        self.__header_menu()

        print(self.message.SEPARATEUR)
        print(self.message.CONFIG_EMAIL + self.app.config['email'])
        print(self.message.CONFIG_PASSWORD + self.app.config['password'])
        print(self.message.CONFIG_OBJET + self.app.config['objet'])
        print(self.message.SEPARATEUR)
        print(self.message.CONFIG_XLSX + self.app.config['xlsx'])
        print(self.message.CONFIG_TEMPLATE + self.app.config['template'])
        print(self.message.CONFIG_PJ, self.app.config['attachment'])
        print(self.message.SEPARATEUR, '\n')

        print(self.message.CONFIGURATION_EMAIL)
        print(self.message.CONFIGURATION_PASSWORD)
        print(self.message.CONFIGURATION_OBJET)
        print(self.message.CONFIGURATION_XLSX)
        print(self.message.CONFIGURATION_TEMPLATE)
        print(self.message.CONFIGURATION_PJ)
        print(self.message.CONFIGURATION_FIN, '\n')

        option :int= self.ask_option()
        self.execute_action(option)

    def ask_option(self) -> int:
        """
        Demander une option
        :return: Option
        :rtype: int
        """
        return int(input(self.message.SELECT_OPTION))

    def change_email(self) -> None:
        """
        Changer l'email
        """
        self.__header_menu()

        print(self.message.CONFIG_EMAIL + self.app.config['email'])
        email :str= input("Nouvel email: ")
        self.app.change_json_prop('email', email)

        self.show_menu()

    def change_password(self) -> None:
        """
        Changer le mot de passe
        """
        self.__header_menu()

        print(self.message.CONFIGURATION_TITRE, '\n')

        print(self.message.CONFIG_PASSWORD + self.app.config['password'])
        password :str= input("Nouveau mot de passe: ")
        self.app.change_json_prop('password', password)

        self.show_menu()

    def change_objet(self) -> None:
        """
        Changer l'objet
        """
        self.__header_menu()

        print(self.message.CONFIGURATION_TITRE, '\n')

        print(self.message.CONFIG_OBJET + self.app.config['objet'])
        objet :str= input("Nouvel objet: ")
        self.app.change_json_prop('objet', objet)

        self.show_menu()

    def change_xlsx(self) -> None:
        """
        Changer le nom du fichier Excel
        """
        self.__header_menu()

        print(self.message.CONFIG_XLSX + self.app.config['xlsx'])
        xlsx :str= input("Nouveau nom du fichier Excel: ")
        self.app.change_json_prop('xlsx', xlsx)

        self.show_menu()

    def change_template(self) -> None:
        """
        Changer le nom du template
        """
        self.__header_menu()

        print(self.message.CONFIG_TEMPLATE + self.app.config['template'])
        template :str= input("Nouveau nom du template: ")
        self.app.change_json_prop('template', template)
        print(self.message.CONFIRMATION_TEMPLATE)

        self.show_menu()

    def change_attachment(self) -> None:
        """
        Changer le nom du fichier à joindre
        """
        self.__header_menu()

        print(self.message.CONFIG_PJ + self.app.config['attachment'])
        attachment :str= input("Nouveau nom du fichier à joindre: ")
        self.app.change_json_prop('attachment', attachment)

        self.show_menu()

    def execute_action(self, option :int) -> None:
        """
        Exécuter une action
        :param option: Option
        :type option: int
        """
        if option == 1:
            self.change_email()
        elif option == 2:
            self.change_password()
        elif option == 3:
            self.change_objet()
        elif option == 4:
            self.change_xlsx()
        elif option == 5:
            self.change_template()
        elif option == 6:
            self.change_attachment()
        elif option == 7:
            self.app.show_menu()
        else:
            self.show_menu()