# Règles d'écriture du fichier .json

Ce fichier dit comment écrire les données que lit `navigateur.html`. Chaque règle indique sa source entre crochets ; [Ajout] = règle propre au modèle. Les règles **bloquantes** sont vérifiées par le modèle : si une seule échoue, il affiche la liste des erreurs au lieu de l'arbre.

## Ce que décrit le fichier

Un domaine découpé en éléments. Chaque élément s'appuie sur des termes plus primitifs, jusqu'à un premier terme unique. Le modèle dessine l'arbre à partir de ce premier terme : dessous, tout ce qui en découle.

## Format

```json
{
  "format": "navigateur-arbre/1",
  "titre": "Flowcharts Mermaid",
  "elements": [
    { "id": "type", "libelle": "Déclarer un type de diagramme (flowchart)", "s_appuie_sur": [] },
    { "id": "noeud", "libelle": "Déclarer un nœud", "s_appuie_sur": ["type"] },
    { "id": "lien", "libelle": "Relier deux nœuds (lien)", "s_appuie_sur": ["noeud"] }
  ]
}
```

| Champ | Type | Rôle |
| --- | --- | --- |
| `format` | texte | Toujours `"navigateur-arbre/1"`. |
| `titre` | texte | Nom du domaine. Sert de titre à l'onglet. |
| `elements` | liste | Les éléments, chacun après ses termes primitifs. |
| `id` | texte | Identifiant court et stable de l'élément. |
| `libelle` | texte | Ce que l'apprenant sait faire, tel qu'affiché dans le rectangle. |
| `s_appuie_sur` | liste d'`id` | Termes primitifs directs de l'élément. Vide pour le premier terme. |

## Règles du fichier (bloquantes)

- JSON valide, encodé en UTF-8, sans commentaire. [Ajout]
- Seulement les champs du tableau, à la racine comme dans les éléments. Un champ inconnu est une erreur, souvent une faute de frappe. [Ajout]
- `format` vaut exactement `"navigateur-arbre/1"`. [Ajout]
- `titre` est un texte non vide. [Ajout]
- `elements` est une liste non vide. [Ajout]

## Règles des éléments (bloquantes)

**Identifiant**

- Commence par une lettre minuscule, puis seulement `a-z`, `0-9` et `_` : ni accent, ni espace. [Ajout]
- Unique dans le fichier. [Ajout]

**Libellé**

