# Issue 2272: subgroups of abelian groups have various problems

Issue created by migration from https://trac.sagemath.org/ticket/2272

Original creator: AlexGhitza

Original creation time: 2008-02-23 00:49:48

Assignee: joyner

While nosing around #1284, I ran into some more trouble with subgroups of abelian groups:


```
sage: A = G.subgroup([a])
sage: G.<a,b> = AbelianGroup(2)
sage: A = G.subgroup([a])
sage: a in A   # should return True
False
sage: A.gens()
[a]
sage: A.0      # should return a
f
```





---

Comment by wdj created at 2008-02-24 17:11:12

I have no idea how to fix this. The __contains__ method on the subclass AbelianGroup_subgroup will default to the parent class if pass or an error is passed. This has messed up every attempt I have made.
One issue is that the group is infinite, so perhaps a NotImplementedError makes sense here?


---

Comment by wdj created at 2008-02-24 18:12:52

The way G.subgroup([a]) is currently written, if you want the generators to have anything other than the default name (f or f1, f2, ...), you must name them explicitly. So, I'm not sure if

```
sage: A.0      # should return a
f
```

is a bug or feature.


---

Comment by was created at 2008-05-07 22:25:09

See also #3127 and #1849


---

Comment by rlm created at 2008-05-10 23:36:51

Patch at #1284 fixes this.


---

Comment by mabshoff created at 2008-05-26 16:43:40

Fixed by merging #1284 in Sage 3.0.3.alpha0.


---

Comment by mabshoff created at 2008-05-26 16:43:40

Resolution: fixed
