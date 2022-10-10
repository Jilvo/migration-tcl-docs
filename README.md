# Statistics
## Métro Croix Paquet:
### Comparaison basique:
Temps : 3 secondes
Succès : 729
Échecs : 32
Soit 95.7%


## Métro Bellecour:
### Création abro + analyse:
Temps  160 secondes
Succès : 4141
Échecs : 39
Soit 99%

## Prêt Plans : 
### Création abro + analyse : 
Temps : 140 secondes + 70228 secondes Soit 19h30
Succès : 60825
Échecs : 41537
Soit 60%


## LIGNE C :
Temps : 493 secondes
Succès : 8746
Échecs : 293
Soit 95%

## Commun C:
Temps : 4957 secondes
Succès : 20671
Échecs : 512
Soit 96%

## Ligne A Cordeliers -> Massena : 
Temps : 731 secondes
Succès : 9408
Échecs : 474
Soit 95%

## Tram 1 Claude Bernard -> Saint André :
Temps : 2 secondes
Succès : 175
Échecs : 0
Soit 100%


# Optimisation
## Station Bellecour avec en parrallèle une extraction des prêt
### Création abro + analyse : 
Temps : 21 sec 

### En enlevant tout les filtres de listes ,en dehors de 'H:' :
Temps : 222 secondes
Succès : 4058
Échecs : 40

Exemple d'une liste : ['Tcl', '105 à 122 - Métro A - stations', 'Bellecour', '01 Courant fort faible', 'HL00HLM0961830000E20PSS00330', 'HL00HLM0961830000E20PSS00330-F04P04']

### En rajoutant une condition d'au moins 2 chiffres par élément et avec un parser:
Temps : 85-95 secondes
Exemple d'une liste : ['HL00HLM0961830000E20PSS00330', 'HL00HLM0961830000E20PSS00330-F04P02']


## 2ème essaie Prêt:
Temps : 61387 secondes soit 17h

Succès : 70937
Échecs : 31022
Soit : 70%

# SERBER:
## 50000
### Création nouveau script :
Temps : 1267 secondes
Succès : 299
Échecs : 160
Soit : 65% 

