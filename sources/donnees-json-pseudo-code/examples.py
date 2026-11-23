from lib import E

# ---------- Algorithme et structure ----------
E('algo-bonjour', 'Algorithme Bonjour', 'Algorithme Bonjour ; Variables prenom : chaîne ; Début ; Écrire "Ton prénom ?" ; Lire prenom ; Écrire "Bonjour ", prenom ; Fin',
  'un algorithme complet tient en quelques lignes : son nom, ses déclarations, puis ses instructions entre Début et Fin', ['algorithme', 'r-structure', 'p-ecrire-algo', 'pseudo-code', 'mot-cle'])
E('moyenne-trois', 'Moyenne de trois notes', 'Algorithme Moyenne3 ; Variables a, b, c, m : réel ; Début ; Lire a ; Lire b ; Lire c ; m ← (a + b + c) / 3 ; Écrire m ; Fin. Avec 12, 15 et 9, il affiche 12.',
  'les trois étapes d’Éduscol se suivent : entrée des données (Lire), traitement (calcul de m), sortie des résultats (Écrire)', ['algorithme', 'entree', 'traitement', 'sortie', 'r-structure', 'sequence', 'p-ecrire-algo'])
E('recette', 'Cuire jusqu’à ce que ce soit doré', 'Une recette dit « faire cuire jusqu’à ce que ce soit doré » : un cuisinier comprend, mais « doré » ne dit pas à un ordinateur quand s’arrêter.',
  'chaque instruction d’un algorithme doit être sans ambiguïté, exécutable à l’identique par n’importe quel exécutant', ['algorithme', 'instruction'])
E('deux-ordres', 'L’ordre compte', 'x ← 2 ; x ← x * 3 ; x ← x + 1 donne x = 7, mais x ← 2 ; x ← x + 1 ; x ← x * 3 donne x = 9.',
  'dans une séquence, chaque instruction travaille sur le résultat des précédentes : changer l’ordre change le résultat', ['sequence', 'r-sequentiel', 'instruction', 'execution', 'r-affecter'])
E('probleme-max', 'Un problème, plusieurs algorithmes', 'Trouver le plus grand de trois nombres a, b, c : on peut comparer a à b puis le plus grand à c, ou bien ranger les trois nombres dans l’ordre et prendre le dernier.',
  'un même problème se résout par plusieurs algorithmes, plus ou moins simples', ['probleme', 'algorithme'])
E('instance', 'Une instance du problème', 'Le problème : « calculer une moyenne ». Une instance : les notes 12, 15 et 9, dont la moyenne est 12.',
  'le problème est général ; une instance fixe des données précises, sur lesquelles on exécute l’algorithme', ['probleme', 'entree', 'execution', 'valeur'])
E('python-cpp', 'Même algorithme, deux programmes', 'x ← x + 1 s’écrit x = x + 1 en Python, et x = x + 1; (avec un point-virgule) en C++.',
  'un algorithme se traduit en programmes différents selon le langage, alors que le pseudo-code ne dépend d’aucun', ['programme', 'pseudo-code', 'algorithme', 'p-traduire'])
E('trois-fleches', '←, := ou « prend la valeur »', 'Le lycée Lafayette accepte aussi := pour l’affectation ; ce support écrit ← ; Éduscol écrit « prend la valeur ».',
  'il n’y a pas de norme : chaque support annonce ses symboles, qui désignent la même instruction', ['pr-pas-norme', 'pseudo-code', 'pr-fleche', 'affectation'])
E('saisir-lire', 'Saisir ou Lire ?', 'Éduscol écrit Saisir N et Afficher S ; ce support écrit Lire N et Écrire S.',
  'deux supports, deux mots-clés pour la même instruction : il faut connaître les conventions du support utilisé', ['pr-pas-norme', 'lecture', 'ecriture', 'mot-cle'])
E('pas-norme-fin', 'FinSi ou barre verticale', 'Ce support ferme un Si par FinSi ; Éduscol marque le bloc par une barre verticale, sans mot de fin.',
  'la façon de délimiter un bloc change d’un support à l’autre, le sens reste le même', ['pr-pas-norme', 'bloc', 'alternative'])
E('mot-cle-interdit', 'Une variable nommée Si', 'Déclarer Si : entier est refusé, car Si est un mot-clé ; on choisit un autre nom, par exemple seuil.',
  'un mot-clé a un sens fixé et ne peut pas servir de nom', ['mot-cle', 'r-nommer', 'nom'])
E('noms-explicites', 'nbNotes plutôt que n2', 'nbNotes, somme, prixTTC disent ce qu’elles contiennent ; n2, truc ou x1 obligent à relire tout l’algorithme.',
  'un bon nom évite les confusions et remplace souvent un commentaire', ['r-nommer', 'nom', 'variable'])
E('nom-espace', 'prix ttc', 'prix ttc (avec un espace) serait lu comme deux noms ; on écrit prixTTC ou prix_ttc.',
  'un nom ne contient pas d’espace, sinon on ne sait pas où il finit', ['r-nommer', 'nom'])
E('commentaire-pourquoi', '// pourquoi, pas quoi', 'max ← L[0] // pas 0 : les valeurs peuvent être négatives. À éviter : i ← i + 1 // ajoute 1 à i.',
  'un bon commentaire explique pourquoi ; un commentaire qui répète l’instruction n’apprend rien', ['commentaire', 'r-commenter'])
E('commentaire-ignore', 'Le commentaire ne s’exécute pas', 'x ← 5 // x ← 10 : après cette ligne, x vaut 5.',
  'tout ce qui suit // jusqu’à la fin de la ligne est ignoré par l’exécution', ['commentaire', 'execution'])
E('commentaire-spec', 'Spécification en commentaire', '// Moyenne(L) : retourne la moyenne des éléments de L ; précondition : L non vide',
  'le commentaire sert aussi à écrire la spécification au-dessus d’un sous-programme', ['commentaire', 'specification', 'r-specifier', 'r-commenter'])
E('bloc-si', 'Le bloc d’un Si', 'Si n > 0 Alors, puis en retrait Écrire "positif" et compteur ← compteur + 1, puis FinSi : les deux lignes en retrait forment le bloc.',
  'un bloc est un ensemble d’instructions qui s’exécutent ensemble, ouvert par Alors et fermé par FinSi', ['bloc', 'indentation', 'r-indenter', 'alternative'])
E('retrait-faux', 'Un retrait trompeur', 'Pour i de 1 à 3 Faire Écrire i FinPour ; Écrire "fin" : si la ligne Écrire "fin" est décalée comme le bloc, le lecteur croit qu’elle est répétée 3 fois.',
  'en pseudo-code, l’indentation guide le lecteur : un mauvais retrait trompe sur ce qui est répété', ['indentation', 'r-indenter', 'bloc'])
E('python-indent', 'Indentation obligatoire en Python', 'En Python, if x > 0: suivi d’une ligne non décalée provoque l’erreur IndentationError.',
  'en Python, l’indentation n’est pas qu’une aide à la lecture : elle définit les blocs', ['indentation', 'programme', 'p-traduire'])
E('debut-fin', 'Début et Fin', 'Début ; Lire n ; Écrire n * 2 ; Fin : le bloc principal va de Début à Fin.',
  'les instructions de l’algorithme forment un bloc, ouvert par Début et fermé par Fin', ['bloc', 'r-structure', 'mot-cle', 'r-indenter'])
E('analyse-ttc', 'Analyser : prix TTC', 'Énoncé : « calculer le prix TTC d’un article ». Entrée : prixHT, réel ≥ 0. Sortie : prixTTC. Traitement : prixTTC ← prixHT * 1.2. Exemple : 50 donne 60.',
  'l’analyse sépare ce qui est donné, ce qui est demandé et le calcul qui les relie', ['p-analyser', 'entree', 'sortie', 'traitement'])
E('analyse-max', 'Analyser : la plus grande note', 'Entrée : une liste de notes non vide. Sortie : la plus grande note. Traitement : comparer chaque note au maximum trouvé jusque-là. Exemple : [12, 17, 9] donne 17.',
  'repérer la précondition (liste non vide) fait partie de l’analyse', ['p-analyser', 'precondition', 'entree', 'sortie'])
E('analyse-age', 'Analyser : majeur ou mineur', 'Entrée : age, entier ≥ 0. Sortie : le message « majeur » ou « mineur ». Traitement : comparer age à 18. Exemples : 17 donne « mineur », 18 donne « majeur ».',
  'les exemples chiffrés choisis pendant l’analyse serviront ensuite de tests', ['p-analyser', 'traitement', 'jeu-tests'])
E('algo-ttc', 'Algorithme PrixTTC', 'Algorithme PrixTTC ; Constante TVA = 0.2 ; Variables prixHT, prixTTC : réel ; Début ; Écrire "Prix HT ?" ; Lire prixHT ; prixTTC ← prixHT * (1 + TVA) ; Écrire "Prix TTC : ", prixTTC ; Fin',
  'l’algorithme suit l’analyse : déclarations, entrée, traitement, sortie', ['p-ecrire-algo', 'constante', 'r-structure', 'r-declarer'])
E('tiroir', 'Le tiroir d’Éduscol', 'La variable S est un tiroir étiqueté S. « S prend la valeur 5000 » : on range 5000 dans le tiroir, et l’ancien contenu est jeté.',
  'une variable est un emplacement de la mémoire qui porte un nom et ne garde qu’une valeur', ['variable', 'memoire', 'nom', 'pr-une-valeur', 'affectation'])
E('memoire-fin', 'Tout s’efface à la fin', 'Un algorithme calcule total = 152 ; une fois l’exécution terminée, total n’existe plus : pour le garder, il faut l’afficher ou l’enregistrer.',
  'la mémoire ne garde les variables que pendant l’exécution', ['memoire', 'execution', 'sortie'])
E('memoire-deux', 'Deux variables, deux emplacements', 'a ← 3 ; b ← a : la mémoire contient deux emplacements, l’un nommé a, l’autre nommé b, qui valent tous deux 3.',
  'chaque variable occupe son propre emplacement dans la mémoire', ['memoire', 'variable', 'r-affecter'])
E('utilisateur-voit', 'Ce que voit l’utilisateur', 'L’algorithme contient Écrire "Ton âge ?" puis Lire age : l’utilisateur voit seulement la question, tape 17 et valide.',
  'l’utilisateur ne voit pas les instructions : il ne connaît que les messages affichés et ce qu’il tape', ['utilisateur', 'lecture', 'r-annoncer'])
E('operation-plus', '3 + 4', 'L’opération 3 + 4 donne 7 ; 3 et 4 restent ce qu’ils sont.',
  'une opération produit une nouvelle valeur sans modifier celles qu’elle utilise', ['operation', 'operateur', 'valeur', 'op-arith'])
E('operation-comparer', 'Comparer est une opération', '7 > 3 donne vrai, 2 > 5 donne faux.',
  'comparer deux valeurs est une opération dont le résultat est un booléen', ['operation', 'op-comp', 'pr-comp-bool', 'booleen'])
E('operation-logique', 'vrai et faux', 'L’opération vrai et faux donne faux ; vrai ou faux donne vrai.',
  'des opérations s’appliquent aussi aux valeurs booléennes', ['operation', 'op-log', 'pr-tables'])
E('execution-deux', 'Deux exécutions, deux résultats', 'Le même algorithme Double (Lire n ; Écrire n * 2) affiche 10 si l’on tape 5, et 14 si l’on tape 7.',
  'chaque exécution travaille avec ses propres données', ['execution', 'entree', 'sortie', 'valeur'])
E('programme-erreur', 'Une parenthèse oubliée', 'En Python, print("Bonjour" (parenthèse oubliée) empêche le programme de s’exécuter ; en pseudo-code, le lecteur comprendrait quand même.',
  'un programme doit respecter exactement la syntaxe du langage, alors que le pseudo-code est plus souple', ['programme', 'pseudo-code'])
E('valeur-fixe', '12 reste 12', 'x ← 12 puis x ← x + 1 : x vaut 13, mais la valeur 12 n’a pas changé ; c’est le contenu de x qui a changé.',
  'une valeur ne change jamais : seule la valeur rangée dans une variable change', ['valeur', 'variable', 'r-affecter'])

