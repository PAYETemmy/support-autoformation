# Règles de la page index.html

`index.html` est un site d'apprentissage rapide : une notion à la fois, avec sa fiche de Frayer, puis la fiche refaite de mémoire le lendemain. Il lit un fichier .json écrit selon `regles-json.md`, puis applique les règles ci-dessous.

Chaque règle indique sa source entre crochets : [Consigne] = demande de l'utilisateur ; [Ajout] = choix propre au modèle ; sinon, la référence.

## Fichiers

| Fichier | Rôle |
| --- | --- |
| `index.html` | Le site : lit le .json, vérifie, affiche. |
| `contenu.json` | Le contenu : ici, les flowcharts Mermaid. |
| `regles-json.md` | Comment remplir le .json. |
| `regles-html.md` | Ce fichier : ce que fait la page. |
| `mermaid.min.js` | Copie locale de Mermaid, qui dessine les exemples. |
| `mermaid-LICENSE.txt` | Licence de Mermaid (MIT), à garder avec la copie. |

Pour un autre sujet, seul le .json change. Pour un autre langage que Mermaid, le dessin des exemples change aussi.

## Chargement

- La page lit `contenu.json`, dans le même dossier. Un autre fichier se choisit par l'adresse : `index.html?donnees=autre.json`. [Ajout]
- Ouverte depuis le disque, la page propose de choisir le fichier ou de le déposer. [Ajout]
- Le fichier est relu à chaque ouverture. [Ajout]

## Vérification

- Avant d'afficher quoi que ce soit, la page applique toutes les règles bloquantes de `regles-json.md`. [Ajout]
- Si une règle échoue, elle n'affiche que la liste des erreurs, chacune avec la notion ou le cas concerné. [Ajout]

## Accueil : le parcours

- Le titre, une phrase qui dit comment on apprend, puis le bouton de la prochaine notion jamais ouverte. [Ajout]
- Le bouton « Réviser » n'apparaît que s'il y a des notions à réviser aujourd'hui. [Ajout]
- Les notions sont rangées par niveau, dans l'ordre du fichier. [Gagné : prérequis d'abord ; Reigeluth : épitomé]
- Chaque niveau est dessiné comme un flowchart vertical, centré dans la page : une forme stade par notion, une flèche vers la suivante. [Ajout : le site parle la langue de son sujet]
- L'état de chaque notion se lit sur sa forme : contour plein = à faire (jamais ouverte) ; pointillé = en cours (ouverte, pas encore refaite de mémoire, ou refaite avec un manque) ; remplie = acquise (refaite de mémoire sans manque). Une légende le rappelle. [Ajout]
- En bas : les cas complets. [Sweller et Cooper, 1985 : exemples travaillés]

## Fiche d'une notion

- La fiche de Frayer : le nom dans une forme stade, entouré des quatre cases Définition, Caractéristiques, Exemples et Non-exemples. [Frayer, Frederick et Klausmeier, 1969]
- Sur tous les écrans, les 4 cases s'empilent, le nom en tête. [Consigne]
- Chaque non-exemple montre l'écriture fautive, puis la raison en rouge. [Tennyson et Boutwell, 1974 : la caractéristique qui manque]
- Sous la fiche : les 2 exemples en entier, le code puis son dessin juste en dessous. [Mayer : principe multimédia et contiguïté spatiale]
- Le tableau de référence, s'il existe, est replié sous les exemples. [Mayer : cohérence, rien de superflu à l'écran]
- En haut : « ← Parcours » et la place de la notion dans son niveau. [Ajout]

## Révision

