# -*- coding: utf-8 -*-

from MaBase_MIB import *

### Question 1 : quel est l'ensemble des gardiens?


les_gardiens = {gardien.Nom for gardien in BaseGardiens}

triples = { (alien.NoCabine, alien.Nom, gardien.Nom) for alien in BaseAliens  for gardien in BaseGardiens if gardien.NoCabine == alien.NoCabine}

### Question 4 : l'ensemble des couples (alien,allée) pour chaque alien

couples = { (alien.Nom, cabine.NoAllee)
            for alien in BaseAliens
            for cabine in BaseCabines
            if cabine.NoCabine == alien.NoCabine}

## Question 5 : l'ensemble de tous les aliens de l'allée 2

ens2 = { (alien.Nom, cabine.NoAllee)
         for alien in BaseAliens
         for cabine in BaseCabines
         if cabine.NoCabine == alien.NoCabine and cabine.NoAllee == str(2) }


##Question 6 : l'ensemble de toutes les planètes dont sont originaires les aliens habitant une cellule de numéro pair

ens6 = { (alien.Planete)
         for alien in BaseAliens
         for cabine in BaseCabines
         if cabine.NoCabine == alien.NoCabine and int(cabine.NoCabine)%2 == 0 } 


##Question 7 :  l'ensemble des aliens dont les gardiens sont originaires de Terminus

ens7 = { (alien.Nom)
         for alien in BaseAliens
         for agents in BaseAgents
         for gardien in BaseGardiens
         if agents.Nom == gardien.Nom and gardien.NoCabine == alien.NoCabine and agents.Ville == 'Terminus' }

##Question 8 : l'ensemble des gardiens des aliens féminins qui mangent du bortsch

ens8 = { (gardien.Nom)
         for gardien in BaseGardiens
         for alien in BaseAliens
         for miam in BaseMiams
         if gardien.NoCabine == alien.NoCabine and alien.Sexe == 'F' and alien.Nom == miam.NomAlien and miam.Aliment== 'Bortsch' }
## Question 9 : 'ensemble des cabines dont les gardiens sont originaires de Terminus ou dont les aliens sont des filles

ens9 = { (gardien.NoCabine)
         for gardien in BaseGardiens
         for agents in BaseAgents
         for alien in BaseAliens
         if agents.Ville == 'Terminus' and agents.Nom == gardien.Nom and gardien.NoCabine == alien.NoCabine and alien.Sexe == 'F' }


## Question 10 :  Y a-t-il des aliments qui commencent par la même lettre que le nom du gardien qui surveille l'alien qui les mange ?

ens10 = { (miam.Aliment)
          for miam in BaseMiams
          for gardien in BaseGardiens
          for alien in BaseAliens
          if gardien.NoCabine == alien.NoCabine and alien.Nom == miam.NomAlien and gardien.Nom[0]==miam.Aliment[0] }

## Question 11 :  Y a-t-il cdes aliens originaires d'Euterpe ?

ens11 = { (alien.Nom)
          for alien in BaseAliens
          if alien.Planete == 'Euterpe' }

