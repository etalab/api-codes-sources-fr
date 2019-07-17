wget https://github.com/etalab/data-codes-sources-fr/archive/master.zip
unzip master.zip "*.json"

mkdir stats
mv data-codes-sources-fr-master/data/stats.json stats/general.json

python stats.py