# ---------- Données ----------
E('decl-age', 'Une section Variables', 'Variables age : entier ; prixHT, prixTTC : réel ; nom : chaîne ; majeur : booléen',
  'chaque déclaration donne un nom et un type ; plusieurs variables du même type se déclarent sur une ligne', ['declaration', 'r-declarer', 'type', 'variable'])
E('decl-oubli', 'Variable non déclarée', 'La ligne total ← total + x apparaît alors que total n’est pas dans la section Variables : on ne connaît ni son type ni sa valeur de départ.',
  'déclarer chaque variable permet de vérifier qu’on n’en a oublié aucune', ['r-declarer', 'declaration', 'r-initialiser'])
E('decl-sans-valeur', 'Déclarer n’est pas affecter', 'Après la déclaration n : entier, n n’a pas encore de valeur ; il faut n ← 0 ou Lire n avant de l’utiliser.',
  'la déclaration annonce la variable mais ne lui donne aucune valeur', ['declaration', 'affectation', 'r-initialiser', 'r-declarer'])
E('type-compter', 'Compter : entier', 'nbEleves : entier ; on ne peut pas avoir 24.5 élèves.',
  'on choisit entier pour ce qui se compte', ['entier', 'r-choisir-type', 'type'])
E('type-mesurer', 'Mesurer : réel', 'taille : réel ; taille ← 1.75 ; moyenne : réel ; moyenne ← 12.4',
  'on choisit réel pour ce qui se mesure, avec un point décimal', ['reel', 'r-choisir-type'])
E('type-oui-non', 'Oui ou non : booléen', 'majeur : booléen ; majeur ← age >= 18 ; avec age = 17, majeur vaut faux.',
  'un booléen garde le résultat d’une question à réponse oui ou non', ['booleen', 'r-choisir-type', 'pr-bool-deux', 'condition'])
E('type-texte', 'Un texte : chaîne', 'ville : chaîne ; ville ← "Saint-Denis"',
  'on choisit chaîne pour un texte, écrit entre guillemets droits', ['chaine', 'r-choisir-type'])
E('type-symbole', 'Un symbole : caractère', 'reponse : caractère ; Lire reponse ; Si reponse = \'o\' Alors …',
  'un seul symbole tient dans un caractère, écrit entre apostrophes droites', ['caractere', 'r-choisir-type'])
E('sept-trois-types', '7, \'7\' et "7"', '7 est un entier, \'7\' un caractère et "7" une chaîne : 7 + 1 vaut 8, mais \'7\' + 1 n’a pas de sens.',
  'la même écriture change de sens selon son type : le type fixe les opérations permises', ['type', 'entier', 'caractere', 'chaine'])
E('type-refus', 'Une chaîne dans un entier', 'age : entier ; age ← "dix-sept" est une erreur, car "dix-sept" est une chaîne.',
  'une variable ne peut recevoir que des valeurs de son type', ['r-type-fixe', 'type', 'entier'])
E('type-garde', 'moyenne reste réelle', 'moyenne : réel ; moyenne ← 12.5 puis moyenne ← 14.25 : elle reste réelle pendant toute l’exécution.',
  'le type est fixé une fois pour toutes, à la déclaration', ['r-type-fixe', 'reel'])
E('type-conv', '3 dans un réel', 'x : réel ; x ← 3 : x vaut 3.0.',
  'un entier peut entrer dans une variable réelle, où il devient le réel correspondant', ['pr-entier-reel', 'r-type-fixe', 'entier', 'reel'])
E('arrondir', '3.7 dans un entier ?', 'n : entier ; n ← 3.7 est une erreur ; il faudrait décider d’arrondir (4) ou de tronquer (3).',
  'un réel n’entre pas dans un entier sans décider comment arrondir', ['pr-entier-reel', 'entier', 'reel'])
E('moyenne-entiers', 'Moyenne de deux entiers', 'a, b : entier ; m : réel ; a ← 7 ; b ← 8 ; m ← (a + b) / 2 : m vaut 7.5.',
  'le résultat de / est un réel, que l’on range dans une variable réelle', ['pr-entier-reel', 'r-division', 'reel'])
E('bool-valeurs', 'vrai, faux, rien d’autre', 'trouvé : booléen peut valoir vrai ou faux ; "oui", 1 ou "vrai" (entre guillemets) ne sont pas des booléens.',
  'le type booléen n’a que deux valeurs, écrites sans guillemets', ['pr-bool-deux', 'booleen'])
E('bool-resultat', 'Une comparaison rangée', 'pair : booléen ; pair ← n mod 2 = 0 ; avec n = 6, pair vaut vrai.',
  'on peut ranger le résultat d’une comparaison dans une variable booléenne', ['pr-bool-deux', 'booleen', 'pr-comp-bool', 'r-parite'])
E('constante-tva', 'Constante TVA = 0.2', 'Constante TVA = 0.2 ; prixTTC ← prixHT * (1 + TVA) : si la TVA change, on ne modifie qu’une ligne.',
  'une constante donne un nom à une valeur fixe et évite de la recopier partout', ['constante', 'pr-constante'])
E('constante-interdite', 'TVA ← 0.1 ?', 'Après Constante TVA = 0.2, la ligne TVA ← 0.1 est une erreur.',
  'aucune affectation ne peut changer une constante', ['pr-constante', 'constante', 'affectation'])
E('constante-pi', 'Constante PI', 'Constante PI = 3.14159 ; aire ← PI * r * r ; avec r = 2, aire vaut 12.56636.',
  'une constante s’utilise dans les expressions comme une valeur qu’on ne modifie jamais', ['constante', 'pr-constante', 'expression'])
E('chaine-index', 'Les lettres de "Python"', 'ch ← "Python" ; ch[0] vaut \'P\', ch[5] vaut \'n\', et Longueur(ch) vaut 6.',
  'une chaîne se lit comme une liste de caractères, indicée à partir de 0', ['pr-chaine-liste', 'chaine', 'caractere', 'longueur', 'indice'])
E('chaine-vide', 'La chaîne vide', 'ch ← "" : Longueur(ch) vaut 0, et ch[0] n’existe pas.',
  'la chaîne vide ne contient aucun caractère', ['pr-chaine-liste', 'chaine', 'longueur'])
E('compter-a', 'Compter les a de "banane"', 'ch ← "banane" ; n ← 0 ; Pour i de 0 à Longueur(ch) - 1 Faire Si ch[i] = \'a\' Alors n ← n + 1 FinSi FinPour : n vaut 3.',
  'on parcourt une chaîne caractère par caractère, comme une liste', ['pr-chaine-liste', 'r-compter', 'parcours', 'caractere'])

# ---------- Calculs et conditions ----------
E('div-7-2', '7 / 2, 7 div 2, 7 mod 2', '7 / 2 vaut 3.5 ; 7 div 2 vaut 3 ; 7 mod 2 vaut 1.',
  '/ donne un réel, div le quotient entier et mod le reste', ['r-division', 'div-mod', 'op-arith'])
E('div-17-5', '17 = 5 × 3 + 2', '17 div 5 vaut 3 et 17 mod 5 vaut 2 ; on vérifie que 5 × 3 + 2 = 17 et que 2 < 5.',
  'le quotient et le reste vérifient l’égalité de la division euclidienne', ['pr-euclide', 'div-mod', 'r-division'])
E('div-minutes', '130 minutes', '130 div 60 vaut 2 et 130 mod 60 vaut 10 : 130 minutes font 2 h 10 min.',
  'div et mod servent à convertir des durées ou des unités', ['div-mod', 'pr-euclide', 'r-division'])
E('div-chiffres', 'Le chiffre des unités', 'n ← 347 ; n mod 10 vaut 7 (les unités) ; n div 10 vaut 34 (le nombre sans son dernier chiffre).',
  'mod 10 donne le dernier chiffre d’un entier, et div 10 le retire', ['div-mod', 'pr-euclide'])
E('parite-8', '8 est pair, 13 est impair', '8 mod 2 = 0 vaut vrai : 8 est pair ; 13 mod 2 = 0 vaut faux : 13 est impair.',
  'le reste de la division par 2 décide de la parité', ['r-parite', 'div-mod', 'condition'])
E('algo-parite', 'Algorithme Parité', 'Lire n ; Si n mod 2 = 0 Alors Écrire n, " est pair" Sinon Écrire n, " est impair" FinSi ; avec 21, affiche 21 est impair.',
  'le test de parité devient la condition d’une alternative', ['r-parite', 'alternative', 'r-si'])
E('multiple-3', 'Multiple de 3', 'n mod 3 = 0 vaut vrai pour 12 et faux pour 14.',
  'la même méthode teste la divisibilité par n’importe quel entier', ['r-parite', 'div-mod'])
E('prio-2-3-4', '2 + 3 * 4', '2 + 3 * 4 vaut 14 (la multiplication d’abord) ; (2 + 3) * 4 vaut 20.',
  '* passe avant +, et les parenthèses changent l’ordre', ['r-priorite', 'expression', 'op-arith'])
E('prio-moyenne', 'Moyenne sans parenthèses', 'm ← a + b / 2 avec a = 10 et b = 14 donne 17, et non 12 : il fallait m ← (a + b) / 2.',
  'oublier des parenthèses est une erreur fréquente dans les moyennes', ['r-priorite', 'expression'])
E('prio-gauche', '20 / 2 * 5', '20 / 2 * 5 vaut 50 : à priorité égale, on calcule de gauche à droite (20 / 2 = 10, puis 10 * 5).',
  '/ et * ont la même priorité et se calculent de gauche à droite', ['r-priorite', 'op-arith'])
E('expr-valeur', '2 * prix + 1', 'Avec prix = 10, l’expression 2 * prix + 1 vaut 21.',
  'une expression se calcule à partir des valeurs actuelles des variables', ['expression', 'operateur', 'variable'])
E('expr-pas-instr', 'Une expression seule', 'La ligne a + b, seule, ne fait rien : il faut l’utiliser, par exemple s ← a + b ou Écrire a + b.',
  'une expression n’est pas une instruction : elle se place dans une instruction', ['expression', 'instruction', 'affectation'])
E('op-types', '+ selon les types', '3 + 4 vaut 7 ; "3" + "4" vaut "34" ; 3 + "4" est une erreur.',
  'un opérateur n’accepte que certains types, et son effet dépend du type', ['operateur', 'type', 'concatenation'])
E('comp-age', 'age >= 18', 'Avec age = 17, age >= 18 vaut faux ; avec age = 18, il vaut vrai.',
  'une comparaison donne toujours vrai ou faux', ['pr-comp-bool', 'op-comp', 'condition'])
E('comp-diff', '<> veut dire différent', 'reponse <> \'n\' vaut vrai si reponse vaut \'o\', et faux si reponse vaut \'n\'.',
  '<> teste la différence entre deux valeurs', ['op-comp', 'pr-comp-bool', 'caractere'])
E('comp-chaine', 'Comparer des chaînes', '"abc" = "abc" vaut vrai ; "abc" = "Abc" vaut faux.',
  'deux chaînes sont égales seulement si elles ont exactement les mêmes caractères, majuscules comprises', ['op-comp', 'chaine'])
E('et-age', 'age >= 18 et age < 65', 'Avec age = 30 : vrai et vrai donne vrai ; avec age = 70 : vrai et faux donne faux.',
  'et ne vaut vrai que si les deux conditions sont vraies', ['pr-tables', 'op-log', 'condition'])
E('ou-weekend', 'jour = 6 ou jour = 7', 'Avec jour = 7 : faux ou vrai donne vrai ; avec jour = 3 : faux ou faux donne faux.',
  'ou vaut vrai dès qu’au moins une condition est vraie', ['pr-tables', 'op-log'])
E('non-trouve', 'non trouvé', 'Avec trouvé = faux, non trouvé vaut vrai : TantQue non trouvé Faire continue la recherche.',
  'non inverse un booléen', ['pr-tables', 'op-log', 'drapeau'])
