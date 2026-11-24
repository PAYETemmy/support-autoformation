from lib import P, C

# ---------- Termes primitifs ----------
P("instruction", "Instruction", "Un ordre élémentaire que l’ordinateur sait exécuter : ranger une valeur, faire un calcul, afficher un message.",
  "S’écrit en général sur une ligne ; fait une seule chose ; l’ordinateur l’exécute sans l’interpréter : il fait exactement ce qui est écrit.", ["ED_INIT"])
P("valeur", "Valeur", "Une donnée précise : un nombre comme 12 ou 3.5, un texte comme \"Bonjour\", ou bien vrai, ou bien faux.",
  "Une valeur ne change jamais : 12 reste 12. Ce qui change pendant l’exécution, c’est la valeur rangée dans une variable.", ["ED_AFF"])
P("nom", "Nom (identificateur)", "Un mot choisi par celui qui écrit l’algorithme pour désigner quelque chose : une variable, un sous-programme, l’algorithme lui-même.",
  "Sans espace, il commence par une lettre ; Éduscol l’appelle identificateur, comme le nom écrit sur la façade d’un tiroir.", ["ED_AFF"])
P("memoire", "Mémoire", "L’ensemble des emplacements où l’ordinateur garde les données pendant que l’algorithme s’exécute.",
  "Elle est découpée en emplacements, chacun garde une valeur ; son contenu disparaît à la fin de l’exécution.", ["ED_AFF"])
P("utilisateur", "Utilisateur", "La personne qui se sert de l’algorithme une fois écrit : elle tape les données et lit les résultats.",
  "Ce n’est pas forcément celui qui a écrit l’algorithme ; il ne voit pas les instructions, seulement les messages et les résultats.", ["ED_ES"])
P("probleme", "Problème", "Une question précise à résoudre à partir de données : calculer une moyenne, trouver le plus grand nombre, trier une liste.",
  "Un même problème peut se résoudre par plusieurs algorithmes ; une instance du problème, ce sont des données précises, par exemple les notes 12, 15 et 9.", ["ED_INIT"])
P("operation", "Opération", "Un calcul élémentaire sur une ou deux valeurs : additionner, multiplier, comparer, combiner vrai et faux.",
  "Elle donne une valeur comme résultat et ne modifie pas les valeurs utilisées : 3 + 4 donne 7, 3 et 4 restent inchangés.", ["ED_CTRL"])
P("execution", "Exécution", "Le déroulement d’un algorithme par l’ordinateur, instruction après instruction, avec des données précises.",
  "Deux exécutions du même algorithme avec des données différentes peuvent donner des résultats différents ; on peut la simuler à la main.", ["ED_VAL"])

# ---------- 1. Algorithme et structure ----------
C("algorithme", "Algorithme", ["instruction", "probleme"], "Suite finie d’instructions, à exécuter dans un ordre déterminé, qui résout un problème.",
  "Il se termine ; chaque instruction est sans ambiguïté ; il transforme des données (entrées) en résultats (sorties) ; il ne dépend d’aucun langage de programmation.", ["ED_INIT"])
C("pseudo-code", "Pseudo-code", ["algorithme"], "Façon d’écrire un algorithme en français, avec quelques mots-clés fixes, sans suivre la syntaxe d’un langage de programmation.",
  "Sert à réfléchir à la méthode avant de programmer ; plus précis que des phrases, moins strict qu’un langage ; il n’existe pas de norme unique.", ["LAF", "ED_INIT"])
C("programme", "Programme", ["algorithme", "instruction"], "Algorithme traduit dans un langage de programmation (Python, C++…), dont l’ordinateur peut exécuter les instructions.",
  "Il doit respecter exactement la syntaxe du langage ; un même algorithme donne des programmes différents selon le langage choisi.", ["NSI_LP"])
C("mot-cle", "Mot-clé", ["nom", "pseudo-code"], "Mot réservé du pseudo-code, dont le sens est fixé : Algorithme, Variables, Début, Fin, Si, Pour, TantQue…",
  "S’écrit toujours de la même façon (ici avec une majuscule) ; ne peut pas servir de nom de variable.", ["CONV"])
