# Issue 2025: bug in applying functions to a symbolic matrix

Issue created by migration from https://trac.sagemath.org/ticket/2025

Original creator: was

Original creation time: 2008-02-01 14:02:18

Assignee: was

Note below that the stupid constant term of the taylor expansion
inside the matrix keeps getting pushed off to the far right!


```
sage: m = matrix(1,[-x/(2*x-4)])
sage: m.apply_map(lambda e: taylor(e,x,0,4))
[x^4/32 + x^3/16 + x^2/8 + x/4]
sage: m.apply_map(lambda e: taylor(e,x,0,4))
[x^4/32 + x^3/16 + x^2/8 + x/4]
sage: m.apply_map(lambda e: taylor(e,x,1,4))
[x + (x - 1)^4 + (x - 1)^3 + (x - 1)^2 - 1/2]
sage: m.apply_map(lambda e: taylor(e,x,2,4))
[-1/(x - 2) - 1/2]
sage: m.apply_map(lambda e: taylor(e,x,3,4))
[x - (x - 3)^4 + (x - 3)^3 - (x - 3)^2 - 9/2]
sage: m[0,0].taylor(x,3,4)
-3/2 + x - 3 - (x - 3)^2 + (x - 3)^3 - (x - 3)^4
```



---

Comment by mhansen created at 2008-02-02 02:30:57

This is caused by the following.



```
sage: a = -x/(2*x-4)
sage: e = lambda e: taylor(e,x,3,4)
sage: b = e(a)._maxima_(); b
x-(x-3)^4+(x-3)^3-(x-3)^2-9/2
```



I don't know a good/easy way to prevent this from happening.


---

Comment by mhansen created at 2008-02-02 02:41:06

Note that this issue arises from using Maxima internally for symbolic matrices.  If we use Sage's generic matrices over SR, then this isn't an issue.


One possible fix would be to add a simplify=False option to tell maxima not to use any simplification rules when constructing the object.


---

Comment by gfurnish created at 2008-03-16 20:10:56

Changing assignee from was to gfurnish.


---

Comment by gfurnish created at 2008-03-16 20:10:56

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-22 22:49:41

Note that this will be fixed when we switch over to Pynac as symbolic arithmetic won't have a huge overhead.


---

Comment by mhansen created at 2009-06-04 21:15:47

Resolution: invalid


---

Comment by mhansen created at 2009-06-04 21:15:47

This is now fixed due to the changes in 4.0


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: m = matrix(1,[-x/(2*x-4)])
sage: sage: m.apply_map(lambda e: taylor(e,x,0,4))
[1/32*x^4 + 1/16*x^3 + 1/8*x^2 + 1/4*x]
sage: sage: m.apply_map(lambda e: taylor(e,x,0,4))
[1/32*x^4 + 1/16*x^3 + 1/8*x^2 + 1/4*x]
sage: sage: m.apply_map(lambda e: taylor(e,x,1,4))
[(x - 1)^4 + (x - 1)^3 + (x - 1)^2 + x - 1/2]
sage: sage: m.apply_map(lambda e: taylor(e,x,2,4))
[-1/(x - 2) - 1/2]
sage: sage: m.apply_map(lambda e: taylor(e,x,3,4))
[-(x - 3)^4 + (x - 3)^3 - (x - 3)^2 + x - 9/2]
sage: sage: m[0,0].taylor(x,3,4)
-(x - 3)^4 + (x - 3)^3 - (x - 3)^2 + x - 9/2
```

