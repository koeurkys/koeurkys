# Bibliothèques
import unittest
import random
from just_price import *

# Classes
class GameTest:
  def __init__(self):
    pass
  def test_nombre_aleatoire(self):
    nombre = generer_nombre_aleatoire()
    self.assertGreaterEqual(nombre, 1)
    self.assertLessEqual(nombre, 100)

  def test_saisie_utilisateur_valide(self):
    # Tests pour les valeur comprise entre 1 et 100
    self.assertEqual(saisie_utilisateur(50),50)  # 50 est valide
    self.assertEqual(saisie_utilisateur(12), 12) # 12 est valide
    self.assertEqual(saisie_utilisateur(93), 93) # 93 est valide
            
  def test_saisie_utilisateur_invalide_grand(self):
    with self.assertRaises(ValueError):
      saisie_utilisateur(101)  # Juste au-dessus de 100
    with self.assertRaises(ValueError):
      saisie_utilisateur(150)  # Valeur éloignée de 100
    with self.assertRaises(ValueError):
      saisie_utilisateur(1000)  # Valeur très élevée
        
  def test_saisie_utilisateur_invalide_petit(self):
    with self.assertRaises(ValueError):
      saisie_utilisateur(0)  # En dessous de 1
    with self.assertRaises(ValueError):
      saisie_utilisateur(-1)  # Valeur négative
    with self.assertRaises(ValueError):
      saisie_utilisateur(-100)  # Valeur très négative
    
  def test_saisie_utilisateru_invalide_type(self):
    with self.assertRaises(TypeError):
      saisie_utilisateur("50")  # Chaîne de caractères
    with self.assertRaises(TypeError):
      saisie_utilisateur(50.5)  # Float
    with self.assertRaises(TypeError):
      saisie_utilisateur([50])  # Liste


    
            
    

# Fonctions


# Programme Principal
if __name__ == '__main__':
    unittest.main()