- Ouvrir une fiche pour la première fois la programme pour le lendemain. Elle revient ensuite après 3, 7, 15 et 30 jours. [Leitner, 1972 : boîtes ; Cepeda et al., 2006 : révisions espacées ; Ajout : les intervalles]
- La révision : refaire la fiche de mémoire devant les 4 cases vides, puis comparer avec la vraie. [Consigne : « le lendemain, refaire la fiche de mémoire, puis comparer »]
- « Je l'avais » : la notion est acquise et passe à l'intervalle suivant. « Il me manquait quelque chose » : elle reste en cours et revient demain. [Leitner ; Roediger et Karpicke, 2006 : se rappeler de mémoire fixe mieux que relire]

## Progression

- Gardée dans le navigateur web de l'apprenant, pour ce titre de site. Rien n'est envoyé. [Ajout]
- Rangée par `id` de notion. [Ajout]
- Si le navigateur web refuse de la garder, le site fonctionne quand même, sans mémoire. [Ajout]

## Affichage

- Tout le site tient dans une colonne centrée de 804 px de contenu au plus : le rendu de l'iPhone à l'horizontale, sur tous les écrans. [Consigne]
- Fond blanc, texte bleu nuit `#17203A`, gris `#5A6478` pour le secondaire. [Ajout]
- Accent violet `#5B3FA8`, formes stade en `#ECECFF` bordées de `#9370DB` : les couleurs par défaut des nœuds Mermaid. [Ajout]
- Vert `#1E7A4E` = juste, rouge `#B3261E` = faux et non-exemple. [Ajout]
- Police IBM Plex Sans pour le texte, IBM Plex Mono pour le code seulement. [Ajout]
- Lignes de texte de 66 caractères au plus. [Bringhurst : 45 à 75 caractères]
- Le code garde ses retours à la ligne ; une ligne trop longue défile dans son cadre. [Ajout]
- Dans les textes, ce qui est entre accents graves s'affiche comme du code. [Ajout]
- Aucune animation. [Ajout]

## Accès

- Toute cible tactile mesure au moins 44 px de haut ; les boutons, 48 px. [Apple, Human Interface Guidelines : 44 points minimum]
- Contour visible autour de l'élément actif au clavier. [WCAG 2.2, 2.4.7]
- Contrastes du texte d'au moins 4,5:1. [WCAG 2.2, 1.4.3]
- Chaque notion du parcours annonce son état aux lecteurs d'écran. [Ajout]
- À l'ouverture d'une fiche ou d'une révision, le focus va sur son titre. [Ajout]

## Dessins des exemples

- Mermaid n'est chargé qu'à l'ouverture d'une fiche ou d'un cas. [Ajout]
- Chaque exemple est dessiné à côté de son code. S'il ne peut pas l'être, un message le dit et le code reste. [Ajout]
- Mode de sécurité `strict` : les clics des exemples n'exécutent aucun script. [Documentation Mermaid : securityLevel]

## Sources

- Frayer, D. A., Frederick, W. C. et Klausmeier, H. J. (1969). *A Schema for Testing the Level of Concept Mastery*. Wisconsin Research and Development Center for Cognitive Learning.
- Tennyson, R. D. et Boutwell, R. C. (1974). Methodology for the sequencing of instances in classroom concept teaching.
- Gagné, R. M. (1968). Learning hierarchies. *Educational Psychologist*, 6, 1–9.
- Reigeluth, C. M. et Stein, F. S. (1983). The elaboration theory of instruction.
- Sweller, J. et Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction*, 2(1), 59–89.
- Roediger, H. L. et Karpicke, J. D. (2006). Test-enhanced learning. *Psychological Science*, 17(3), 249–255.
- Leitner, S. (1972). *So lernt man lernen*. Herder.
- Cepeda, N. J. et al. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3), 354–380.
- Mayer, R. E. (2009). *Multimedia Learning* (2e édition). Cambridge University Press.
- Bringhurst, R. *The Elements of Typographic Style* : longueur de ligne.
- W3C. *Web Content Accessibility Guidelines (WCAG) 2.2*.
- Apple. *Human Interface Guidelines* : taille des cibles tactiles.
- [Documentation Mermaid](https://mermaid.js.org/).
