import csv
import json
import glob
import os
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import shutil

GITHUB_SRC = 'etalab/inventaire-codes-sources-organismes-publics'

REPOS_DATA_FOLDER = 'data/repos/'
ORGS_DATA_FOLDER = 'data/organisations/'
REPOS_TARGET_FOLDER = 'api/repos/'
ORGS_TARGET_FOLDER = 'api/organisations/'


def convert_csv(base_folder, target_folder):
    for csv_filepath in glob.glob(base_folder + '/*.csv'):
        filename = os.path.splitext(os.path.basename(csv_filepath))[0]
        json_filepath = target_folder + filename + '.json'

        with open(csv_filepath) as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        with open(json_filepath, 'w') as f:
            json.dump(rows, f, ensure_ascii=False)


folders = [
    REPOS_DATA_FOLDER, ORGS_DATA_FOLDER,
    REPOS_TARGET_FOLDER, ORGS_TARGET_FOLDER,
]
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Save CSV files
resp = urlopen("https://github.com/" + GITHUB_SRC + "/archive/master.zip")
archive = ZipFile(BytesIO(resp.read()))
for file in [f for f in archive.namelist() if '/repositories/' in f]:
    filename = os.path.basename(file)
    if not filename:
        continue

    source = archive.open(file)
    target = open(os.path.join(REPOS_DATA_FOLDER, filename), "wb")
    with source, target:
        shutil.copyfileobj(source, target)

os.rename(REPOS_DATA_FOLDER + '/all_repositories.csv', REPOS_DATA_FOLDER + '/all.csv')

orgs_url = 'https://raw.githubusercontent.com/' + GITHUB_SRC + '/master/organisations/comptes-organismes-publics.csv'
with urlopen(orgs_url) as orgs_file, open(ORGS_DATA_FOLDER + 'all.csv', 'w') as f:
    f.write(orgs_file.read().decode())

# Convert CSV files to JSON
convert_csv(REPOS_DATA_FOLDER, REPOS_TARGET_FOLDER)
convert_csv(ORGS_DATA_FOLDER, ORGS_TARGET_FOLDER)
