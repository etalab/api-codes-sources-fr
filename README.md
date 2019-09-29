[![CircleCI build status](https://img.shields.io/circleci/project/github/AntoineAugusti/api-codes-sources-fr.svg?style=flat-square)](https://circleci.com/gh/AntoineAugusti/api-codes-sources-fr)
[![Software License](https://img.shields.io/badge/License-MIT-orange.svg?style=flat-square)](https://github.com/AntoineAugusti/api-codes-sources-fr/blob/master/LICENSE.md)

# API Codes Sources France
Une API pour lister les dépôts de code publiés par les comptes d’organisation d’organismes publics en France.

Les données proviennent du [répertoire etalab/data-codes-sources-fr](https://github.com/etalab/data-codes-sources-fr).

## Déploiement et hébergement
Le déploiement est assuré par Netlify, le fichier de build se trouve dans `build.sh`. Le build est lancé régulièrement [grâce à CircleCI](https://circleci.com/gh/AntoineAugusti/api-codes-sources-fr).

## Endpoints
Les endpoints retournent des données au format JSON. L'URL de base est https://api-codes-sources-fr.antoine-augusti.fr.

- Tous les répertoires : [`/api/repertoires/all`](https://api-codes-sources-fr.antoine-augusti.fr/api/repertoires/all)
- Toutes les organisations : [`/api/organisations/all`](https://api-codes-sources-fr.antoine-augusti.fr/api/organisations/all)
- Tous les répertoires d'un organisme : `/api/repertoires/:slug`

Exemple :
- https://api-codes-sources-fr.antoine-augusti.fr/api/repertoires/dgfip
```json
[
   {
      "nom":"Test-Compta-Demat",
      "organisation_nom":"DGFiP",
      "organisation_url":"https://github.com/DGFiP",
      "repertoire_url":"https://github.com/DGFiP/Test-Compta-Demat",
      "description":"Ce logiciel permet de contrôler le respect des normes des fichiers d'écritures comptables (FEC) conformément aux dispositions de l'article A.47 A-1 du livre des procédures fiscales.",
      "est_fork":false,
      "date_creation":"2014-08-19T10:30:26Z",
      "derniere_mise_a_jour":"2018-12-23T08:50:58Z",
      "homepage":"http://www.economie.gouv.fr/dgfip/controle-fiscal-et-lutte-contre-fraude",
      "nombre_stars":17,
      "nombre_forks":8,
      "licence":null,
      "nombre_issues_ouvertes":17,
      "langage":"Perl",
      "topics":""
   }
]
```

- Les informations sur une organisation `/api/organisations/:slug`

Exemple :
- https://api-codes-sources-fr.antoine-augusti.fr/api/organisations/dgfip
```json
{
   "nom":"Direction générale des finances publiques",
   "organisation":null,
   "organisation_url":"https://github.com/DGFiP",
   "blog":"http://www.economie.gouv.fr/dgfip",
   "adresse":"France",
   "email":"",
   "est_verifiee":false,
   "nombre_repertoires":1,
   "date_creation":"2014-09-15T13:24:47Z"
}
```

### Statistiques
- [`/api/stats/general`](https://api-codes-sources-fr.antoine-augusti.fr/api/stats/general) : des statistiques à propos du nombre de dépôts, des organisations les plus actives, les principales licences etc.
- [`/api/stats/last_repositories`](https://api-codes-sources-fr.antoine-augusti.fr/api/stats/last_repositories) : les 10 derniers répertoires créés

## Licence
MIT
