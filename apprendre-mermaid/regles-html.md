# Règles de la page index.html

`index.html` est un site d'apprentissage rapide : une notion à la fois, sa fiche de Frayer, puis trois questions sans la fiche. Il lit un fichier .json écrit selon `regles-json.md`, puis applique les règles ci-dessous.

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

- Le titre, une phrase qui dit comment on apprend, puis le bouton de la prochaine notion à faire. [Ajout]
- Le bouton « Réviser » n'apparaît que s'il y a des notions à réviser aujourd'hui. [Ajout]
- Les notions sont rangées par niveau, dans l'ordre du fichier. [Gagné : prérequis d'abord ; Reigeluth : épitomé]
- Chaque niveau est dessiné comme un flowchart vertical : une forme stade par notion, une flèche vers la suivante. [Ajout : le site parle la langue de son sujet]
- L'état de chaque notion se lit sur sa forme : contour plein = à faire ; pointillé = à revoir ; remplie = acquise. Une légende le rappelle. [Ajout]
- En bas : les cas complets. [Sweller et Cooper, 1985 : exemples travaillés]

## Fiche d'une notion

- La fiche de Frayer : le nom dans une forme stade, entouré des quatre cases Définition, Caractéristiques, Exemples et Non-exemples. [Frayer, Frederick et Klausmeier, 1969]
- Sur ordinateur, les 4 cases forment une grille de 2 sur 2, le nom au croisement. Sur téléphone, elles s'empilent, le nom en tête. [Ajout]
- Chaque non-exemple montre l'écriture fautive, puis la raison en rouge. [Tennyson et Boutwell, 1974 : la caractéristique qui manque]
- Sous la fiche : les 2 exemples en entier, le code à côté de son dessin. [Mayer : principe multimédia et contiguïté spatiale]
- Le tableau de référence, s'il existe, est replié sous les exemples. [Mayer : cohérence, rien de superflu à l'écran]
- En haut : « ← Parcours » et la place de la notion dans son niveau. [Ajout]

## Questions

- Trois questions, tirées de la fiche : [Frayer et al., 1969 : tester la définition, les caractéristiques et les non-exemples]
    1. Quelle notion a cette définition ? 4 réponses.
    2. Laquelle est une caractéristique de la notion ? 3 réponses.
    3. Pourquoi ce non-exemple n'en est pas un ? 3 réponses.
- Pendant les questions, la fiche est cachée : on répond de mémoire. [Roediger et Karpicke, 2006 : effet de test]
- Les mauvaises réponses viennent des autres notions du même niveau. [Merrill et Tennyson, 1977 : concepts coordonnés]
- Une mauvaise réponse qui cite le terme de la notion, ou une raison vague (« n'existe pas »), n'est jamais proposée. [Ajout : pas de piège ambigu]
- À chaque essai, la caractéristique, le non-exemple et l'ordre des réponses sont tirés au hasard. [Ajout]
- Après chaque réponse : juste ou faux, la bonne réponse, et la notion d'où vient la mauvaise. [Shute, 2008 : rétroaction élaborée]
- 3 bonnes réponses sur 3 : notion acquise. Sinon : à revoir, avec le bouton « Revoir la fiche ». [Bloom, 1968 : apprentissage de maîtrise]

## Révision

- Une notion acquise revient après 1 jour, puis 3, 7, 15 et 30 jours. [Leitner, 1972 : boîtes ; Cepeda et al., 2006 : révisions espacées ; Ajout : les intervalles]
- La révision : refaire la fiche de mémoire devant les 4 cases vides, puis comparer avec la vraie. [Consigne : « le lendemain, refaire la fiche de mémoire, puis comparer »]
- « Je l'avais » : la notion passe à l'intervalle suivant. « Il me manquait quelque chose » : elle revient demain. [Leitner]

## Progression

- Gardée dans le navigateur web de l'apprenant, pour ce titre de site. Rien n'est envoyé. [Ajout]
- Rangée par `id` de notion. [Ajout]
- Si le navigateur web refuse de la garder, le site fonctionne quand même, sans mémoire. [Ajout]

## Affichage

- Fond blanc, texte bleu nuit `#17203A`, gris `#5A6478` pour le secondaire. [Ajout]
- Accent violet `#5B3FA8`, formes stade en `#ECECFF` bordées de `#9370DB` : les couleurs par défaut des nœuds Mermaid. [Ajout]
- Vert `#1E7A4E` = juste, rouge `#B3261E` = faux et non-exemple. [Ajout]
- Police IBM Plex Sans pour le texte, IBM Plex Mono pour le code seulement. [Ajout]
- Lignes de texte de 66 caractères au plus. [Bringhurst : 45 à 75 caractères]
- Le code garde ses retours à la ligne ; une ligne trop longue défile dans son cadre. [Ajout]
- Dans les textes, ce qui est entre accents graves s'affiche comme du code. [Ajout]
- Un seul mouvement : l'apparition de chaque question et du résultat. Supprimé si l'appareil demande moins d'animations. [Ajout ; WCAG 2.2, 2.3.3]

## Accès

- Toute cible tactile mesure au moins 44 px de haut ; boutons et réponses, 48 px. [Apple, Human Interface Guidelines : 44 points minimum]
- Contour visible autour de l'élément actif au clavier. [WCAG 2.2, 2.4.7]
- Contrastes du texte d'au moins 4,5:1. [WCAG 2.2, 1.4.3]
- Chaque notion du parcours annonce son état aux lecteurs d'écran. [Ajout]
- À l'ouverture d'une fiche, d'une question, d'un résultat ou d'une révision, le focus va sur son titre. [Ajout]

## Dessins des exemples

- Mermaid n'est chargé qu'à l'ouverture d'une fiche ou d'un cas. [Ajout]
- Chaque exemple est dessiné à côté de son code. S'il ne peut pas l'être, un message le dit et le code reste. [Ajout]
- Mode de sécurité `strict` : les clics des exemples n'exécutent aucun script. [Documentation Mermaid : securityLevel]

## Sources

- Frayer, D. A., Frederick, W. C. et Klausmeier, H. J. (1969). *A Schema for Testing the Level of Concept Mastery*. Wisconsin Research and Development Center for Cognitive Learning.
- Merrill, M. D. et Tennyson, R. D. (1977). *Teaching Concepts: An Instructional Design Guide*. Educational Technology Publications.
- Tennyson, R. D. et Boutwell, R. C. (1974). Methodology for the sequencing of instances in classroom concept teaching.
- Gagné, R. M. (1968). Learning hierarchies. *Educational Psychologist*, 6, 1–9.
- Reigeluth, C. M. et Stein, F. S. (1983). The elaboration theory of instruction.
- Sweller, J. et Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction*, 2(1), 59–89.
- Roediger, H. L. et Karpicke, J. D. (2006). Test-enhanced learning. *Psychological Science*, 17(3), 249–255.
- Shute, V. J. (2008). Focus on formative feedback. *Review of Educational Research*, 78(1), 153–189.
- Bloom, B. S. (1968). Learning for mastery. *Evaluation Comment*, 1(2).
- Leitner, S. (1972). *So lernt man lernen*. Herder.
- Cepeda, N. J. et al. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3), 354–380.
- Mayer, R. E. (2009). *Multimedia Learning* (2e édition). Cambridge University Press.
- Bringhurst, R. *The Elements of Typographic Style* : longueur de ligne.
- W3C. *Web Content Accessibility Guidelines (WCAG) 2.2*.
- Apple. *Human Interface Guidelines* : taille des cibles tactiles.
- [Documentation Mermaid](https://mermaid.js.org/).