- Texte non vide de 80 caractères au plus. [Ajout]
- Unique dans le fichier, sans distinguer majuscules et minuscules. [Ajout]
- Pas de numérotation en tête : « 9. Formes complètes » est refusé. [Consigne de l'utilisateur]
- Ne commence pas par un verbe vague : comprendre, connaître, savoir, maîtriser, découvrir, apprendre. [Mager : verbes vagues à proscrire]

**Termes primitifs (`s_appuie_sur`)**

- Chaque id cité existe dans le fichier. [Ajout]
- Un élément ne s'appuie pas sur lui-même et ne cite pas deux fois le même terme. [ISO 704:2022, 6.5.2 : la définition circulaire est une définition déficiente]
- Un seul premier terme : un seul élément a une liste vide. [Ajout]
- Chaque élément vient après tous ses termes primitifs ; le premier terme est donc en tête. Cette règle interdit aussi toute boucle. [Doignon et Falmagne : relation de prérequis ; l'ordre du fichier est un ajout]
- Seulement les termes directs : si B s'appuie déjà sur A, un élément qui cite B ne cite pas A. [Doignon et Falmagne : diagramme de Hasse]
- L'arbre déplié compte au plus 3 000 rectangles. Au-delà, découper le domaine en plusieurs fichiers. [Ajout : limite du modèle]

## Règles d'écriture (non vérifiées par le modèle)

**Trouver les éléments et leurs termes primitifs**

- Partir des éléments les plus spécifiques, ceux que l'apprenant veut savoir faire. Pour chacun, demander : « que faut-il déjà savoir faire, juste avant, pour apprendre ceci avec une simple consigne ? ». Chaque réponse devient un terme primitif. [Gagné, 1962]
- Répéter jusqu'au premier terme, le seul élément du domaine qui ne s'appuie sur rien. [Gagné, 1968]
- Garder un terme primitif seulement si, sans lui, l'apprenant échoue sur l'élément. « Utile » ou « lié » ne suffit pas. [Gagné, 1968 : transfert positif]
- Plusieurs termes primitifs sont tous nécessaires (ET). Si deux chemins suffisent chacun (OU), l'écrire dans le libellé ou découper l'élément. [Ajout ; le OU correspond aux « clauses » de Doignon et Falmagne]
- Vérifier avec des apprenants : qui réussit un élément doit réussir ses termes primitifs. Un découpage est accepté quand au moins 90 % des résultats respectent cet ordre. [Gagné : validation par le transfert positif, seuil 0,90]
- Ce qui se mémorise (une liste de 48 formes), les attitudes et les gestes ne se découpent pas ainsi : ce ne sont pas des éléments. [Gagné : les hiérarchies ne portent que sur les habiletés intellectuelles]
- « S'appuie sur » n'est pas « est une sorte de ». Le losange est une sorte de forme, mais utiliser une forme n'exige pas de connaître le losange. [Ajout : comparaison entre Gagné et ISO 25964]
- Ne pas prendre l'ordre habituel d'un cours pour un vrai prérequis, ni ajouter un terme « au cas où ». [Ajout]

**Écrire un libellé**

- Verbe à l'infinitif + objet : « Relier deux nœuds », jamais « Les liens ». [Anderson et Krathwohl, 2001]
- Verbe observable : déclarer, relier, écrire, colorer, corriger. [Mager]
- Un seul verbe, une seule nouveauté : « Déclarer et colorer un nœud » se découpe en deux éléments. [Pratique de rédaction d'objectifs : un seul verbe mesurable par objectif]
- Dans la langue de l'apprenant ; le terme technique d'origine entre parenthèses : « Relier deux nœuds (lien) ». [Ajout]
- Texte brut, sans Markdown : le modèle l'affiche tel quel. [Ajout]
- Court : la condition et le critère de réussite restent hors du libellé. [Ajout]

**Identifiant**

- Ne jamais renommer un id existant : la sélection mémorisée en dépend. [Ajout]

**Ordre des éléments**

- Sous un même élément, l'ordre de gauche à droite suit l'ordre du fichier. Ranger du plus général au plus détaillé. [Reigeluth, 1999 : concepts larges avant concepts précis]

## Mettre à jour un fichier

- **Ajouter un élément** : le placer après ses termes primitifs, ne citer que les directs, puis retirer les liens devenus déduits ailleurs. [Ajout]
- **Retirer un élément** : reporter ses termes primitifs sur les éléments qui s'appuyaient sur lui, puis retirer les liens devenus déduits. [Ajout]
- **Vérifier** : ouvrir le fichier avec `navigateur.html` et corriger chaque erreur affichée jusqu'à voir l'arbre. [Ajout]

## Procédure complète

- Choisir les éléments les plus spécifiques du domaine.
- Les décomposer en termes primitifs, jusqu'au premier terme.
- Écrire chaque libellé.
- Ranger la liste : chaque élément après ses termes primitifs.
- Retirer les liens déduits.
- Ouvrir le fichier avec `navigateur.html` : aucune erreur, l'arbre s'affiche.

## Sources

- Gagné, R. M. (1962). The acquisition of knowledge. *Psychological Review*, 69(4), 355–365.
- Gagné, R. M. (1968). Learning hierarchies. *Educational Psychologist*, 6, 1–9.
- [Conditions of Learning, encyclopédie SAGE des technologies éducatives](https://sk.sagepub.com/ency/edvol/embed/the-sage-encyclopedia-of-educational-technology/chpt/conditions-learning) : cinq capacités, ordre des habiletés intellectuelles.
- [Validation des hiérarchies d'apprentissage, Florida Journal of Educational Research](https://journals.flvc.org/fjer/article/download/133788/137741/246379) : seuil 0,90.
- Doignon, J.-P. et Falmagne, J.-C. (1999). *Knowledge Spaces*. Springer.
- [Falmagne et Doignon, Knowledge Spaces and Learning Spaces (arXiv)](https://arxiv.org/pdf/1511.06757) : relation de prérequis, clauses.
- Mager, R. F. (1997). *Preparing Instructional Objectives* (3e édition).
- [Mager's Guideline, Weber State University](https://weber.instructure.com/courses/307280/pages/magers-guideline) : verbes vagues à proscrire.
- [Writing Learning Objectives, University of Illinois Springfield](https://www.uis.edu/colrs/foundations-course-design/assessing-learners/writing-learning-objectives) : un seul verbe mesurable par objectif.
- Anderson, L. W. et Krathwohl, D. R. (2001). *A Taxonomy for Learning, Teaching, and Assessing*. Longman.
- [Revised Bloom's Taxonomy, Iowa State University](https://www.celt.iastate.edu/teaching/effective-practice/revised-blooms-taxonomy/) : objectif = verbe + objet.
- [ISO 704:2022, Terminology work — Principles and methods (sommaire)](https://webstore.ansi.org/preview-pages/ISO/preview_ISO+704-2022.pdf) : 6.5.2, définitions circulaires.
- [Extrait d'ISO 25964-1, section 10.2](https://dl1.cuni.cz/pluginfile.php/640483/mod_book/chapter/46577/Hierarchie-ISO25964.pdf) : relations hiérarchiques.
- [Résumé du chapitre de Reigeluth (1999)](https://idtheory.sitehost.iu.edu/chapter_18_summary.html) : concepts larges avant concepts précis.
