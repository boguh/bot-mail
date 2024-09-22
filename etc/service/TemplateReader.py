########################################################################################################################

# Description: Classe permettant de lire le template du mail
# Auteur : Hugo BOURDAIS
# Date : 20/09/2024

########################################################################################################################
# IMPORTS
########################################################################################################################

import os

########################################################################################################################
# CLASSE
########################################################################################################################

class TemplateReader:
    """
    Classe permettant de lire le template du mail
    """

    # Chemin du répertoire contenant le template
    RES_FILE_PATH :str = "res"

    def __init__(self, file_name:str):
        """
        Constructeur de la classe
        :param file_name: Nom du fichier contenant le template
        :type file_name: str
        """
        self.file_name :str= file_name
        self.template :str= self.__read()
        self.template_properties :list= self.get_template_properties()

    def __read(self) -> str:
        """
        Lire le fichier contenant le template
        :return: Contenu du fichier
        :rtype: str
        """
        # Obtenir le répertoire courant
        current_dir: str = os.getcwd()
        # Construire le chemin complet
        chemin_fichier: str = os.path.join(current_dir, self.RES_FILE_PATH, self.file_name)
        with open(chemin_fichier, "r") as f:
            return f.read()

    def get_template_properties(self) -> list:
        """
        Obtenir les gaps du template qui sont entre {{ et }}
        ex: 'Blabla {{NOM}} et {{PRENOM}} blabla' -> ['NOM', 'PRENOM']
        :return: Liste des gaps
        :rtype: list
        """
        # On initialise la liste des gaps
        gaps :list= []
        # On parcourt le template
        for i in range(len(self.template)):
            # Si on trouve un {{
            if self.template[i] == "{" and self.template[i + 1] == "{":
                # On initialise le gap
                gap :str= ""
                # On parcourt le template a partir de la position i + 2
                for j in range(i + 2, len(self.template)):
                    # Si on trouve un }}
                    if self.template[j] == "}" and self.template[j + 1] == "}":
                        # On ajoute le gap a la liste
                        gaps.append(gap)
                        # On sort de la boucle
                        break
                    # On ajoute le caractère au gap
                    gap += self.template[j]
        # On retourne la liste des gaps
        return gaps

    def fill_template(self, data:dict) -> str:
        """
        Remplacer les gaps du template par les valeurs du dictionnaire
        ex: '{{{ NOM }}}' -> 'DUPONT'
        :param data: Dictionnaire contenant les valeurs
        :type data: dict
        :return: Template rempli
        :rtype: str
        """
        # On vérifie que les gaps et les propriétés du template sont de même taille
        if len(self.template_properties) != len(data) - 1:
            raise Exception("Le nombre de gaps du template et le nombre de propriétés du dictionnaire ne sont pas égaux")

        # On vérifie que les gaps du template sont présents dans le dictionnaire
        for prop in self.template_properties:
            if prop not in data:
                raise Exception(f"Le gap {prop} n'est pas présent dans le dictionnaire")

        # On initialise le template a remplir
        template :str= self.template

        # On remplace les gaps par les valeurs
        for prop in self.template_properties:
            # On construit le champ a remplacer
            gap :str= "{{" + prop + "}}"
            # On remplace le champ par la valeur
            template = template.replace(gap, data[prop])

        # On retourne le template rempli
        return template