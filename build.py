import csv
import json
import glob
import os
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import shutil

DATA_FOLDER = 'data'
TARGET_FOLDER = 'api/repos/'

# Save CSV files
os.mkdir(DATA_FOLDER)

resp = urlopen("https://github.com/etalab/inventaire-codes-sources-organismes-publics/archive/master.zip")
archive = ZipFile(BytesIO(resp.read()))
for file in [f for f in archive.namelist() if '/repositories/' in f]:
    filename = os.path.basename(file)
    if not filename:
        continue

    source = archive.open(file)
    target = open(os.path.join(DATA_FOLDER, filename), "wb")
    with source, target:
        shutil.copyfileobj(source, target)

# Convert CSV files to JSON
for csv_filepath in glob.glob(DATA_FOLDER + '/*.csv'):
    filename = os.path.splitext(os.path.basename(csv_filepath))[0]
    json_filepath = TARGET_FOLDER + filename + '.json'

    with open(csv_filepath) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open(json_filepath, 'w') as f:
        json.dump(rows, f, ensure_ascii=False)
