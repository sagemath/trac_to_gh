# Issue 1764: the url in the trac emails is wrong

Issue created by migration from https://trac.sagemath.org/ticket/1764

Original creator: was

Original creation time: 2008-01-13 04:46:12

Assignee: mabshoff

The url in trac emails is typically something like

```
http://modular.math.washington.edu:9002/sage_trac/ticket/1657
```

but it should be

```
http://trac.sagemath.org/sage_trac/ticket/1657
```


This is very bad, because people behind certain firewalls can only
view the latter URL and not the former.  Also the latter URL is stable,
but the former could easily change, e.g., if I run trac on a different port. 


---

Comment by malb created at 2008-01-13 11:35:58

dupe of #1710


---

Comment by malb created at 2008-01-13 11:35:58

Resolution: duplicate
