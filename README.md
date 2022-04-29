# httpCat
A http.cat viewer with GUI made in python using MDkivy

# Setup
 -  Make sure you have python (< 3.10) with venv instlaled ```python -m pip install --upgrade pip setuptools virtualenv ```
 - Clone the repo ```git clone https://github.com/f1ammable/httpCat.git ```
 - Move into project directory ```cd httpCat```
 - Create venv ```python -m virtualenv kivy_venv``` (or name it whatever you want, I'm just using the kivy docs)
 - Activate venv, run the script in ``` venv/scripts/activate ```
 - Install the packages ```pip install -r reqs.txt```

# If you have problems
 - Delete venv and make a new one
 - Activate new venv
 - Run ```python -m pip install -U pip```
 - Run ```python -m pip install -U --force-reinstall -r reqs.txt```
 - Hopfully this solves the issue with not being able to import sdl2
 - Set ```include-system-site-packages = true``` if you encounter further problems 

### Thank you very much to Axel for helping me with OOP stuff
