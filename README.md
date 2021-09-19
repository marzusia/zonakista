<div align="center">
<div><img height="86" src="zonakista/static/vedia-rounded.png"/></div>
<p></p>

**zonakista** kora kra udarsam huzas as
</div>

## Mamseta
Karsi tona Pythonas kaisur aipa. Gunicorn kra harzeta nuda.
```
python -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/python manage.py migrate
venv/bin/python manage.py createsuperuser
```

Krasta `.env` kaiseta eli, n-akas `.env.example` dorsaina as.
Hisár si hamurta, karni luka:
```
# mamseta
venv/bin/python manage.py runserver

# krabu
venv/bin/gunicorn zonakista:application
```