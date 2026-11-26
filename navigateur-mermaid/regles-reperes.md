# Règles du modèle reperes.html — Repères des modules et de leurs prérequis

`reperes.html` affiche les modules d'un domaine et leurs prérequis, sous forme d'arbre. Chaque rectangle est un module (« élément » dans le .json). Il lit un fichier .json écrit selon `regles-reperes-json.md`, puis applique les règles ci-dessous. Chaque règle indique sa source entre crochets ; [Ajout] = choix propre au modèle.

## Fichiers

| Fichier | Rôle |
| --- | --- |
| `reperes.html` | Le modèle : lit le .json et dessine l'arbre. |
| `reperes.json` | Le contenu : ici, les flowcharts Mermaid. |
| `regles-reperes-json.md` | Comment écrire le .json. |
| `regles-reperes.md` | Ce fichier : ce que fait le modèle. |

Pour un autre domaine, seul le .json change.

## Chargement

- Le modèle lit `reperes.json`, placé dans le même dossier. [Ajout]
- Un autre fichier se choisit par l'adresse : `reperes.html?donnees=autre.json`. [Ajout]
- Ouvert d'un double-clic depuis le disque, le navigateur web refuse souvent de lire un fichier voisin. Le modèle propose alors de choisir le fichier, ou de le déposer sur la page. [Ajout]
- Un fichier .json déposé sur la page remplace le contenu affiché. [Ajout]
- Le titre de l'onglet reprend le champ `titre`, suivi de « repères des modules et de leurs prérequis ». [Ajout]

## Vérification

- Avant d'afficher quoi que ce soit, le modèle applique toutes les règles bloquantes de `regles-reperes-json.md`. [Ajout]
- Si une règle échoue, il n'affiche que la liste des erreurs, chacune avec l'id ou la position concernés. [Ajout]

## Arbre

- Le premier terme est en haut. Sous chaque élément, ceux qui s'appuient directement sur lui. [Ajout ; chaque élément se définit à partir de termes plus primitifs : ISO 704]
- Sous un même élément, l'ordre de gauche à droite suit l'ordre du fichier. [Ajout]
- Un élément qui s'appuie sur plusieurs termes apparaît sous chacun d'eux. [NLM, MeSH : un terme peut figurer à plusieurs places ; ISO 25964 : polyhiérarchie]
- Tout est déplié, rien ne se replie. [Ajout]
- Chaque rectangle affiche le libellé, puis une ligne d'information : « premier terme · N en découlent », « N éléments en découlent » ou « rien n'en découle ». [Ajout]

## Sélection

**Ce qui se sélectionne**

- Toucher ou cliquer un rectangle le sélectionne ; rien ne s'ouvre. [Ajout]
- Vers le haut : ses termes primitifs, jusqu'au premier terme, se sélectionnent avec lui. [Doignon et Falmagne : un état de connaissance contient tous les prérequis de ses éléments]
- Vers le bas : tout ce qui en découle se sélectionne aussi. [NLM, MeSH : explosion d'un terme]
- La sélection se propage le long de l'arbre : choisir un élément choisit son parent jusqu'à la racine ; retirer un élément retire ce qui en dépend. [Batory, 2005 ; modèles de caractéristiques : Kang et al., 1990]
- Seule la branche touchée s'allume ; les copies du même élément ailleurs restent éteintes. [Ajout]
- Plusieurs branches peuvent être sélectionnées en même temps. [Ajout]
- Écart assumé : pour maîtriser juste le nécessaire, la règle de référence ne garde que le sens vers le haut. Le sens vers le bas ajoute des éléments non nécessaires. [Ajout]

**Retirer une sélection**

- Toucher l'élément choisi le désélectionne avec sa branche. [Ajout]
- Toucher un élément sélectionné automatiquement ne fait rien. [Ajout]
- « Effacer » retire toute la sélection. [Ajout]

**Ce qui s'affiche**

- Les rectangles sélectionnés passent en noir, avec « sélectionné », « terme primitif · sélectionné », « premier terme · sélectionné » ou « en découle · sélectionné ». Les autres pâlissent. [Ajout]
- Après une sélection, le graphique se recadre pour montrer la branche, de l'élément jusqu'au premier terme, en dézoomant si besoin. [Ajout]

## Affichage

- Le graphique occupe tout l'écran, en largeur et en hauteur. [Ajout]
- Aucun titre, aucune légende, aucun contour autour du graphique. [Ajout]
- En bas à gauche, dans le graphique : + et −, puis « Effacer » quand une sélection existe. Tout petits, de taille fixe quel que soit le zoom. [Ajout]
- Thème clair ou sombre selon le réglage de l'appareil. [Ajout]

## Navigation

- Glisser déplace le graphique : au doigt sur téléphone, en cliquer-glisser à la souris sur ordinateur. Un glisser ne sélectionne rien. [Ajout]
- Sur ordinateur, la roulette zoome et dézoome autour du curseur. [Ajout]
- + et − zooment autour du centre de l'écran. [Ajout]
- Le zoom va de 10 % à 160 %. [Ajout]
- Au départ, le premier terme est centré, à 90 % sur téléphone et 100 % sur ordinateur. [Ajout]
- Sur ordinateur, les barres de défilement font 5 px, presque transparentes, et foncent à peine quand on les attrape. [Ajout]

## Mémoire

- La sélection est gardée dans le navigateur web, pour ce contenu précis. [Ajout]
- Si les éléments du fichier changent, la sélection repart à zéro. [Ajout]

## Sources

- [Falmagne et Doignon, Knowledge Spaces and Learning Spaces (arXiv)](https://arxiv.org/pdf/1511.06757) : états de connaissance, relation de prérequis.
- [NLM, MeSH : recherche et explosion](https://www.nlm.nih.gov/mesh/intro_retrieval.html) : termes plus spécifiques inclus par défaut.
- [NLM, MeSH : structure en arbres](https://www.nlm.nih.gov/mesh/intro_trees.html) : un terme peut figurer à plusieurs endroits.
- [Extrait d'ISO 25964-1, section 10.2](https://dl1.cuni.cz/pluginfile.php/640483/mod_book/chapter/46577/Hierarchie-ISO25964.pdf) : polyhiérarchie.
- [ISO 704:2022, Terminology work — Principles and methods (sommaire)](https://webstore.ansi.org/preview-pages/ISO/preview_ISO+704-2022.pdf) : définitions.
- Batory, D. (2005). [Feature Models, Grammars, and Propositional Formulas](https://www.cs.utexas.edu/ftp/predator/TR-05-14.pdf) : enfant choisi implique parent choisi.
- Kang, K. C., Cohen, S. G., Hess, J. A., Novak, W. E. et Peterson, A. S. (1990). [Feature-Oriented Domain Analysis (FODA) Feasibility Study](https://www.sei.cmu.edu/library/feature-oriented-domain-analysis-foda-feasibility-study/) (CMU/SEI-90-TR-021). Software Engineering Institute.
