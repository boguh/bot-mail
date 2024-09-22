########################################################################################################################

# Description: Fichier contenant la classe MenuMail qui permet d'envoyer des mails à partir d'un fichier Excel et d'un
# Author: Hugo BOURDAIS
# Date: 22/09/2024

########################################################################################################################
# IMPORTS
########################################################################################################################

import os
import time

from etc.menu.HotMail import HotMail
from etc.service.ExcelReader import ExcelReader
from etc.service.MailFactory import MailFactory
from etc.service.MailService import MailService
from etc.service.TemplateReader import TemplateReader
from etc.utils.Messages import Messages

########################################################################################################################
# CLASSE
########################################################################################################################

class MenuMail:

    def __init__(self, app :HotMail) -> None:
        """
        Constructeur de la classe
        :param app: Instance de la classe HotMail
        :type app: HotMail
        """
        self.NOM_XLSX = "mon_fichier.xlsx"
        self.NOM_TEMPLATE = "mon_template.txt"

        self.message = Messages()
        self.app :HotMail= app

        self.__er: ExcelReader = ExcelReader(self.NOM_XLSX)
        self.__tr: TemplateReader = TemplateReader(self.NOM_TEMPLATE)
        self.__mf: MailFactory = MailFactory(self.__tr, self.__er)
        self.__mails: list[dict] = self.__mf.mails

    def __header_menu(self) -> None:
        """
        Afficher l'en-tête du menu
        :return: None
        """
        os.system('cls')
        print(self.message.LOGO)
        print(self.message.AUTEUR, '\n')
        print(self.message.MAIL_TITRE, '\n')

    def show_menu(self) -> None:
        """
        Afficher le menu d'envoi des mails
        :return: None
        """
        self.__header_menu()

        print(self.message.MAIL_INFO_NOMBRE + str(len(self.__mails)), '\n')

        print(self.message.MAIL_ENVOI)
        print(self.message.MAIL_LISTE)
        print(self.message.MAIL_APERCU)
        print(self.message.MAIL_QUITTER, '\n')

        option :int= self.ask_option()
        self.execute_action(option)

    def ask_option(self) -> int:
        """
        Demander une option
        :return: Option
        :rtype: int
        """
        return int(input(self.message.SELECT_OPTION))

    def execute_action(self, option :int) -> None:
        """
        Exécuter l'action correspondant à l'option choisie
        :param option: Option choisie
        :type option: int
        :return: None
        """
        if option == 1:
            # Envoyer le(s) mail(s)
            self.send_mails()
        elif option == 2:
            # Liste des destinataires
            self.show_list()
        elif option == 3:
            # Aperçu du mail
            self.show_preview()
        elif option == 4:
            # Quitter
            self.app.show_menu()
        else:
            self.show_menu()

    def send_mails(self) -> None:
        """
        Envoyer le(s) mail(s)
        """
        self.__header_menu()

        # On indique que l'action une fois lancée est irréversible
        print(self.message.MAIL_ATTENTION, '\n')
        confirmation: str = input(self.message.MAIL_CONFIRMATION)

        # Si l'utilisateur ne confirme pas, on revient au menu
        if confirmation != 'o':
            self.show_menu()

        # Sinon, on envoie les mails
        else :
            ms :MailService= MailService(self.app.config['email'], self.app.config['password'])
            for mail in self.__mails:
                self.__header_menu()
                temp :bool = ms.send(mail['to'], self.app.config['objet'], mail['mail'])
                if not temp:
                    print("Erreur lors de l'envoi du mail à :", mail['to'])
                    break
                else:
                    print("Mail envoyé à :", mail['to'], "(Total envoyé :", self.__mails.index(mail) + 1, "/", len(self.__mails), ")")
                    time.sleep(1)

            input("\nAppuyez sur une touche pour continuer...")
            self.show_menu()

    def show_list(self) -> None:
        """
        Afficher la liste des destinataires
        :return:
        """
        os.system('cls')

        print(self.message.LOGO)
        print(self.message.AUTEUR, '\n')

        print(self.message.MAIL_TITRE, '\n')

        for i, mail in enumerate(self.__mails):
            print(f"\t{i + 1}/ {mail['to']}")

        input("\nAppuyez sur une touche pour continuer...")
        self.show_menu()

    def show_preview(self) -> None:
        """
        Afficher un aperçu du mail
        :return:
        """
        os.system('cls')

        print(self.message.LOGO)
        print(self.message.AUTEUR, '\n')

        print(self.message.MAIL_TITRE, '\n')

        print(self.__tr.template, '\n')
        input("Appuyez sur une touche pour continuer...")
        self.show_menu()