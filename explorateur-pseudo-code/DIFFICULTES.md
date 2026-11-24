# Difficultés — circuit de résolution

On traite les difficultés **une par une**, ensemble, jusqu'à ce qu'elles soient résolues.

## Méthode
Elle s'appuie sur trois méthodes reconnues :
- **Roue de Deming (PDCA)** : planifier, faire, vérifier, ajuster.
- **5 Pourquoi** (Toyota) : remonter à la cause en demandant « pourquoi ? » plusieurs fois.
- **Kanban** : une seule difficulté *En cours* à la fois.

Pour chaque difficulté :
1. **Contexte** : où et quand ça arrive.
2. **Difficulté** : ce que tu constates, avec tes mots.
3. **Cause** : trouvée avec les 5 Pourquoi.
4. **Solution** : ce qu'on met en place, avec la version.
5. **Vérification** : tu testes. Si c'est résolu, on passe à la suivante ; sinon, retour à l'étape 3.

**Statuts** : À traiter → En cours → À vérifier → Résolu

## Tableau de suivi
| N° | Contexte | Difficulté | Statut | Version |
|---|---|---|---|---|
| D1 | Réviser un élément du parcours | On perd le fil du parcours conseillé | Résolu | 9.7 |
| D2 | Carte d'entraînement | Pas d'endroit pour écrire | Résolu | 9.8 → 10.2 |
| D3 | Page « Apprendre » | Concepts, règles et procédures mélangés | Résolu | 10.0 → 10.1 |
| D4 | Apprendre les concepts | C'est barbant et lent | À vérifier | 10.4 → 11.1 |
| D5 | Mots-clés des termes primitifs | Mots-clés illogiques (Constante pour Exécution) | Résolu | 10.7 |
| D6 | Mots-clés d'une définition | Les mots-clés ne suffisent pas à deviner la phrase | À vérifier | 11.1 |
| D7 | Utiliser l'app | « Je n'arrive à rien, l'app ne marche pas » | En cours | — |

## Fiches

### D1 — Perdre le fil du parcours · Résolu (9.7)
- **Contexte** : en révisant un élément du parcours conseillé.
- **Difficulté** : l'entraînement s'ouvrait dans la page, et on perdait sa place dans le parcours.
- **Cause** : sur téléphone, l'entraînement était placé sous le parcours, et y aller faisait défiler la page.
- **Solution** : l'entraînement s'ouvre dans une fenêtre fixe, qui laisse le parcours en place ; « Acquis » ferme la fenêtre (9.9).
- **Vérification** : faite.

### D2 — Écrire ses propres définitions · Résolu (9.8 → 10.2)
- **Contexte** : carte d'entraînement.
- **Difficulté** : il n'y avait aucun endroit pour écrire.
- **Solution** : une zone de notes (9.8), devenue « Ma définition » toujours visible (10.2).
- **Vérification** : faite.

### D3 — Tout mélangé · Résolu (10.0 → 10.1)
- **Contexte** : page « Apprendre ».
- **Difficulté** : concepts, règles et procédures étaient dans un seul parcours.
- **Solution** : 3 espaces, Concepts · Règles · Procédures, présentés en liste simple (10.1).
- **Vérification** : faite.

### D4 — Apprendre les concepts est barbant · À vérifier (10.4 → 11.1)
- **Contexte** : cartes des concepts.
- **Difficulté** : lire une carte puis s'auto-noter, c'est passif et lent.
- **Cause** : on relit sans rien produire. Or produire soi-même sa réponse fait mieux retenir (effet de génération).
- **Solution** : « Ma définition » guidée par des mots-clés qui passent au vert ; toute la carte affichée d'emblée (10.8).
- **Vérification** : à faire, sur plusieurs séances.

### D5 — Mots-clés illogiques pour les termes primitifs · Résolu (10.7)
- **Difficulté** : « Exécution » avait comme mots-clés Terminaison · Trace d'exécution · Constante.
- **Cause** : les mots étaient choisis automatiquement, parmi des concepts vus en fin de parcours.
- **Solution** : des mots-clés choisis à la main dans le JSON (champ `motsImposes`).

### D6 — Les mots-clés ne suffisent pas à deviner la définition · À vérifier (11.1)
- **Difficulté** : il manquait des verbes (« fixe ») et des mots de liaison (« qui », « et »).
- **Cause** : les mots-clés gardaient surtout les noms. Or ce sont les verbes et les mots de liaison qui disent comment la phrase s'enchaîne.
- **Solution** : des groupes de sens (mot plein + mot de liaison), dans l'ordre de la définition. Règle écrite dans `REGLES_donnees_json.md` (11.1).
- **Vérification** : à faire. Les mots-clés suffisent-ils, seuls, à retrouver la phrase ?

### D7 — « L'app ne marche pas » · En cours
- **Contexte** : 24/11, après la mise en ligne de la 11.1.
- **Difficulté** : « je n'arrive à rien, l'app ne marche pas ».
- **Cause** : à trouver. En local, les tests de la 11.1 réussissent : chargement des 507 éléments, mots-clés qui passent au vert, passage depuis les anciennes versions sans perte.
  - Pistes : page ouverte depuis un fichier téléchargé au lieu du lien en ligne, ancienne version gardée en cache, ou blocage précis non encore décrit.
- **Prochaine étape** : une capture d'écran et le geste exact au moment du blocage (ouvrir l'app, toucher Réviser, écrire…).
