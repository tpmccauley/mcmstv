mcmstv
======

An app that collects and displays information regarding the operation of the LHC
and the CMS experiment.

https://mcmstv.web.cern.ch/

## Developing and running locally
Check out this repository:
```
git clone git@github.com:tpmccauley/mcmstv.git
```

Create a virtual environment, install, and run a development server:
```
cd mcmstv
virtualenv cmstv
source cmstv/bin/activate
pip install -r requirements.txt
flask run
```
