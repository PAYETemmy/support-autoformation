# Règles pour remplir contenu.json

Ce fichier dit comment écrire le contenu que lit `index.html`. Chaque règle indique sa source entre crochets : [Consigne] = demande de l'utilisateur ; [Page] = convention de la page Notion « Apprendre le vocabulaire Mermaid avec Frayer » ; [Ajout] = règle propre au modèle ; sinon, la référence.

Les règles **bloquantes** sont vérifiées par la page : si une seule échoue, elle affiche la liste des erreurs au lieu du site.

## Ce que décrit le fichier

Un domaine découpé en notions, une fiche de Frayer par notion, rangées par niveau, plus des cas complets. Une notion est un concept, donc un nom : « Lien », « Sous-graphe ». [Frayer, Frederick et Klausmeier, 1969]

## Format

```json
{
  "format": "frayer-apprentissage/1",
  "titre": "Mermaid, les flowcharts",
  "source": "Notion, page « Apprendre le vocabulaire Mermaid avec Frayer »",
  "copie_du": "2026-11-25",
  "version_mermaid": "11.16",
  "niveaux": [
    { "id": "bases", "titre": "Bases", "but": "Le minimum pour dessiner un diagramme simple complet." }
  ],
  "notions": [
    {
      "id": "lien",
      "nom": "Lien",
      "niveau": "bases",
      "definition": "Trait qui relie deux nœuds.",
      "caracteristiques": ["Entre deux identifiants", "Au moins 2 tirets", "Style variable"],
      "exemples": [
        {
          "domaine": "E-commerce",
          "situation": "tunnel d'achat",
          "explication": "Les étapes ont un ordre obligatoire → flèche `-->`.",
          "code": "flowchart LR\n    A[Panier] --> B[Livraison] --> C[Paiement]"
        },
        {
          "domaine": "Informatique",
          "situation": "réseau d'un bureau",
          "explication": "Les appareils sont reliés, sans sens de circulation → trait `---`.",
          "code": "flowchart LR\n    A[Box internet] --- B[Switch]"
        }
      ],
      "non_exemples": [
        { "ecrit": "`A -> B`", "raison": "1 seul tiret" },
        { "ecrit": "`A B`", "raison": "aucun lien" }
      ]
    }
  ],
  "cas": [
    {
      "id": "panne_internet",
      "titre": "Arbre de diagnostic « pas d'Internet »",
      "domaine": "Support informatique",
      "contexte": "…",
      "objectif": "…",
      "code": "flowchart TD\n    …",
      "notions": [ { "id": "forme", "precision": "losanges en cascade" }, { "id": "etiquette" } ]
    }
  ]
}
```