E('prio-non-et-ou', 'non a ou b et c', 'Avec a = vrai, b = vrai, c = faux : non a ou b et c se calcule (non a) ou (b et c) = faux ou faux = faux.',
  'non passe avant et, qui passe avant ou', ['r-priorite-log', 'op-log'])
E('prio-log-paren', 'Des parenthèses qui changent tout', '(note < 0 ou note > 20) et saisie n’a pas le même sens que note < 0 ou note > 20 et saisie, qui se lit note < 0 ou (note > 20 et saisie).',
  'sans parenthèses, et est calculé avant ou, ce qui peut changer le sens', ['r-priorite-log', 'condition'])
E('prio-log-tarif', 'Tarif réduit', 'age < 12 ou age >= 65 et etudiant se lit age < 12 ou (age >= 65 et etudiant), ce qui n’était peut-être pas voulu.',
  'le regroupement par défaut n’est pas toujours celui qu’on voulait : mieux vaut écrire les parenthèses', ['r-priorite-log', 'op-log'])
E('egal-fleche-1', 'x ← 5 ou x = 5', 'x ← 5 range 5 dans x ; Si x = 5 Alors … compare x à 5 sans rien modifier.',
  '← agit sur la variable, = pose une question', ['r-egal-fleche', 'affectation', 'op-comp'])
E('egal-fleche-2', 'Si x ← 5 Alors', 'Si x ← 5 Alors … n’a pas de sens : une condition doit être une comparaison, pas une affectation.',
  'on ne met jamais ← dans une condition', ['r-egal-fleche', 'condition'])
E('egal-python', '= et == en Python', 'En Python, x = 5 range 5 dans x, et x == 5 compare ; le pseudo-code, avec ← et =, évite cette confusion.',
  'le signe = n’a pas le même rôle en pseudo-code et en Python', ['r-egal-fleche', 'p-traduire'])
E('intervalle-note', 'Une note entre 0 et 20', 'note >= 0 et note <= 20 vaut vrai pour 15, et faux pour 25 comme pour -2.',
  'un intervalle se teste avec deux comparaisons reliées par et', ['r-intervalle', 'op-log', 'op-comp'])
E('intervalle-hors', 'En dehors d’un intervalle', 'note < 0 ou note > 20 vaut vrai pour 25 : c’est le contraire de l’intervalle.',
  'être en dehors d’un intervalle se teste avec ou', ['r-intervalle', 'pr-tables'])
E('intervalle-age', 'Tranche d’âge', 'age >= 12 et age <= 17 repère un adolescent : vrai pour 15, faux pour 11 et pour 18.',
  'chaque borne s’écrit avec sa propre comparaison', ['r-intervalle', 'condition'])
E('concat-bonjour', '"Bon" + "jour"', '"Bon" + "jour" vaut "Bonjour" ; "jour" + "Bon" vaut "jourBon".',
  'la concaténation met bout à bout, et l’ordre compte', ['r-concat', 'concatenation', 'chaine'])
E('concat-espace', 'Penser à l’espace', '"Bonjour" + prenom avec prenom = "Léa" donne "BonjourLéa" ; il faut "Bonjour " + prenom.',
  'aucun espace n’est ajouté automatiquement', ['r-concat', 'concatenation'])
E('concat-accu', 'Construire une chaîne', 'mot ← "" ; Pour i de 1 à 3 Faire mot ← mot + "ha" FinPour : mot vaut "hahaha".',
  'une chaîne peut servir d’accumulateur, en partant de la chaîne vide', ['r-concat', 'concatenation', 'accumulateur', 'r-accumuler'])

# ---------- Affectation, entrées, sorties ----------
E('x-plus-1', 'x ← x + 1', 'x vaut 3 ; x ← x + 1 : x + 1 est calculé avec l’ancienne valeur (4), puis x prend 4.',
  'le calcul à droite se fait avant le rangement à gauche', ['r-affecter', 'affectation', 'expression', 'pr-fleche'])
E('ecrase', 'L’ancienne valeur est perdue', 'x ← 5 puis x ← 8 : x vaut 8, et rien ne garde la trace du 5.',
  'une affectation remplace l’ancienne valeur', ['r-affecter', 'pr-une-valeur', 'variable'])
E('a-b-copie', 'a ← b ne lie pas a à b', 'b ← 2 ; a ← b ; b ← 9 : a vaut toujours 2.',
  'a reçoit la valeur de b au moment de l’affectation, pas un lien vers b', ['r-affecter', 'affectation'])
E('prend-la-valeur', 'S prend la valeur 5000', 'Éduscol écrit « S prend la valeur 5000 » ; ce support écrit S ← 5000 ; au clavier, on tape S <- 5000.',
  'trois écritures pour la même affectation, qui se lit de droite à gauche', ['pr-fleche', 'affectation'])
E('fleche-sens', 'La flèche montre le sens', 'total ← prix * 2 : la valeur calculée à droite part vers la variable de gauche.',
  'la flèche indique le sens du rangement', ['pr-fleche', 'r-gauche'])
E('gauche-5x', '5 ← x', '5 ← x n’a pas de sens : 5 n’est pas une variable, on ne peut rien y ranger.',
  'à gauche de ← il faut une variable', ['r-gauche', 'affectation'])
E('gauche-somme', 'a + b ← 10', 'a + b ← 10 est une erreur : on ne sait pas comment répartir 10 entre a et b.',
  'à gauche de ← il y a une seule variable, jamais une expression', ['r-gauche', 'expression'])
E('gauche-element', 'L[2] ← 7', 'L[2] ← 7 est correct : un élément de liste se comporte comme une variable.',
  'à gauche de ← peut aussi figurer un élément de liste ou un champ', ['r-gauche', 'element', 'r-indice'])
E('init-somme', 'somme ← 0 oublié', 'Sans somme ← 0 avant la boucle, somme ← somme + x utilise une valeur inconnue au premier tour : le résultat est faux.',
  'une variable utilisée dans un calcul doit d’abord recevoir une valeur', ['r-initialiser', 'accumulateur', 'r-accumuler'])
E('init-compteur', 'n ← 0 avant de compter', 'n ← 0 ; Pour … Si note >= 10 Alors n ← n + 1 FinSi FinPour : sans n ← 0, le compte part d’une valeur inconnue.',
  'un compteur commence à 0, avant la boucle', ['r-initialiser', 'compteur', 'r-compter'])
E('init-max', 'max ← L[0], pas 0', 'Pour un maximum, on initialise max ← L[0] et non max ← 0 : avec [-5, -2, -8], max ← 0 donnerait 0, qui n’est même pas dans la liste.',
  'la valeur de départ doit être choisie avec soin, ce n’est pas toujours 0', ['r-initialiser', 'p-maximum'])
E('lire-age', 'Lire age', 'Lire age : l’algorithme s’arrête ; l’utilisateur tape 17 ; age vaut 17 et l’exécution continue.',
  'Lire attend une valeur de l’utilisateur et la range dans la variable', ['r-lire', 'lecture', 'entree', 'utilisateur'])
E('lire-ecrase', 'Lire remplace', 'x ← 5 ; Lire x ; l’utilisateur tape 2 : x vaut 2.',
  'comme une affectation, Lire remplace l’ancienne valeur', ['r-lire', 'lecture', 'pr-une-valeur'])
E('lire-saisir', 'Saisir N', 'Éduscol écrit Saisir N : c’est la même instruction que Lire N.',
  'Lire est le nom, dans ce support, de l’entrée des données d’Éduscol', ['r-lire', 'lecture'])
E('annonce-age', 'Une question avant Lire', 'Écrire "Ton âge ?" ; Lire age : l’utilisateur sait quoi taper.',
  'un message avant Lire guide l’utilisateur', ['r-annoncer', 'ecriture', 'lecture'])
E('annonce-oubli', 'Un écran muet', 'Sans message, Lire n laisse l’utilisateur devant un écran vide : il ne sait pas qu’on attend un nombre.',
  'Lire seul n’affiche rien', ['r-annoncer', 'utilisateur'])
E('annonce-unite', 'Préciser l’unité', 'Écrire "Taille en mètres (ex. 1.75) ?" ; Lire taille : l’utilisateur tape 1.75 et non 175.',
  'un bon message précise aussi le format attendu', ['r-annoncer', 'reel'])
E('ecrire-msg-var', 'Écrire "Moyenne : ", m', 'Avec m = 12.5, Écrire "Moyenne : ", m affiche Moyenne : 12.5.',
  'le texte s’affiche tel quel, la variable par sa valeur', ['r-ecrire', 'ecriture', 'sortie'])
E('ecrire-guillemets', 'Écrire m ou Écrire "m"', 'Avec m = 12.5, Écrire m affiche 12.5, alors que Écrire "m" affiche la lettre m.',
  'les guillemets font la différence entre un texte et une variable', ['r-ecrire', 'ecriture', 'chaine'])
E('ecrire-expr', 'Écrire a + b', 'Avec a = 2 et b = 3, Écrire "Somme : ", a + b affiche Somme : 5.',
  'Écrire peut afficher la valeur d’une expression', ['r-ecrire', 'expression', 'ecriture'])

# ---------- Alternatives ----------
E('si-majeur', 'Majeur ou mineur', 'Si age >= 18 Alors Écrire "majeur" Sinon Écrire "mineur" FinSi ; avec age = 16, affiche mineur.',
  'selon la condition, un seul des deux blocs s’exécute', ['r-si', 'alternative', 'condition', 'structure-controle'])
E('si-une-fois', 'La condition est calculée une fois', 'Si x > 0 Alors x ← -x Sinon Écrire "négatif" FinSi ; avec x = 4 : x devient -4, et le Sinon ne s’exécute pas, même si x est maintenant négatif.',
  'la condition est évaluée une seule fois, au début du Si', ['r-si', 'alternative'])
E('si-reprise', 'Après FinSi', 'Si n > 10 Alors Écrire "grand" FinSi ; Écrire "fin" : fin s’affiche dans tous les cas.',
  'après le Si, l’exécution reprend à la ligne qui suit FinSi', ['r-si', 'r-si-sans-sinon', 'bloc'])
E('bonus', 'Bonus seulement si…', 'Si note >= 18 Alors bonus ← bonus + 1 FinSi ; avec note = 12, rien ne change.',
  'sans Sinon, une condition fausse ne déclenche rien', ['r-si-sans-sinon', 'alternative'])
E('valeur-absolue', 'Valeur absolue', 'Si x < 0 Alors x ← -x FinSi ; avec -3, x devient 3 ; avec 5, x reste 5.',
  'un Si sans Sinon suffit quand un seul cas demande une action', ['r-si-sans-sinon', 'alternative'])
E('plus-grand-deux', 'Le plus grand de deux nombres', 'Si a > b Alors max ← a Sinon max ← b FinSi ; avec a = 3 et b = 8, max vaut 8.',
  'chacune des deux branches donne une valeur à max', ['alternative', 'r-si', 'structure-controle'])
E('mentions', 'Les mentions', 'Si note >= 16 Alors "TB" Sinon Si note >= 14 Alors "B" Sinon Si note >= 12 Alors "AB" Sinon "aucune" FinSi FinSi FinSi ; 15 donne B.',
  'des Si imbriqués distinguent plusieurs cas, testés du plus exigeant au moins exigeant', ['r-cas-multiples', 'si-imbrique'])
E('mentions-ordre', 'Tests dans le mauvais ordre', 'Si l’on teste d’abord note >= 12, une note de 17 reçoit la mention AB : le premier test vrai l’emporte.',
  'dans des Si imbriqués, l’ordre des tests compte', ['r-cas-multiples', 'si-imbrique'])
E('signe', 'Positif, négatif ou nul', 'Si n > 0 Alors "positif" Sinon Si n < 0 Alors "négatif" Sinon "nul" FinSi FinSi ; 0 donne nul.',
  'trois cas qui s’excluent demandent deux Si imbriqués, chacun avec son retrait', ['r-cas-multiples', 'si-imbrique', 'indentation'])
E('selon-jour', 'Jour de la semaine', 'Selon jour Faire Cas 1 : Écrire "lundi" ; Cas 2 : Écrire "mardi" ; … ; Autrement : Écrire "erreur" FinSelon ; avec jour = 2, affiche mardi.',
  'seul le Cas égal à la valeur s’exécute', ['r-selon', 'selon', 'structure-controle'])
