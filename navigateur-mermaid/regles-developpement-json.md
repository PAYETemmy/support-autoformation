# Règles d'écriture du fichier .json du développement

Ce fichier dit comment écrire le contenu que lit `developpement.html`. Chaque règle indique sa source entre crochets ; [Consigne] = demande de l'utilisateur ; [Ajout] = règle propre au modèle. Les règles **bloquantes** sont vérifiées par le modèle : si une seule échoue, il affiche la liste des erreurs au lieu du développement.

## Ce que décrit le fichier

Tout le contenu du développement, dans un seul fichier : les compétences, les fiches qu'elles mobilisent et les cas complets. [Consigne]

## Format

```json
{
  "format": "developpement/1",
  "titre": "Flowcharts Mermaid",
  "source": "Notion, page « Apprendre le vocabulaire Mermaid avec Frayer »",
  "copie_du": "2026-11-25",
  "competences": [
    {
      "id": "type",
      "competence": "Déclarer un type de diagramme (flowchart)",
      "avant": [],
      "quand": "Sur une page vide de mermaid.live",
      "reussi_si": "Le diagramme s'affiche sans erreur",
      "fiches": ["Diagramme"]
    }
  ],
  "fiches": {
    "Diagramme": {
      "definition": "type de schéma déclaré en première ligne.",
      "caracteristiques": "toujours en 1re ligne ; décide de la syntaxe du reste.",
      "exemple": {
        "titre": "RH : processus de recrutement",
        "texte": "Des étapes et des décisions qui s'enchaînent → `flowchart`.",
        "code": "flowchart LR\n    A[Candidature reçue] --> B{Profil retenu ?}"
      },
      "non_exemples": ["`flowchat` (faute de frappe)", "`flowchart` placé après des nœuds (pas en 1re ligne)"]
    }
  },
  "cas": [
    {
      "id": "cas_connexion",
      "titre": "Connexion sécurisée à un compte",
      "domaine": "Génie logiciel",
      "contexte": "Une banque en ligne subit des tentatives de piratage…",
      "objectif": "Que le développeur, le testeur et le support appliquent la même règle.",
      "code": "flowchart TD\n    …",
      "fiches": [{ "fiche": "Forme", "precision": "losange" }]
    }
  ]
}
```

