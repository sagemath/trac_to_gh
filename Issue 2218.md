# Issue 2218: assuming an expression is not equal to zero doesn't work

Issue created by migration from https://trac.sagemath.org/ticket/2218

Original creator: mhansen

Original creation time: 2008-02-20 03:50:43

Assignee: mhansen

CC:  b.w.barker@smokejive.net


```
sage: v,c = var('v,c')
sage: assume(c!=0)
sage: integral((1+v^2/c^2)^3/(1-v^2/c^2)^(3/2),v)
...
<type 'exceptions.TypeError'>: Computation failed since Maxima requested additional constraints (use assume):
Is  c  zero or nonzero?
```


This is caused by the following:

```
sage: eq = c != 0
sage: eq._maxima_init_(assume=True)
'(c)#(0)'

(%i1) assume(c#0);
`assume': `#' means syntactic nonequality in Maxima. Maybe you want to use `not equal'.
 -- an error.  To debug this try debugmode(true);

```

and is fixed by the following:

```
sage: sage.calculus.calculus.maxima.assume('notequal(c,0)');
sage: integral((1+v^2/c^2)^3/(1-v^2/c^2)^(3/2),v)
-75*sqrt(c^2)*arcsin(sqrt(c^2)*v/c^2)/8 - v^5/(4*c^4*sqrt(1 - v^2/c^2)) - 17*v^3/(8*c^2*sqrt(1 - v^2/c^2)) + 83*v/(8*sqrt(1 - v^2/c^2))

```



---

Comment by mhansen created at 2008-02-20 03:58:48

Changing status from new to assigned.


---

Attachment


---

Comment by was created at 2008-02-20 06:08:00

Very nice getting to the bottom of this.


---

Comment by mabshoff created at 2008-02-20 09:41:32

Resolution: fixed


---

Comment by mabshoff created at 2008-02-20 09:41:32

Merged in Sage 2.10.2.alpha2
