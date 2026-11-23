# Générateur de donnees.json (pseudo-code) — briques communes
ITEMS, LINKS = [], []
PRIM = "Terme primitif (non défini)"

ED = "Éduscol, « Algorithmique », ressources pour la classe de seconde (2009)"
SRC = {
 "ED_INIT": ED + ", § « Une initiation à l’algorithmique » (définition, trois étapes : préparation, traitement, sortie).",
 "ED_AFF":  ED + ", § « L’affectation de données dans des variables » (image du tiroir, « prend la valeur »).",
 "ED_ES":   ED + ", § « La lecture (ou entrée) des données » et « L’écriture (ou sortie) des données » (Saisir, Afficher).",
 "ED_CTRL": ED + ", § « Instructions (ou structures) de contrôle » (Si … alors … Sinon, conditions, ET, OU).",
 "ED_BCL":  ED + ", § « Les structures répétitives » (Pour, Tant que, Répète … jusqu’à ; boucle infinie).",
 "ED_VAL":  ED + ", « Présentation générale » : valider un algorithme par des traces d’exécution et des jeux d’essais simples.",
 "LAF":     "Lycée Lafayette (Brioude), page « Pseudo-code » (structure ALGORITHME / VARIABLES / DÉBUT / FIN, types, absence de norme), citée par le support « Pseudo-code · modèle v1 ».",
 "CONV":    "Convention de ce support, reprise des supports « Pseudo-code » du dépôt (d’après Éduscol et le lycée Lafayette).",
 "AJOUT":   "Ajout de ce support, conforme à l’usage courant des pseudo-codes en français.",
 "NSI_ALGO":"Programme de NSI de première générale (BO spécial n° 1 du 22 janvier 2019), partie « Algorithmique » (parcours, tris, dichotomie, invariant, variant, coût).",
 "NSI_LP":  "Programme de NSI de première générale (BO spécial n° 1 du 22 janvier 2019), partie « Langages et programmation » (constructions élémentaires, spécification, mise au point et tests, diversité des langages).",
 "NSI_TC":  "Programme de NSI de première générale (BO spécial n° 1 du 22 janvier 2019), partie « Représentation des données : types construits » (tableaux, tableaux de tableaux, p-uplets nommés).",
 "NSI_REC": "Programme de NSI de terminale générale (BO spécial n° 8 du 25 juillet 2019), partie « Langages et programmation », notion « Récursivité ».",
 "PY":      "Documentation officielle de Python (docs.python.org), tutoriel, chapitres 3 et 4 (types de base, structures de contrôle).",
}
def fnd(*keys):
    return [{"type": "Source documentaire", "text": SRC[k]} for k in keys]
DEMO = [{"type": "Démonstration ou raisonnement", "text": "Vérifié pas à pas : trace d’exécution à la main ou application directe de la définition."}]

def _item(id, type, name, fields, foundations):
    ITEMS.append({"id": id, "type": type, "name": name, "status": "Établi", "life": "Actif",
                  "fields": {k: v for k, v in fields.items() if v}, "foundations": foundations,
                  "formulation": "", "autoForm": True})
def link(s, t, type):
    LINKS.append({"source": s, "target": t, "type": type, "note": ""})

def P(id, name, intuition, traits, src):            # terme primitif
    _item("pc-" + id, "Concept", name, {"domain": "le pseudo-code", "nature": PRIM, "intuition": intuition, "traits": traits}, fnd(*src))
def C(id, name, defs, definition, traits, src):      # concept défini
    _item("pc-" + id, "Concept", name, {"domain": "le pseudo-code", "definition": definition, "traits": traits}, fnd(*src))
    for d in defs: link("pc-" + id, "pc-" + d, "Se définit à partir de")
def PR(id, name, rel, targets, domain, relation, obj, src, qualifier=""):   # propriété
    _item("pc-pr-" + id, "Propriété", name, {"domain": domain, "qualifier": qualifier, "relation": relation, "object": obj}, fnd(*src))
    for t in targets: link("pc-pr-" + id, "pc-" + t, rel)
def R(id, name, kind, context, condition, conclusion, porte, src, exception=""):
    mode = "Exception réelle" if exception else "Aucune exception identifiée dans ce domaine"
    _item("pc-r-" + id, "Règle", name, {"kind": {"D": "Descriptive", "A": "D’action"}[kind], "context": context, "condition": condition,
          "conclusion": conclusion, "exceptionMode": mode, "exception": exception}, fnd(*src))
    for t in porte: link("pc-r-" + id, "pc-" + t, "Porte sur")
def PROC(id, name, context, goal, inputs, steps, result, success, src, appuie=(), applique=(), contient=()):
    _item("pc-p-" + id, "Procédure", name, {"context": context, "goal": goal, "inputs": inputs,
          "steps": "\n".join(f"{i}. {s}" for i, s in enumerate(steps, 1)), "result": result, "success": success}, fnd(*src))
    for t in appuie: link("pc-p-" + id, "pc-" + t, "S’appuie sur")
    for t in applique: link("pc-p-" + id, "pc-r-" + t, "Applique")
    for t in contient: link("pc-p-" + id, "pc-p-" + t, "Contient")
def E(id, name, case, shown, targets):               # exemple ; cibles : ids complets sans « pc- »
    _item("pc-e-" + id, "Exemple", name, {"case": case, "shown": shown}, DEMO)
    for t in targets: link("pc-e-" + id, "pc-" + t, "Illustre")
def X(id, name, case, condition, verdict, targets, src=None):   # contre-exemple
    V = {"2a": "Hors du domaine prévu (2a) : pas de contradiction dans le domaine", "T": "Traité : énoncé révisé"}[verdict]
    _item("pc-x-" + id, "Contre-exemple", name, {"case": case, "condition": condition, "verdict": V}, fnd(*src) if src else DEMO)
    for t in targets: link("pc-x-" + id, "pc-" + t, "Met à l’épreuve")
def chain(ids):                                       # ordre pédagogique : chacun après le précédent
    for a, b in zip(ids[1:], ids[:-1]): link(a, b, "A pour prérequis")
