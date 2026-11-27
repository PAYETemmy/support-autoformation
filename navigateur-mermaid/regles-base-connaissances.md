# Règles du modèle base-connaissances.html — Documentation d'apprentissage

`base-connaissances.html` affiche les connaissances de chaque module de « Repères des modules et de leurs prérequis », une carte par module. Il lit un fichier .json écrit selon `regles-base-connaissances-json.md`, puis applique les règles ci-dessous. Chaque règle indique sa source entre crochets ; [Consigne] = demande de l'utilisateur ; [Ajout] = choix propre au modèle.

## Fichiers

| Fichier | Rôle |
| --- | --- |
| `base-connaissances.html` | Le modèle : lit le .json et affiche la documentation d'apprentissage. |
| `base-connaissances.json` | Le contenu : ici, les flowcharts Mermaid. |
| `regles-base-connaissances-json.md` | Comment écrire le .json. |
| `regles-base-connaissances.md` | Ce fichier : ce que fait le modèle. |

Pour un autre domaine, seul le .json change.

## Nature

- « Repères des modules et de leurs prérequis » donne la structure du domaine ; cette page donne les connaissances de chaque module. [Doignon et Falmagne : structure de connaissances]
- Une documentation d'apprentissage réunit des cartes autonomes, consultées selon le besoin : la page ne se lit pas d'un bout à l'autre. [Consigne : nom « documentation d'apprentissage » ; Diátaxis : documentation orientée apprentissage]
- Chaque carte réunit les trois types de connaissances : conditionnelles (« Quand »), procédurales (la compétence, « Réussi si ») et déclaratives (les fiches). [Tardif, 1992]
- Chaque carte est une compétence, avec sa condition et son critère de réussite. [Mager ; référentiels de compétences de la formation professionnelle, RNCP]
- Chaque carte forme une unité de sens autonome : elle se comprend sans lire les autres. [OASIS DITA : topic autonome ; Horn, Information Mapping]

## Chargement

- Le modèle lit `base-connaissances.json`, placé dans le même dossier. [Ajout]
- Un autre fichier se choisit par l'adresse : `base-connaissances.html?donnees=autre.json`. [Ajout]
- Ouvert d'un double-clic depuis le disque, le navigateur web refuse souvent de lire un fichier voisin. Le modèle propose alors de choisir le fichier, ou de le déposer sur la page. [Ajout]
- Le fichier est relu à chaque ouverture : modifier le .json met la page à jour. [Ajout]

## Vérification

- Avant d'afficher quoi que ce soit, le modèle applique toutes les règles bloquantes de `regles-base-connaissances-json.md`. [Ajout]
- Si une règle échoue, il n'affiche que la liste des erreurs, chacune avec la compétence, la fiche ou le cas concernés. [Ajout]

## Sommaire

- À l'ouverture : le titre, puis le sommaire, et rien d'autre. [Consigne]
- Deux listes : « Compétences », puis « Cas complets ». [Ajout]
- Chaque liste est rangée par ordre alphabétique, sans tenir compte des accents ni des majuscules. [Consigne ; ISO 999 : classement alphabétique des index]
- Les entrées sont groupées sous leur initiale : É se range sous E. [ISO 999]
- Toucher une entrée ouvre sa carte. [Consigne]

## Carte

- Une seule carte affichée à la fois : celle choisie. [Consigne]
- Compétence : titre, « Avant, savoir », « Quand », « Réussi si », puis ses fiches dans l'ordre du fichier. [Mager : condition et critère]
- « Avant, savoir » liste les compétences prérequises directes ; chacune est un lien vers sa carte. [Gagné : hiérarchies d'apprentissage]
- Fiche : définition, caractéristiques, tableau s'il existe, un exemple avec son code, les non-exemples. [Frayer ; un exemple par fiche : Consigne]
- Une fiche citée par plusieurs compétences est affichée en entier dans chacune de leurs cartes : jamais de renvoi « vu plus haut ». [OASIS DITA : réutilisation par référence, conref]
- Cas complet : titre, domaine, contexte, objectif, code, puis « Fiches utilisées ». Chaque fiche est un lien vers la première compétence, dans l'ordre du fichier, qui la cite. [Roegiers : situation d'intégration]

## Affichage

- Fond blanc, texte sombre, liens bleus, police Inter. Mêmes couleurs que `reperes.html`. [Ajout]
- Le code est en police à chasse fixe, sans retour à la ligne automatique : une ligne trop longue défile à l'horizontale dans son cadre. [Ajout]
- Dans les textes, ce qui est entre accents graves s'affiche comme du code. [Ajout]
- Sur téléphone, les intitulés passent au-dessus de leur valeur. [Ajout]
- Chaque entrée du sommaire mesure au moins 44 px de haut. [Apple, Human Interface Guidelines : cible tactile de 44 points]
- Aucun bouton en dehors de « ← Sommaire ». [Consigne]

## Navigation

- Sur une carte, « ← Sommaire » en haut ramène au sommaire. [Ajout]
- Chaque carte a sa propre adresse (`#id`). Le retour arrière du navigateur web ou de l'iPhone revient à la carte précédente. [Ajout]
- Ouvrir une carte affiche son haut. [Ajout]
- Le titre de l'onglet reprend la carte ouverte. [Ajout]

## Sources

- Tardif, J. (1992). *Pour un enseignement stratégique : l'apport de la psychologie cognitive*. Éditions Logiques : connaissances déclaratives, procédurales et conditionnelles.
- Doignon, J.-P. et Falmagne, J.-C. (1999). *Knowledge Spaces*. Springer : structure de connaissances.
- Procida, D. *Diátaxis, a systematic approach to technical documentation* : tutoriel, guide pratique, référence, explication. https://diataxis.fr/
- OASIS. *Darwin Information Typing Architecture (DITA) Version 1.3* : topics autonomes, réutilisation par conref.
- Horn, R. E. (1989). *Mapping Hypertext*. The Lexington Institute : découpage en blocs autonomes (Information Mapping).
- ISO 999:1996. *Information et documentation — Principes directeurs pour l'élaboration des index*.
- Mager, R. F. (1997). *Preparing Instructional Objectives* (3e édition) : performance, condition, critère.
- France Compétences : référentiels d'activités, de compétences et d'évaluation des certifications du RNCP.
- Gagné, R. M. (1968). Learning hierarchies. *Educational Psychologist*, 6, 1–9.
- Frayer, D. A., Frederick, W. C. et Klausmeier, H. J. (1969). *A Schema for Testing the Level of Concept Mastery*. Wisconsin Research and Development Center for Cognitive Learning.
- Roegiers, X. (2000). *Une pédagogie de l'intégration*. De Boeck : situations d'intégration.
- Apple. *Human Interface Guidelines*, Accessibility : taille minimale des cibles tactiles.
