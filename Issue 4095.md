# Issue 4095: Major bug in GF(109)['x', 'y']

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-09-10 02:22:42

Assignee: somebody

Nick Alexander reported in http://groups.google.com/group/sage-devel/t/66e73453bc0b863a

```
sage: GF(109)['x', 'y'](-10)
-10
sage: GF(109)['x'](-10)
99
```



---

Comment by malb created at 2008-09-15 17:45:29

Michael Brickenstein wrote on [sage-devel]:

```
ok, it isn't normalize, but a very small function called npWrite

void npWrite (number &a)
{
  if ((long)a > (npPrimeM >>1)) StringAppend("-%d",(int)(npPrimeM-
((long)a)));
  else                          StringAppend("%d",(int)((long)a));
}

This is set to the current ring
in numbers.cc
n->nWrite = npWrite;
It should just affect the output, so I think would be okay to change it.
```



---

Comment by AlexGhitza created at 2009-01-22 18:18:39

Changing type from defect to enhancement.