C("commentaire", "Commentaire", ["pseudo-code"], "Texte d’explication écrit après // dans un pseudo-code, que l’exécution ignore.",
  "S’adresse au lecteur, pas à l’ordinateur ; explique pourquoi une ligne est là ; va jusqu’à la fin de la ligne.", ["CONV"])
C("bloc", "Bloc", ["instruction"], "Suite d’instructions qui forment un tout et s’exécutent ensemble : entre Début et Fin, après Alors, dans une boucle…",
  "S’ouvre après un mot-clé et se ferme par un mot-clé de fin (Fin, FinSi, FinPour…) ; ses lignes sont décalées vers la droite ; Éduscol le marque d’une barre verticale.", ["ED_CTRL"])
C("indentation", "Indentation", ["bloc"], "Décalage vers la droite des lignes d’un bloc, qui montre à quel bloc chaque instruction appartient.",
  "Même retrait pour toutes les lignes d’un bloc, un retrait de plus par bloc imbriqué ; en pseudo-code elle sert la lecture, en Python elle est obligatoire.", ["CONV"])
C("sequence", "Séquence", ["instruction"], "Suite d’instructions exécutées l’une après l’autre, dans l’ordre où elles sont écrites.",
  "La structure la plus simple ; changer l’ordre de deux instructions peut changer le résultat.", ["NSI_LP"])
C("entree", "Entrée", ["valeur", "algorithme"], "Valeur qu’un algorithme reçoit pour faire son travail : tapée par l’utilisateur, lue dans un fichier ou donnée en paramètre.",
  "Se repère avant d’écrire l’algorithme, avec son type et ses valeurs permises ; correspond à l’étape de préparation d’Éduscol.", ["ED_INIT"])
C("sortie", "Sortie", ["valeur", "algorithme"], "Valeur qu’un algorithme produit et communique : affichée à l’écran, enregistrée ou retournée.",
  "C’est le résultat attendu ; un algorithme sans sortie ne sert à rien.", ["ED_INIT"])
C("traitement", "Traitement", ["instruction", "entree", "sortie"], "Partie d’un algorithme formée des instructions qui calculent les sorties à partir des entrées.",
  "Se place entre la préparation (les entrées) et la sortie des résultats ; contient les calculs, les tests et les boucles.", ["ED_INIT"])

# ---------- 2. Données ----------
C("variable", "Variable", ["nom", "memoire", "valeur"], "Emplacement de la mémoire, désigné par un nom, qui contient une valeur à la fois.",
  "Sa valeur peut changer pendant l’exécution ; Éduscol la compare à un tiroir qui porte un nom sur sa façade ; elle a un type.", ["ED_AFF"])
C("type", "Type", ["valeur"], "Catégorie de valeurs qui fixe les valeurs possibles et les opérations permises sur elles.",
  "Se désigne par un mot-clé : entier, réel, booléen, caractère, chaîne ; on ne fait pas les mêmes calculs sur un nombre et sur un texte.", ["LAF"])
C("entier", "Entier", ["type"], "Type des nombres sans partie décimale : …, −2, −1, 0, 1, 2, …",
  "Sert à compter et à numéroter ; permet div et mod ; s’écrit sans point : 12, −3.", ["LAF"])
C("reel", "Réel", ["type"], "Type des nombres qui peuvent avoir une partie décimale, écrite après un point : 3.5, −0.25.",
  "Sert à mesurer : prix, moyenne, distance ; le résultat de / est toujours un réel.", ["LAF"])
C("booleen", "Booléen", ["type"], "Type qui n’a que deux valeurs : vrai et faux.",
  "C’est le résultat d’une comparaison ; il se combine avec et, ou, non ; il sert de condition dans Si et TantQue.", ["LAF"])
C("caractere", "Caractère", ["type"], "Type d’un seul symbole (lettre, chiffre, ponctuation ou espace), écrit entre apostrophes droites : 'a', '7', '?'.",
  "'7' est un caractère, pas le nombre 7 ; une chaîne est faite de caractères.", ["LAF"])
