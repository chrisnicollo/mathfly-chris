from talon import Context, Module

mod = Module()

mod.list("tex_greek_letters", desc="TeX greek letters")
mod.list("tex_symbols", desc="TeX mathematical symbols")
ctx = Context()

symbols = {
    # operators
    "fraction": "frac",
    # "summation": "sum",
    # "product": "prod",
    # "limit": "lim",
    "root": "sqrt",
    "square root": "sqrt",
    "generic root": "root",
    "integral": "int",
    "double integral": "iint",
    "triple integral": "iiint",
    "times": "times",
    "divide": "div",
    "C dot": "cdot",
    "plus or minus": "pm",
    "partial": "partial",
    "infinity": "infty",
    # "(nice frack | nice fraction)": "nicefrac",
    "nice frack": "nicefrac",
    "nice fraction": "nicefrac",
    "binomial": "binom",
    "vector nabla": "nabla",
    # accents
    "accent hat": "hat",
    "accent tilde": "tilde",
    "accent dot": "dot",
    "accent double dot": "ddot",
    # "accent bar": "bar",
    "accent vector": "vec",
    # trig
    "sine": "sin",
    "cosine": "cos",
    "tangent": "tan",
    "secant": "sec",
    "cosecant": "csc",
    "cotangent": "cot",
    "arc sine": "arcsin",
    "arc cosine": "arccos",
    "arc tan": "arctan",
    "hyperbolic sine": "sinh",
    "hyperbolic cosine": "cosh",
    "hyperbolic cotangent": "coth",
    "hyperbolic tangent": "tanh",
    # functions
    # "argument": "arg",
    "maximum": "max",
    "minimum": "min",
    "modulus": "bmod",
    "infimum": "inf",
    "supremum": "sup",
    # relations
    "there exists": "exists",
    "member": "in",
    "member of": "in",
    "not in": "notin",
    "for all": "forall",
    # "[is] not equal [to]": "neq",
    "not equal": "neq",
    "greater or equal": "geq",
    "less or equal": "leq",
    # "[is] approximately [equal] [to]": "approx",
    "approximately": "approx",
    # "proportional [to]": "propto",
    "proportional": "propto",
    # "preference less [than]": "prec",
    "preference less": "prec",
    "preference less equal": "preceq",
    # "preference greater [than]": "succ",
    "preference greater": "succ",
    "preference greater equal": "succeq",
    # logic
    "mark and": "land",
    "mark or": "lor",
    "mark not": "lnot",
    #
    "left arrow": "leftarrow",
    "right arrow": "rightarrow",
    "up arrow": "uparrow",
    "down arrow": "downarrow",
    "left right arrow": "leftrightarrow",
    "maps to": "mapsto",
    "oh plus": "oplus",
    "oh times": "otimes",
    "big oh plus": "bigoplus",
    "big oh times": "bigotimes",
    #
    "dot dot dot": "dots",
    "diagonal dots": "ddots",
    "horizontal dots": "cdots",
    "vertical dots": "vdots",
    # sets
    "empty set": "emptyset",
    "subset": "subseteq",
    "superset": "supset",
    "strict subset": "subsetneq",
    "strict superset": "supsetneq",
    "intersection": "cap",
    "union": "cup",
    "GCD": "gcd",
    "cat hom": "hom",
    "kernel": "ker",
    "unit": "unitone",
    "unit two": "unittwo",
    "unit fraction": "unitfrac",
    "text fraction": "tfrac",
    "display fraction": "dfrac",
    "continued fraction": "cfrac",
    # "continued fraction (left)": "cfracleft",
    "continued fraction left": "cfracleft",
    # "continued fraction (right)": "cfracright",
    "continued fraction right": "cfracright",
    "text binomial": "tbinom",
    "display binomial": "dbinom",
    # my additions (ma-anwar's additions)
    "long right arrow": "longrightarrow",
    # denote magnitude of vectors
    "mag": "Vert",
    "low dots": "ldots",
    # "square root": "sqrt",
    "equivalent": "leftrightarrow",
    "medium space": ":",
    "proper subset": "subset",
    # "stop": "cdot", # talon was getting this confused with slap
    # "member": "in",
    "normal tech": "textrm",
    "long equivalent": "longleftrightarrow",
    "overline": "overline",
    "restriction": "restriction",
    #  "minus set": "setminus",
    "circle": "circ",
    "diamond": "diamond",
    "congruent": "equiv",
    "sat minus":"setminus"
}

greek_letters = {
    "alpha": "alpha",
    "beater": "beta",
    "gamma": "gamma",
    "delta": "delta",
    "epsilon": "varepsilon",
    "zita": "zeta",
    "eater": "eta",
    "theta": "theta",
    "iota": "iota",
    "kappa": "kappa",
    "lambda": "lambda",
    "mu": "mu",
    "new": "nu",
    "zee": "xi",
    "pie": "pi",
    "row": "rho",
    "sigma": "sigma",
    "tau": "tau",
    # "oopsilon": "upsilon",
    "phi": "phi",
    "chi": "chi",
    "sigh": "psi",
    "omega": "omega",
}


ctx.lists["user.tex_symbols"] = symbols


ctx.lists["user.tex_greek_letters"] = {
    **greek_letters,
    **{f"big {k}": v.title() for k, v in greek_letters.items()},
}
