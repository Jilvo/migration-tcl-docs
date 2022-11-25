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
<summary>BUG Connus</summary>

</details>

<details>
<summary>STATS</summary>

</details>

## Contexte :

### Cadre de la mission

Dans le cadre d'une migration de GED technique, le client souhaite changer la GED actuelle.

- Extraction de la BDD existante (120 000 références) pour environ (500 000 fichiers).
- Création de fichiers CSV afin de lier des fichiers avec des métadonnées.
- Préprocessing des données

## Solutions choisies :

### Extraction

- Extraction des références réalisées par RS2I sous format CSV

### Transformation

- Utilisation de Python afin de faire le processus d'extraction.
- Utilisation de Pandas pour la transformation et création de fichier CSV finaux.

## TCLDOCS :

### Problème

Trouver les références dans le chemin

### Solution proposé

- On crée différents Dataframes pour chaque station sélectionnée
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

- Créer un dataframe avec toutes les références prêtées (colonne Définitif (P pour prêtés ou D pour définitif))
- Script REGEX voir TCLDOCS
- Output:
  - chemin d'un fichier
  - Référence TCL

## SERBER :

### Problème

Associer les fichiers SERBER avec des références dans l’extraction TCLDOC

### Solution proposé

- Créer un Dataframe filtrant les références contenant l'armoire SERBER.
- Créer un deuxième Dataframe filtrant toutes les références qui sont en AA et qui ne sont pas SERBER.
- On compare ensuite l'arborescence avec le premier Dataframe et on retraite ensuite les échecs avec le deuxième Dataframe.
- Output:
  - chemin d'un fichier
  - Référence TCL

## SEMALY :

### Problème

Construire un fichier fusionnant l'arborescence SEMALY ainsi qu'un fichier de métadonnées préexistant

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

Construire un fichier fusionnant l'arborescence SEMALY ainsi qu'un fichier de métadonnées préexistant

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

### Exécution du script TCLDOCS

Lancer le script, ajouter les stations ou ligne voulu et laisser le script tourner

```
python main.py
```

### Exécution du script Prêt

Il faut modifier le chemin (si besoin) du fichier en modifiant la variable DIRNAME dans le fichier menu_arborescence.py

```
python main.py
```

### Exécution du script SERBER

Il faut modifier le chemin (si besoin) du fichier en modifiant la variable DIRNAME dans le fichier arborescence_serber.py

```
python main.py
```

### Exécution du script SEMALY

Il faut modifier le chemin (si besoin) du fichier en modifiant la variable DIRNAME

```
python arborescence_semaly.py
```

### Exécution du script MR TRAM

Il faut modifier le chemin (si besoin) du fichier en modifiant la variable DIRNAME_MRTRAM

```
python arborescence_mr_tram.py
```
## Installation et configuration :

### Environnement

Avoir les droits d'administrateur le PC n'est pas nécessaire mais permet de simplifier la mise en place.

En premier lieu il faut installer le langage de programmation
[Python ici version 3.10](https://www.python.org/downloads/)

Ensuite un logiciel de programmation, par exemple [Visual Studio Code](https://code.visualstudio.com/download)

### Paquets nécessaires

Afin d'installer les paquets nécessaires, il faut lancer la commande suivante dans un terminal:

```
pip install -r requirements.txt
```

Il faut ensuite créer le dossier *output_datas*

### Mise en place des inputs et outputs:
Dans le dossier inputs_datas:
  - 20221010_ExtratTCLDoc complete modifié sans AR.csv
  - 20221010_ExtratTCLDoc complete modifié.csv
  - Extraction Serber juste AA et non serber.csv
  - LISTES URL SEMALY.csv
  - listes_arrets_lignes.csv
  - metadonnes_TRAM.csv
  - parse_filter.txt

Fichiers d'Extraction:
- Dans un premier temps, vérifier les colonnes du fichier (il faut au minimum les colonnes : __REFFIC__,__DEFINITIF__,__LIBSITE__,__ARMOIRE__,__SUPPORT_DOC__,__NUMERO_REF_FOURN__)
- Ensuite il faut créer un fichier sans les références commencant par AR
- Afin de faire la seconde passe sur les fichiers SERBER en gardant juste les AA qui ne sont pas SERBER.

Le nom des fichiers des inputs peut être modifié dans le fichier *fichier_et_constantes.py*

Avant de lancer un script, il faut créer le dossier *output_datas*
Certains outputs se trouvent dans *fichier_et_constantes.py*.
Pour modifier plus en profondeurs les outputs, ils se trouvent dans *main.py*.

## Copie des fichiers sur un autre serveur

### Problème
Afin de ne pas perdre les fichiers non rapprochés on souhaite les copier sur un serveur/un dossier.
### Solution proposé

On modifie (si besoin) le chemin du fichier dans le script *fichier_et_constantes.py* dans la constante : 

__FICHIER_ECHECS_A_COPIER_SUR_AUTRE_SERVEUR__ ainsi que le dossier de sortie des fichiers __DESTINATION_FICHIERS_COPIE__ .

Puis on lance le script *copy_file_another_server.py*, les fichiers seront copiés dans le dossier choisi précédent ou par défaut "output_datas/tcl_copy_files".
## BUG Connus
- Différence d'encodage entre un fichier csv python et celui d'un utilisateur, il faut donc modifier l'encodage
  
  encoding="utf-8-sig"  = fichier crée par python

  encoding="cp1252"  = fichier modifié par l'humain
- Bien vérifier que les fichiers csv portant les noms des fichiers de sortie ne sont pas ouverts lors du lancement du script
- Ne pas mettre un nom de fichier CSV trop long 

## Lancer les scripts avec Powershell :
1.	Taper powershell dans la barre de recherche
2.	La fenêtre s’ouvre
3.	Se déplacer dans le bon répertoire par exemple si le code se trouve dans Documents/migration-tcl-docs 1 comme sur le pc de G.PEREZ il faut faire « cd Documents/migration-tcl-docs 1 »
Tuto ici : https://www.journaldunet.fr/web-tech/developpement/1441153-comment-changer-le-repertoire-directory-de-powershell/
4.	Une fois que vous êtes au bon endroit faites « ls » afin de vérifier, vous pouvez aussi le faire avant pour voir ou vous êtes
5.	Si vous êtes au bon endroit, lancez le script python de votre choix comme marqué plus haut dans le doc (exemple : « python main.py »

## STATS

VOIR STATS.XLSX

