# Vérification d’un groupe de sens dans un texte — même algorithme que l’app (fonction groupOk dans index.html)
import re, unicodedata
IGNORES = {"le", "la", "les", "un", "une", "des", "de", "du", "au", "aux", "a", "en", "se", "ce", "cet", "cette", "y",
           "il", "ils", "elle", "elles", "on", "lui", "son", "sa", "ses", "leur", "leurs"}  # articles, pronoms, possessifs
def mots(t):
    t = t.lower().replace("’", "'").replace("‘", "'")
    t = "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")
    t = re.sub(r"qu'", "que ", t)
    t = re.sub(r"\b([ldsjnmtc])'", r"\1e ", t)
    return [w for w in re.findall(r"[a-z0-9²]+|//|\+", t) if w not in IGNORES]
def egal(g, w): return w == g if len(g) <= 3 else w.startswith(g[:max(4, len(g) - 2)])
def groupe_ok(groupe, texte, ecart=3):
    G, T = mots(groupe), mots(texte)
    if not G: return True
    for s in range(len(T)):
        if not egal(G[0], T[s]): continue
        k, p = 1, s
        while k < len(G):
            n = next((q for q in range(p + 1, min(len(T), p + 2 + ecart)) if egal(G[k], T[q])), None)
            if n is None: break
            k, p = k + 1, n
        if k == len(G): return True
    return False