E('selon-autrement', 'Aucun Cas ne correspond', 'Avec jour = 9 dans le Selon des jours, aucun Cas ne correspond : Autrement affiche erreur.',
  'Autrement traite toutes les valeurs non prévues', ['r-selon', 'selon'])
E('selon-menu', 'Un menu', 'Lire choix ; Selon choix Faire Cas \'a\' : ajouter un élément ; Cas \'q\' : quitter ; Autrement : Écrire "choix inconnu" FinSelon',
  'Selon convient bien aux menus, où chaque touche déclenche une action', ['r-selon', 'selon', 'caractere', 'r-choisir-selon'])
E('si-vers-selon', 'Trois Si sur mois', 'Si mois = 1 … Si mois = 2 … Si mois = 3 … se remplace par Selon mois Faire Cas 1 : … Cas 2 : … Cas 3 : … FinSelon.',
  'des Si qui testent l’égalité d’une même variable deviennent un Selon plus lisible', ['r-choisir-selon', 'selon', 'alternative'])
E('selon-impossible', 'Selon ne compare pas', 'On ne peut pas écrire Cas note >= 16 dans un Selon : chaque Cas est une valeur précise.',
  'Selon ne teste que l’égalité, pas les intervalles', ['r-choisir-selon', 'selon'])

# ---------- Boucles ----------
E('pour-1-5', 'Pour i de 1 à 5', 'Pour i de 1 à 5 Faire Écrire i FinPour affiche 1 2 3 4 5.',
  'le compteur prend chaque valeur de 1 à 5, borne d’arrivée incluse', ['r-pour', 'pour', 'compteur', 'iteration', 'boucle'])
E('pour-tours', 'Combien de tours ?', 'Pour i de 3 à 7 fait 7 - 3 + 1 = 5 tours ; Pour i de 0 à N - 1 fait N tours.',
  'le nombre de tours se calcule avant de commencer', ['pr-pour-tours', 'pour'])
E('pour-zero', 'Pour i de 1 à 0', 'Avec N = 0, Pour i de 1 à N Faire … ne fait aucun tour.',
  'si la valeur de départ dépasse celle d’arrivée, le bloc ne s’exécute pas', ['pr-pour-tours', 'pour', 'iteration'])
E('table-7', 'Table de 7', 'Pour i de 1 à 10 Faire Écrire 7, " × ", i, " = ", 7 * i FinPour affiche les 10 lignes de la table de 7.',
  'le compteur s’utilise dans le bloc pour faire varier le calcul', ['r-pour', 'compteur', 'pour'])
E('pas-2', 'Pour i de 0 à 10 pas 2', 'Pour i de 0 à 10 pas 2 Faire Écrire i FinPour affiche 0 2 4 6 8 10.',
  'le pas change l’avance du compteur', ['pas', 'pour', 'pr-pour-tours'])
E('rebours', 'Compte à rebours', 'Pour i de 10 à 1 pas -1 Faire Écrire i FinPour affiche 10 9 8 … 1.',
  'un pas négatif fait diminuer le compteur jusqu’à la valeur d’arrivée', ['r-pas-negatif', 'pas'])
E('rebours-liste', 'Une liste à l’envers', 'Pour i de Longueur(L) - 1 à 0 pas -1 Faire Écrire L[i] FinPour ; avec L = [4, 7, 1], affiche 1 7 4.',
  'le pas -1 permet de parcourir une liste de la fin vers le début', ['r-pas-negatif', 'parcours', 'indice'])
E('rebours-3', 'Pour i de 9 à 0 pas -3', 'i vaut 9, 6, 3, puis 0 : quatre tours.',
  'le compteur diminue de 3 à chaque tour tant qu’il reste supérieur ou égal à la valeur d’arrivée', ['r-pas-negatif', 'pas'])
E('compteur-modifie', 'i ← i + 1 dans un Pour', 'Pour i de 1 à 10 Faire Écrire i ; i ← i + 1 FinPour : un nombre sur deux est sauté, et le nombre de tours devient incertain.',
  'modifier le compteur dans le bloc brouille la boucle', ['r-compteur-intouchable', 'compteur', 'pour'])
E('compteur-lu', 'Utiliser i sans le changer', 'Pour i de 1 à 5 Faire carre ← i * i ; Écrire carre FinPour : i est lu, jamais affecté.',
  'dans le bloc, on lit le compteur mais on ne l’affecte pas', ['r-compteur-intouchable', 'compteur'])
E('compteur-tq', 'Avancer autrement : TantQue', 'Pour avancer de 2 en 2, on écrit pas 2 ; si l’avance dépend des données, on prend une boucle TantQue.',
  'si l’avance du compteur doit varier, la boucle Pour n’est pas la bonne', ['r-compteur-intouchable', 'r-choisir-boucle', 'pas'])
E('tq-doubler', 'Doubler jusqu’à 100', 'x ← 1 ; TantQue x < 100 Faire x ← x * 2 FinTantQue : x vaut 128, après 7 tours.',
  'la condition est testée avant chaque tour, et la boucle s’arrête quand elle devient fausse', ['r-tantque', 'tantque', 'iteration', 'condition'])
E('tq-zero', 'TantQue n < 0 avec n = 3', 'n ← 3 ; TantQue n < 0 Faire n ← n + 1 FinTantQue : aucun tour.',
  'si la condition est fausse dès le départ, le bloc ne s’exécute jamais', ['pr-tq-zero', 'tantque', 'r-tantque'])
E('epargne', 'Doubler son épargne', 'capital ← 1000 ; annees ← 0 ; TantQue capital < 2000 Faire capital ← capital * 1.05 ; annees ← annees + 1 FinTantQue : annees vaut 15.',
  'TantQue convient quand le nombre de tours n’est pas connu d’avance', ['r-tantque', 'tantque', 'r-choisir-boucle', 'compteur'])
E('tq-liste-vide', 'Une liste vide', 'i ← 0 ; TantQue i < Longueur(L) Faire … ; avec L = [], aucun tour : la liste vide est traitée sans erreur.',
  'le test fait avant le premier tour protège des cas vides', ['pr-tq-zero', 'tantque', 'jeu-tests'])
E('rep-note', 'Redemander une note', 'Répéter Écrire "Note ?" ; Lire note Jusqu’à note >= 0 et note <= 20 ; l’utilisateur tape 25 puis 14 : note vaut 14.',
  'le bloc s’exécute, puis la condition décide s’il faut recommencer', ['r-repeter', 'repeter', 'p-saisie'])
E('rep-un-tour', 'Condition déjà vraie', 'x ← 50 ; Répéter x ← x + 1 Jusqu’à x > 10 : x vaut 51, un tour a été fait.',
  'Répéter fait toujours au moins un tour, même si la condition est déjà vraie', ['pr-rep-un', 'repeter'])
E('rep-de', 'Lancer un dé jusqu’au 6', 'Répéter : de prend un nombre tiré au hasard entre 1 et 6 ; essais ← essais + 1 ; Jusqu’à de = 6.',
  'on ne sait pas combien de lancers il faudra, mais il en faut au moins un', ['pr-rep-un', 'repeter', 'r-choisir-boucle'])
E('rep-vs-tq', 'Jusqu’à ou TantQue', 'Répéter … Jusqu’à x > 10 s’arrête quand x > 10 ; TantQue x <= 10 Faire … tourne tant que x <= 10 : les deux conditions sont contraires.',
  'Jusqu’à donne la condition d’arrêt, TantQue la condition pour continuer', ['r-repeter', 'repeter', 'tantque'])
E('infinie-oubli', 'i jamais modifié', 'i ← 0 ; TantQue i < 10 Faire Écrire i FinTantQue : i reste à 0, la boucle ne s’arrête jamais.',
  'si le bloc ne modifie aucune variable de la condition, la boucle est infinie', ['boucle-infinie', 'r-faire-evoluer', 'tantque'])
E('infinie-sens', 'i ← i - 1 au lieu de i + 1', 'i ← 0 ; TantQue i < 10 Faire i ← i - 1 FinTantQue : i s’éloigne de 10, la boucle est infinie.',
  'la variable doit évoluer dans le bon sens', ['boucle-infinie', 'r-faire-evoluer'])
E('div-par-2', 'Diviser par 2 jusqu’à 1', 'n ← 100 ; TantQue n > 1 Faire n ← n div 2 FinTantQue : n vaut 50, 25, 12, 6, 3, 1, puis la boucle s’arrête.',
  'une instruction du bloc modifie n, qui finit par rendre la condition fausse', ['r-faire-evoluer', 'tantque', 'div-mod'])
E('choisir-pour', '10 notes : Pour', 'Saisir exactement 10 notes : on sait qu’il faut 10 tours, on prend Pour i de 1 à 10.',
  'nombre de tours connu d’avance : boucle Pour', ['r-choisir-boucle', 'pour'])
E('choisir-tq', 'Jusqu’à -1 : TantQue', 'Lire des notes jusqu’à ce que l’utilisateur tape -1 : on lit une première note, puis TantQue note <> -1 Faire … traiter la note, lire la suivante … FinTantQue.',
  'nombre de tours inconnu : boucle TantQue', ['r-choisir-boucle', 'tantque'])
E('choisir-rep', 'Mot de passe : Répéter', 'Demander un mot de passe jusqu’à ce qu’il soit correct : il faut le demander au moins une fois, on prend Répéter.',
  'bloc à exécuter au moins une fois : boucle Répéter', ['r-choisir-boucle', 'repeter'])
E('pour-en-tq', 'Un Pour réécrit en TantQue', 'Pour i de 1 à 3 Faire Écrire i FinPour équivaut à i ← 1 ; TantQue i <= 3 Faire Écrire i ; i ← i + 1 FinTantQue : les deux affichent 1 2 3.',
  'une boucle Pour est un TantQue dont le compteur est géré automatiquement', ['r-pour-tantque', 'pour', 'tantque'])
E('pour-en-tq-oubli', 'L’avance oubliée', 'Dans la version TantQue, oublier i ← i + 1 donne une boucle infinie ; la boucle Pour, elle, ne peut pas l’oublier.',
  'la boucle Pour évite d’oublier l’avance du compteur', ['r-pour-tantque', 'boucle-infinie'])
E('for-while', 'for et while en Python', 'for i in range(1, 4): et i = 1 ; while i <= 3: … i = i + 1 affichent les mêmes valeurs.',
  'l’équivalence entre les deux boucles existe aussi en Python', ['r-pour-tantque', 'p-traduire'])
E('somme-1-100', 'Somme de 1 à 100', 's ← 0 ; Pour i de 1 à 100 Faire s ← s + i FinPour : s vaut 5050.',
  'l’accumulateur part de 0 et grossit à chaque tour', ['r-accumuler', 'accumulateur', 'r-initialiser'])
E('produit-1-5', 'Produit de 1 à 5', 'p ← 1 ; Pour i de 1 à 5 Faire p ← p * i FinPour : p vaut 120.',
  'un produit s’initialise à 1, pas à 0, sinon il resterait nul', ['r-accumuler', 'accumulateur'])
E('somme-liste', 'Somme d’une liste', 'total ← 0 ; Pour i de 0 à Longueur(L) - 1 Faire total ← total + L[i] FinPour ; avec L = [4, 7, 1], total vaut 12.',
  'l’accumulation se combine avec le parcours d’une liste', ['r-accumuler', 'accumulateur', 'parcours', 'r-parcourir'])
E('compter-reussis', 'Notes d’au moins 10', 'n ← 0 ; Pour i de 0 à Longueur(L) - 1 Faire Si L[i] >= 10 Alors n ← n + 1 FinSi FinPour ; avec [12, 8, 15, 10], n vaut 3.',
  'le compteur n’augmente que lorsque la condition est vraie', ['r-compter', 'compteur', 'p-compter'])
E('compter-pairs', 'Nombres pairs de 1 à 10', 'n ← 0 ; Pour i de 1 à 10 Faire Si i mod 2 = 0 Alors n ← n + 1 FinSi FinPour : n vaut 5.',
  'on peut compter les valeurs du compteur de boucle qui vérifient une condition', ['r-compter', 'r-parite'])
