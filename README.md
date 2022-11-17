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

<details>
<summary>Copie des fichiers sur un autre serveur</summary>

- Problème
- Solution proposé

</details>

<details>
<summary>STATS</summary>

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

## Lancement du programme :

### Execution du script TCLDOCS

Lancer le script, ajouter les stations ou ligne voulu et laisser le script tourner

```
python main.py
```

### Execution du script Prêt

Il faut modifier le chemin (si besoin) du fichier en modifiant la variable DIRNAME dans le fichier menu_arborescence.py

Dans le menu choisir le numéro 9

```
python main.py
```

### Execution du script SERBER

Il faut modifier le chemin (si besoin) du fichier en modifiant la variable DIRNAME dans le fichier arborescence_serber.py

Dans le menu choisir le numéro 8

```
python main.py
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
## Installation et configuration :

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

Le nom des fichiers des inputs peut être modifié dans le fichier *fichier_et_constantes.py*

Certains outputs se trouvent dans *fichier_et_constantes.py*.
Pour modifier plus en profondeurs les outputs, ils se trouvent dans *main.py*.

## Copie des fichiers sur un autre serveur

### Problème
Afin de ne pas perdre les fichiers non rapprochés on souhaite les copiers sur un serveur/un dossier.
### Solution proposé

On modifie (si besoin ) le chemin du fichier dans le script *fichier_et_constantes.py* dans la constante : 

__FICHIER_ECHECS_A_COPIER_SUR_AUTRE_SERVEUR__ ainsi que le dossier de sortie des fichiers __DESTINATION_FICHIERS_COPIE__ .

Puis on lance le script *copy_file_another_server.py*, les fichiers seront copiés dans le dossier choisit précédent ou par défaut "output_datas/tcl_copy_files".

## STATS

VOIR STATS.XLSX