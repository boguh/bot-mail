########################################################################################################################

# Description: Classe permettant de lire un fichier Excel
# Auteur : Hugo BOURDAIS
# Date : 20/09/2024

########################################################################################################################
# IMPORTS
########################################################################################################################

import pandas as pd
import os

from pandas import DataFrame

########################################################################################################################
# CLASSE
########################################################################################################################

class ExcelReader:
    """
    Classe permettant de lire un fichier Excel
    """

    # Chemin du répertoire contenant les fichiers Excel
    RES_FILE_PATH :str = "res"

    def __init__(self, file_name:str):
        """
        Constructeur de la classe
        :param file_name: Nom du fichier Excel
        :type file_name: str
        """
        self.file_name :str= file_name
        self.df :DataFrame= self.read()

    def read(self) -> DataFrame:
        """
        Lire le fichier Excel
        :return: DataFrame contenant les données du fichier Excel
        :rtype: DataFrame
        """
        # Obtenir le répertoire courant
        current_dir :str= os.getcwd()
        # Construire le chemin complet
        chemin_fichier :str= os.path.join(current_dir, self.RES_FILE_PATH, self.file_name)
        return pd.read_excel(chemin_fichier)

    def get_row(self, row:int) -> DataFrame:
        """
        Obtenir une ligne du fichier Excel
        :param row: Numéro de la ligne
        :type row: int
        :return: DataFrame contenant la ligne du fichier Excel
        :rtype: DataFrame
        """
        return self.read().iloc[row]

    def get_number_of_rows(self) -> int:
        """
        Obtenir le nombre de lignes du fichier Excel
        :return: Nombre de lignes
        :rtype: int
        """
        return len(self.read())

    def row_to_json(self, row:int) -> dict:
        """
        Construire un dictionnaire à partir d'une ligne du fichier Excel
        :param row: Numéro de la ligne
        :type row: int
        :return: Dictionnaire contenant les données de la ligne
        :rtype: dict
        """
        return self.get_row(row).to_dict()

    def rows_to_json(self) -> list:
        """
        Construire une liste de dictionnaires à partir des lignes du fichier Excel
        :return: Liste de dictionnaires contenant les données des lignes
        :rtype: list
        """
        return self.read().to_dict(orient="records")

    def get_columns(self) -> list:
        """
        Obtenir les noms des colonnes du fichier Excel
        :return: Liste des noms des colonnes
        :rtype: list
        """
        return self.read().columns.tolist()

########################################################################################################################