C("chaine", "Chaîne", ["type", "caractere"], "Type des textes : une suite de caractères écrite entre guillemets droits, comme \"Bonjour\" ou \"\" (la chaîne vide).",
  "Se met bout à bout avec + ; sa longueur est son nombre de caractères ; \"12\" est une chaîne, pas un nombre.", ["LAF"])
C("declaration", "Déclaration", ["variable", "type"], "Ligne de la section Variables qui annonce une variable : son nom, deux-points, son type : age : entier.",
  "Se place avant Début ; plusieurs variables du même type se déclarent ensemble : a, b : entier ; elle ne donne aucune valeur.", ["CONV"])
C("constante", "Constante", ["nom", "valeur"], "Nom associé à une valeur fixée une fois pour toutes, qui ne change pas pendant l’exécution : Constante TVA = 0.2.",
  "Se déclare avant Début avec sa valeur ; rend l’algorithme plus lisible et plus facile à modifier : une seule ligne à changer.", ["AJOUT"])

# ---------- 3. Calculs et conditions ----------
C("operateur", "Opérateur", ["operation"], "Symbole ou mot-clé qui désigne une opération : +, *, div, <, et…",
  "S’applique à une ou deux valeurs ; chaque opérateur n’accepte que certains types.", ["CONV"])
C("expression", "Expression", ["valeur", "operateur", "variable"], "Écriture qui se calcule pour donner une valeur : des valeurs et des variables reliées par des opérateurs, avec d’éventuelles parenthèses : 2 * prix + 1.",
  "N’est pas une instruction : elle se place à droite de ←, dans Écrire ou dans une condition ; sa valeur a un type.", ["NSI_LP"])
C("op-arith", "Opérateur arithmétique", ["operateur"], "Opérateur de calcul sur des nombres : + (addition), - (soustraction), * (multiplication), / (division), div et mod.",
  "* et / passent avant + et - ; / donne un réel ; div et mod ne s’appliquent qu’à des entiers.", ["CONV"])
C("div-mod", "Quotient et reste (div, mod)", ["op-arith", "entier"], "Opérateurs de la division euclidienne entre entiers : a div b donne le quotient entier, a mod b le reste.",
  "17 div 5 vaut 3 et 17 mod 5 vaut 2, car 17 = 5 × 3 + 2 ; mod sert à tester la divisibilité et la parité.", ["CONV"])
C("op-comp", "Opérateur de comparaison", ["operateur", "booleen"], "Opérateur qui compare deux valeurs et donne un booléen : = (égal), <> (différent), <, >, <=, >=.",
  "= compare, il ne range rien ; on compare deux nombres, ou deux valeurs du même type.", ["ED_CTRL", "CONV"])
C("op-log", "Opérateur logique", ["operateur", "booleen"], "Opérateur qui combine des booléens : et, ou, non.",
  "Sert à écrire des conditions composées : age >= 18 et age < 65 ; non passe avant et, qui passe avant ou.", ["ED_CTRL"])
C("condition", "Condition", ["expression", "booleen"], "Expression dont la valeur est un booléen : vrai ou faux.",
  "Simple (une comparaison : a < b) ou composée (des comparaisons reliées par et, ou, non) ; décide du chemin suivi dans Si, TantQue et Répéter.", ["ED_CTRL"])
C("concatenation", "Concaténation", ["chaine", "operateur"], "Opération qui met deux chaînes bout à bout, notée + : \"Bon\" + \"jour\" donne \"Bonjour\".",
  "L’ordre compte ; aucun espace n’est ajouté automatiquement ; ne s’applique qu’à des chaînes.", ["AJOUT"])

# ---------- 4. Instructions de base ----------
C("affectation", "Affectation", ["instruction", "variable", "expression"], "Instruction qui range dans une variable la valeur d’une expression : x ← expression, qui se lit « x prend la valeur… ».",
  "Remplace l’ancienne valeur ; à gauche une seule variable, à droite une expression ; s’écrit ← (ou <- au clavier).", ["ED_AFF"])
C("lecture", "Lecture (Lire)", ["instruction", "entree", "variable"], "Instruction Lire x : elle attend une valeur tapée par l’utilisateur et la range dans la variable x.",
  "Fait entrer une donnée dans l’algorithme ; Éduscol l’écrit Saisir x ; elle remplace l’ancienne valeur de x.", ["ED_ES"])
