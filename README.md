environment creation
```bash
conda create -n wineq python=3.7 -y
conda activate wineq
pip install -r requirements.txt
```
download data

initializing git and dvc
```bash
git init
dvc init
dvc add data_given/winequality.csv
```
```bash
git remote add origin url
```
```bash
git add . && git commit -m "first_commit"
```

tox command -
```bash
tox
```
for rebuilding -
```bash
tox -r 
```
pytest command
```bash
pytest -v
```

setup commands -
```bash
pip install -e . 
```

build your own package commands- 
```bash
python setup.py sdist bdist_wheel
```
