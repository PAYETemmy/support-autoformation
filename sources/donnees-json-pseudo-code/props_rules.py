from lib import PR, R, X, chain

D_PC, D_SUP = "du pseudo-code", "du pseudo-code de ce support"
# ---------- Propriétés (dans l’ordre du parcours) ----------
PROPS = []
def pr(id, *a, **k): PR(id, *a, **k); PROPS.append("pc-pr-" + id)
pr("pas-norme", "Pas de norme unique", "Caractérise", ["pseudo-code"], "de l’algorithmique", "n’a pas",
   "de norme unique : chaque support fixe ses mots-clés et ses symboles, et doit les annoncer", ["LAF"])
pr("une-valeur", "Une valeur à la fois", "Caractérise", ["variable"], D_PC, "ne contient",
   "qu’une valeur à la fois ; pour une liste, cette valeur unique est la liste entière", ["ED_AFF"])
pr("bool-deux", "Deux valeurs seulement", "Définit", ["booleen"], "de la logique", "n’a que", "deux valeurs : vrai et faux", ["LAF"])
pr("entier-reel", "Entiers et réels compatibles", "Met en relation", ["entier", "reel"], "des nombres", "sont compatibles dans un sens :",
   "une valeur entière peut être rangée dans une variable réelle (3 devient 3.0), mais pas l’inverse sans arrondir", ["AJOUT"])
pr("constante", "Valeur fixe", "Définit", ["constante"], D_PC, "garde", "la même valeur du début à la fin de l’exécution : aucune affectation ne la change", ["AJOUT"])
pr("chaine-liste", "Texte lu comme une liste", "Caractérise", ["chaine"], D_SUP, "se lit",
   "comme une liste de caractères : ch[0] est le premier, Longueur(ch) donne leur nombre", ["AJOUT"])
pr("fleche", "Écriture de la flèche", "Caractérise", ["affectation"], D_SUP, "s’écrit",
   "avec la flèche ← (tapée <- au clavier) et se lit « prend la valeur »", ["ED_AFF", "CONV"])
pr("euclide", "Égalité de la division euclidienne", "Caractérise", ["div-mod"], "des entiers positifs", "vérifient",
   "a = b × (a div b) + (a mod b), avec 0 ≤ a mod b < b", ["CONV"], qualifier="de a par b (b > 0)")
pr("comp-bool", "Résultat d’une comparaison", "Caractérise", ["op-comp"], D_PC, "donne toujours", "un booléen : vrai ou faux", ["ED_CTRL"])
pr("tables", "Tables de et, ou, non", "Caractérise", ["op-log"], "de la logique", "suivent",
   "ces tables : a et b est vrai seulement si a et b sont vrais ; a ou b est faux seulement si a et b sont faux ; non a vaut l’inverse de a", ["ED_CTRL"])
pr("pour-tours", "Nombre de tours d’un Pour", "Caractérise", ["pour"], D_SUP, "fait",
   "exactement b - a + 1 tours si a ≤ b, et aucun tour si a > b", ["ED_BCL"], qualifier="de i de a à b, avec un pas de 1,")
pr("tq-zero", "Zéro tour possible", "Caractérise", ["tantque"], D_PC, "peut faire",
   "zéro tour : si la condition est fausse au départ, le bloc ne s’exécute jamais", ["ED_BCL"])
pr("rep-un", "Au moins un tour", "Caractérise", ["repeter"], D_PC, "fait toujours",
   "au moins un tour, car la condition n’est testée qu’après le bloc", ["ED_BCL"])
pr("indices", "Indices de 0 à N - 1", "Caractérise", ["liste"], D_SUP, "a des indices",
   "allant de 0 à N - 1, comme en Python et en C++", ["CONV"], qualifier="de longueur N")
pr("meme-type", "Éléments du même type", "Définit", ["liste"], D_PC, "range",
   "des éléments tous du même type, dans un ordre fixé", ["CONV"])
pr("dicho", "Recherche par moitiés", "Caractérise", ["liste-triee"], D_PC, "permet",
   "une recherche par dichotomie : chaque comparaison élimine la moitié des éléments restants", ["NSI_ALGO"])
