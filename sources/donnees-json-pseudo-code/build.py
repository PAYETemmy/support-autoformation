# Usage : python3 build.py ../../explorateur-pseudo-code/donnees.json
import json, collections, sys
import lib, concepts, props_rules, procs, examples  # noqa: F401  (l’import remplit lib.ITEMS / lib.LINKS)
from lib import ITEMS, LINKS

ids = {x["id"] for x in ITEMS}
dup = [k for k, v in collections.Counter(x["id"] for x in ITEMS).items() if v > 1]
bad = [(l["source"], l["target"], l["type"]) for l in LINKS if l["target"] not in ids or l["source"] not in ids]
if dup or bad:
    print("ID DUPLIQUÉS:", dup); print("CIBLES INCONNUES:", bad); sys.exit(1)
# identifiants de relation : l-source-cible (suffixe si plusieurs types pour la même paire)
seen = collections.Counter()
for l in LINKS:
    base = f"l-{l['source']}-{l['target']}"; seen[base] += 1
    l["id"] = base if seen[base] == 1 else f"{base}-{seen[base]}"
LINKS[:] = [{k: l[k] for k in ("id", "source", "target", "type", "note")} for l in LINKS]
# compte d’exemples
byid = {x["id"]: x for x in ITEMS}
ex = collections.Counter(l["target"] for l in LINKS if l["type"] == "Illustre")
low = [(x["id"], ex[x["id"]]) for x in ITEMS if x["type"] in ("Concept", "Propriété", "Règle", "Procédure") and ex[x["id"]] < 3]
print("éléments:", len(ITEMS), dict(collections.Counter(x["type"] for x in ITEMS)), "| relations:", len(LINKS))
print("MOINS DE 3 EXEMPLES:", low)
data = {"format": "modele-representation-connaissance", "version": 10.1,
        "titre": "Pseudo-code : écrire, vérifier et analyser des algorithmes (d’après Éduscol et le programme de NSI)",
        "items": ITEMS, "links": LINKS}
txt = json.dumps(data, ensure_ascii=False, indent=2)
open(sys.argv[1] if len(sys.argv) > 1 else "donnees.json", "w", encoding="utf-8").write(txt + "\n")