E('compter-tours', 'Compter les tours d’un TantQue', 'n ← 0 ; TantQue x > 1 Faire x ← x div 2 ; n ← n + 1 FinTantQue ; avec x = 32, n vaut 5.',
  'un compteur mesure combien de tours a fait une boucle non bornée', ['compteur', 'r-compter', 'cout-log'])
E('drapeau-negatif', 'Y a-t-il un nombre négatif ?', 'neg ← faux ; Pour i de 0 à Longueur(L) - 1 Faire Si L[i] < 0 Alors neg ← vrai FinSi FinPour ; avec [3, -1, 4], neg vaut vrai.',
  'le drapeau se lève une fois et reste levé', ['r-drapeau', 'drapeau'])
E('drapeau-erreur', 'Un drapeau rebaissé', 'Avec Si L[i] < 0 Alors neg ← vrai Sinon neg ← faux FinSi, la liste [3, -1, 4] donne neg = faux, car le dernier élément le remet à faux.',
  'un drapeau ne doit jamais être baissé dans la boucle', ['r-drapeau', 'drapeau'])
E('drapeau-arret', 'Arrêter la boucle', 'trouvé ← faux ; i ← 0 ; TantQue i < Longueur(L) et non trouvé Faire … FinTantQue',
  'le drapeau sert aussi à arrêter une boucle TantQue dès que l’événement arrive', ['r-drapeau', 'drapeau', 'p-recherche'])
E('iteration-valeurs', 'Un tour, de nouvelles valeurs', 'Dans Pour i de 1 à 3 Faire s ← s + i FinPour (avec s ← 0 avant) : au tour 1, s vaut 1 ; au tour 2, 3 ; au tour 3, 6.',
  'les variables changent d’un tour à l’autre : chaque tour est une itération', ['iteration', 'trace', 'accumulateur'])
E('boucle-cent', 'Cent lignes ou trois', 'Écrire 1 ; Écrire 2 ; … ; Écrire 100 fait cent lignes ; avec une boucle Pour, trois lignes suffisent.',
  'une boucle évite de recopier un bloc identique', ['boucle', 'pour', 'structure-controle'])

# ---------- Listes et données composées ----------
E('notes-liste', 'notes ← [12, 15, 9]', 'notes : liste de réel ; notes ← [12, 15, 9] ; notes[0] vaut 12 et notes[2] vaut 9.',
  'une liste range plusieurs valeurs sous un seul nom, repérées par leur indice', ['liste', 'indice', 'element', 'r-indice', 'pr-indices'])
E('dernier-indice', 'Le dernier indice', 'Pour L = [5, 8, 2, 6], Longueur(L) vaut 4 et les indices vont de 0 à 3 : L[3] vaut 6.',
  'le dernier indice est la longueur moins 1', ['pr-indices', 'longueur', 'indice'])
E('element-modifier', 'L[1] ← 0', 'L ← [5, 8, 2] ; L[1] ← 0 : L vaut [5, 0, 2].',
  'un élément s’utilise comme une variable : on peut lui affecter une valeur', ['r-indice', 'element'])
E('indice-variable', 'L[i] avec i variable', 'i ← 2 ; Écrire L[i] affiche le troisième élément ; i ← i + 1 ; Écrire L[i] affiche le quatrième.',
  'l’indice peut être une variable, ce qui permet les parcours', ['r-indice', 'indice', 'parcours'])
E('hors-limites-4', 'L[4] dans une liste de 4', 'L ← [5, 8, 2, 6] ; Écrire L[4] est une erreur : les indices s’arrêtent à 3.',
  'un indice égal à la longueur sort de la liste', ['r-hors-limites', 'pr-indices'])
E('hors-limites-boucle', 'Un tour de trop', 'Pour i de 0 à Longueur(L) Faire Écrire L[i] FinPour fait un tour de trop : le dernier accès, L[Longueur(L)], est une erreur.',
  'la borne d’un parcours est Longueur(L) - 1, pas Longueur(L)', ['r-hors-limites', 'r-parcourir', 'longueur'])
E('hors-limites-vide', 'L[0] dans une liste vide', 'L ← [] ; Écrire L[0] est une erreur : la liste vide n’a aucun élément.',
  'même l’indice 0 n’existe pas dans une liste vide', ['r-hors-limites', 'longueur', 'jeu-tests'])
E('parcours-afficher', 'Afficher chaque élément', 'Pour i de 0 à Longueur(L) - 1 Faire Écrire L[i] FinPour ; avec [3, 1, 4], affiche 3 1 4.',
  'le parcours visite chaque élément, dans l’ordre des indices', ['r-parcourir', 'parcours', 'longueur'])
E('parcours-vide', 'Parcourir une liste vide', 'Avec L = [], Pour i de 0 à Longueur(L) - 1 devient Pour i de 0 à -1 : aucun tour, aucune erreur.',
  'le parcours écrit avec Longueur(L) - 1 fonctionne aussi pour la liste vide', ['r-parcourir', 'pr-pour-tours', 'longueur'])
E('ajouter-fin', 'Ajouter(L, 14)', 'L ← [12, 15] ; Ajouter(L, 14) : L vaut [12, 15, 14] et Longueur(L) vaut 3.',
  'Ajouter met l’élément à la fin et augmente la longueur de 1', ['r-ajouter', 'liste', 'longueur'])
E('ajouter-construire', 'Construire une liste', 'L ← [] ; Pour i de 1 à 5 Faire Ajouter(L, i * i) FinPour : L vaut [1, 4, 9, 16, 25].',
  'on construit une liste en partant de la liste vide et en ajoutant les éléments un par un', ['r-ajouter', 'liste', 'accumulateur'])
E('ajouter-saisie', 'Garder les saisies', 'notes ← [] ; Pour i de 1 à 3 Faire Lire x ; Ajouter(notes, x) FinPour ; l’utilisateur tape 12, 9 et 15 : notes vaut [12, 9, 15].',
  'Ajouter permet de garder toutes les valeurs saisies', ['r-ajouter', 'lecture'])
E('meme-type-ok', 'Une liste de réels', 'notes : liste de réel accepte [12.5, 9, 15] ; [12, "absent", 15] ne convient pas.',
  'tous les éléments d’une liste ont le même type', ['pr-meme-type', 'liste'])
E('prenoms', 'Une liste de chaînes', 'prenoms : liste de chaîne ; prenoms ← ["Léa", "Noé", "Inès"]',
  'une liste peut contenir des valeurs de n’importe quel type, du moment que c’est toujours le même', ['pr-meme-type', 'liste', 'chaine'])
E('meme-type-enreg', 'Des données mélangées', 'Pour un élève, on a un nom (chaîne) et une moyenne (réel) : on ne les met pas dans une même liste, mais dans un enregistrement.',
  'des données de types différents ne vont pas ensemble dans une liste', ['pr-meme-type', 'r-liste-ou-enreg', 'enregistrement'])
E('doubler-liste', 'Doubler les éléments', 'Procédure Doubler(L : liste d’entier) fait L[i] ← 2 * L[i] pour chaque i ; T ← [1, 2] ; Doubler(T) : T vaut [2, 4].',
  'une liste passée à un sous-programme est partagée : ses modifications sont visibles chez l’appelant', ['pr-partage', 'procedure-sp', 'parametre'])
E('trier-sur-place', 'Trier sur place', 'TriSélection(notes) ne retourne rien : après l’appel, c’est la liste notes elle-même qui est triée.',
  'c’est grâce au partage qu’une procédure de tri peut modifier la liste', ['pr-partage', 'p-tri-selection', 'procedure-sp'])
E('partage-python', 'Le même comportement en Python', 'def doubler(L): L[0] = 2 * L[0] ; T = [5] ; doubler(T) : T vaut [10].',
  'le pseudo-code de ce support se comporte comme Python pour les listes', ['pr-partage', 'p-traduire'])
E('triee-oui', 'Triée ou non ?', '[2, 5, 5, 9] est triée ; [2, 9, 5] ne l’est pas, car 9 > 5.',
  'chaque élément doit être inférieur ou égal au suivant', ['liste-triee'])
E('triee-limites', 'Listes triées d’office', '[] et [7] sont triées : aucun élément n’est plus grand que celui qui le suit.',
  'la liste vide et une liste d’un seul élément sont triées', ['liste-triee', 'jeu-tests'])
E('annuaire', '1 000 noms triés', 'Dans un annuaire trié de 1 000 noms, on regarde le milieu : le nom cherché est avant ou après ; en 10 étapes au plus, on le trouve ou l’on sait qu’il n’y est pas.',
  'sur une liste triée, chaque comparaison élimine la moitié des éléments', ['pr-dicho', 'liste-triee', 'cout-log', 'p-dichotomie'])
E('deviner', 'Deviner un nombre', 'Deviner un nombre entre 1 et 100 en proposant toujours le milieu (50, puis 25 ou 75…) : 7 essais suffisent.',
  'couper l’intervalle en deux à chaque fois est une dichotomie', ['pr-dicho', 'cout-log', 'r-cout-log'])
E('dicho-non-triee', 'Dichotomie sur [9, 2, 7]', 'Chercher 9 dans [9, 2, 7] par dichotomie : au milieu, 2 < 9, on cherche à droite… et on ne trouve pas 9, qui est pourtant en première position.',
  'sur une liste non triée, la dichotomie peut se tromper', ['r-precondition-dicho', 'liste-triee', 'precondition'])
E('dicho-verifier', 'Respecter la précondition', 'Avant d’appeler RechercheDicho(L, v), on s’assure que L est triée, ou on la trie d’abord.',
  'c’est à l’appelant de respecter la précondition', ['r-precondition-dicho', 'precondition'])
E('dicho-decroissant', 'Triée dans l’autre sens', '[9, 7, 2] est triée dans l’ordre décroissant : la version croissante de la dichotomie part du mauvais côté et peut rater la valeur.',
  'la précondition dit précisément quel ordre est attendu', ['r-precondition-dicho', 'liste-triee'])
E('grille-3x3', 'Une grille 3 × 3', 'M ← [[1, 2, 3], [4, 5, 6], [7, 8, 9]] ; M[1] vaut [4, 5, 6] et M[1][2] vaut 6.',
  'le premier indice choisit la ligne, le second la colonne', ['r-deux-indices', 'liste-listes', 'indice'])
E('grille-modif', 'M[0][0] ← 0', 'Dans la grille de 1 à 9, M[0][0] ← 0 remplace 1 par 0.',
  'un élément d’une liste de listes s’utilise comme une variable', ['r-deux-indices', 'liste-listes', 'element'])
E('morpion', 'Un plateau de morpion', 'plateau : liste de liste de caractère ; plateau[2][0] ← \'X\' place une croix en bas à gauche.',
  'une liste de listes représente naturellement un plateau de jeu', ['r-deux-indices', 'liste-listes', 'caractere'])
E('grille-somme', 'Somme d’une grille', 'total ← 0 ; Pour i … Pour j de 0 à Longueur(M[i]) - 1 Faire total ← total + M[i][j] FinPour FinPour : 45 pour la grille de 1 à 9.',
  'deux boucles imbriquées visitent toutes les cases', ['r-double-boucle', 'p-grille', 'liste-listes'])
E('grille-afficher', 'Afficher ligne par ligne', 'Pour i … Pour j … Écrire M[i][j], " " FinPour, puis un passage à la ligne, FinPour : la grille s’affiche en 3 lignes.',
  'la boucle extérieure parcourt les lignes, la boucle intérieure les colonnes', ['r-double-boucle', 'p-grille'])
E('grille-cout', 'Une grille de 100 × 100', 'Pour une grille de 100 lignes et 100 colonnes, la double boucle fait 10 000 tours.',
  'parcourir une grille de n lignes et n colonnes demande n² opérations', ['r-double-boucle', 'r-cout-quadratique', 'cout-quadratique'])
