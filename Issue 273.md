# Issue 273: sage-location path extraction thrown off by extra "local"

Issue created by migration from https://trac.sagemath.org/ticket/273

Original creator: nbruin

Original creation time: 2007-02-21 02:05:02

Assignee: was

line 35 in sage-location tries to split off SAGE-ROOT by looking for the first occurrence of
"local/" in the string. This fails if, for instance, sage is installed in
"/usr/local/sage/latestversion/..."

A fix that seems to work at present if to search for the last occurrence of "local/" instead:

```
           i = z.rfind('local/')
```


One would have to check that no further "local/" can occur inside
$SAGE_ROOT/local/
in order for this criterion to work.


---

Comment by was created at 2007-02-24 03:06:52

Resolution: fixed


---

Comment by was created at 2007-02-24 03:06:52

Fixed for sage-2.2.
