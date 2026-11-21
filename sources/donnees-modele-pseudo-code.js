var PAGE={
 kicker:"Pseudo-code · modèle v1",
 titre:"Écrire la moyenne en pseudo-code",
 objectif:"À la fin, tu écris seul la procédure qui calcule la moyenne de N notes.",
 domaine:"Le pseudo-code de ce support, d'après Éduscol et le lycée Lafayette (pas de norme unique, voir P4).",
 aide:"Pastilles bleues : aller à l'élément cité.",
 sources:[
  {t:"Éduscol, Algorithmique, ressource pour la classe de seconde (2009)"},
  {t:"Lycée Lafayette (Brioude), page Pseudo-code",url:"https://sites.google.com/view/lycee-lafayette-brioude/ressources_1/pseudo-code"}
 ],
 pied:"Construit avec le modèle de représentation d'une connaissance, version 1."
};
var EL=[
/* ---------- Concepts ---------- */
{id:"Variable",type:"concept",nom:"Variable",t:"Emplacement de mémoire désigné par un nom, qui contient une valeur à la fois.",par:["P1"],f:["établi","Éduscol (image du tiroir)","reformulée"]},
{type:"exemple",cible:"Variable",t:"`age` : un nom qui désigne un emplacement contenant une valeur, par exemple 17.",f:["établi","convention","ajout"]},
{type:"contre",cible:"Variable",label:"Contre-exemple (définition trop large)",t:"\"Une variable est un nom dans un algorithme\" est trop large : le nom de l'algorithme, écrit après ALGORITHME, est un nom mais pas une variable.",f:["établi","lycée Lafayette (structure ALGORITHME / DEBUT / FIN)","ajout"]},
{id:"Affectation",type:"concept",nom:"Affectation",t:"Instruction qui range une valeur dans une variable. Elle se lit \"prend la valeur\".",f:["établi","Éduscol (\"prend la valeur\")","reformulée"]},
{id:"Condition",type:"concept",nom:"Condition",t:"Expression qui vaut vrai ou faux.",f:["établi","Éduscol","reformulée"]},
{type:"exemple",cible:"Condition",t:"`note > 20` vaut vrai si note vaut 25, faux si note vaut 14.",f:["établi","démonstration","ajout"]},
{id:"Boucle",type:"concept",nom:"Boucle",t:"Structure qui répète un traitement.",f:["établi","lycée Lafayette (\"structures de répétition\")","reformulée"]},

/* ---------- Propriétés ---------- */
{id:"P1",type:"propriete",nom:"une valeur à la fois",t:"Une variable ne contient qu'une valeur à la fois.",porte:["Variable"],f:["établi","Éduscol","reformulée"]},
{id:"P2",type:"propriete",nom:"écriture de l'affectation",t:"Dans ce support, l'affectation s'écrit `←` : `x ← 5` se lit \"x prend la valeur 5\".",porte:["Affectation"],f:["admis","convention (le lycée Lafayette accepte aussi `:=`)","ajout"]},
{id:"P3",type:"propriete",nom:"types",t:"Dans la convention du lycée Lafayette, une variable a un type : entier, réel, booléen, caractère ou chaîne.",porte:["Variable"],f:["établi","lycée Lafayette","reformulée"]},
{id:"P4",type:"propriete",nom:"pas de norme",t:"Il n'existe pas de norme unique du pseudo-code : chaque support fixe ses conventions (ici P2, P5, P6).",porte:["le pseudo-code"],f:["établi","lycée Lafayette (\"Il n'y a pas de norme qui régisse ce langage\")","reformulée"]},
{id:"P5",type:"propriete",nom:"lire / afficher",t:"Dans ce support, `lire x` range dans x la valeur tapée par l'utilisateur ; `afficher x` montre la valeur de x.",porte:["Variable"],f:["admis","convention (Éduscol écrit \"Saisir\" et \"Afficher\")","ajout"]},
{id:"P6",type:"propriete",nom:"écriture des boucles",t:"Dans ce support, une boucle s'écrit `pour i de 1 jusqu'à N`, `tant que condition` ou `répéter … jusqu'à condition`. Les lignes répétées sont décalées vers la droite.",porte:["Boucle","Condition"],f:["admis","convention, d'après les boucles d'Éduscol (Pour, Tant que, Répète…jusqu'à)","ajout"]},

/* ---------- Règles ---------- */
{id:"R1",type:"regle",nom:"Affectation",ctx:"exécution d'un pseudo-code",si:"`x ← e` s'exécute",alors:"e est calculée avec les valeurs actuelles, puis x prend ce résultat ; l'ancienne valeur de x est perdue",sauf:"aucune exception identifiée dans ce domaine",porte:["Affectation","Variable"],f:["établi","Éduscol","reformulée"]},
{type:"exemple",cible:"R1",t:"`x ← 5` : après, x vaut 5, quelle que soit sa valeur avant.",f:["établi","démonstration à partir de R1","ajout"]},
{type:"exemple",cible:"R1",t:"x vaut 3, puis `x ← x + 1` : x vaut 4, car x + 1 est calculé avec l'ancienne valeur, avant le remplacement.",f:["établi","démonstration à partir de R1","ajout"]},
{id:"R2",type:"regle",nom:"Boucle Pour",ctx:"une boucle `pour i de 1 jusqu'à N`",si:"elle s'exécute",alors:"les lignes décalées s'exécutent N fois : i vaut 1, puis 2, …, puis N",sauf:"aucune exception identifiée dans ce domaine",porte:["Boucle"],f:["établi","Éduscol (boucle Pour)","reformulée"]},
{type:"exemple",cible:"R2",t:"`pour i de 1 jusqu'à 3` puis, décalé, `afficher i` : affiche 1, 2, 3.",f:["établi","démonstration à partir de R2","ajout"]},
{id:"R3",type:"regle",nom:"Boucle Tant que",ctx:"une boucle `tant que condition`",si:"la condition est fausse au départ",alors:"les lignes décalées ne s'exécutent jamais",sauf:"aucune exception identifiée dans ce domaine",porte:["Boucle","Condition"],f:["établi","Éduscol","reformulée"]},
{type:"exemple",cible:"R3",t:"n vaut 3 et `tant que n < 0` : la condition est fausse dès le départ, rien ne s'exécute.",f:["établi","démonstration à partir de R3","ajout"]},
{id:"R4",type:"regle",nom:"Boucle Répéter",ctx:"une boucle `répéter … jusqu'à condition`",si:"la condition est déjà vraie au départ",alors:"les lignes s'exécutent quand même une fois : la condition n'est testée qu'après",sauf:"aucune exception identifiée dans ce domaine",porte:["Boucle","Condition"],f:["établi","Éduscol","reformulée"]},
{id:"R5",type:"action",nom:"Choisir la boucle",ctx:"écriture d'un pseudo-code",si:"il faut répéter un traitement",alors:"utiliser une boucle `pour`",sauf:"le nombre de tours n'est pas connu à l'avance : alors utiliser `tant que`",porte:["Boucle"],f:["établi","Éduscol","reformulée"]},
{type:"contre",cible:"R5",label:"Contre-exemple apparent",t:"Lire des notes jusqu'à ce que l'utilisateur tape −1 semble contredire R5 : on répète, mais `pour` ne convient pas. Ce cas relève de l'exception prévue : le nombre de tours n'est pas connu à l'avance.",f:["établi","démonstration à partir de R5","ajout"]},

/* ---------- Procédures ---------- */
{id:"Pr1",type:"procedure",nom:"Échange",ctx:"pseudo-code de ce support",pour:"échanger les valeurs de deux variables a et b",depart:"a et b contiennent chacune une valeur",etapes:["t ← a","a ← b","b ← t"],produit:"a contient l'ancienne valeur de b, et b l'ancienne valeur de a",si:"aucune condition particulière",mob:["R1"],f:["établi","démonstration à partir de R1","ajout"]},
{type:"exemple",cible:"Pr1",entrees:"a = 1, b = 2",resultat:"a = 2, b = 1",f:["établi","démonstration à partir de R1","ajout"]},
{type:"contre",cible:"Pr1",label:"Contre-exemple (sans t)",t:"`a ← b` puis `b ← a` n'échange pas : avec a = 1 et b = 2, on obtient a = 2 et b = 2. R1 l'explique : après `a ← b`, l'ancienne valeur de a est perdue.",f:["établi","démonstration à partir de R1","ajout"]},
{id:"Pr2",type:"procedure",nom:"Saisie d'une note",ctx:"pseudo-code de ce support",pour:"obtenir une note entre 0 et 20",depart:"l'utilisateur tape des valeurs",etapes:["lire note","tant que note < 0 ou note > 20","    lire note"],produit:"note contient une valeur entre 0 et 20",si:"l'utilisateur finit par taper une note valide",mob:["P5","R3","R5","Condition"],f:["à vérifier","test sur trois cas : 15 ; −2 puis 15 ; 25 puis 30 puis 8","ajout"]},
{type:"exemple",cible:"Pr2",entrees:"25, puis 14",resultat:"note = 14 (25 est refusé, 14 est gardé)",f:["établi","test","ajout"]},

/* ---------- À toi ---------- */
{id:"Pr3",type:"exercice",nom:"Moyenne",ctx:"pseudo-code de ce support",pour:"calculer et afficher la moyenne de N notes",depart:"N, le nombre de notes, avec N ≥ 1 ; l'utilisateur tape les notes une par une",produit:"la moyenne affichée",si:"les notes tapées sont des nombres",mob:["R1","R2","R5","P5","P6"],consigne:"Écris ici, une instruction par ligne. La solution est cachée.",etapes:["somme ← 0","pour i de 1 jusqu'à N","    lire note","    somme ← somme + note","moyenne ← somme / N","afficher moyenne"],f:["à vérifier","test sur un cas (celui ci-dessus)","ajout"]},
{type:"exemple",cible:"Pr3",avant:1,entrees:"N = 5 ; notes 12, 14, 9, 16, 11",resultat:"12,4 (62 / 5)"},
{type:"contre",cible:"Pr3",label:"Contre-exemple (N = 0)",t:"Avec N = 0, la boucle ne tourne pas et `somme / N` divise par zéro. D'où la condition N ≥ 1 dans \"À partir de\" : on a précisé la condition au lieu de réviser la procédure.",f:["établi","démonstration","ajout"]}
];
