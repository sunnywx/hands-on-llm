conda env setup
==

```
# create a python-3.11 global env
conda create -n py311 python=3.11

# activate py-3.11
conda activate py311

# create a local virtual env
python -m venv venv

# activate local python/pip
source venv/bin/activate

# install deps
pip install -r requirements.txt

```