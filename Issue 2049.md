# Issue 2049: symbolic matrix exp (easy to implement)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-05 04:55:07

Assignee: was


```

> On a related issue: is there a command corresponding to Mathematica's
> MatrixExp? For example,
> 
> sage: var('t')
> sage: M=matrix(SR,2,[0,t,-t,0])
> sage: M.matrix_exp()
> 
> [cos(t), sin(t)]
> [-sin(t), cos(t)]
> 

There is no such command in Sage, really.  Maxima
does have such a command, so it would be
possible to implement something easily:

sage: t = var('t')
sage: M = matrix(SR,2,[0,t,-t,0])
sage: mm = maxima(M)
sage: mm.matrixexp()
matrix([%e^-(%i*t)*(%e^(2*%i*t)+1)/2,-%e^-(%i*t)*(%i*%e^(2*%i*t)-%i)/2],[%e^-(%i*t)*(%i*%e^(2*%i*t)-%i)/2,%e^-(%i*t)*(%e^(2*%i*t)+1)/2])

So there will be an M.exp() function in some future version
of Sage. 
```



---

Comment by was created at 2008-02-05 05:15:18

Changing status from new to assigned.


---

Attachment

This patch has already been merged (checked in 2.10.2.rc0).


---

Comment by AlexGhitza created at 2008-02-23 01:23:26

Resolution: fixed


---

Comment by mabshoff created at 2008-02-23 01:27:59

This one snuck in via one of the bundles from #174 or #2190. Bundles are bad.

It would be nice if anybody could give this a proper review, despite the fact that it already is in 2.10.2.

Cheers,

Michael


---

Comment by AlexGhitza created at 2008-02-23 01:36:02

Oh, yes, I looked at it, thought it looked good, tried to import the patch and got a bunch of rejects, noticed that it had already been merged.

Conclusion: it's good, should be applied, and was applied.