pr("copie", "Copie de l’argument", "Caractérise", ["parametre"], D_SUP, "reçoit",
   "une copie de l’argument : le modifier ne change pas la variable de l’appelant", ["CONV"],
   qualifier="de type entier, réel, booléen, caractère ou chaîne")
pr("partage", "Liste partagée", "Caractérise", ["liste"], D_SUP, "est partagée",
   "avec lui : s’il modifie ses éléments, l’appelant voit les modifications, comme en Python", ["CONV"],
   qualifier="passée en argument à un sous-programme")
pr("locale", "Durée de vie limitée", "Caractérise", ["locale"], D_PC, "n’existe",
   "que pendant l’exécution du sous-programme où elle est déclarée", ["CONV"])
pr("recursion", "Se rapprocher du cas de base", "Caractérise", ["recursive"], D_PC, "doit avoir",
   "au moins un cas de base, et chaque appel doit s’en rapprocher, sinon les appels ne s’arrêtent pas", ["NSI_REC"])
pr("tests", "Tester n’est pas prouver", "Caractérise", ["jeu-tests"], "de la mise au point", "ne prouve pas",
   "la correction : un test réussi montre seulement que ce cas-là fonctionne", ["NSI_LP"])
pr("invariant", "De l’invariant au résultat", "Caractérise", ["invariant"], "de la preuve d’algorithmes", "donne",
   "la postcondition : c’est ainsi qu’on prouve qu’une boucle calcule le bon résultat", ["NSI_ALGO"],
   qualifier="combiné à la condition de sortie de la boucle,")
pr("variant", "Un entier qui diminue s’arrête", "Caractérise", ["variant"], "de la preuve d’algorithmes", "garantit",
   "la terminaison : un entier positif qui diminue strictement à chaque tour ne peut pas diminuer indéfiniment", ["NSI_ALGO"])
pr("ordre-couts", "Classement des coûts", "Met en relation", ["cout-log", "cout-lineaire", "cout-quadratique"], "des grandes données", "se classent ainsi :",
   "logarithmique < linéaire < quadratique ; pour n = 1 000, environ 10, 1 000 et 1 000 000 opérations", ["NSI_ALGO"])
chain(PROPS)

# ---------- Règles (dans l’ordre du parcours) ----------
RULES = []
def r(id, *a, **k): R(id, *a, **k); RULES.append("pc-r-" + id)
X_EXEC, X_ECR = "de l’exécution d’un algorithme", "de l’écriture d’un algorithme en pseudo-code"
# 1. Structure
r("sequentiel", "Exécution de haut en bas", "D", X_EXEC, "aucune structure de contrôle n’intervient",
  "les instructions s’exécutent une par une, de haut en bas, chacune après la fin de la précédente", ["sequence", "instruction"], ["ED_INIT"])
r("structure", "Plan d’un algorithme", "A", X_ECR, "on écrit un algorithme complet",
  "écrire dans l’ordre : Algorithme Nom, la section Variables avec les déclarations, puis les instructions entre Début et Fin", ["algorithme", "declaration", "bloc"], ["LAF", "CONV"])
r("declarer", "Déclarer avant d’utiliser", "A", X_ECR, "une variable sert dans l’algorithme",
  "la déclarer dans la section Variables, avec son type, avant Début", ["declaration", "variable", "type"], ["LAF", "CONV"])
r("nommer", "Bien nommer", "A", X_ECR, "on choisit le nom d’une variable",
  "prendre un nom sans espace ni accent, qui commence par une lettre, qui dit ce que la variable contient et qui n’est pas un mot-clé : somme, nbNotes",
  ["variable", "nom", "mot-cle"], ["CONV"])
r("indenter", "Décaler et fermer les blocs", "A", X_ECR, "des instructions font partie d’un bloc (après Début, Alors, Sinon, Faire, Répéter)",
  "les décaler vers la droite d’un même retrait, et fermer le bloc par son mot-clé de fin (Fin, FinSi, FinPour, FinTantQue, Jusqu’à)", ["indentation", "bloc"], ["ED_CTRL", "CONV"])
