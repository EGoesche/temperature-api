<!--lint disable no-literal-urls-->
# Temperature-API
Bei diesem Projekt handelt es sich um eine einfache REST-API, welche die CRUD-Operationen verwendet. Die API verwendet Flask als Framework und SQLite als Datenbank. Die API wurde auf Heroku deployed.

Übersicht
---------------------
 * Installation
 * Funktionen
 * Unter Verwendung von
 * Autoren
 * Lizenz
 
 Installation
------------
Die folgenden Anweisungen helfen Ihnen, eine Kopie dieses Projektes auf Ihrem System zu erstellen, zu bearbeiten und auszuführen.
Bevor das Projekt kopiert und genutzt werden kann, benötigen Sie folgende Softwarepakete:

```
Flask 1.1.2 (oder neuer)
Flask-SQLAlchemy 2.x (oder neuer)
```
Um die Datenbank zu erstellen, müssen die Befehle ```from models import Temperature```,  ```from app import db, create_app```
und ```db.create_all(app=create_app())``` nacheinander in einer Python-Shell ausgeführt werden.
Um den Code einsehen zu können, importieren Sie die Quellcode-Dateien in eine IDE bzw. einem Editor Ihrer Wahl.

 Funktionen
------------
* Temperaturen in einer Datenbank:
 >* Hinzufügen
 >* Anzeigen
 >* Ändern
 >* Löschen

Unter Verwendung von
------------
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Webframework
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - Modul für die Unterstützung von SQLAlchemy

 Autoren
------------
* **Erik** - *Developer* - [EGoesche](https://github.com/EGoesche)

Um zu erfahren, wer zusätzlich an diesem Projekt gearbeitet hat, lesen Sie bitte die contributors-Datei.

Lizenz
------------
Dieses Projekt ist lizensiert unter der MIT-Lizenz - weitere Informationen unter [LICENSE](LICENSE).

