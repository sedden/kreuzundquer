### Start der Testumgebung

#### Vorbedingungen:

 * Git wird als VCS eingesetzt
 * Python 2.6 oder 2.7, sowie Python virtualenv müssen installiert sein

Zum Installieren der Abhängigkeiten unter Ubuntu genügt:

    sudo apt-get install git python2.7-dev python-virtualenv

#### Initiales Setup:

Clone des Quellcode-Repositories:

    git clone git@bitbucket.org:kuq/kreuzundquer.git
    cd kreuzundquer/

Wechsel auf den Entwicklungszweig `django1.4`:

    git checkout --track -b django1.4 origin/django1.4

Erstellen von `venv/` mit allen benoetigten Python Bibliotheken:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Synchronisieren/Erstellen der Datenbank:

    python manage.py syncdb


#### Setzen der Umgebungsvariablen fuer S3:

    export AWS_ACCESS_KEY_ID=...
    export AWS_SECRET_ACCESS_KEY=...
    export S3_BUCKET_NAME=django-kreuzundquer

#### Start des Webservers:

Static Files zusammentragen (nach `kreuzundquer/sitestatic/` kopieren):

    python manage.py collectstatic

Server starten, Variante 1:

    python manage.py runserver

Server starten, Variante 2:

    foreman start

#### Aufruf der Webseite: 

Nach Variante 1: <http://localhost:8000/>

Nach Variante 2: <http://localhost:5000/>

#### Deployment auf Heroku und wichtige Befehle:

Aktuellen Branch deployen:

    git push heroku django1.4:master

Einen Blick auf die Logs werfen:

    heroku logs

Aktuelle Konfiguration anzeigen:

    heroku config

Konfiguration fuer S3 setzen:

    heroku config:set AWS_ACCESS_KEY_ID=...

    heroku config:set AWS_SECRET_ACCESS_KEY=...

    heroku config:set S3_BUCKET_NAME=django-kreuzundquer

Datenbank-Update durchfuehren:

    heroku run python manage.py syncdb

Auf Datenbank verbinden:

    heroku pg:psql --app kuq HEROKU_POSTGRESQL_COBALT

Datenbank Backup wiederherstellen:

    heroku pgbackups:restore DATABASE 'http://django-kreuzundquer.s3-eu-west-1.amazonaws.com/kreuzundquer3.dump'

Wichtige DB-Queries:

    SELECT SUM(n_live_tup) FROM pg_stat_user_tables;

    SELECT schemaname,relname,n_live_tup
    FROM pg_stat_user_tables
    ORDER BY n_live_tup DESC;


