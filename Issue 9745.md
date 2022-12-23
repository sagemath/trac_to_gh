# Issue 9745: Pickling of FFELT (finite field element) PARI/GP elements broken

Issue created by migration from https://trac.sagemath.org/ticket/9745

Original creator: jdemeyer

Original creation time: 2010-08-14 11:08:12

Assignee: was

Keywords: pari gp

The new version of PARI (see #9343) introduces a new type t_FFELT (finite field element).  Unfortunately, they pickle badly in Sage:


```
sage: gp_el = gp('ffgen(ffinit(2,3))')
sage: gp_el.type()
t_FFELT
sage: loads(dumps(gp_el)).type()
t_POL
```


A possible solution would be to implement pickling using PARI's `writebin()` and `read()`.
