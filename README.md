# PyDocToLaTeX
Ziel des Projekts ist ein Programm, welches Python Docstrings oder sogar ganze Python-Quellcodedateien in eine LaTeX Darstellung als Dokumentation konvertiert.
Die Aufteilung beläuft sich dabei vorerst im wesentlichen auf die beiden Skripte 'extractor.py' und 'docBuilder.py'.
Diese beinhalten die folgenden Funktionalitäten (teilweise noch in Arbeit):

## Module
`extractor.py`
=> Bietet Funktionen zum Auslesen von Quellcode-Dateien und deren Separation in Variablen, Funktionen und Klassen
* Einlesen von Dateien
* Extrahieren von  Variablennamen und deren Docstring-Beschreibung (sofern vorhanden) aus einem gegebenen String
- Extrahieren von Funktionen und deren Docstring-Beschreibung (inklusive Parameterliste) aus einem gegebenen String
- Extrahieren von Klassen und deren Docstring-Beschreibung (inklusive Attributen und Methoden) aus einem gegebenen String
  
`docBuilder.py`
=> Bietet Funktionen zum Nachbilden der Struktur einer Python-Quellcodedatei und den Export dieser Struktur in eine LaTeX Dokumentation
* Nachbildung der Quellcodestruktur durch die Klassen 'Class', 'Function', 'Field' und 'Parameter'
* Bestandteile haben jeweils einen Namen und eine Beschreibung, sowie ggf. Listen der anderen Klassen als Unterbestandteile

`pyToTeX.py`
=> koordiniert das Ausführen der Konversion einer .py Datei in eine LaTeX Dokumentation und stellt ein CLI bereit
* Funktion `convert(...)` leitet die Konversion für den übergebenen Pfad ein
* Das CLI führt die funktion `convert(...)` aus und setzt bei gewählter Option `-o` den Flag zum Überschreiben auf  `True`
