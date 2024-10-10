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

# Fonctions


# Programme Principal
if __name__ == '__main__':
    unittest.main()