r("commenter", "Commenter le pourquoi", "A", X_ECR, "une ligne ou une étape n’est pas évidente",
  "ajouter un commentaire après // qui explique pourquoi, sans répéter ce que dit l’instruction", ["commentaire"], ["CONV"])
# 2. Données et calculs
r("type-fixe", "Un type pour toute l’exécution", "D", X_EXEC, "une variable est déclarée avec un type",
  "elle ne peut contenir que des valeurs de ce type pendant toute l’exécution", ["type", "variable"], ["LAF"],
  exception="une valeur entière peut être rangée dans une variable réelle : elle devient le réel correspondant (3 devient 3.0)")
r("choisir-type", "Choisir le type", "A", X_ECR, "on déclare une variable",
  "choisir entier pour compter, réel pour mesurer, booléen pour oui ou non, caractère pour un seul symbole, chaîne pour un texte",
  ["type", "entier", "reel", "booleen", "caractere", "chaine"], ["LAF"])
r("division", "Trois divisions", "D", "du calcul sur des entiers positifs", "on divise un entier positif a par un entier b > 0",
  "a / b donne un réel (7 / 2 vaut 3.5), a div b le quotient entier (7 div 2 vaut 3) et a mod b le reste (7 mod 2 vaut 1)",
  ["op-arith", "div-mod", "entier", "reel"], ["CONV"])
r("parite", "Tester la parité", "A", "du calcul sur des entiers", "il faut savoir si un entier n est pair",
  "tester n mod 2 = 0 : vrai si n est pair, faux s’il est impair", ["div-mod", "condition"], ["CONV"])
r("priorite", "Priorité des opérateurs", "D", "du calcul d’une expression", "une expression contient plusieurs opérateurs arithmétiques sans parenthèses",
  "*, /, div et mod sont calculés avant + et -, et de gauche à droite à priorité égale ; les parenthèses passent avant tout", ["expression", "op-arith"], ["CONV"])
r("priorite-log", "Priorité de non, et, ou", "D", "du calcul d’une condition", "une condition contient plusieurs opérateurs logiques sans parenthèses",
  "non est calculé d’abord, puis et, puis ou ; des parenthèses lèvent toute ambiguïté", ["op-log", "condition"], ["ED_CTRL"])
r("egal-fleche", "Ne pas confondre = et ←", "A", X_ECR, "on hésite entre = et ←",
  "écrire ← pour ranger une valeur dans une variable, et = seulement pour comparer deux valeurs dans une condition", ["affectation", "op-comp"], ["ED_AFF", "CONV"])
r("intervalle", "Tester un intervalle", "A", X_ECR, "il faut tester qu’une valeur x est comprise entre a et b",
  "écrire x >= a et x <= b, avec deux comparaisons reliées par et (et non a <= x <= b)", ["op-log", "condition", "op-comp"], ["ED_CTRL"])
r("concat", "Mettre bout à bout", "D", "du calcul sur des chaînes", "on applique + à deux chaînes",
  "on obtient une nouvelle chaîne : la première suivie de la seconde, sans espace ajouté", ["concatenation", "chaine"], ["AJOUT"])
# 3. Affectation, entrées, sorties
r("affecter", "Effet d’une affectation", "D", X_EXEC, "x ← e s’exécute",
  "e est d’abord calculée avec les valeurs actuelles des variables, puis x prend ce résultat ; l’ancienne valeur de x est perdue",
  ["affectation", "variable", "expression"], ["ED_AFF"])
r("gauche", "Une variable à gauche", "D", X_ECR, "on écrit une affectation",
  "à gauche de ← il y a toujours une seule variable, et à droite une expression : 5 ← x n’a pas de sens", ["affectation", "variable"], ["ED_AFF"])
r("initialiser", "Donner une valeur de départ", "A", X_ECR, "une variable va être utilisée dans un calcul ou une condition",
  "lui donner d’abord une valeur, par une affectation (somme ← 0) ou par Lire", ["variable", "accumulateur", "compteur"], ["ED_AFF"])
