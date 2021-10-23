import json

IN_FOLDER = "data-codes-sources-fr-master/data/"
OUT_FOLDER = "stats/"

with open(IN_FOLDER + "repositories/json/all.json") as f:
    repertoires = json.load(f)


def last_repositories(repertoires):
    last_repo = sorted(repertoires, key=lambda k: k["creation_date"], reverse=True)[:10]

    with open(OUT_FOLDER + "last_repositories.json", "w") as f:
        json.dump(last_repo, f)


last_repositories(repertoires)
