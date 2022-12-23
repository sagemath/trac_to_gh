# Issue 4713: make an apply_map function for vectors

Issue created by migration from https://trac.sagemath.org/ticket/4713

Original creator: jason

Original creation time: 2008-12-05 08:08:13

Assignee: was

Matrices have the function; it would be handy for vectors to also have this utility function.


---

Comment by jason created at 2008-12-05 08:32:49

Changing assignee from was to jason.


---

Comment by jason created at 2008-12-05 08:32:49

Changing status from new to assigned.


---

Comment by was created at 2008-12-06 23:26:02

You could also do this in the first example:

```
sage: m = vector(ZZ, 9, range(9)) 
sage: k.<a> = GF(9) 
sage: m.apply_map(k)
(0, 1, 2, 0, 1, 2, 0, 1, 2)
```


I think it would be nice to have a really simple first example, that requires much less knowledge of "abstract algebra".  Maybe the first example could be for engineers or something?

```
sage: m = vector([1,x,sin(x+1)])
sage: m.apply_map(x^2)
(1, x^2, sin(x + 1)^2)
sage: m.apply_map(sin)
(sin(1), sin(x), sin(sin(x + 1)))
```



---

Comment by was created at 2008-12-06 23:26:46

By the way, definitely positive review pending adding the doctests suggested above.


---

Attachment

updated patch with the suggestions.  Accordingly, marking this positive review.


---

Comment by mabshoff created at 2008-12-07 09:06:44

Resolution: fixed


---

Comment by mabshoff created at 2008-12-07 09:06:44

Merged in Sage 3.2.2.alpha1
