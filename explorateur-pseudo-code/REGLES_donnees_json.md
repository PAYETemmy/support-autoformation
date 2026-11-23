# Règles d'écriture de `donnees.json`
Explorateur de connaissances, v10.1. Ces règles sont celles que l'application applique quand elle lit le fichier.

## 0. Consigne à donner à une IA (à copier)
> Remplis `donnees.json` en respectant strictement ce document. Écris un JSON valide, en français, et recopie les valeurs imposées au caractère près, y compris l'apostrophe typographique ’. Chaque concept, propriété, règle et procédure doit avoir au moins 3 exemples. Chaque chaîne de définitions doit aboutir à des termes primitifs. Avant de rendre le fichier, vérifie la check-list de la section 8.

---

## 1. Structure générale
```json
{
  "format": "modele-representation-connaissance",
  "version": 10.1,
  "titre": "Nom du contenu",
  "items": [ ... ],
  "links": [ ... ]
}
```
- `items` et `links` sont **obligatoires** et doivent être des tableaux. Sinon le fichier est considéré comme illisible.
- `format`, `version` et `titre` sont informatifs : l'application les ignore.
- Le JSON doit être valide : UTF-8, sans commentaire et sans virgule finale.
- Le fichier se place à côté de l'application : `explorateur-pseudo-code/donnees.json` (ou `explorateur/donnees.json` pour l’explorateur Python).

---

## 2. Élément (`items[]`)
```json
{
  "id": "geo-segment",
  "type": "Concept",
  "name": "Segment",
  "status": "Établi",
  "life": "Actif",
  "fields": { },
  "foundations": [ { "type": "Définition de référence", "text": "…" } ],
  "formulation": "",
  "autoForm": true
}
```