r("lire", "Effet de Lire", "D", X_EXEC, "Lire x s’exécute",
  "l’algorithme attend que l’utilisateur tape une valeur, puis la range dans x ; l’ancienne valeur de x est perdue", ["lecture", "variable", "entree"], ["ED_ES"])
r("annoncer", "Annoncer avant de lire", "A", X_ECR, "on demande une valeur à l’utilisateur",
  "écrire d’abord un message qui dit quoi taper : Écrire \"Ton âge ?\" puis Lire age", ["lecture", "ecriture", "utilisateur"], ["CONV"])
r("ecrire", "Effet d’Écrire", "D", X_EXEC, "Écrire suivi d’éléments séparés par des virgules s’exécute",
  "chaque élément s’affiche à la suite : les textes entre guillemets tels quels, les variables et les expressions par leur valeur", ["ecriture", "sortie"], ["ED_ES", "CONV"])
# 4. Alternatives
r("si", "Effet de Si … Sinon", "D", X_EXEC, "Si condition Alors bloc1 Sinon bloc2 FinSi s’exécute",
  "la condition est calculée une fois : si elle vaut vrai, seul bloc1 s’exécute, sinon seul bloc2 ; l’exécution reprend après FinSi", ["alternative", "condition"], ["ED_CTRL"])
r("si-sans-sinon", "Si sans Sinon", "D", X_EXEC, "un Si n’a pas de Sinon et sa condition vaut faux",
  "aucune instruction du Si ne s’exécute : l’exécution passe directement après FinSi", ["alternative"], ["ED_CTRL"])
r("cas-multiples", "Plus de deux cas", "A", X_ECR, "il faut distinguer plus de deux cas qui s’excluent (mentions, tranches de prix)",
  "imbriquer des Si dans les Sinon, en testant les cas dans l’ordre, du plus restrictif au plus large", ["si-imbrique", "alternative"], ["ED_CTRL"])
r("selon", "Effet de Selon", "D", X_EXEC, "Selon x Faire s’exécute",
  "seul le bloc du Cas égal à la valeur de x s’exécute ; si aucun Cas ne correspond, c’est le bloc Autrement, s’il existe", ["selon"], ["CONV"])
r("choisir-selon", "Remplacer des Si par un Selon", "A", X_ECR, "plusieurs Si successifs comparent la même variable à des valeurs précises",
  "les remplacer par un seul Selon sur cette variable", ["selon", "alternative"], ["CONV"],
  exception="Selon ne teste que l’égalité : pour des intervalles (note >= 16), il faut garder des Si")
# 5. Boucles
r("pour", "Effet d’un Pour", "D", X_EXEC, "Pour i de a à b Faire s’exécute, avec a ≤ b et un pas de 1",
  "i prend la valeur a, le bloc s’exécute, i augmente de 1, et ainsi de suite jusqu’au tour où i vaut b, inclus", ["pour", "compteur", "iteration"], ["ED_BCL"])
r("pas-negatif", "Compter à rebours", "D", X_EXEC, "Pour i de a à b pas p Faire s’exécute avec un pas p négatif et a ≥ b",
  "i diminue de -p à chaque tour, et la boucle tourne tant que i ≥ b", ["pas", "pour"], ["CONV"])
r("compteur-intouchable", "Laisser le compteur", "A", X_ECR, "on écrit le bloc d’une boucle Pour",
  "ne jamais affecter le compteur dans le bloc : c’est la boucle qui le fait avancer", ["compteur", "pour"], ["CONV"])
r("tantque", "Effet d’un TantQue", "D", X_EXEC, "TantQue condition Faire s’exécute",
  "la condition est testée avant chaque tour : vraie, le bloc s’exécute et on la reteste ; fausse, l’exécution passe après FinTantQue",
  ["tantque", "condition", "iteration"], ["ED_BCL"])
r("repeter", "Effet d’un Répéter", "D", X_EXEC, "Répéter bloc Jusqu’à condition s’exécute",
  "le bloc s’exécute, puis la condition est testée : fausse, on recommence ; vraie, on sort de la boucle", ["repeter", "condition"], ["ED_BCL"])