C("ecriture", "Écriture (Écrire)", ["instruction", "sortie"], "Instruction Écrire qui affiche à l’écran des messages et des valeurs : Écrire \"Moyenne : \", m.",
  "Fait sortir un résultat ; les textes entre guillemets s’affichent tels quels, les variables par leur valeur ; Éduscol l’écrit Afficher.", ["ED_ES"])

# ---------- 5. Alternatives ----------
C("structure-controle", "Structure de contrôle", ["instruction", "bloc"], "Instruction qui décide quels blocs s’exécutent et combien de fois : alternative (Si, Selon) ou boucle (Pour, TantQue, Répéter).",
  "Sans elle, un algorithme n’est qu’une séquence ; elle s’ouvre par un mot-clé et se ferme par un mot-clé de fin.", ["ED_CTRL"])
C("alternative", "Alternative (Si)", ["structure-controle", "condition"], "Structure de contrôle qui exécute un bloc si une condition est vraie, et éventuellement un autre bloc sinon : Si … Alors … Sinon … FinSi.",
  "Un seul des deux blocs s’exécute ; Sinon est facultatif ; elle se ferme par FinSi.", ["ED_CTRL"])
C("si-imbrique", "Alternatives imbriquées", ["alternative"], "Alternative placée à l’intérieur d’un bloc d’une autre alternative.",
  "Permet de distinguer plus de deux cas ; chaque niveau prend un retrait de plus ; chaque Si a son propre FinSi.", ["ED_CTRL"])
C("selon", "Choix multiple (Selon)", ["structure-controle", "variable"], "Structure de contrôle qui exécute le bloc du Cas égal à la valeur d’une variable : Selon x Faire, Cas 1 : …, Autrement : …, FinSelon.",
  "Ne teste que l’égalité à des valeurs précises ; un seul Cas s’exécute ; Autrement traite toutes les autres valeurs.", ["CONV"])

# ---------- 6. Boucles ----------
C("boucle", "Boucle", ["structure-controle", "bloc"], "Structure de contrôle qui répète un bloc d’instructions.",
  "Bornée (Pour : nombre de tours connu d’avance) ou non bornée (TantQue, Répéter : arrêt par une condition) ; se ferme par un mot-clé de fin.", ["ED_BCL", "NSI_LP"])
C("iteration", "Itération (tour)", ["boucle"], "Une exécution complète du bloc d’une boucle.",
  "Une boucle fait zéro, une ou plusieurs itérations ; les variables peuvent changer de valeur d’une itération à l’autre.", ["ED_BCL"])
C("compteur", "Compteur", ["variable", "entier"], "Variable entière qui compte quelque chose : les tours d’une boucle, ou le nombre de valeurs qui vérifient une condition.",
  "Commence en général à 0 ; augmente de 1 à chaque fois : n ← n + 1 ; dans une boucle Pour, il avance tout seul.", ["ED_BCL"])
C("pour", "Boucle Pour", ["boucle", "compteur"], "Boucle bornée qui répète son bloc pour chaque valeur d’un compteur, d’une valeur de départ à une valeur d’arrivée : Pour i de 1 à N Faire … FinPour.",
  "Le nombre de tours est connu avant de commencer ; le compteur augmente de 1 à chaque tour, sauf si un pas est donné ; Éduscol écrit « Pour I de 1 jusqu’à N faire ».", ["ED_BCL", "CONV"])
C("pas", "Pas", ["pour"], "Valeur ajoutée au compteur d’une boucle Pour après chaque tour, 1 par défaut : Pour i de 0 à 10 pas 2.",
  "Peut être négatif pour compter à rebours : Pour i de 10 à 1 pas -1 ; ne vaut jamais 0.", ["CONV"])
C("tantque", "Boucle TantQue", ["boucle", "condition"], "Boucle non bornée qui teste une condition avant chaque tour et répète son bloc tant qu’elle est vraie : TantQue condition Faire … FinTantQue.",
  "Le nombre de tours n’est pas connu d’avance ; elle peut faire zéro tour ; son bloc doit pouvoir rendre la condition fausse.", ["ED_BCL"])