| Champ | Type | Rôle |
| --- | --- | --- |
| `format` | texte | Toujours `"frayer-apprentissage/1"`. |
| `titre` | texte | Nom du site, en tête de l'accueil. |
| `source`, `copie_du` | texte, date ; facultatifs | D'où vient le contenu, et date de la copie (AAAA-MM-JJ). |
| `version_mermaid` | texte, facultatif | Version de Mermaid où les exemples ont été testés. |
| `niveaux` | liste | Les niveaux, du plus simple au plus avancé. |
| `id` (niveau) | texte | Identifiant court, cité par les notions. |
| `titre`, `but` (niveau) | texte ; `but` facultatif | Nom du niveau, et ce qu'on sait faire à la fin. |
| `notions` | liste | Les fiches, dans l'ordre d'apprentissage. |
| `id` (notion) | texte | Identifiant court et stable : adresse de la fiche (`#/n/id`) et clé de la progression. |
| `nom` | texte | Le terme préféré : centre de la fiche. |
| `niveau` | texte | L'`id` d'un niveau. |
| `definition` | texte | Case Définition. |
| `caracteristiques` | liste de textes | Case Caractéristiques. |
| `exemples` | liste | Case Exemples : `domaine`, `situation`, `explication`, `code`. |
| `non_exemples` | liste | Case Non-exemples : `ecrit` (l'écriture fautive) et `raison` (ce qui manque). |
| `tableau` | objet, facultatif | `colonnes` et `lignes` : un tableau de référence sous les exemples. |
| `cas` | liste, facultatif | Cas complets. |
| `notions` (cas) | liste | `id` d'une notion et `precision` (facultatif) : ce que le cas en utilise. |

## Règles bloquantes

**Fichier**

- JSON valide, en UTF-8, sans commentaire. [Ajout]
- Seulement les champs du tableau, à chaque niveau : un champ inconnu est une erreur, souvent une faute de frappe. [Ajout]
- `format` vaut exactement `"frayer-apprentissage/1"`. [Ajout]
- `titre` : texte non vide. `copie_du`, s'il existe : date AAAA-MM-JJ. [Ajout]
- `niveaux` : liste non vide. `notions` : au moins 4, pour que chaque question ait 3 mauvaises réponses. [Ajout]
- Dans tous les textes, les accents graves vont par paires. [Ajout]

**Niveaux**

- `id` : commence par une lettre minuscule, puis seulement `a-z`, `0-9` et `_` ; unique. [Ajout]
- `titre` non vide. [Ajout]

**Notions**

- `id` : même forme ; unique. [Ajout]
- `nom` : non vide, unique, sans numéro en tête. [Consigne]
- `niveau` : l'`id` d'un niveau existant. [Ajout]
- `definition` : 15 mots au plus, terminée par un point, sans le terme défini. [Consigne ; ISO 704:2022, 6.5.2 : la définition circulaire est déficiente]
- `caracteristiques` : de 1 à 5 textes non vides. [Consigne]
- `exemples` : exactement 2, de deux domaines différents ; `domaine`, `situation`, `explication` et `code` non vides. [Consigne]
- `non_exemples` : exactement 2 ; `ecrit` et `raison` non vides. [Page ; Tennyson et Boutwell, 1974]
- `tableau`, s'il existe : chaque ligne a autant de cases que `colonnes`. [Ajout]

**Cas**

- `id` : même forme ; unique parmi les cas. [Ajout]
- `titre`, `domaine`, `contexte`, `objectif` et `code` non vides. [Page]
- `notions` : au moins 2, chacune présente dans `notions`. [Page : un cas mobilise plusieurs fiches]

## Règles d'écriture (non vérifiées par la page)

**Ordre et niveaux**

- Une notion vient après celles dont elle a besoin pour être comprise. [Gagné, 1968]
- Trois niveaux : bases (le minimum pour un diagramme complet), flowchart complet, cas avancés. [Page ; Reigeluth : épitomé, du général au détail]

**Nom**

- Le terme préféré, en français, sous forme de nom. [Page]
- Un mot-clé du langage entre accents graves : « Alias `graph` ». [Page]
- Une précision ou une version minimale entre parenthèses : « Clic (interaction) », « (v11.3+) ». [Page]

**Définition**

- D'abord la catégorie plus large, puis ce qui distingue : « Trait qui relie deux nœuds. » [ISO 704 : définition par genre et différence]
- Ni le terme ni un mot de sa famille (« cliquant » pour Clic). Le mot générique d'un terme composé est permis : « lien » dans la définition de Lien invisible. [ISO 704, 6.5.2]
- Seulement des mots courants ou des notions déjà vues. [Ajout]
- Écrite par l'auteur, jamais copiée de la documentation. [Consigne]

**Caractéristiques**

- Seulement les essentielles : si on en retire une, ce n'est plus la notion. Essentielle = présente dans les 2 exemples. [Frayer]
- On ne complète jamais pour faire nombre. [Ajout]
- Chacune se montre du doigt dans le code. [Ajout]
- Courte, commence par une majuscule, sans point final. [Ajout]

**Exemples**

- Un métier et une situation réels, jamais « pour remplir ». [Consigne]
- Les 2 montrent deux facettes : un cas typique, puis un cas inattendu. [Merrill et Tennyson, 1977 : exemples divergents]
- `explication` dit pourquoi c'est la notion, et finit si utile par « → `syntaxe clé` ». [Page]
- `code` : complet et court, 3 à 6 nœuds, textes en français. Il s'affiche sans erreur dans `version_mermaid`. [Page]
- Si l'exemple dépend d'un outil ou d'une version (pack d'icônes, images en ligne, Mermaid 12), le dire dans `explication`. [Page]
- Chaque exemple a toutes les caractéristiques. [Consigne]

