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

def test_coup_gagnant():
    grille = [[0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]
    joueur = 1
    i = 2
    j = 2
    assert coup_gagnant(joueur, i, j, grille) == False

    grille = [[0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0],
              [0, 0, 1, 0, 0, 0],
              [0, 0, 1, 0, 0, 0]]
    joueur = 1
    i = 5
    j = 2
    assert coup_gagnant(joueur, i, j, grille) == True

    grille = [[0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0],
              [0, 1, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0]]
    joueur = 1
    i = 5
    j = 0
    assert coup_gagnant(joueur, i, j, grille) == True



