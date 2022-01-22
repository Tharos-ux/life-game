'''
Automated unit tests
'''

import random
import unittest
from unittest.main import main
from unittest.mock import patch
import io
import sys
#TODO imports

""" Il est conseillé d'utiliser la commande
python -m unittest -v tests.py
dans un shell afin d'exécuter les tests unitaires.
"""

def documentation():
    "Affiche la doc utilisateur"
    print("\nIl est conseillé d'utiliser la commande\n\"python -m unittest -v tests.py\"\ndans un shell afin d'exécuter les tests unitaires.\n")

class TestMethods(unittest.TestCase):

############################# UNITTEST ##################################

    def test_raiseError(self):
        "Check ValueError"
        error_type = ValueError
        with self.assertRaises(error_type):
            # exercices.fonction_erreur()
            pass

    def test_valide(self):
        "Check if sucess"
        condition = 3
        resultat = True
        self.assertEqual(resultat,condition)

    # TODO tests ici :)

############################# AUTORUN ##################################

# si on lance le fichier en ligne de commande, on affiche la documentation générale
# pour que l'utilisateur sache comment utiliser les tests unitaires
if __name__ == "__main__":
    documentation()