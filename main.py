########################################################################################################################

# Description: Fichier principal du programme
# Auteur: Hugo BOURDAIS
# Date: 22/09/2024

########################################################################################################################
# IMPORTS
########################################################################################################################

from etc.menu.HotMail import HotMail

########################################################################################################################
# Programme principal
########################################################################################################################

# Programme principal
if __name__ == '__main__':

    # Instance de HotMail
    hm: HotMail = HotMail()
    hm.show_menu()