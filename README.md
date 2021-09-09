# ChatBot-System
ChatBot Managment System

## Installation
Clone this Project:

```bash
git clone https://github.com/Elraawy/ChatBot-System.git
```
Go to Project Directory:
```bash
cd ChatBot-System
```
#### Prepare the environment:
Windows: 
```bash
 python -m venv venv
 . \venv\Scripts\activate
 pip install -r requirements.txt
```

Linux: 
```bash
 python3 -m venv venv
 source venv/bin/activate
 pip install -r requirements.txt
```

### Download NLTK dependencies
If you get an error during the first run, you also need to install `nltk.tokenize.punkt`:
Run this once in your terminal:
 ```console
$ python
>>> import nltk
>>> nltk.download('punkt')
```

## Usage
Windows:
```bash
  py manage.py makemigrations
  py manage.py migrate
  py manage.py runserver 
```
Linux:
```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py runserver
```