| Champ | Type | Rôle |
| --- | --- | --- |
| `format` | texte | Toujours `"developpement/1"`. |
| `titre` | texte | Nom du domaine, en tête du sommaire. |
| `source` | texte, facultatif | D'où vient le contenu. |
| `copie_du` | date, facultatif | Date de la copie depuis la source, AAAA-MM-JJ. |
| `competences` | liste | Une carte par compétence. |
| `id` | texte | Identifiant court et stable ; sert d'adresse à la carte (`#id`). |
| `competence` | texte | Ce que l'apprenant sait faire : titre de la carte. |
| `avant` | liste d'`id` | Compétences prérequises directes. Vide s'il n'y en a pas. |
| `quand` | texte | Condition : la situation de départ. |
| `reussi_si` | texte | Critère : ce qui prouve la réussite. |
| `fiches` (compétence) | liste de noms | Fiches de la carte, dans l'ordre de lecture. |
| `fiches` (racine) | objet | Les fiches, rangées par nom. |
| `definition`, `caracteristiques` | texte | Cases Définition et Caractéristiques. |
| `exemple` | objet | `titre` (« Domaine : situation »), `texte` (pourquoi c'est un exemple), `code`. |
| `non_exemples` | liste de textes | Chacun : écriture fautive, puis la raison entre parenthèses. |
| `tableau` | objet, facultatif | `colonnes` (liste) et `lignes` (liste de listes). |
| `cas` | liste, facultatif | Cas complets. |
| `domaine`, `contexte`, `objectif`, `code` | texte | Le métier, la situation, qui doit comprendre quoi, le diagramme. |
| `fiches` (cas) | liste | `fiche` (nom) et `precision` (facultatif) : ce que le cas en utilise. |

## Règles du fichier (bloquantes)

- JSON valide, encodé en UTF-8, sans commentaire. [Ajout]
- Seulement les champs du tableau, à chaque niveau. Un champ inconnu est une erreur, souvent une faute de frappe. [Ajout]
- `format` vaut exactement `"developpement/1"`. [Ajout]
- `titre` est un texte non vide ; `copie_du`, s'il existe, est une date AAAA-MM-JJ. [Ajout]
- `competences` est une liste non vide ; `fiches` est un objet non vide. [Ajout]
- Dans tous les textes, les accents graves vont par paires. [Ajout]

## Règles des compétences (bloquantes)

- `id` : commence par une lettre minuscule, puis seulement `a-z`, `0-9` et `_`. Unique parmi les compétences et les cas. [Ajout]
- `competence` : texte non vide de 80 caractères au plus, unique sans distinguer majuscules et minuscules. [Ajout]
- `competence` ne commence ni par un numéro ni par un verbe vague : comprendre, connaître, savoir, maîtriser, découvrir, apprendre. [Consigne : pas de numérotation ; Mager : verbes vagues à proscrire]
- `quand` et `reussi_si` sont des textes non vides. [Mager : condition et critère]
- `avant` ne cite que des `id` de compétences, jamais la compétence elle-même, jamais deux fois le même. [ISO 704:2022, 6.5.2 : la définition circulaire est déficiente]
- `avant` ne forme aucune boucle. [Doignon et Falmagne : relation de prérequis]
- `fiches` : liste non vide de noms présents dans `fiches`, sans doublon. [Ajout]

## Règles des fiches (bloquantes)

- Nom non vide, sans numéro en tête. [Consigne]
- `definition` et `caracteristiques` : textes non vides. [Frayer]
- `exemple` : `titre`, `texte` et `code` non vides. Un seul exemple par fiche. [Frayer ; un seul : Consigne]
- `non_exemples` : au moins un texte non vide. [Frayer]
- `tableau`, s'il existe : chaque ligne a autant de cases que `colonnes`. [Ajout]
- Chaque fiche est citée par au moins une compétence. [Ajout]

## Règles des cas (bloquantes)

- `id` : même forme que pour les compétences, unique parmi les compétences et les cas. [Ajout]
- `titre`, `domaine`, `contexte`, `objectif` et `code` : textes non vides. [Ajout]
- `fiches` : au moins une ; chaque `fiche` existe dans `fiches`. [Ajout]

## Règles d'écriture (non vérifiées par le modèle)

**Compétence**

- Verbe à l'infinitif + objet : « Relier deux nœuds », jamais « Les liens ». [Anderson et Krathwohl, 2001]
- Verbe observable, un seul verbe, une seule nouveauté. [Mager]
- Le terme technique d'origine entre parenthèses : « Relier deux nœuds (lien) ». [Ajout]
- `quand` décrit la situation de départ, pas une consigne : « À partir d'une question à réponse oui ou non ». [Mager : condition]
- `reussi_si` se constate en regardant le résultat : « Un losange mène à deux branches étiquetées ». [Mager : critère observable]
- `avant` ne cite que les prérequis directs : si B s'appuie déjà sur A, ne pas citer A. [Gagné, 1968]
- Les compétences, leurs libellés et `avant` reprennent `donnees.json` du navigateur : `competence` = `libelle`, `avant` = `s_appuie_sur`, mêmes `id`. Modifier l'un, c'est modifier l'autre. [Ajout]
- L'ordre des compétences dans le fichier n'est pas affiché, mais il décide de la carte ouverte depuis un cas : les ranger comme dans `donnees.json`. [Ajout]

**Fiche**

- Nom : le terme préféré, sous forme de nom ; précision ou version entre parenthèses si besoin : « Clic (interaction) », « (v11.3+) ». [Pratique de la page Notion]
- Définition : une phrase de 15 mots au plus, qui commence par la catégorie puis dit ce qui distingue le concept, sans le terme défini ni un mot de sa famille. [ISO 704 ; Consigne]
- Caractéristiques : 5 au plus, seulement les essentielles, séparées par « ; ». Essentielle = présente dans tous les exemples. [Frayer]
- Exemple : un métier et une situation réels ; le code est complet, court, s'affiche sans erreur. [Consigne]
- Non-exemples : 2. Chacun ressemble au concept, mais il lui manque une seule caractéristique, nommée entre parenthèses. Jamais une écriture qui fonctionne. [Tennyson et Boutwell, 1974 : non-exemples appariés]
- Code dans les textes : entre accents graves. Le code de l'exemple va dans `code`, sans accent grave. [Ajout]

**Cas complet**

- Une situation réelle d'un métier où le diagramme sert vraiment. [Roegiers : situation d'intégration]
- Il mobilise plusieurs fiches, de plusieurs compétences. [Roegiers]
- `objectif` dit qui doit comprendre quoi. [Ajout]

## Mettre à jour le fichier

- **Après une modification dans Notion** : refaire la copie des fiches, puis mettre `copie_du` à jour. [Ajout]
- **Ajouter une compétence** : l'ajouter aussi dans `donnees.json`, avec le même `id`. [Ajout]
- **Vérifier** : ouvrir `developpement.html` et corriger chaque erreur affichée jusqu'à voir le sommaire. [Ajout]

## Sources

- Mager, R. F. (1997). *Preparing Instructional Objectives* (3e édition).
- Anderson, L. W. et Krathwohl, D. R. (2001). *A Taxonomy for Learning, Teaching, and Assessing*. Longman.
- Gagné, R. M. (1968). Learning hierarchies. *Educational Psychologist*, 6, 1–9.
- Doignon, J.-P. et Falmagne, J.-C. (1999). *Knowledge Spaces*. Springer.
- ISO 704:2022. *Terminology work — Principles and methods*.
- Frayer, D. A., Frederick, W. C. et Klausmeier, H. J. (1969). *A Schema for Testing the Level of Concept Mastery*.
- Tennyson, R. D. et Boutwell, R. C. (1974). Methodology for the sequencing of instances in classroom concept teaching.
- Roegiers, X. (2000). *Une pédagogie de l'intégration*. De Boeck.
