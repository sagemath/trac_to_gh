# Issue 6638: Implement a way to import default shortcuts, say from SymmetricFunctions(QQ)

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-07-27 12:50:53

Assignee: mhansen

CC:  sage-combinat

Implement a way to import default shortcuts, say from SymmetricFunctions(QQ), WeylGroups(["A",3]), or RootSystem(["A",3])

Option 1:

```
    sage: Sym = SymmetricFunctions(QQ)
    sage: %from Sym.shortcuts() import *
    sage: s[3] + h[2]
    s[3] + s[2]

    sage: %from Sym.shortcuts() import s, h, p

    sage: Sym.shorcuts()
    { s: SymmetricFunctions in the Schur basis,
      h: SymmetricFunctions in the complete basis,
      ...
    }
```


Option 2:

```
    sage: Sym = SymmetricFunctions(QQ)
    sage: Sym.import_shortcuts()
    sage: s[3] + h[2]
    s[3] + s[2]

    sage: Sym.import_shortcuts("s", "h", "p")
```



---

Comment by nthiery created at 2009-07-27 12:54:54

Changing type from defect to enhancement.