r("faire-evoluer", "Faire évoluer la condition", "A", X_ECR, "on écrit une boucle TantQue ou Répéter",
  "vérifier qu’une instruction du bloc modifie une variable de la condition, pour qu’elle finisse par changer de valeur",
  ["boucle-infinie", "tantque", "repeter"], ["ED_BCL"])
r("choisir-boucle", "Choisir la boucle", "A", X_ECR, "il faut répéter un traitement",
  "prendre Pour si le nombre de tours est connu avant de commencer, Répéter si le bloc doit s’exécuter au moins une fois, et TantQue sinon",
  ["boucle", "pour", "tantque", "repeter"], ["ED_BCL"])
r("pour-tantque", "Un Pour est un TantQue", "D", X_EXEC, "une boucle Pour i de a à b s’exécute, avec un pas de 1",
  "elle fait la même chose que : i ← a ; TantQue i <= b Faire … ; i ← i + 1 ; FinTantQue", ["pour", "tantque"], ["CONV"])
r("accumuler", "Accumuler", "A", X_ECR, "il faut calculer une somme ou un produit de valeurs vues une par une",
  "initialiser l’accumulateur avant la boucle (0 pour une somme, 1 pour un produit), puis le mettre à jour dans la boucle : somme ← somme + x",
  ["accumulateur", "boucle"], ["NSI_ALGO"])
r("compter", "Compter", "A", X_ECR, "il faut compter les valeurs qui vérifient une condition",
  "écrire n ← 0 avant la boucle, puis Si condition Alors n ← n + 1 FinSi dans la boucle", ["compteur", "alternative"], ["NSI_ALGO"])
r("drapeau", "Lever un drapeau", "A", X_ECR, "il faut savoir si un événement s’est produit au moins une fois pendant une boucle",
  "écrire trouvé ← faux avant la boucle, trouvé ← vrai quand l’événement arrive, et ne jamais le remettre à faux dans la boucle", ["drapeau"], ["NSI_ALGO"])
# 6. Listes et données composées
r("indice", "Accès par l’indice", "D", X_EXEC, "L est une liste de longueur N et on écrit L[i], avec 0 ≤ i ≤ N - 1",
  "on désigne l’élément de position i, qui s’utilise comme une variable : on peut le lire ou lui affecter une valeur", ["indice", "element", "liste"], ["CONV"])
r("hors-limites", "Indice hors limites", "D", X_EXEC, "on utilise L[i] avec i < 0 ou i ≥ Longueur(L)",
  "l’accès est une erreur, car cet élément n’existe pas", ["indice", "longueur"], ["CONV"])
r("parcourir", "Parcourir une liste", "A", X_ECR, "il faut traiter tous les éléments d’une liste L",
  "écrire Pour i de 0 à Longueur(L) - 1 Faire, puis traiter L[i] dans le bloc", ["parcours", "longueur", "pour"], ["NSI_ALGO"])
r("ajouter", "Effet d’Ajouter", "D", X_EXEC, "Ajouter(L, x) s’exécute",
  "x devient le dernier élément de L, et Longueur(L) augmente de 1", ["liste", "longueur"], ["CONV"])
r("deux-indices", "Ligne puis colonne", "D", X_EXEC, "M est une liste de listes",
  "M[i] désigne la ligne i, et M[i][j] l’élément de la colonne j de cette ligne", ["liste-listes", "indice"], ["NSI_TC"])
r("double-boucle", "Parcourir une grille", "A", X_ECR, "il faut traiter toutes les cases d’une liste de listes M",
  "imbriquer deux boucles Pour : i sur les lignes, puis j de 0 à Longueur(M[i]) - 1 sur les colonnes", ["liste-listes", "parcours"], ["NSI_TC"])
r("champ", "Accès à un champ", "D", X_EXEC, "e est un enregistrement de type Élève, qui a un champ nom",
  "e.nom désigne ce champ, qui s’utilise comme une variable de son type", ["champ", "enregistrement"], ["NSI_TC"])