C("repeter", "Boucle Répéter", ["boucle", "condition"], "Boucle non bornée qui exécute son bloc puis teste une condition, et recommence jusqu’à ce qu’elle soit vraie : Répéter … Jusqu’à condition.",
  "Fait toujours au moins un tour ; s’arrête quand la condition devient vraie, à l’inverse de TantQue ; idéale pour redemander une saisie.", ["ED_BCL"])
C("boucle-infinie", "Boucle infinie", ["boucle"], "Boucle dont la condition d’arrêt n’est jamais atteinte : l’algorithme ne se termine pas.",
  "Erreur majeure selon Éduscol ; vient souvent d’une variable de la condition que le bloc ne modifie jamais.", ["ED_BCL"])
C("accumulateur", "Accumulateur", ["variable"], "Variable qui cumule un résultat au fil des tours d’une boucle : somme ← somme + x.",
  "Initialisé avant la boucle (0 pour une somme, 1 pour un produit, \"\" pour une chaîne) ; sa valeur finale est le résultat.", ["NSI_ALGO"])
C("drapeau", "Drapeau", ["variable", "booleen"], "Variable booléenne qui mémorise qu’un événement s’est produit : trouvé ← vrai.",
  "Initialisé avant la boucle ; changé une seule fois, quand l’événement arrive ; peut servir à arrêter une boucle TantQue.", ["NSI_ALGO"])

# ---------- 7. Listes et données composées ----------
C("liste", "Liste (tableau)", ["variable", "valeur"], "Variable qui contient plusieurs valeurs du même type, rangées dans un ordre et repérées par leur position : notes ← [12, 15, 9].",
  "Se déclare avec le type de ses valeurs : notes : liste de réel ; s’écrit entre crochets ; on l’appelle aussi tableau.", ["CONV", "NSI_TC"])
C("indice", "Indice", ["liste", "entier"], "Entier qui donne la position d’une valeur dans une liste, en commençant à 0 : notes[0] est la première.",
  "Pour une liste de N valeurs, il va de 0 à N - 1 ; il peut être une variable : notes[i] ; il s’écrit entre crochets.", ["CONV"])
C("element", "Élément", ["liste", "indice"], "Une des valeurs rangées dans une liste, désignée par la liste et son indice : notes[2].",
  "S’utilise comme une variable : on peut le lire ou lui affecter une valeur ; tous les éléments d’une liste ont le même type.", ["CONV"])
C("longueur", "Longueur", ["liste", "entier"], "Nombre d’éléments d’une liste (ou de caractères d’une chaîne), donné par Longueur(L).",
  "Vaut 0 pour la liste vide [] ; le dernier indice est Longueur(L) - 1 ; augmente de 1 avec Ajouter.", ["CONV"])
C("parcours", "Parcours", ["liste", "pour"], "Visite de chaque élément d’une liste, un par un, par une boucle sur les indices.",
  "Pour i de 0 à Longueur(L) - 1 Faire … ; sert à calculer une somme ou un maximum, à compter, à chercher ; son coût est linéaire.", ["NSI_ALGO"])
C("liste-triee", "Liste triée", ["liste"], "Liste dont les éléments sont rangés dans l’ordre croissant : chaque élément est inférieur ou égal au suivant.",
  "[2, 5, 5, 9] est triée ; la liste vide et une liste d’un seul élément sont triées ; c’est la condition de la recherche dichotomique.", ["NSI_ALGO"])
C("liste-listes", "Liste de listes", ["liste"], "Liste dont chaque élément est lui-même une liste : un tableau à deux dimensions, en lignes et en colonnes.",
  "grille[i] est la ligne i ; grille[i][j] est l’élément de la ligne i et de la colonne j ; se parcourt avec deux boucles imbriquées.", ["NSI_TC"])
C("enregistrement", "Enregistrement", ["type", "nom"], "Type construit qui regroupe sous un seul nom plusieurs valeurs, de types éventuellement différents, appelées champs.",
  "Se déclare : Type Élève = Enregistrement nom : chaîne, moyenne : réel FinEnregistrement ; décrit un objet réel (un élève, un produit) ; proche du p-uplet nommé de NSI.", ["NSI_TC"])
