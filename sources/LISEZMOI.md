# Sources des cartes

- `gabarit-guide.html` : gabarit commun (les données remplacent `/*DATA*/`).
- `donnees-*.js` : une carte par fichier.
- `construire.py <donnees.js> "<Sujet>" <dossier> "<nom court>"` : construit la page du dossier.
- `essai.py <page.html> <pc|iphone> [étapes]` : trace toute la carte et signale les atomes hors écran.

# Supports au format modèle v1 (page à lire, sans graphe)

- `gabarit-modele.html` : gabarit commun (les données remplacent `/*DATA*/`).
- `donnees-modele-*.js` : un support par fichier (`PAGE` + `EL` : concepts, propriétés, règles, procédures, exemples, contre-exemples, exercice).
- `construire-modele.py <donnees.js> <dossier> "<nom court>"` : construit la page du dossier.

# Données de l’explorateur pseudo-code

- `donnees-json-pseudo-code/` : générateur de `explorateur-pseudo-code/donnees.json` (concepts, propriétés et règles, procédures, exemples).
- `mots.py` : les mots-clés de « Ma définition » de chaque concept (groupes de sens de la définition, dans l’ordre) ; `groupes.py` : la vérification d’un groupe, identique à celle de l’app.
- Construire : `cd sources/donnees-json-pseudo-code && python3 build.py ../../explorateur-pseudo-code/donnees.json` (signale les éléments qui ont moins de 3 exemples et les mots-clés introuvables dans leur définition).
