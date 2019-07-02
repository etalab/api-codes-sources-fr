wget https://github.com/etalab/data-codes-sources-fr/archive/master.zip
unzip master.zip "*.json"
mkdir stats

python stats.py
