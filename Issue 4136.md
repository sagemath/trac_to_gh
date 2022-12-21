# Issue 4136: [with patch, needs review] enable tail reduction when reducing multivariate polynomials

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-09-16 17:53:33

Assignee: malb

This was reported on *[sage-support]*:

```
hi there,

this is going to be even worse than my recent bug report in terms of
reproducing the error. I guess i'll start with describing what
happens, and then if someone tells me that it's a bug and not a
feature, then i'll try to get a minimal example.

So I've got a polynomial ring with a few dozens variables, over a
cyclotomic field, and i've got an ideal J with hundreds of generators.
J contains at least y9 + y12. Then i got something like:

sage: J.reduce(y9 - y12)
2*y9   #which is fine

sage: J.reduce(y13*y15)
y13*y15 #why not

sage: J.reduce(y13*y15 + y9 - y12)
y13*y15 + y9 - y12

Now what's up with that ? shouldn't it be y13*y15 + 2*y9 ? that's what
i expect from the term 'reduction' anyway. Is this normal or is it a
bug ? if it's a bug, could it influence the equivalence x in J iff
J.reduce(x) == 0 ?

So if this is a bug i'll give you more details.

thanks!
Pierre
```


http://groups.google.com/group/sage-support/browse_thread/thread/138e473f31c2f2b5

```

```




---

Comment by malb created at 2008-09-20 15:49:01

Changing status from new to assigned.


---

Comment by PolyBoRi created at 2008-10-17 06:24:01

it's ok.


---

Comment by mabshoff created at 2008-10-20 11:53:20

Mhhh, what are the patch dependencies here?

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha0/devel/sage$ patch -p1  < trac_4136_tail_reduce.patch 
patching file sage/rings/polynomial/multi_polynomial_element.py
Hunk #1 FAILED at 1485.
Hunk #2 FAILED at 1511.
2 out of 2 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_element.py.rej
```


Cheers,

Michael


---

Attachment


---

Comment by malb created at 2008-10-20 13:21:00

I rebased the patch to 3.1.3


---

Comment by mabshoff created at 2008-10-20 14:32:34

Merged in Sage 3.2.alpha0


---

Comment by mabshoff created at 2008-10-20 14:32:34

Resolution: fixed
