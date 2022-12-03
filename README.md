## PDM - Python package manager & dependencies manager, NPM style
### PDM init project by creating pyproject.toms
``pdm init``

### add packages to ``__pypackages__`` folder PEP582
``pdm add pypasser``

### export to requirements.txt for compatibility with pip
``pdm export -o requirements.txt``

### reinstall deps from pdm.lock file
``pdm install``

### build artifacts to publish on PyPI
``pdm build``

### add PEP582 support to python (allow to run python script with PEP582)
`` eval "$(pdm --pep582)"``

[https://pdm.fming.dev/](https://pdm.fming.dev/)

## zipapp - compress project to python zip executable 
* create a folder `build` and copy/paste the project packages and requirements.txt
* in that folder run: `python -m pip install -r requirements.txt --target ./`
* in parent folder create archive: `python -m zipapp build -m 'main:test'`

in the above case, entry point is module `main.py` function `test()`

[https://docs.python.org/3/library/zipapp.html](https://docs.python.org/3/library/zipapp.html)