E('type-eleve', 'Type Élève', 'Type Élève = Enregistrement nom : chaîne ; age : entier ; moyenne : réel FinEnregistrement ; e : Élève',
  'un enregistrement regroupe des données de types différents sur un même objet', ['enregistrement', 'champ', 'type'])
E('eleve-champs', 'e.moyenne ← 14.5', 'e.nom ← "Léa" ; e.moyenne ← 14.5 ; Écrire e.nom, " : ", e.moyenne affiche Léa : 14.5.',
  'chaque champ se lit et s’affecte comme une variable de son type', ['r-champ', 'champ', 'enregistrement'])
E('classe', 'Une classe d’élèves', 'classe : liste de Élève ; classe[0].nom désigne le nom du premier élève de la liste.',
  'liste et enregistrement se combinent : une liste d’objets, chacun avec ses champs', ['r-champ', 'liste', 'enregistrement', 'r-liste-ou-enreg'])
E('produit', 'Un produit en stock', 'Type Produit = Enregistrement libelle : chaîne ; prix : réel ; stock : entier FinEnregistrement ; après une vente, p.stock ← p.stock - 1.',
  'un enregistrement décrit un objet réel par ses champs', ['enregistrement', 'champ', 'r-champ'])
E('notes-ou-fiche', 'Des notes ou une fiche ?', 'Les 30 notes d’un devoir vont dans une liste de réel ; le nom, l’âge et la moyenne d’un élève vont dans un enregistrement.',
  'même type et même rôle : liste ; données différentes d’un même objet : enregistrement', ['r-liste-ou-enreg', 'liste', 'enregistrement'])
E('temperatures', 'Températures de la semaine', 'temp : liste de réel de 7 éléments, temp[0] pour lundi, plutôt que sept variables t1, t2, …, t7.',
  'une liste évite de multiplier des variables de même rôle et permet les parcours', ['r-liste-ou-enreg', 'liste'])

# ---------- Sous-programmes ----------
E('carre', 'Fonction Carré', 'Fonction Carré(x : réel) : réel ; Début ; Retourner x * x ; Fin ; y ← Carré(3) : y vaut 9.',
  'une fonction reçoit une valeur, calcule et retourne un résultat', ['fonction', 'r-appel', 'retour', 'parametre', 'argument', 'appel'])
E('appel-expr', 'Deux appels dans une expression', 'z ← Carré(2) + Carré(3) : les deux appels sont remplacés par 4 et 9, donc z vaut 13.',
  'un appel de fonction est remplacé par sa valeur de retour', ['r-appel', 'appel', 'retour', 'expression'])
E('puissance-ordre', 'Puissance(2, 3) ou Puissance(3, 2)', 'Fonction Puissance(x : réel, n : entier) : réel ; Puissance(2, 3) vaut 8, mais Puissance(3, 2) vaut 9.',
  'les arguments se placent dans l’ordre des paramètres', ['r-appel', 'argument', 'parametre'])
E('argument-calcule', 'Un argument calculé', 'Carré(a + 1) avec a = 4 : l’argument a + 1 est calculé d’abord (5), puis x reçoit 5 ; le résultat est 25.',
  'un argument peut être une expression, calculée avant l’appel', ['argument', 'r-appel'])
E('apres-retourner', 'Une ligne jamais exécutée', 'Fonction F() : entier ; Début ; Retourner 1 ; Écrire "jamais" ; Fin : le message ne s’affiche jamais.',
  'Retourner termine aussitôt la fonction', ['r-retourner', 'retour', 'fonction'])
E('deux-retourner', 'Deux Retourner', 'Fonction Max2(a, b : réel) : réel ; Si a > b Alors Retourner a FinSi ; Retourner b : avec 7 et 3, le premier Retourner termine la fonction.',
  'plusieurs Retourner sont possibles : le premier exécuté termine la fonction', ['r-retourner', 'retour', 'p-fonction'])
E('retourner-boucle', 'Retourner dans une boucle', 'Fonction Contient(L, v) : booléen ; Pour i … Si L[i] = v Alors Retourner vrai FinSi FinPour ; Retourner faux',
  'Retourner dans une boucle arrête aussi la boucle : la recherche s’arrête dès que v est trouvée', ['r-retourner', 'fonction', 'p-recherche'])
E('trois-classes', 'Une moyenne pour trois classes', 'Pour trois classes, au lieu de recopier trois fois le calcul de la moyenne, on écrit une Fonction Moyenne(L) et on l’appelle trois fois.',
  'un traitement répété s’écrit une seule fois dans un sous-programme', ['r-decouper', 'sous-programme', 'appel'])
E('principal-lisible', 'Un algorithme principal lisible', 'Début ; notes ← SaisirNotes(N) ; m ← Moyenne(notes) ; AfficherBilan(notes, m) ; Fin',
  'découpé en sous-programmes, l’algorithme principal se lit comme un plan', ['r-decouper', 'sous-programme', 'procedure-sp'])
E('tester-a-part', 'Tester à part', 'On vérifie que Moyenne([10, 20]) vaut 15 avant de l’utiliser dans le bilan.',
  'un sous-programme se teste séparément, avec ses propres cas', ['r-decouper', 'sous-programme', 'jeu-tests'])
E('moyenne-ou-bilan', 'Moyenne ou AfficherBilan', 'Moyenne(L) calcule une valeur : c’est une Fonction ; AfficherBilan(L, m) ne fait qu’afficher : c’est une Procédure.',
  'on choisit une fonction quand l’appelant a besoin d’une valeur', ['r-fonction-ou-procedure', 'fonction', 'procedure-sp'])
E('afficher-ligne', 'Procédure AfficherLigne', 'Procédure AfficherLigne(n : entier) ; Début ; Pour i de 1 à n Faire Écrire "*" FinPour ; Fin ; l’appel AfficherLigne(5) affiche *****.',
  'une procédure agit sans renvoyer de valeur et s’appelle seule sur sa ligne', ['procedure-sp', 'r-fonction-ou-procedure', 'appel'])
E('procedure-expr', 'y ← AfficherLigne(3) ?', 'y ← AfficherLigne(3) n’a pas de sens : une procédure ne retourne aucune valeur.',
  'une procédure ne s’utilise pas dans une expression', ['procedure-sp', 'r-fonction-ou-procedure'])
E('carre-affiche', 'Une fonction qui affiche', 'Si Carré affichait x * x au lieu de le retourner, y ← Carré(3) + 1 deviendrait impossible.',
  'une fonction qui affiche au lieu de retourner ne peut pas servir dans un calcul', ['r-retourner-pas-afficher', 'fonction', 'retour'])
E('admis', 'L’appelant décide', 'm ← Moyenne(notes) ; Si m >= 10 Alors Écrire "admis" FinSi : c’est l’appelant qui choisit quoi faire de la valeur.',
  'retourner laisse le choix à l’appelant : afficher, comparer ou garder', ['r-retourner-pas-afficher', 'retour'])
E('lire-dans-fonction', 'Une fonction qui lit', 'Une fonction Moyenne qui lirait elle-même les notes ne pourrait pas servir sur une liste déjà connue.',
  'les données d’une fonction arrivent par ses paramètres, pas par Lire', ['r-retourner-pas-afficher', 'parametre', 'fonction'])
E('augmenter', 'Augmenter(a)', 'Procédure Augmenter(n : entier) fait n ← n + 1 ; a ← 5 ; Augmenter(a) : a vaut toujours 5.',
  'le paramètre reçoit une copie : le modifier ne change pas la variable de l’appelant', ['pr-copie', 'parametre', 'argument'])
E('crier', 'Crier(msg)', 'Procédure Crier(m : chaîne) fait m ← m + "!" ; msg ← "oui" ; Crier(msg) : msg vaut toujours "oui".',
  'une chaîne est elle aussi transmise par copie', ['pr-copie', 'chaine'])
E('plus-un', 'Pour changer a, retourner', 'Fonction Plus1(n : entier) : entier ; Retourner n + 1 ; a ← Plus1(a) : a passe de 5 à 6.',
  'pour modifier une variable simple, on retourne la nouvelle valeur et on l’affecte', ['pr-copie', 'retour', 'r-retourner-pas-afficher'])
E('locale-i', 'Le i de Moyenne', 'Moyenne(L) déclare une variable locale i ; après l’appel, l’algorithme principal ne connaît pas ce i.',
  'une variable locale disparaît à la fin du sous-programme', ['pr-locale', 'locale', 'portee'])
E('locale-repart', 'Chaque appel repart de zéro', 'Une fonction qui fait c ← 0 puis c ← c + 1 sur une variable locale c retourne 1 à chaque appel.',
  'chaque appel recrée ses variables locales', ['pr-locale', 'locale'])
E('deux-i', 'Deux i différents', 'Somme(L) et Max(L) ont chacune une variable locale i : quand Somme modifie son i, celui de Max ne change pas.',
  'deux variables locales de même nom, dans deux sous-programmes, sont indépendantes', ['r-portee', 'portee', 'locale'])
E('taux-parametre', 'Passer taux en paramètre', 'Dans ce support, une fonction n’utilise pas une variable taux de l’algorithme principal : on lui passe taux en paramètre.',
  'un sous-programme n’utilise que ses paramètres et ses variables locales', ['portee', 'r-portee', 'parametre'])
E('meme-nom-arg', 'Le même nom des deux côtés', 'Carré(x) appelée avec une variable x de l’algorithme principal : ce x et le paramètre x sont deux variables distinctes.',
  'le nom du paramètre et celui de l’argument peuvent être identiques ou différents, sans lien entre eux', ['r-portee', 'portee', 'argument'])
E('fact', 'Factorielle récursive', 'Fonction Fact(n : entier) : entier ; Si n = 0 Alors Retourner 1 Sinon Retourner n * Fact(n - 1) FinSi ; Fact(4) vaut 24.',
  'la fonction s’appelle elle-même sur n - 1 jusqu’au cas de base n = 0', ['recursive', 'cas-base', 'r-recursion', 'r-ecrire-recursive', 'p-recursive'])
E('fact-deroule', 'Le déroulé de Fact(3)', 'Fact(3) attend 3 * Fact(2), qui attend 2 * Fact(1), qui attend 1 * Fact(0) = 1 ; puis 1, 2 et 6 remontent : Fact(3) vaut 6.',
  'les appels descendent jusqu’au cas de base, puis les résultats remontent dans l’ordre inverse', ['r-recursion', 'recursive', 'appel', 'trace'])
E('puissance-rec', 'Puissance récursive', 'Puiss(x, n) : Si n = 0 Alors Retourner 1 Sinon Retourner x * Puiss(x, n - 1) ; Puiss(2, 5) vaut 32.',
  'le cas de base correspond à la donnée la plus petite, n = 0', ['recursive', 'cas-base', 'r-ecrire-recursive', 'p-recursive'])
E('somme-rec', 'Somme de 1 à n', 'S(n) : Si n = 0 Alors Retourner 0 Sinon Retourner n + S(n - 1) ; S(4) vaut 10.',
  'un problème sur n se ramène au même problème sur n - 1', ['r-ecrire-recursive', 'recursive', 'p-recursive', 'r-recursion'])
E('sans-cas-base', 'Oubli du cas de base', 'F(n) : Retourner n * F(n - 1), sans Si : F(3) appelle F(2), F(1), F(0), F(-1)… sans fin.',
  'sans cas de base, la suite d’appels ne s’arrête jamais', ['cas-base', 'pr-recursion', 'boucle-infinie'])
E('s-eloigner', 'Des appels qui s’éloignent', 'F(n) : Si n = 0 Alors Retourner 0 Sinon Retourner F(n + 1) : avec n = 1, les appels s’éloignent de 0 et ne s’arrêtent pas.',
  'chaque appel doit se rapprocher du cas de base', ['pr-recursion', 'recursive', 'terminaison'])
E('fact-negatif', 'Fact(-1)', 'Avec Fact qui s’arrête à n = 0, Fact(-1) appelle Fact(-2), Fact(-3)… : la précondition doit dire n ≥ 0.',
  'un cas de base ne protège que les données qui l’atteignent : la précondition l’écrit', ['pr-recursion', 'cas-base', 'precondition'])

