########################################################################################################################

# Description: Classe HotMail permettant de gérer les actions du menu principal
# Author: Hugo BOURDAIS
# Date: 22/09/2024

########################################################################################################################
# Importation de modules
########################################################################################################################

from etc.service.ExcelReader import ExcelReader
from etc.service.TemplateReader import TemplateReader

########################################################################################################################
# Classe MailFactory
########################################################################################################################

class MailFactory:
    """
    Classe permettant de lire le template du mail et le fichier Excel
    puis de construire les mails
    """

    def __init__(self, tr:TemplateReader, er:ExcelReader):
        """
        Constructeur de la classe
        :param tr: Instance de la classe TemplateReader
        :type tr: TemplateReader
        :param er: Instance de la classe ExcelReader
        :type er: ExcelReader
        """
        self.__tr :TemplateReader= tr
        self.__er :ExcelReader= er

        # On extrait les gaps du template
        self.__template_properties :list= self.__tr.get_template_properties()
        # On regarde si les gaps du template sont présents dans le fichier Excel
        self.__check_properties()

        # Si tout est bon, on construit les mails
        self.__template :str= self.__tr.template
        self.mails :list[dict]= self.__build_mails()

    def __check_properties(self) -> None:
        """
        Vérifier si les gaps du template sont présents dans le fichier Excel
        :exception: Exception si un gap n'est pas présent dans le fichier Excel
        """
        # On extrait les noms des colonnes du fichier Excel
        excel_properties :list[str]= self.__er.get_columns()

        # On vérifie que les gaps et les propriétés du template sont de même taille
        if len(self.__template_properties) != len(excel_properties) - 1:
            raise Exception("Le nombre de gaps du template et le nombre de propriétés du fichier Excel ne sont pas égaux")

        # On vérifie si les gaps du template sont présents dans le fichier Excel
        for prop in self.__template_properties:
            if prop not in excel_properties:
                raise Exception(f"Le gap {prop} n'est pas présent dans le fichier Excel")

    def __build_mail(self, row:dict) -> str:
        """
        Construire un mail à partir d'une ligne du fichier Excel
        :param row: Ligne du fichier Excel
        :type row: dict
        :return: Mail
        :rtype: str
        """
        return self.__tr.fill_template(row)

    def __build_mails(self) -> list[dict]:
        """
        Construire les mails à partir des lignes du fichier Excel
        :return: Liste des mails
        :rtype: list[str]
        """
        mails :list[dict]= []
        for row in self.__er.rows_to_json():
            mail :str= self.__build_mail(row)
            to :str= row['email']
            temp :dict= {'mail': mail, 'to': to}
            mails.append(temp)
        return mails