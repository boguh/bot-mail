########################################################################################################################
import os
# Description: Classe HotMail permettant de gérer les actions du menu principal
# Author: Hugo BOURDAIS
# Date: 22/09/2024

########################################################################################################################
# Importation de modules
########################################################################################################################

import smtplib
from email import encoders
from email.mime.base import MIMEBase

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

########################################################################################################################
# Classe MailService
########################################################################################################################

class MailService:
    """
    Service d'envoi de mail
    """

    RES_FILE_PATH = "res"

    def __init__(self, email :str, password :str) -> None:
        """
        Constructeur de la classe MailService
        :param email: Adresse email
        :type email: str
        :param password: Mot de passe
        :type password: str
        """
        # Configuration
        self.__SMTP_SERVER = 'smtp.gmail.com'
        self.__PORT = 587

        # Authentification
        self.__email = email
        self.__password = password

    def send(self, email :str, subject :str, message :str, attachment :str) -> bool:
        """
        Envoyer un mail
        :param email: Adresse email du destinataire
        :type email: str
        :param subject: Objet du mail
        :type subject: str
        :param message: Contenu du mail
        :type message: str
        :param attachment: Chemin du fichier à joindre
        :type attachment: str
        :return: True si le mail a été envoyé, False sinon
        :rtype: bool
        """
        # Créer un message
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Obtenir le répertoire courant
        current_dir: str = os.getcwd()
        # Construire le chemin complet
        chemin_fichier: str = os.path.join(current_dir, self.RES_FILE_PATH, attachment)
        # Joindre un fichier
        with open(chemin_fichier, 'rb') as temp:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(temp.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {attachment}')
        msg.attach(part)

        # Envoyer le message
        with smtplib.SMTP(self.__SMTP_SERVER, self.__PORT) as server:
            server.starttls()
            try :
                server.login(self.__email, self.__password)
            except smtplib.SMTPAuthenticationError:
                print("Erreur d'authentification")
                return False
            try:
                server.send_message(msg)
            except smtplib.SMTPException:
                print("Erreur lors de l'envoi du mail")
                return False
            server.quit()
            return True