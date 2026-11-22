var MOL=[
 {id:"r1",t:"R1 Affectation",c:"r1",kw:"règle",
  a:{r1:"R1 Affectation",r1_ctx:"Exécution d'un pseudo-code",r1_si:"x ← e s'exécute",r1_alors:"e est calculée, puis remplace la valeur de x",r1_sauf:"Aucune exception identifiée",r1_e1:"x ← 5 : x vaut 5",r1_e2:"x vaut 3 ; x ← x + 1 : x vaut 4"},
  b:[["r1","r1_ctx","contexte","Contexte : l'exécution d'un pseudo-code.",0,null,180],
     ["r1","r1_si","si","Si x ← e s'exécute…",0,null,240],
     ["r1","r1_alors","alors","… alors e est calculée avec les valeurs actuelles, puis x prend ce résultat ; l'ancienne valeur de x est perdue.",0,null,300],
     ["r1","r1_sauf","sauf si","Sauf si : aucune exception identifiée dans ce domaine.",0,null,0],
     ["r1","r1_e1","exemple","Exemple : x ← 5. Après, x vaut 5, quelle que soit sa valeur avant.",0,null,60],
     ["r1","r1_e2","exemple","Exemple : x vaut 3, puis x ← x + 1. x vaut 4, car x + 1 est calculé avec l'ancienne valeur.",0,null,120]]}
];
var DIR=1;var NOPRIM=1;
