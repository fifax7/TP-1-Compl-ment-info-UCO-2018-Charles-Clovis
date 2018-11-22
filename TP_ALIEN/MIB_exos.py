# -*- coding: utf-8 -*-

from MaBase_MIB import *

### Question 1 : quel est l'ensemble des gardiens?


les_gardiens = {gardien.Nom for gardien in BaseGardiens}

triples = { (alien.NoCabine, alien.Nom, gardien.Nom) for alien in BaseAliens  for gardien in BaseGardiens if gardien.NoCabine == alien.NoCabine}



couples = { (alien.Nom, Cabine.NoAllee) for alien in BaseAliens for NoAllee in BaseCabines if alien.NoCabine == cabines.NoCabine }




