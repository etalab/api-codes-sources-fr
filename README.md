# API Codes Sources France
Une API pour lister les dépôts de code publiés par les comptes d’organisation d’organismes publics en France.

Les données proviennent du [répertoire etalab/inventaire-codes-sources-organismes-publics](https://github.com/etalab/inventaire-codes-sources-organismes-publics/).

## Déploiement et hébergement
Le déploiement est assuré par Netlify, le fichier de build se trouve dans `build.py`. Le build est lancé automatiquement toutes les 3 heures grâce à CircleCI.

## Endpoints
- `https://api-codes-sources-fr.antoine-augusti.fr/api/repos/:slug`

Exemple :
- https://api-codes-sources-fr.antoine-augusti.fr/api/repos/dgfip
```json
[
   {
      "Nom":"Test-Compta-Demat",
      "Organisation":"https://github.com/DGFiP",
      "URL":"https://github.com/DGFiP/Test-Compta-Demat",
      "Description":"Ce logiciel permet de contrôler le respect des normes des fichiers d'écritures comptables (FEC) conformément aux dispositions de l'article A.47 A-1 du livre des procédures fiscales.",
      "Fork?":"false",
      "Créé":"2014-08-19T10:30:26Z",
      "Mis à jour":"2018-09-25T07:44:11Z",
      "Homepage":"http://www.economie.gouv.fr/dgfip/controle-fiscal-et-lutte-contre-fraude",
      "Stars":"17",
      "# forks":"7",
      "Licence":"",
      "Issues":"17",
      "Langages":"Perl"
   }
]
```

## Licence
MIT
