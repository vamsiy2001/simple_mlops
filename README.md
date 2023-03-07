conda create -n wineq python=3.7 -y
conda activate wineq
pip install -r requirements.txt

download data

git init
dvc init
dvc add data_given/winequality.csv

git remote add origin url

git add . && git commit -m "first_commit"
