# Issue 2409: plot'ting constants

Issue created by migration from https://trac.sagemath.org/ticket/2409

Original creator: jbmohler

Original creation time: 2008-03-06 20:33:24

Assignee: was

The command 

```
sage: plot(x+1,(x,1,4))
```

produces a very nice line with slope 1 (and I love the syntax which I think is a moderately recent improvement!).

By analogy,

```
sage: plot(1,(x,1,4))
```

should produce a horizontal line.



---

Comment by mhansen created at 2008-08-26 02:00:09

These will be fixed by #3952


---

Comment by mhansen created at 2008-08-26 02:03:38

Note that this depends on #2410 and #3853.


---

Comment by mabshoff created at 2008-08-26 21:54:49

Resolution: fixed


---

Comment by mabshoff created at 2008-08-26 21:54:49

Since #3952 was merged this is fixed.

Cheers,

Michael
