# Migration GED technique Keolis
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/VichithLy/pokedex-vue-tailwindcss/blob/master/LICENSE)
## Sommaire :

<details>
<summary>Contexte</summary>

- Cadre de la mission

</details>

<details>
<summary>Solutions choisi pour ETL</summary>

- Extraction
- Transformation

</details>

<details>
<summary>TCLDOCS</summary>

- Problème
- Solution proposé

</details>

<details>
<summary>Prêt</summary>

- Problème
- Solution proposé

</details>

<details>
<summary>SERBER</summary>

- Problème
- Solution proposé

</details>

<details>
<summary>SEMALY</summary>

- Problème
- Solution proposé
</details>

<details>
<summary>MR TRAM</summary>

- Problème
- Solution proposé

</details>

<details>
<summary>Installation et configuration</summary>

- Environnement
- Paquets nécessaires
- Mise en place des inputs et outputs

</details>

<details>
<summary>Lancement du programme</summary>

- Execution du script TCLDOCS
- Execution du script Prêt
- Execution du script SERBER
- Execution du script SEMALY
- Execution du script MR TRAM

</details>

## Contexte :

### Cadre de la mission

Dans le cadre d'une migration de GED technique, le client souhaite changer la GED actuelle.

- Extraction de la BDD existante (120 000 références) pour environ (500 000 fichiers).
- Création de fichiers CSV afin de lier des fichiers avec des métadonnées.
- Préprocessing de la données

## Solutions choisies :

### Extraction

- Extraction des références réalises par RS2I sous format CSV

### Transformation

- Utilisation de Python afin de faire le processus d'extraction.
- Utilisation de Pandas pour la transformation et création de fichier CSV finaux.

## TCLDOCS :

### Problème

Trouver la références dans le chemin

### Solution proposé

- On crée différents dataframes pour chaque station sélectionnée
- Création d'un script cherchant qui découpe chaque étage du chemin dans une liste, filtre ensuite avec un algo de tri via des REGEX afin de ne garder que les éléments potentiellement intéressants.
- Dans un premier temps on compare chaque station avec la station correspondante (on peut trouver la station dans le chemin du fichier)
- Pour les échecs restants on compare les fichiers échoués avec les références de la ligne entière.
- Output:
  - chemin d'un fichier
  - Référence TCL

## Prêt :

### Problème

Associer les références prêtées avec les fichiers dans le dossier Prêt

### Solution proposé

- Créer un dataframe avec toutes les références prêtées (colonne Défenitif (P pour prêtés ou D pour définitif))
- Script REGEX voir TCLDOCS
- Output:
  - chemin d'un fichier
  - Référence TCL

## SERBER :

### Problème

Associer les fichiers SERBER avec des références dans l'extractions TCLDOC

### Solution proposé

- Créer un dataframe filtrant les références contenant l'armoire SERBER.
- Créer un deuxième dataframe filtrant toutes les références qui sont en AA et qui ne sont pas SERBER.
- On compare ensuite l'arborescence avec le premier dataframe et on retraite ensuite les échecs avec le deuxième dataframe.
- Output:
  - chemin d'un fichier
  - Référence TCL

## SEMALY :

### Problème

Construire un fichier fusionnant l'arborescence SEMALY ainsi qu'un fichier de métadonnées pré-exsistant

### Solution proposé

- Créer l'arborescence SEMALY du dossier PDF puis TIFF
- Si le chemin se trouve dans le fichier des métadonnées alors on ajoute ces métadonnées à notre fichier final, sinon on le rajoute dans les échecs.
- Output
  - NIVEAU 1
  - NIVEAU 2
  - NIVEAU 3
  - NUM_PLAN
  - INDICE
  - LIBELLE
  - Chemin
  - Code Ouvrage

## MR TRAM :

### Problème

Construire un fichier fusionnant l'arborescence SEMALY ainsi qu'un fichier de métadonnées pré-exsistant

### Solution proposé

- Output
  - Chemin
  - Reference
  - Plan
  - Indice
  - Titre
  - Format
  - Date

## Installation :

### Environnement

Avoir les droits d'administrateur le PC n'est pas nécéssaire mais permet de simplifier la mise en place.

En premier lieu il faut installer le language de programmation
[Python ici version 3.10](https://www.python.org/downloads/)

Ensuite un logiciel de programmation, par exemple [Visual Studio Code](https://code.visualstudio.com/download)

### Paquets nécessaires

Afin d'installer les paquets nécessaires, il faut lancer la commande suivante dans un terminal:

```
pip install -r requirements.txt
```

### Mise en place des inputs et outputs:
dans le dossier inputs_datas:
  - parse_filter.txt
  - listes_arrets_lignes.csv
  - 20221010_ExtratTCLDoc complete modifié.csv
  - Extraction Serber juste AA et non serber.csv

## Lancement du programme :

### Execution du script TCLDOCS

Lancer le script, ajouter les stations ou ligne voulu et laisser le script tourner

```
python menu_arborescence.py
```

### Execution du script Prêt

Il faut modifier le chemin (si besoin) du fichier en modifiant la variable DIRNAME dans le fichier menu_arborescence.py

Dans le menu choisir le numéro 9

```
python menu_arborescence.py
```

### Execution du script SERBER

Il faut modifier le chemin (si besoin) du fichier en modifiant la variable DIRNAME dans le fichier arborescence_serber.py

Dans le menu choisir le numéro 8

```
python menu_arborescence.py
```

### Execution du script SEMALY

Il faut modifier le chemin (si besoin) du fichier en modifiant la variable DIRNAME

```
python arborescence_semaly.py
```

### Execution du script MR TRAM

Il faut modifier le chemin (si besoin) du fichier en modifiant la variable DIRNAME_MRTRAM

```
python arborescence_mr_tram.py
```

# Première Itération :

## Métro Croix Paquet:

### Comparaison basique:

Temps : 3 secondes
Succès : 729
Échecs : 32
Soit 95.7%

## Métro Bellecour:

### Création abro + analyse:

Temps 160 secondes
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

Temps : 3716 secondes
Succès : 6870
Échecs : 539
Soit : 90%

## Prêt 2017 :

Temps : 3725 secondes
Succès : 19203
Échecs : 1693
Soit : 92%

## Prêt Complet :

Temps : 3725 secondes
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
Échecs : 280
Soit : %

## Ligne C Interstations: :

Temps : 940 secondes
Succès : 39
Échecs : 5
Soit : %

## Ligne A :

Temps : 8289 secondes
Succès : 73284
Échecs : 3681
Soit : 95%

## Ligne B :

Temps : 1794 secondes
Succès : 37175
Échecs : 4649
Soit : 89%

## SERBER Complet :

Temps : 43200 secondes
Succès : 19802
Échecs : 10425
Soit : 65%

## Rhone Express Communs :

Temps : 21 secondes
Succès : 388
Échecs : 378
Soit : 50%

## TRAM Communs :

Temps : 577 secondes
Succès : 7638
Échecs : 2398
Soit : 76%

## Funiculaires Communs

Temps : 577 secondes
Succès : 961
Échecs : 140
Soit : 87%

## Métro ABC Communs

Temps : 577 secondes
Succès : 3070
Échecs : 339
Soit : 90%

## Métro Communs

Temps : 577 secondes
Succès : 3070
Échecs : 339
Soit : 90%

# A faire:

## REFAIRE Readme

## voir surface multi site ?
