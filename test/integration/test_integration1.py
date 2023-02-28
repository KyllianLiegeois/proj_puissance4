import pytest

from noyau import *

def test_exemple():
   joueur=0
   i=2
   j=0
   grille=[[-1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1],
           [0, -1, -1, -1, -1, -1, -1],
           [0,  1, -1, -1, -1, -1, -1],
           [0,  1, -1, -1, -1, -1, -1],
           [0,  1, -1, -1, -1, -1, -1]]
   assert True==True

def test_maj_jeu():
    grille=[[-1]*7 for _ in range(6)]
    niveau=[5]*7
    joueur = 0
    i, j = maj_jeu('b1', grille, niveau, joueur)
    assert i == 5 and j == 0 and grille[i][j] == joueur
    i, j = maj_jeu('b1', grille, niveau, joueur)
    assert i == 4 and j == 0 and grille[i][j] == joueur
    i, j = maj_jeu('b1', grille, niveau, joueur)
    assert i == 3 and j == 0 and grille[i][j] == joueur
  