# ---------- Vérifier un algorithme ----------
E('spec-moyenne', 'Spécifier Moyenne', '// Moyenne(L : liste de réel) : réel ; précondition : L non vide ; postcondition : retourne la somme des éléments divisée par Longueur(L)',
  'la spécification dit ce que fait la fonction avant de dire comment', ['specification', 'r-specifier', 'precondition', 'postcondition'])
E('spec-max', 'Spécifier Max', '// Max(L : liste d’entier) : entier ; précondition : Longueur(L) ≥ 1 ; postcondition : le résultat est un élément de L, supérieur ou égal à tous les autres',
  'une postcondition précise se vérifie sur chaque test', ['specification', 'postcondition', 'r-specifier', 'p-maximum'])
E('spec-dicho', 'Spécifier la recherche dichotomique', '// RechercheDicho(L, v) : booléen ; précondition : L triée dans l’ordre croissant ; postcondition : vrai si et seulement si v est dans L',
  'la précondition « liste triée » fait partie du contrat', ['specification', 'precondition', 'r-specifier'])
E('n-sup-1', 'N ≥ 1 pour une moyenne', 'Moyenne de N notes avec N = 0 : la division par N est impossible ; la précondition N ≥ 1 exclut ce cas.',
  'la précondition écarte les entrées pour lesquelles l’algorithme n’a pas de sens', ['precondition', 'p-somme-moyenne'])
E('post-tri', 'Postcondition d’un tri', 'Après TriSélection(L) : L est triée, et elle contient exactement les mêmes éléments qu’avant.',
  'une postcondition complète dit aussi ce qui ne doit pas changer', ['postcondition', 'p-tri-selection'])
E('post-test', 'La postcondition comme référence', 'Postcondition de Max : « le résultat est dans L et supérieur ou égal à tous ». Sur [3, 9, 4], 9 la vérifie ; 4 ne la vérifierait pas.',
  'la postcondition permet de juger n’importe quel résultat obtenu', ['postcondition', 'jeu-tests'])
E('trace-somme', 'Trace de la somme de 1 à 3', 's ← 0 ; Pour i de 1 à 3 Faire s ← s + i FinPour ; trace : (i = 1, s = 1), (i = 2, s = 3), (i = 3, s = 6).',
  'la trace note chaque nouvelle valeur des variables, tour par tour', ['trace', 'r-tracer', 'p-trace', 'iteration'])
E('trace-echange', 'Trace d’un échange raté', 'a = 1, b = 2 ; a ← b donne a = 2 ; b ← a donne b = 2 : la trace montre que l’ancienne valeur de a est perdue.',
  'une trace fait apparaître l’erreur ligne par ligne', ['trace', 'r-tracer', 'p-echange'])
E('trace-tq', 'Trace d’un TantQue', 'x ← 1 ; TantQue x < 10 Faire x ← x * 3 ; trace : x = 1 (vrai), 3 (vrai), 9 (vrai), 27 (faux) : 3 tours.',
  'on note aussi la valeur de la condition à chaque test', ['trace', 'p-trace', 'r-tantque'])
E('tests-moyenne', 'Tests de Moyenne', 'Cas : [10, 20] → 15 ; [12] → 12 ; [0, 0, 0] → 0 ; [-5, 5] → 0.',
  'un jeu de tests associe à chaque entrée la sortie attendue, calculée à la main', ['jeu-tests', 'p-tester', 'r-cas-limites'])
E('tests-max', 'Cas limites de Max', '[7] (un seul élément), [4, 4, 4] (valeurs égales), [9, 1, 2] (maximum en premier), [1, 2, 9] (en dernier), [-3, -1] (négatifs).',
  'les cas limites sont ceux où les algorithmes se trompent le plus souvent', ['r-cas-limites', 'jeu-tests', 'p-tester'])
E('tests-recherche', 'Tests d’une recherche', 'v en premier, en dernier, au milieu, absente, et liste vide : cinq cas pour une recherche séquentielle.',
  'on teste toutes les positions possibles de la valeur cherchée', ['r-cas-limites', 'p-recherche', 'p-tester'])
E('test-passe-faux', 'Un test qui passe, un algorithme faux', 'Une moyenne écrite (a + b) div 2 réussit le test (10, 20) → 15, mais donne 7 au lieu de 7.5 pour (7, 8).',
  'un test réussi ne prouve que ce cas-là', ['pr-tests', 'jeu-tests', 'correction'])
E('max-zero-cache', 'Une erreur cachée', 'Un maximum initialisé à 0 réussit le test [3, 8, 2] → 8, mais échoue sur [-4, -2] (il donne 0).',
  'tant qu’on n’a pas testé le bon cas, l’erreur reste cachée', ['pr-tests', 'r-cas-limites'])
E('prouver-somme', 'Prouver plutôt que tester', 'Pour la somme de 1 à n, l’invariant « s = 1 + … + i » prouve le résultat pour tous les n ; aucun nombre de tests ne le ferait.',
  'seule une preuve couvre tous les cas', ['pr-tests', 'invariant', 'correction'])
E('somme-correcte', 'La somme est correcte', 'Après s ← 0 ; Pour i de 1 à n Faire s ← s + i, s vaut 1 + 2 + … + n pour tout n ≥ 0 : c’est la postcondition.',
  'un algorithme correct donne le résultat annoncé pour toutes les entrées valides', ['correction', 'postcondition', 'p-correction'])
E('pour-termine', 'Un Pour se termine', 'Pour i de 1 à N fait exactement N tours, sans rien à prouver, tant qu’on ne modifie pas i dans le bloc.',
  'la terminaison est acquise pour une boucle bornée', ['terminaison', 'pour', 'r-compteur-intouchable'])
E('saisie-termine', 'Une saisie qui dépend de l’utilisateur', 'Répéter Lire note Jusqu’à note >= 0 et note <= 20 ne se termine que si l’utilisateur finit par taper une note valide.',
  'la terminaison d’une boucle non bornée peut dépendre des entrées', ['terminaison', 'repeter', 'p-saisie'])
E('variant-rebours', 'Compte à rebours avec TantQue', 'n ← 5 ; TantQue n > 0 Faire n ← n - 1 FinTantQue : n vaut 5, 4, 3, 2, 1, 0 ; n est un variant.',
  'un entier positif qui diminue de 1 à chaque tour garantit l’arrêt', ['variant', 'pr-variant', 'r-variant', 'p-terminaison'])
E('variant-dicho', 'Variant de la dichotomie', 'Dans la recherche dichotomique, droite - gauche diminue strictement à chaque tour sans trouver, et la boucle s’arrête quand il devient négatif.',
  'le variant de la dichotomie est la taille de la zone de recherche', ['variant', 'r-variant', 'p-dichotomie', 'p-terminaison'])
E('variant-euclide', 'Variant d’Euclide', 'Dans l’algorithme d’Euclide, b est remplacé par a mod b, qui est strictement plus petit que b : b est un variant.',
  'le reste d’une division est plus petit que le diviseur, donc b diminue', ['variant', 'r-variant', 'p-pgcd', 'pr-variant'])
E('invariant-somme', 'Invariant de la somme', 'Avant le tour i, s = 1 + … + (i - 1) ; vrai au départ (s = 0) ; un tour ajoute i ; à la sortie (i = n + 1), s = 1 + … + n.',
  'l’invariant, vrai à chaque tour, donne le résultat à la sortie', ['invariant', 'pr-invariant', 'r-invariant', 'p-correction'])
E('invariant-max', 'Invariant du maximum', 'Après le tour i, max est le plus grand de L[0], …, L[i] ; à la fin, c’est le plus grand de toute la liste.',
  'l’invariant décrit ce que contient max après chaque tour', ['invariant', 'r-invariant', 'p-maximum', 'p-correction'])
E('invariant-tri', 'Invariant du tri par sélection', 'Après le tour i, L[0] à L[i] contiennent les i + 1 plus petits éléments, dans l’ordre croissant.',
  'l’invariant du tri par sélection prouve qu’à la fin toute la liste est triée', ['invariant', 'pr-invariant', 'p-tri-selection'])
E('cout-moyenne', 'Moyenne de n notes', 'Pour n notes, la boucle fait n additions : 1 000 notes, 1 000 additions ; 2 000 notes, 2 000 additions.',
  'un parcours a un coût linéaire', ['cout-lineaire', 'r-cout-lineaire', 'cout', 'p-cout'])
E('cout-recherche', 'Recherche séquentielle', 'Dans le pire cas (valeur absente), la recherche compare v aux n éléments : coût linéaire.',
  'on évalue le coût dans le pire cas', ['cout-lineaire', 'r-cout-lineaire', 'p-recherche', 'cout'])
E('cout-max', 'Maximum d’une liste', 'Trouver le maximum de n éléments demande n - 1 comparaisons.',
  'une seule boucle sur les données donne un coût linéaire', ['r-cout-lineaire', 'cout-lineaire', 'p-maximum'])
E('cout-tri-sel', 'Tri par sélection de 1 000 éléments', 'Environ n² / 2 comparaisons : 500 000 pour n = 1 000, et 2 000 000 pour n = 2 000.',
  'doubler n multiplie le travail par 4 : coût quadratique', ['cout-quadratique', 'r-cout-quadratique', 'p-tri-selection'])
E('cout-tri-ins', 'Tri par insertion, pire cas', 'Sur une liste triée à l’envers, chaque élément recule jusqu’au début : environ n² / 2 décalages.',
  'le tri par insertion est quadratique dans le pire cas', ['cout-quadratique', 'p-tri-insertion', 'r-cout-quadratique'])
E('cout-tri-ins-meilleur', 'Tri par insertion, meilleur cas', 'Sur une liste déjà triée, la boucle TantQue ne fait aucun tour : seulement n - 1 comparaisons.',
  'le coût dépend aussi des données : on précise s’il s’agit du pire ou du meilleur cas', ['p-tri-insertion', 'cout', 'cout-lineaire'])
E('doublons', 'Comparer toutes les paires', 'Pour i … Pour j … Si i <> j et L[i] = L[j] … : chercher des doublons ainsi fait n × n comparaisons.',
  'deux boucles imbriquées sur les mêmes données donnent un coût quadratique', ['r-cout-quadratique', 'cout-quadratique'])
E('dicho-million', 'Dichotomie sur un million', 'Dans une liste triée d’un million d’éléments, il faut au plus 20 comparaisons, car 2²⁰ ≈ 1 000 000.',
  'diviser par 2 à chaque tour donne un coût logarithmique', ['r-cout-log', 'cout-log', 'p-dichotomie'])
E('sequentiel-vs-dicho', 'Séquentielle contre dichotomie', 'Pour n = 1 000 000 : la recherche séquentielle fait jusqu’à 1 000 000 comparaisons, la dichotomie 20.',
  'l’ordre de grandeur du coût compte plus que la vitesse de l’ordinateur', ['pr-ordre-couts', 'cout-log', 'cout-lineaire', 'p-cout'])
E('n-mille', 'n = 1 000', 'Logarithmique : environ 10 opérations ; linéaire : 1 000 ; quadratique : 1 000 000.',
  'les trois coûts s’écartent énormément dès que n grandit', ['pr-ordre-couts', 'cout-quadratique', 'cout'])
E('n-quatre', 'n = 4', 'Pour n = 4 : 2, 4 et 16 opérations ; sur de si petites données, les écarts sont faibles.',
  'le coût compte surtout pour de grandes données', ['pr-ordre-couts', 'cout'])
E('trois-n-plus-5', '3n + 5 opérations', 'Un algorithme qui fait 3n + 5 opérations a un coût linéaire : on garde n et l’on oublie 3 et 5.',
  'seul l’ordre de grandeur compte', ['cout', 'p-cout', 'cout-lineaire'])

# ---------- Procédures ----------
E('echange-1-2', 'Échanger 1 et 2', 't ← a ; a ← b ; b ← t avec a = 1 et b = 2 : t = 1, puis a = 2, puis b = 1.',
  'la variable temporaire garde l’ancienne valeur de a', ['p-echange', 'r-affecter'])
