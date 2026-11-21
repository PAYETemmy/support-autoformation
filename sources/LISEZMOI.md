# Sources des cartes

- `gabarit-guide.html` : gabarit commun (les données remplacent `/*DATA*/`).
- `donnees-*.js` : une carte par fichier.
- `construire.py <donnees.js> "<Sujet>" <dossier> "<nom court>"` : construit la page du dossier.
- `essai.py <page.html> <pc|iphone> [étapes]` : trace toute la carte et signale les atomes hors écran.

# Supports au format modèle v1 (page à lire, sans graphe)

- `gabarit-modele.html` : gabarit commun (les données remplacent `/*DATA*/`).
- `donnees-modele-*.js` : un support par fichier (`PAGE` + `EL` : concepts, propriétés, règles, procédures, exemples, contre-exemples, exercice).
- `construire-modele.py <donnees.js> <dossier> "<nom court>"` : construit la page du dossier.
