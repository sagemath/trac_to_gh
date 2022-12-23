# Issue 3047: version option returning clone branch name

Issue created by migration from https://trac.sagemath.org/ticket/3047

Original creator: wdj

Original creation time: 2008-04-27 20:20:33

Assignee: was

The attached patch adds to version an option which returns the version and the branch clone name.
New behavior:
sage: version()
returns exactly the same thing it did before no change.
sage: version(True) # or replace "True" by anything except "0" or "False"
returns 
(Version, Branch name)
For example,

```
sage: version(1)

('SAGE Version 3.0, Release Date: 2008-04-22',
 'Mercurial clone branch: version')
```

in a Mercurial clone branch created using "sage -clone version".


---

Comment by wdj created at 2008-04-27 20:21:49

This ticket should be deleted. I meant only to create trac 3046.


---

Comment by mhansen created at 2008-04-27 21:52:40

Resolution: duplicate
