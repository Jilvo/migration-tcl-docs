# How to run files :
## Configuration PC:
## Lancement des fichiers :

# Première Itération : 
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


# Seconde itération en filtrant ligne par ligne Optimisation
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
Succès : 380
Échecs : 78
Soit : 83% 


# SEMALY
### Analyse matching PDF et TIF:
Temps : 670 secondes
Succès : 11585
Échecs : 3
Soit : 99% 



# Script tri fichier ExtractionTCLDoc Complete
## Croix paquet :
Temps 32 secondes
Succès : 737
Échecs : 1
Soit : 99% 

## Ligne C :
Temps : 940 secondes
Succès : 8818
Échecs : 179
Soit : 98% 

## Ligne T1 :
Temps : 3716  secondes
Succès : 6870
Échecs : 539
Soit : 90% 

## Prêt 2017 : 
Temps : 3725  secondes
Succès : 19203
Échecs : 1693
Soit : 92% 

## Prêt Complet : 
Temps : 3725  secondes
Succès : 99311
Échecs : 12002
Soit : 89% 

## SERBER 100000:
Temps : 1614 secondes
Succès : 1705
Échecs : 2681

## SERBER 500000:
Temps : 145 secondes
Succès : 380
Échecs : 78
Soit : 83%

## SERBER Complet:
Temps : 62000 secondes
Succès : 16000
Échecs : 14000

## SEMALY TIF:
Temps : 35513 secondes
Soit : 100%

## MR TRAM
Temps : 3 secondes
Succès : 
Échecs : 819
Soit : %


# Troisième itération en filtrant station par station:

## Ligne C :
Temps : 940 secondes
Succès : 8757
Échecs : 179
Soit : 98% 

## Ligne C Commun:
Temps : 3128 secondes
Succès : 20232
Échecs : 179
Soit : % 

## Ligne C Interstations: :
Temps : 940 secondes
Succès : 8757
Échecs : 179
Soit : % 

## Ligne A : 
Temps : 1939 secondes
Succès : 73284
Échecs : 3681
Soit : 95% 

## Ligne B : 
Temps : 1794 secondes
Succès : 37175
Échecs : 4649
Soit : % 

## SERBER Complet: 
Temps : 43200 secondes
Succès : 19802
Échecs : 10425
Soit : 65% 