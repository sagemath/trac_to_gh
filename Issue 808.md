# Issue 808: construction of function fields

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2007-10-03 15:40:30

Assignee: somebody

The following does not work and it seems to fail in an odd way wrt. the preparser

```
P1.<t> = QQ[].fraction_field()
```

There doesn't seem to be a convenient way of constructing a rational function field
with a named variable.


---

Comment by nbruin created at 2007-10-03 15:51:44

Resolution: duplicate
