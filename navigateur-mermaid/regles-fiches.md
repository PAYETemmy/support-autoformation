# Règles d'écriture de fiches.json

Ce fichier dit comment écrire le contenu que lit `guide.html`. Source entre crochets ; [Ajout] = règle propre au modèle.

## Rôle

- `donnees.json` donne l'ordre et les liens (« s'appuie sur »). `fiches.json` donne le contenu. Une seule source par information. [Ajout, principe du single sourcing DITA]
- Le guide relit les deux fichiers à chaque ouverture. [Ajout]

## Format

```json
{
  "format": "guide-navigateur/1",
  "source": "Notion, page « Apprendre le vocabulaire Mermaid avec Frayer »",
  "copie_du": "2026-11-25",
  "elements": {
    "type": { "condition": "Sur une page vide de mermaid.live", "critere": "Le diagramme s'affiche sans erreur", "fiches": ["Diagramme"] }
  },
  "fiches": {
    "Diagramme": {
      "definition": "type de schéma déclaré en première ligne.",
      "caracteristiques": "toujours en 1re ligne ; décide de la syntaxe du reste.",
      "exemples": [ { "titre": "RH : processus de recrutement", "texte": "… → `flowchart`.", "code": "flowchart LR\n    A --> B" } ],
      "non_exemples": ["`flowchat` (faute de frappe)"]
    }
  },
  "cas_complets": [
    { "titre": "…", "domaine": "…", "contexte": "…", "objectif": "…", "code": "flowchart TD\n    …",
      "vocabulaire": [ { "fiche": "Forme", "precision": "losange" } ] }
  ]
}
```

| Champ | Rôle |
| --- | --- |
| `format` | Toujours `"guide-navigateur/1"`. |
| `source`, `copie_du` | D'où vient le contenu, et date de la copie (AAAA-MM-JJ). |
| `elements` | Une entrée par `id` de `donnees.json`. |
| `condition` | Dans quelle situation l'élément s'applique. [Mager : condition de l'objectif] |
| `critere` | Ce qui prouve la réussite, observable. [Mager : critère de l'objectif] |
| `fiches` | Noms des fiches de Frayer de l'élément, dans l'ordre de lecture. |
| `fiches` (racine) | Les fiches, indexées par leur nom exact. |
| `definition`, `caracteristiques` | Définition intensionnelle et caractéristiques essentielles. [Frayer ; ISO 704] |
| `exemples` | Le guide n'affiche que le premier. [Ajout] |
| `non_exemples` | Chacun : `` `code` (raison) ``. [Frayer ; Tennyson et Boutwell, non-exemples appariés] |
| `tableau` | Facultatif : `{ "colonnes": [...], "lignes": [[...]] }`. |
| `cas_complets` | Cas d'application complets, en fin de guide. Facultatif. |

## Règles

- Chaque `id` de `donnees.json` a une entrée dans `elements`, et seulement ceux-là. [Ajout]
- Chaque nom de `elements.*.fiches` et de `vocabulaire.*.fiche` existe dans `fiches`. [Ajout]
- Chaque fiche est rattachée à au moins un élément. [Ajout]
- Pas de numéro dans les noms de fiches ; on renvoie à une fiche par son nom. [Ajout]
- Code entre accents graves dans les textes : `` `A --> B` ``. Le code des exemples va dans `code`, sans accent grave. [Ajout]
- Une fiche partagée par plusieurs éléments est affichée une fois, au premier élément ; ensuite, un renvoi. [Ajout]
- Après une modification des fiches dans Notion, refaire la copie et mettre à jour `copie_du`. [Ajout]