| Clé | Règle | Si absent ou invalide |
|---|---|---|
| `id` | Texte **unique et stable**. Convention : `prefixe-nom` (ex. `geo-segment`). | Un id est généré, et la progression est perdue à chaque chargement |
| `type` | `Concept`, `Propriété`, `Règle`, `Procédure`, `Exemple` ou `Contre-exemple` | Devient `Concept` |
| `name` | Nom court affiché | `Sans nom` |
| `status` | `À examiner`, `Proposé`, `Établi`, `Contesté` ou `Réfuté` | `À examiner` |
| `life` | `Actif` ou `Archivé` (un élément archivé est exclu du parcours, des révisions et du compte d'exemples) | `Actif` |
| `fields` | Champs du gabarit du type (section 3) | `{}` |
| `foundations` | Liste de `{type, text}` (section 4) | `[]` |
| `formulation` | Laisse `""` : elle est composée automatiquement si `autoForm` vaut `true` | — |
| `autoForm` | Mets `true`. Avec `false`, `formulation` est affichée telle quelle. | — |

- Changer un `id` fait perdre la progression de l'élément, car elle est rattachée à l'id.
- N'écris pas `level` ni `seen` : c'est la progression, conservée dans le navigateur.
- Un champ vide (`""`) est supprimé.

---

## 3. Champs par type (`fields`)
- Les noms de clés sont exacts.
- Les valeurs à choix sont à recopier **au caractère près**.
- Chaque champ s'insère dans une phrase gabarit : commence-le comme indiqué dans la colonne « Commence par ».

### Concept
Gabarit : `[Nom] : [définition]. Caractéristiques : [traits].`

| Clé | Contenu | Commence par |
|---|---|---|
| `domain` | Domaine | « le pseudo-code » |
| `nature` | **Absent** = concept défini à partir d'autres concepts. `Terme primitif (non défini)` = terme primitif. | — |
| `definition` | Uniquement pour un concept défini. Utilise les concepts cibles de « Se définit à partir de ». | — |
| `intuition` | Uniquement pour un terme primitif : son sens intuitif, en mots simples | — |
| `traits` | Ce qui le distingue des concepts voisins | — |

### Propriété
Gabarit : `Dans le domaine [domain], « Concept » [qualifier] [relation] [object].`

| Clé | Contenu | Commence par |
|---|---|---|
| `domain` | Domaine de validité | « du … » / « de la … » |
| `qualifier` | Précision sur le concept (facultatif) | « de taille N » |
| `relation` | Verbe | « a des indices », « contient » |
| `object` | Caractéristique ou autre concept | « allant de 0 à N−1 » |

⚠️ N'écris **jamais** le nom du concept dans les champs : il vient de la relation `Définit`, `Caractérise` ou `Met en relation`.

### Règle
Gabarit : `Dans le contexte [context], si [condition], alors [conclusion], sauf si [exception].`

| Clé | Contenu | Commence par |
|---|---|---|
| `kind` | `Descriptive` (dit ce qui se passe) ou `D’action` (dit quoi faire) | — |
| `context` | Contexte | « de l’exécution… », « du … » |
| `condition` | Si… | sujet + verbe |
| `conclusion` | Alors… | sujet + verbe |
| `exceptionMode` | `Exception réelle`, `Aucune exception identifiée dans ce domaine` ou `Limites encore inconnues` | — |
| `exception` | Uniquement si `exceptionMode` vaut `Exception réelle` | — |

N'invente pas d'exception : utilise plutôt `Aucune exception identifiée dans ce domaine`.

### Procédure
Gabarit : `Dans le contexte [context], pour [goal], à partir de [inputs] : [steps] Elle produit [result], si [success].`

| Clé | Contenu | Commence par |
|---|---|---|
| `context` | Contexte | « du … » |
| `goal` | But | un infinitif (« calculer… ») |
| `inputs` | Entrées et préconditions | « un tableau T… » |
| `steps` | Une étape par ligne, séparées par `\n` : `1. …\n2. Si …, alors …` | — |
| `result` | Résultat | « la somme… » |
| `success` | Conditions de réussite | sujet + verbe |

### Exemple
Gabarit : `« [case] » illustre [cibles] parce que [shown].`

| Clé | Contenu |
|---|---|
| `case` | Cas concret, précis, avec des valeurs |
| `shown` | Caractéristique montrée. Commence en minuscule : l'application ajoute « parce que ». |

La cible n'est **pas** écrite dans les champs : elle vient de la relation `Illustre`.

### Contre-exemple
Gabarit : `« [case] » montre que [énoncé] ne s’applique pas lorsque [condition].`

| Clé | Contenu |
|---|---|
| `case` | Cas qui met l'énoncé à l'épreuve |
| `condition` | Ne s'applique pas lorsque… (sujet + verbe) |
| `verdict` | L'une des valeurs ci-dessous |

Valeurs de `verdict` :
- `Hors du domaine prévu (2a) : pas de contradiction dans le domaine`
- `Condition à préciser (2b)`
- `Énoncé à réviser, éventuellement par une exception (2c)`
- `Traité : énoncé révisé`

---

## 4. Fondements (`foundations[]`)
- `type` : `Définition de référence`, `Démonstration ou raisonnement`, `Source documentaire`, `Observation ou expérience`, ou `Non précisé`. Un type inconnu devient `Non précisé`.
- `text` : la justification. Un texte vide fait supprimer le fondement.
- Un élément peut avoir plusieurs fondements.

---

## 5. Relation (`links[]`)
```json
{ "id": "l-geo-segment-geo-point", "source": "geo-segment", "target": "geo-point", "type": "Se définit à partir de", "note": "" }
```
- `source` et `target` sont des `id` existants. Sinon la relation est **supprimée sans avertissement**.
- `id` est unique. Convention : `l-<source>-<target>`.
- `note` est facultatif.
- Pas de relation d'un élément vers lui-même.
- Un doublon (même source, cible et type) est supprimé.
- **Sens de lecture :** source → verbe → cible. Exemples : `Segment` *se définit à partir de* `Point` ; `Exemple` *illustre* `Concept`.

| Source | `type` (exact) | Cibles autorisées | Contrainte |
|---|---|---|---|
| Concept | `Se définit à partir de` | Concept | Source jamais primitive ; pas de définition circulaire |
| Propriété | `Définit` | Concept | La propriété fait partie de la définition |
| Propriété | `Caractérise` | Concept | Toujours vraie, sans définir ; pas `Définit` et `Caractérise` vers le même concept |
| Propriété | `Met en relation` | Concept | Au moins 2 concepts |
| Règle | `Porte sur` | Concept | — |
| Procédure | `Applique` | Règle | Uniquement une règle `D’action` |
| Procédure | `S’appuie sur` | Concept, Propriété, Règle | Pour une règle : uniquement une règle `Descriptive` |
| Procédure | `Contient` | Procédure | Sous-procédure |
| Exemple | `Illustre` | Concept, Propriété, Règle, Procédure | — |
| Contre-exemple | `Met à l’épreuve` | Concept, Propriété, Règle, Procédure | — |
| Tous | `A pour prérequis` | Tous | La cible s'apprend avant la source ; aucune boucle |
| Propriété, Règle | `Se contredit avec` | Propriété, Règle | — |

⚠️ `S’appuie sur`, `Met à l’épreuve` et `D’action` s'écrivent avec l'apostrophe **’** (U+2019), pas avec `'`.

---

## 6. Exigences d'apprentissage
Elles s'appliquent à chaque Concept, Propriété, Règle et Procédure actif.
- **Au moins 3 exemples** : 3 éléments `Exemple` actifs reliés par `Illustre`. Un même exemple peut illustrer plusieurs éléments.
- **Chaîne de définitions** : tout concept défini a au moins une relation `Se définit à partir de`. En remontant ces relations, on doit atteindre des **termes primitifs**.
- Une Propriété, une Règle ou une Procédure doit être reliée aux concepts qu'elle mobilise. Leurs définitions et termes primitifs s'affichent alors automatiquement dans « Apprendre ».

---

## 7. Conformité au modèle (sinon, avertissement dans la fiche)
| Type | Champs requis | Relation requise |
|---|---|---|
| Concept défini | `definition`, `traits` | ≥ 1 `Se définit à partir de` |
| Terme primitif | `intuition`, `traits` | Aucune `Se définit à partir de` sortante |
| Propriété | `domain`, `relation`, `object` | ≥ 1 `Définit`, `Caractérise` ou `Met en relation` |
| Règle | `kind`, `context`, `condition`, `conclusion`, `exceptionMode` (+ `exception` si réelle) | ≥ 1 `Porte sur` |
| Procédure | `goal`, `inputs`, `steps`, `result`, `success` | ≥ 1 `S’appuie sur`, `Applique` ou `Contient` |
| Exemple | `case`, `shown` | ≥ 1 `Illustre` |
| Contre-exemple | `case`, `condition`, `verdict` | ≥ 1 `Met à l’épreuve` |

Cohérence des statuts :
- `Établi` + un contre-exemple non résolu (verdict absent, 2b ou 2c) → avertissement. Analyse le contre-exemple ou passe le statut à `Contesté`.
- `Réfuté` exige un contre-exemple dont le verdict est 2b ou 2c. Un cas 2a ne réfute pas l'énoncé.

---

## 8. Check-list avant livraison
- [ ] Le JSON est valide, et `items` et `links` sont présents.
- [ ] Les `id` sont uniques et stables.
- [ ] Toutes les relations pointent vers des `id` existants.
- [ ] Les valeurs à choix sont recopiées exactement, avec l'apostrophe ’.
- [ ] Chaque concept est soit défini (`definition` + `Se définit à partir de`), soit primitif (`nature` + `intuition`).
- [ ] Il n'y a ni boucle de définitions ni boucle de prérequis.
- [ ] Il y a ≥ 3 exemples par Concept, Propriété, Règle et Procédure.
- [ ] Aucun nom de concept ou de cible n'est écrit dans les champs d'une Propriété, d'un Exemple ou d'un Contre-exemple.
- [ ] `formulation` vaut `""` et `autoForm` vaut `true`.
- [ ] `level` et `seen` sont absents.

---

## 9. Exemple minimal complet (conforme, sans avertissement)
```json
{
  "format": "modele-representation-connaissance",
  "version": 10.1,
  "titre": "Géométrie : le segment",
  "items": [
    { "id": "geo-point", "type": "Concept", "name": "Point", "status": "Établi", "life": "Actif",
      "fields": { "domain": "la géométrie plane", "nature": "Terme primitif (non défini)",
        "intuition": "Un emplacement précis, sans longueur ni épaisseur.",
        "traits": "Il se désigne par une lettre majuscule. Deux points distincts occupent deux emplacements différents." },
      "foundations": [ { "type": "Définition de référence", "text": "Terme primitif de la géométrie euclidienne." } ],
      "formulation": "", "autoForm": true },
    { "id": "geo-segment", "type": "Concept", "name": "Segment", "status": "Établi", "life": "Actif",
      "fields": { "domain": "la géométrie plane",
        "definition": "Portion de droite limitée par deux points, appelés extrémités.",
        "traits": "Il se note [AB]. Il a une longueur. [AB] et [BA] désignent le même segment." },
      "foundations": [ { "type": "Définition de référence", "text": "Définition du cours de géométrie." } ],
      "formulation": "", "autoForm": true },
    { "id": "geo-ex-feuille", "type": "Exemple", "name": "[AB] sur une feuille", "status": "Établi", "life": "Actif",
      "fields": { "case": "Le trait tiré à la règle entre les points A et B d’une feuille", "shown": "il est limité par deux points, ses extrémités" },
      "foundations": [], "formulation": "", "autoForm": true },
    { "id": "geo-ex-triangle", "type": "Exemple", "name": "Côté d’un triangle", "status": "Établi", "life": "Actif",
      "fields": { "case": "Le côté [BC] d’un triangle ABC", "shown": "il est limité par deux sommets, qui sont des points" },
      "foundations": [], "formulation": "", "autoForm": true },
    { "id": "geo-ex-regle", "type": "Exemple", "name": "Règle graduée", "status": "Établi", "life": "Actif",
      "fields": { "case": "Sur une règle graduée, la portion entre les graduations 2 et 7", "shown": "elle est délimitée par deux points précis et mesure 5 unités" },
      "foundations": [], "formulation": "", "autoForm": true }
  ],
  "links": [
    { "id": "l-geo-segment-geo-point", "source": "geo-segment", "target": "geo-point", "type": "Se définit à partir de", "note": "" },
    { "id": "l-geo-ex-feuille-geo-segment", "source": "geo-ex-feuille", "target": "geo-segment", "type": "Illustre", "note": "" },
    { "id": "l-geo-ex-feuille-geo-point", "source": "geo-ex-feuille", "target": "geo-point", "type": "Illustre", "note": "" },
    { "id": "l-geo-ex-triangle-geo-segment", "source": "geo-ex-triangle", "target": "geo-segment", "type": "Illustre", "note": "" },
    { "id": "l-geo-ex-triangle-geo-point", "source": "geo-ex-triangle", "target": "geo-point", "type": "Illustre", "note": "" },
    { "id": "l-geo-ex-regle-geo-segment", "source": "geo-ex-regle", "target": "geo-segment", "type": "Illustre", "note": "" },
    { "id": "l-geo-ex-regle-geo-point", "source": "geo-ex-regle", "target": "geo-point", "type": "Illustre", "note": "" }
  ]
}
```
Exemple plus riche, avec les 6 types : le `donnees.json` actuel (pseudo-code).