C("champ", "Champ", ["enregistrement", "nom"], "Une des valeurs d’un enregistrement, désignée par un nom et notée avec un point : e.nom.",
  "S’utilise comme une variable de son type : e.moyenne ← 14.5 ; deux enregistrements du même type ont les mêmes champs.", ["NSI_TC"])

# ---------- 8. Sous-programmes ----------
C("sous-programme", "Sous-programme", ["algorithme", "nom"], "Algorithme nommé, écrit à part, qu’on peut lancer depuis un autre algorithme autant de fois qu’on veut.",
  "C’est une fonction ou une procédure ; évite de recopier le même traitement ; se teste séparément.", ["CONV"])
C("fonction", "Fonction", ["sous-programme", "valeur"], "Sous-programme qui calcule une valeur et la renvoie avec Retourner : Fonction Carré(x : réel) : réel.",
  "Annonce le type de sa valeur de retour ; s’appelle dans une expression : y ← Carré(3) ; ne devrait ni lire ni afficher.", ["CONV"])
C("procedure-sp", "Procédure (sous-programme)", ["sous-programme"], "Sous-programme qui agit sans renvoyer de valeur (afficher, modifier une liste) : Procédure AfficherLigne(n : entier).",
  "Pas de Retourner avec une valeur ; s’appelle comme une instruction, seule sur sa ligne.", ["CONV"])
C("parametre", "Paramètre", ["sous-programme", "variable"], "Variable de l’en-tête d’un sous-programme, qui reçoit une valeur au moment de l’appel : x dans Carré(x : réel).",
  "Se déclare entre parenthèses avec son type ; n’existe que dans le sous-programme ; on dit aussi paramètre formel.", ["CONV"])
C("argument", "Argument", ["parametre", "valeur"], "Valeur donnée à un paramètre au moment d’un appel : dans Carré(3), l’argument est 3.",
  "Peut être une valeur, une variable ou une expression ; les arguments se placent dans l’ordre des paramètres ; on dit aussi paramètre effectif.", ["CONV"])
C("appel", "Appel", ["sous-programme", "instruction"], "Instruction ou expression qui lance un sous-programme par son nom, avec ses arguments entre parenthèses : Carré(3).",
  "L’algorithme qui appelle attend la fin du sous-programme, puis reprend juste après l’appel.", ["NSI_LP"])
C("retour", "Valeur de retour", ["fonction", "valeur"], "Valeur qu’une fonction renvoie à l’appelant avec Retourner : elle remplace l’appel dans l’expression.",
  "Son type est annoncé dans l’en-tête ; Retourner termine aussitôt la fonction.", ["CONV"])
C("locale", "Variable locale", ["variable", "sous-programme"], "Variable déclarée dans un sous-programme, qui n’existe que pendant son exécution.",
  "Invisible depuis l’algorithme principal ; deux sous-programmes peuvent avoir chacun une locale du même nom sans conflit.", ["CONV"])
C("portee", "Portée", ["variable", "sous-programme"], "Partie de l’algorithme où le nom d’une variable est connu et utilisable.",
  "Celle d’une variable locale est son sous-programme ; dans ce support, un sous-programme n’utilise que ses paramètres et ses variables locales.", ["CONV"])
C("recursive", "Fonction récursive", ["fonction", "appel"], "Fonction qui s’appelle elle-même, sur une donnée plus petite, pour résoudre son problème.",
  "A au moins un cas de base, traité sans appel ; chaque appel doit se rapprocher du cas de base : Factorielle(n) = n × Factorielle(n - 1).", ["NSI_REC"])
C("cas-base", "Cas de base", ["recursive"], "Cas d’une fonction récursive traité directement, sans appel récursif, qui arrête la suite des appels.",
  "S’écrit en premier, dans un Si : Si n = 0 Alors Retourner 1 ; sans lui, les appels ne s’arrêtent jamais.", ["NSI_REC"])

# ---------- 9. Vérifier un algorithme ----------
C("precondition", "Précondition", ["condition", "entree"], "Condition que les entrées doivent vérifier pour que l’algorithme ou le sous-programme fonctionne : N ≥ 1, liste triée.",
  "C’est à l’appelant de la respecter ; elle s’écrit dans la spécification ; hors précondition, le résultat n’est pas garanti.", ["NSI_LP"])
