[![CircleCI build status](https://img.shields.io/circleci/project/github/etalab/api-codes-sources-fr.svg?style=flat-square)](https://circleci.com/gh/etalab/api-codes-sources-fr)
[![Software License](https://img.shields.io/badge/License-MIT-orange.svg?style=flat-square)](https://github.com/etalab/api-codes-sources-fr/blob/master/LICENSE.md)

**Archivé** : ce dépôt est archivé et l'API n'est plus en place.

Pour consulter les dépôts développés par le pôle logiciels libres d'Etalab, rendez-vous sur [SourceHut](https://git.sr.ht/~etalab/readme-logiciels-libres).

# API Codes Sources France

Une API pour lister les dépôts de code publiés par les comptes d’organisation d’organismes publics en France.

Les données proviennent du [répertoire etalab/data-codes-sources-fr](https://github.com/etalab/data-codes-sources-fr).

## Déploiement et hébergement

Le déploiement est assuré par Netlify, le fichier de build se trouve dans `build.sh`. Le build est lancé régulièrement [grâce à CircleCI](https://circleci.com/gh/etalab/api-codes-sources-fr).

## Endpoints

Les endpoints retournent des données au format JSON. L'URL de base est `https://api-code.etalab.gouv.fr`.

- Tous les répertoires : [`/api/repositories/all`](https://api-code.etalab.gouv.fr/api/repositories/all)
- Toutes les organisations : [`/api/organizations/all`](https://api-code.etalab.gouv.fr/api/organizations/all)
- Tous les répertoires d'un organisme : `/api/repositories/:slug`

Exemple :
- https://api-code.etalab.gouv.fr/api/repositories/dgfip
```json
[
   {
      "name":"Test-Compta-Demat",
      "organization_name":"DGFiP",
      "organization_url":"https://github.com/DGFiP",
      "repository_url":"https://github.com/DGFiP/Test-Compta-Demat",
      "description":"Ce logiciel permet de contrôler le respect des normes des fichiers d'écritures comptables (FEC) conformément aux dispositions de l'article A.47 A-1 du livre des procédures fiscales.",
      "is_fork":false,
      "creation_date":"2014-08-19T10:30:26Z",
      "last_update":"2018-12-23T08:50:58Z",
      "homepage":"http://www.economie.gouv.fr/dgfip/controle-fiscal-et-lutte-contre-fraude",
      "stars_count":17,
      "forks_count":8,
      "license":null,
      "open_issues_count":17,
      "language":"Perl",
      "topics":""
   }
]
```

- Les informations sur une organisation `/api/organizations/:slug`

Exemple :

- https://api-code.etalab.gouv.fr/api/organizations/dgfip

```json
{
   "name":"Direction générale des finances publiques",
   "organization":null,
   "organization_url":"https://github.com/DGFiP",
   "website":"http://www.economie.gouv.fr/dgfip",
   "location":"France",
   "email":"",
   "is_verified":false,
   "repository_count":1,
   "creation_date":"2014-09-15T13:24:47Z"
}
```

### Statistiques

- [`/api/stats/general`](https://api-code.etalab.gouv.fr/api/stats/general) : des statistiques à propos du nombre de dépôts, des organisations les plus actives, les principales licences etc.
- [`/api/stats/last_repositories`](https://api-code.etalab.gouv.fr/api/stats/last_repositories) : les 10 derniers répertoires créés

## Licence

MIT