r("liste-ou-enreg", "Liste ou enregistrement", "A", X_ECR, "il faut ranger plusieurs données ensemble",
  "prendre une liste si ce sont des valeurs du même type et du même rôle (des notes), un enregistrement si ce sont des données différentes d’un même objet (nom, âge, moyenne)",
  ["liste", "enregistrement"], ["NSI_TC"])
# 7. Sous-programmes
r("appel", "Déroulement d’un appel", "D", X_EXEC, "une fonction est appelée",
  "chaque paramètre reçoit la valeur de son argument, dans l’ordre ; le corps s’exécute jusqu’à Retourner ; l’appel est remplacé par la valeur retournée",
  ["appel", "parametre", "argument", "retour"], ["NSI_LP", "CONV"])
r("retourner", "Retourner termine", "D", X_EXEC, "Retourner s’exécute dans une fonction",
  "la fonction s’arrête aussitôt : les instructions qui suivent dans la fonction ne s’exécutent pas", ["retour", "fonction"], ["CONV"])
r("decouper", "Découper en sous-programmes", "A", X_ECR, "un même traitement revient plusieurs fois, ou l’algorithme devient long",
  "écrire ce traitement une seule fois dans un sous-programme nommé, puis l’appeler", ["sous-programme", "appel"], ["CONV"])
r("fonction-ou-procedure", "Fonction ou procédure", "A", X_ECR, "on écrit un sous-programme",
  "écrire une Fonction s’il calcule une valeur dont l’appelant a besoin, et une Procédure s’il agit seulement (afficher, modifier une liste)",
  ["fonction", "procedure-sp"], ["CONV"])
r("retourner-pas-afficher", "Retourner plutôt qu’afficher", "A", X_ECR, "une fonction doit calculer un résultat",
  "retourner ce résultat au lieu de l’afficher : c’est l’appelant qui décide quoi en faire", ["fonction", "retour", "ecriture"], ["CONV"])
r("portee", "Noms identiques, variables distinctes", "D", X_EXEC, "deux sous-programmes ont chacun une variable locale du même nom",
  "ce sont deux variables différentes : modifier l’une ne change pas l’autre", ["portee", "locale"], ["CONV"])
r("recursion", "Déroulement d’une récursion", "D", X_EXEC, "une fonction récursive est appelée",
  "chaque appel attend le résultat de l’appel sur la donnée plus petite ; une fois le cas de base atteint, les résultats remontent dans l’ordre inverse des appels",
  ["recursive", "cas-base", "appel"], ["NSI_REC"])
r("ecrire-recursive", "Écrire une récursion", "A", X_ECR, "un problème se ramène au même problème sur une donnée plus petite",
  "traiter d’abord le cas de base dans un Si, puis appeler la fonction sur la donnée plus petite et combiner son résultat", ["recursive", "cas-base"], ["NSI_REC"])
# 8. Vérifier
r("specifier", "Spécifier d’abord", "A", "de la conception d’un sous-programme", "on va écrire un sous-programme",
  "écrire d’abord son en-tête, ses préconditions et ses postconditions, puis seulement son corps", ["specification", "precondition", "postcondition"], ["NSI_LP"])
r("tracer", "Faire une trace", "A", "de la vérification d’un algorithme", "il faut comprendre ou vérifier un algorithme à la main",
  "faire une trace : une colonne par variable, une ligne par instruction exécutée, et noter chaque nouvelle valeur", ["trace"], ["ED_VAL"])
r("cas-limites", "Tester les cas limites", "A", "de la vérification d’un algorithme", "on construit un jeu de tests",
  "y mettre un cas ordinaire et les cas limites : liste vide ou d’un seul élément, valeurs égales, valeur cherchée en premier, en dernier ou absente", ["jeu-tests"], ["NSI_LP", "ED_VAL"])
r("precondition-dicho", "Dichotomie sur liste triée", "D", "de la recherche dans une liste", "on applique la recherche dichotomique à une liste non triée",
  "le résultat peut être faux : la méthode suppose que la liste est triée", ["liste-triee", "precondition"], ["NSI_ALGO"])
r("variant", "Prouver qu’une boucle s’arrête", "A", "de la preuve d’un algorithme", "un algorithme contient une boucle TantQue ou Répéter",
  "trouver un variant : un entier positif ou nul qui diminue strictement à chaque tour", ["variant", "terminaison"], ["NSI_ALGO"])