C("postcondition", "Postcondition", ["condition", "sortie"], "Condition que vérifie le résultat quand les préconditions étaient respectées : « retourne le plus grand élément de L ».",
  "Décrit ce que fait le sous-programme, pas comment ; sert de référence pour les tests.", ["NSI_LP"])
C("specification", "Spécification", ["sous-programme", "precondition", "postcondition"], "Description de ce que fait un sous-programme : son en-tête (nom, paramètres et types, type du résultat), ses préconditions et ses postconditions.",
  "S’écrit avant le corps, en commentaire ; permet d’utiliser le sous-programme sans lire ses instructions.", ["NSI_LP"])
C("trace", "Trace d’exécution", ["execution", "variable"], "Tableau qui note, ligne après ligne, la valeur de chaque variable pendant une exécution faite à la main.",
  "Une colonne par variable, une ligne par instruction exécutée ; montre où un algorithme se trompe ; Éduscol demande de valider par des traces.", ["ED_VAL"])
C("jeu-tests", "Jeu de tests", ["entree", "sortie"], "Ensemble de cas de test : pour chacun, des entrées choisies et la sortie attendue, à comparer avec la sortie obtenue.",
  "Contient des cas ordinaires et des cas limites ; un test réussi ne prouve pas que l’algorithme est correct.", ["NSI_LP", "ED_VAL"])
C("correction", "Correction", ["algorithme", "postcondition"], "Propriété d’un algorithme qui, pour toute entrée qui respecte les préconditions, produit une sortie qui vérifie la postcondition.",
  "Se prouve par un raisonnement (un invariant), pas par des tests ; un algorithme peut être correct et lent.", ["NSI_ALGO"])
C("terminaison", "Terminaison", ["algorithme", "execution"], "Propriété d’un algorithme qui s’arrête après un nombre fini d’instructions, pour toute entrée qui respecte les préconditions.",
  "Acquise pour une boucle Pour dont on ne modifie pas le compteur ; à prouver pour TantQue et Répéter, avec un variant.", ["NSI_ALGO"])
C("invariant", "Invariant de boucle", ["condition", "boucle"], "Condition vraie avant la boucle et après chaque tour, qui permet de prouver ce que la boucle calcule.",
  "Exemple : « somme contient la somme des i premiers éléments » ; à la sortie, avec la condition de sortie, il donne la postcondition.", ["NSI_ALGO"])
C("variant", "Variant de boucle", ["boucle", "entier"], "Quantité entière, positive ou nulle, qui diminue strictement à chaque tour d’une boucle.",
  "Prouve la terminaison : un entier positif ne peut pas diminuer indéfiniment ; en dichotomie, c’est droite - gauche.", ["NSI_ALGO"])
C("cout", "Coût", ["algorithme", "operation"], "Nombre d’opérations élémentaires qu’exécute un algorithme, exprimé en fonction de la taille n de ses données, en ordre de grandeur.",
  "On regarde souvent le pire cas ; il compare deux algorithmes sans dépendre de l’ordinateur ; il compte surtout pour de grandes données.", ["NSI_ALGO"])
C("cout-lineaire", "Coût linéaire", ["cout"], "Coût proportionnel à n : doubler la taille des données double à peu près le nombre d’opérations.",
  "Typique d’un parcours : une boucle de n tours avec un travail fixe par tour ; noté O(n).", ["NSI_ALGO"])
C("cout-quadratique", "Coût quadratique", ["cout"], "Coût proportionnel à n² : doubler la taille des données multiplie à peu près par 4 le nombre d’opérations.",
  "Typique de deux boucles imbriquées : tri par sélection, tri par insertion dans le pire cas ; noté O(n²).", ["NSI_ALGO"])
C("cout-log", "Coût logarithmique", ["cout"], "Coût proportionnel au nombre de fois qu’on peut diviser n par 2 : doubler la taille des données ajoute à peu près une seule étape.",
  "Typique de la recherche dichotomique : environ 10 étapes pour 1 000 éléments, 20 pour un million ; noté O(log n).", ["NSI_ALGO"])