**Non-exemples**

- Chacun ressemble à la notion, mais une seule caractéristique essentielle manque. [Tennyson et Boutwell, 1974 : non-exemples appariés]
- De préférence, un « presque juste » (`A -> B`) et une notion voisine qu'on confond (`A{ }` pour Style). [Page]
- `ecrit` : l'écriture fautive, code entre accents graves, sans la raison. [Ajout]
- `raison` : la caractéristique qui manque, ou la notion confondue, en minuscule. « N'existe pas » ne suffit pas. [Ajout]
- Un non-exemple ne fonctionne jamais comme la notion. [Ajout]

**Cas complets**

- Un métier où le flowchart sert vraiment : génie logiciel, DevOps, support, processus, données. [Page]
- `objectif` : qui doit comprendre quoi. [Page]
- Plusieurs notions, de plusieurs niveaux. [Page ; Sweller et Cooper, 1985 : exemples travaillés]

## Ordre de travail pour une notion

1. Exemples, puis non-exemples, puis caractéristiques, puis définition : du concret à l'abstrait. [Consigne]
2. Tester chaque `code` dans `version_mermaid`. [Page]
3. Ouvrir `index.html` : corriger chaque erreur affichée jusqu'à voir l'accueil. [Ajout]

## Mettre à jour le fichier

- Après une modification dans Notion : refaire la copie, puis mettre `copie_du` à jour. [Ajout]
- Ne jamais changer l'`id` d'une notion : la progression de l'apprenant y est rangée. [Ajout]

## Écarts connus dans contenu.json

- **Raisons ajoutées** : 10 non-exemples de la page Notion n'avaient pas de raison entre parenthèses. Elles ont été écrites pour ce fichier : Sous-graphe (2), Sous-graphe avancé, Configuration (2), Pièges de syntaxe (2), Sous-graphe replié, Espacement, Codes de caractères.
- **Raisons vagues** (« n'existe pas », « faute », « invalide », « inexistant ») : Diagramme, Direction, Forme, Style, Extrémité de lien (2), Longueur de lien, Chaînage et liens multiples, Thème, Alias `graph` (2), Formes nommées, Animation niveau 2, Courbe par lien, Sous-graphe replié, Rendu. La page ne les propose pas comme mauvaises réponses aux questions.
- **Mot de la même famille dans la définition** : Clic (« cliquant »), Animation de lien (« animé »).
- **Images en ligne** : les 2 exemples d'Image dans un nœud chargent des logos depuis github.com. Sans connexion, le dessin ne s'affiche pas ; le code reste visible.

## Sources

- Frayer, D. A., Frederick, W. C. et Klausmeier, H. J. (1969). *A Schema for Testing the Level of Concept Mastery*. Wisconsin Research and Development Center for Cognitive Learning.
- ISO 704:2022. *Terminology work — Principles and methods*.
- Merrill, M. D. et Tennyson, R. D. (1977). *Teaching Concepts: An Instructional Design Guide*. Educational Technology Publications.
- Tennyson, R. D. et Boutwell, R. C. (1974). Methodology for the sequencing of instances in classroom concept teaching.
- Gagné, R. M. (1968). Learning hierarchies. *Educational Psychologist*, 6, 1–9.
- Reigeluth, C. M. et Stein, F. S. (1983). The elaboration theory of instruction. Dans C. M. Reigeluth (dir.), *Instructional-Design Theories and Models*. Erlbaum.
- Sweller, J. et Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction*, 2(1), 59–89.
- [Documentation Mermaid, flowcharts](https://mermaid.js.org/syntax/flowchart.html).