r("invariant", "Prouver ce que calcule une boucle", "A", "de la preuve d’un algorithme", "il faut prouver qu’une boucle calcule le bon résultat",
  "trouver un invariant, montrer qu’il est vrai avant la boucle et qu’un tour le conserve, puis l’utiliser à la sortie de la boucle", ["invariant", "correction"], ["NSI_ALGO"])
r("cout-lineaire", "Une boucle sur n données", "D", "du coût d’un algorithme", "un algorithme parcourt une fois ses n données, avec un nombre fixe d’opérations par tour",
  "son coût est linéaire : il double quand n double", ["cout-lineaire", "parcours"], ["NSI_ALGO"])
r("cout-quadratique", "Deux boucles imbriquées", "D", "du coût d’un algorithme", "deux boucles imbriquées font chacune de l’ordre de n tours",
  "le coût est quadratique : environ n² opérations, multiplié par 4 quand n double", ["cout-quadratique", "boucle"], ["NSI_ALGO"])
r("cout-log", "Diviser par deux à chaque tour", "D", "du coût d’un algorithme", "chaque tour divise par 2 la taille de la zone qui reste à traiter",
  "le nombre de tours est d’environ log₂(n) : 10 tours pour n = 1 000, 20 pour n = 1 000 000", ["cout-log", "iteration"], ["NSI_ALGO"])
chain(RULES)

# ---------- Contre-exemples ----------
X("reel-entier", "x : réel ; x ← 3", "La variable x est déclarée réelle, et l’affectation x ← 3 lui donne une valeur entière.",
  "la valeur rangée est un entier et la variable est réelle", "T", ["r-type-fixe"])
X("selon-intervalle", "Mentions avec Selon", "Pour donner les mentions, on compare la note à 16, 14 et 12 dans plusieurs Si successifs sur la même variable note.",
  "les cas sont des intervalles (note >= 16), pas des valeurs précises", "T", ["r-choisir-selon"])
X("pour-inverse", "Pour i de 5 à 1 Faire", "Avec un pas de 1, la boucle Pour i de 5 à 1 Faire … FinPour ne fait aucun tour.",
  "la valeur de départ dépasse la valeur d’arrivée (a > b), alors que la règle suppose a ≤ b", "2a", ["r-pour"])
X("lire-sans-affecter", "Lire x puis Écrire x", "Lire x puis Écrire x : x est utilisée sans aucune affectation avant, et l’algorithme est correct.",
  "la variable reçoit sa première valeur par Lire et non par une affectation", "T", ["r-initialiser"])
X("liste-une-valeur", "notes contient trois nombres", "notes ← [12, 15, 9] : la variable notes contient trois nombres.",
  "la variable est une liste", "T", ["pr-une-valeur"])
X("liste-modifiee", "Une procédure modifie une liste", "Procédure Doubler(L : liste d’entier) fait L[i] ← 2 * L[i] pour chaque i ; après Doubler(T), T est modifiée chez l’appelant.",
  "le paramètre est une liste, et non une valeur entière, réelle, booléenne, caractère ou chaîne", "2a", ["pr-copie"])
X("encadrement-python", "0 <= x <= 20 en Python", "En Python, 0 <= x <= 20 est accepté et vaut vrai si x vaut 15.",
  "on écrit en Python, pas dans le pseudo-code de ce support", "2a", ["r-intervalle"], ["PY"])
X("div-negatif", "-7 div 2", "-7 div 2 : Python (-7 // 2) donne -4, alors que d’autres langages donnent -3.",
  "un des entiers est négatif : les langages ne s’accordent pas", "T", ["r-division", "pr-euclide"], ["PY"])
X("recherche-arret", "Recherche qui s’arrête tôt", "Une recherche séquentielle trouve la valeur cherchée dès L[0] et s’arrête après une seule comparaison, même si L a un million d’éléments.",
  "la boucle s’arrête avant d’avoir parcouru toutes les données", "2a", ["r-cout-lineaire"])
