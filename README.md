conda create -n wineq python=3.7 -y
conda activate wineq
pip install -r requirements.txt

download data

git init
dvc init
dvc add data_given/winequality.csv
