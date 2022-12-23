# Issue 5707: plus signs missing in typesetting of modular symbols

Issue created by migration from https://trac.sagemath.org/ticket/5707

Original creator: was

Original creation time: 2009-04-07 21:28:39

Assignee: craigcitro

Try this and see no plus signs! Ouch.

```
sage: x = ModularSymbols(43)(vector([0,0,0,0,1,1,1]))
sage: show(x.modular_symbol_rep())
```



---

Comment by mabshoff created at 2009-04-08 00:51:11

Bumping it since according to William this is lower priority.

Cheers,

Michael


---

Comment by was created at 2009-04-12 01:16:59

Resolution: duplicate


---

Comment by was created at 2009-04-12 01:16:59

I am closing this since it is easy to fix as part of #5766.