E('echange-liste', 'Échanger deux éléments', 't ← L[0] ; L[0] ← L[2] ; L[2] ← t : [5, 8, 1] devient [1, 8, 5].',
  'la même méthode échange deux éléments d’une liste, comme dans le tri par sélection', ['p-echange', 'element', 'p-tri-selection'])
E('oui-non', 'Répondre o ou n', 'Répéter Écrire "Continuer (o/n) ?" ; Lire rep Jusqu’à rep = \'o\' ou rep = \'n\'',
  'la saisie contrôlée refuse toute réponse autre que celles prévues', ['p-saisie', 'r-repeter', 'caractere'])
E('n-positif', 'Un entier strictement positif', 'Répéter Écrire "N (> 0) ?" ; Lire N Jusqu’à N > 0 ; l’utilisateur tape 0, puis -3, puis 4 : N vaut 4 après trois tours.',
  'la boucle tourne autant de fois que nécessaire, et au moins une fois', ['p-saisie', 'pr-rep-un'])
E('moyenne-saisie', 'Moyenne de 3 notes saisies', 'N = 3 ; l’utilisateur tape 12, 15 et 9 : somme vaut 36, moyenne vaut 12.',
  'somme accumule les notes, puis la moyenne divise par N', ['p-somme-moyenne', 'accumulateur'])
E('moyenne-7-8', 'Une moyenne non entière', 'N = 2 ; notes 7 et 8 : somme vaut 15 et moyenne 7.5, car / donne un réel.',
  'la moyenne se range dans une variable réelle', ['p-somme-moyenne', 'r-division', 'reel'])
E('mots-longs', 'Compter les mots longs', 'Dans ["chat", "éléphant", "souris"], compter les mots de plus de 5 lettres avec Si Longueur(L[i]) > 5 : n vaut 2.',
  'la méthode reste la même, seule la condition change', ['p-compter', 'r-compter', 'longueur'])
E('compter-vide', 'Compter dans une liste vide', 'Avec L = [], la boucle ne tourne pas et n vaut 0.',
  'initialiser à 0 donne le bon résultat même sans aucun élément', ['p-compter', 'r-initialiser'])
E('insertion-pas', 'Insertion pas à pas', '[5, 2, 4] : on insère 2 avant 5, ce qui donne [2, 5, 4] ; puis on insère 4 entre 2 et 5, ce qui donne [2, 4, 5].',
  'chaque élément est inséré à sa place dans la partie déjà triée, à sa gauche', ['p-tri-insertion', 'liste-triee', 'invariant'])
E('inverser-chat', 'Inverser "chat"', 'inv ← "" ; i va de 3 à 0 : inv vaut "t", puis "ta", "tah" et enfin "tahc".',
  'on ajoute les caractères du dernier au premier', ['p-inverser', 'r-pas-negatif', 'concatenation'])
E('inverser-vide', 'Inverser la chaîne vide', 'Pour ch = "", la boucle de -1 à 0 pas -1 ne fait aucun tour : inv reste "".',
  'le cas limite de la chaîne vide fonctionne sans traitement particulier', ['p-inverser', 'pr-chaine-liste'])
E('kayak', 'kayak', 'L’inverse de "kayak" est "kayak" : le mot est un palindrome ; l’inverse de "radio" est "oidar".',
  'comparer une chaîne à son inverse teste si c’est un palindrome', ['p-inverser', 'op-comp', 'chaine'])
E('pgcd-48-18', 'PGCD(48, 18)', '(48, 18) → (18, 12) → (12, 6) → (6, 0) : le PGCD vaut 6.',
  'on remplace (a, b) par (b, a mod b) jusqu’à ce que b vaille 0', ['p-pgcd', 'div-mod', 'r-tantque'])
E('pgcd-17-5', 'PGCD(17, 5)', '(17, 5) → (5, 2) → (2, 1) → (1, 0) : le PGCD vaut 1, donc 17 et 5 sont premiers entre eux.',
  'un PGCD égal à 1 signifie que les nombres n’ont aucun autre diviseur commun que 1', ['p-pgcd', 'pr-euclide'])
E('pgcd-0-7', 'PGCD(0, 7)', '(0, 7) → (7, 0) : le PGCD vaut 7.',
  'l’algorithme fonctionne aussi quand a vaut 0, grâce à la précondition b > 0', ['p-pgcd', 'precondition'])
E('premier-13', '13 est premier', 'd = 2 : 13 mod 2 = 1 ; d = 3 : 13 mod 3 = 1 ; d = 4 : 4 × 4 = 16 > 13, on s’arrête : 13 est premier.',
  'on ne teste les diviseurs que jusqu’à la racine carrée', ['p-premier', 'div-mod'])
E('premier-15', '15 n’est pas premier', 'd = 2 : 15 mod 2 = 1 ; d = 3 : 15 mod 3 = 0, premier devient faux, et la boucle s’arrête.',
  'dès qu’un diviseur est trouvé, le drapeau arrête la boucle', ['p-premier', 'drapeau', 'r-drapeau'])
E('premier-1', '1 n’est pas premier', 'Avec n = 1, premier ← n >= 2 vaut faux d’emblée : la boucle ne tourne pas.',
  'les cas 0 et 1 sont réglés par la valeur de départ du drapeau', ['p-premier', 'r-cas-limites'])
E('fonction-ttc', 'Fonction PrixTTC', 'Fonction PrixTTC(ht : réel) : réel ; Début ; Retourner ht * 1.2 ; Fin ; PrixTTC(50) vaut 60.',
  'une fonction courte, spécifiée et testée, se réutilise partout', ['p-fonction', 'fonction'])
E('fonction-moyenne', 'Fonction Moyenne', 'Fonction Moyenne(L : liste de réel) : réel ; Variables s : réel ; i : entier ; Début ; s ← 0 ; Pour i de 0 à Longueur(L) - 1 Faire s ← s + L[i] FinPour ; Retourner s / Longueur(L) ; Fin',
  'les variables de travail sont locales, et le résultat est retourné', ['p-fonction', 'locale', 'r-accumuler'])
E('carre-tests', 'Tester Carré', 'Carré(0) = 0, Carré(3) = 9, Carré(-2) = 4, Carré(0.5) = 0.25.',
  'une fonction se teste par quelques appels dont on connaît le résultat', ['p-fonction', 'jeu-tests'])
E('trace-max', 'Trace du maximum', 'L = [3, 9, 4] : max = 3 ; i = 1 : 9 > 3, max = 9 ; i = 2 : 4 > 9 est faux, max reste 9.',
  'la trace montre à quel tour max change', ['p-trace', 'p-maximum'])
E('valider-moyenne', 'Valider Moyenne', 'Relecture : s reçoit 0 avant la boucle ; tests : [10, 20] → 15 réussi, [7, 8] → 7.5 réussi ; la boucle Pour se termine d’elle-même.',
  'valider combine relecture, tests et terminaison', ['p-valider'])
E('valider-erreur', 'Un test échoue', 'Le test [-4, -2] → -2 échoue pour un Max qui donne 0 ; la trace montre max ← 0 au départ ; on corrige en max ← L[0], puis on refait tous les tests.',
  'un échec mène à une trace, une correction, puis à refaire tous les tests', ['p-valider', 'p-trace', 'r-tracer'])
E('valider-tq', 'Valider une boucle TantQue', 'Pour la recherche séquentielle, Longueur(L) - i diminue à chaque tour où v n’est pas trouvée : la boucle s’arrête.',
  'valider une boucle non bornée demande aussi un variant', ['p-valider', 'variant', 'p-terminaison'])
E('grille-max', 'La plus grande case', 'max ← M[0][0] ; deux boucles imbriquées comparent chaque M[i][j] à max : 9 pour la grille de 1 à 9.',
  'la double boucle s’adapte à n’importe quel traitement des cases', ['p-grille', 'r-double-boucle'])

# ---------- Compléments (au moins 3 exemples par élément) ----------
E('seq-ttc', 'Lire, calculer, afficher', 'Lire prixHT ; prixTTC ← prixHT * 1.2 ; Écrire prixTTC : avec 50, on obtient 60.',
  'en séquence, chaque instruction s’exécute après la précédente : la lecture, puis le calcul, puis l’affichage', ['sequence', 'r-sequentiel'])
E('seq-valeurs', 'Les valeurs laissées par les lignes précédentes', 'a ← 1 ; b ← a + 1 ; a ← b * 10 : b vaut 2 et a vaut 20 ; la dernière ligne utilise le b calculé juste avant.',
  'chaque instruction voit les valeurs laissées par les instructions précédentes', ['r-sequentiel', 'sequence', 'trace'])
E('probleme-tri', 'Trier : un problème', 'Problème : ranger une liste de nombres dans l’ordre croissant. Instance : [5, 2, 4], de solution [2, 4, 5]. Algorithmes possibles : tri par sélection, tri par insertion.',
  'un problème dit ce qu’on veut obtenir, sans dire comment ; plusieurs algorithmes le résolvent', ['probleme', 'p-tri-selection', 'p-tri-insertion', 'liste-triee'])
E('boucle-types', 'Trois boucles, un même affichage', 'Afficher 1 2 3 : Pour i de 1 à 3 ; ou i ← 1 puis TantQue i <= 3 ; ou i ← 1 puis Répéter … Jusqu’à i > 3.',
  'les trois boucles répètent un bloc ; elles diffèrent par la façon de décider du nombre de tours', ['boucle', 'pour', 'tantque', 'repeter'])
E('tq-zero-saisie', 'Une saisie déjà correcte', 'Lire note ; TantQue note < 0 ou note > 20 Faire Lire note FinTantQue : si la première note vaut 14, la boucle ne fait aucun tour.',
  'la boucle TantQue ne tourne pas quand tout va bien dès le départ', ['pr-tq-zero', 'tantque', 'r-intervalle'])
E('dicho-etapes', 'Chercher 23 parmi 8 éléments', 'L = [2, 5, 8, 12, 16, 23, 38, 56] : au milieu, 12 < 23, on garde [16, 23, 38, 56] ; au milieu, 23 : trouvé en 2 comparaisons.',
  'chaque comparaison au milieu élimine la moitié des éléments restants', ['pr-dicho', 'p-dichotomie', 'liste-triee'])
E('locale-disparue', 'Une locale introuvable', 'Après m ← Moyenne(L), la ligne Écrire s, où s est la variable locale de Moyenne, est une erreur : s n’existe plus.',
  'une variable locale n’existe que pendant l’exécution de son sous-programme', ['pr-locale', 'locale', 'portee'])
E('invariant-compteur', 'Invariant d’un compteur', 'Pour compter les notes d’au moins 10 : « après le tour i, n est le nombre de ces notes parmi L[0] à L[i] » ; à la sortie, n compte toute la liste.',
  'l’invariant, appliqué à la sortie de la boucle, donne exactement le résultat annoncé', ['pr-invariant', 'r-invariant', 'invariant', 'p-compter'])
E('variant-recherche', 'Variant de la recherche séquentielle', 'Dans TantQue i < Longueur(L) et non trouvé, la quantité Longueur(L) - i est positive et diminue de 1 à chaque tour sans trouver.',
  'une quantité entière positive qui diminue à chaque tour garantit que la boucle s’arrête', ['pr-variant', 'variant', 'p-recherche'])
E('commentaire-etapes', 'Commenter les étapes', '// 1. Saisie des notes … // 2. Calcul de la moyenne … // 3. Affichage : des commentaires découpent un long algorithme en étapes.',
  'les commentaires rendent visible le plan de l’algorithme', ['r-commenter', 'commentaire'])
E('pour-trace', 'Trace d’un Pour', 'Pour i de 2 à 4 Faire Écrire i * 10 FinPour : i = 2 (affiche 20), i = 3 (30), i = 4 (40), puis la boucle s’arrête.',
  'le compteur prend la valeur de départ, augmente de 1 à chaque tour, et la valeur d’arrivée est incluse', ['r-pour', 'trace', 'iteration'])
E('cout-log-1024', '1 024 éléments', '1 024 → 512 → 256 → … → 1 : en divisant par 2 à chaque tour, on atteint 1 en 10 tours.',
  'diviser la zone par 2 à chaque tour donne environ log₂(n) tours', ['r-cout-log', 'cout-log', 'iteration'])
