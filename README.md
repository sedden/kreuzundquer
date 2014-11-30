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

#### Start des Webservers:

    python manage.py runserver

#### Aufruf der Webseite: 

<http://localhost:8000/>
