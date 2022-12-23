# Issue 9955: latex(-1/2 * polynom) broken

Issue created by migration from https://trac.sagemath.org/ticket/9956

Original creator: schilly

Original creation time: 2010-09-20 18:26:19

Assignee: burcin

Notice that in the latex expression the negative coefficient applies only to the 4*m^2 term in the numerator thus giving a completely different value.


```
sage: var('t k m')
sage: latex(-1/2*(4*m^2 - 9*m - t + 8)/m)
\frac{-4 \, m^{2} - 9 \, m - t + 8}{2 \, m}
```


Note: This was reported via the "report a problem" form for 4.5.2 for the "typset" option in the notebook, and I confirmed this on 4.5.3 for this simpler example.


---

Comment by burcin created at 2010-09-21 06:22:06

After installing the pynac package at #9901, this works for me:


```
sage: var('t k m')
(t, k, m)
sage: latex(-1/2*(4*m^2 - 9*m - t + 8)/m)
-\frac{4 \, m^{2} - 9 \, m - t + 8}{2 \, m}
```


Although the problem was never reported in this form, which is much more severe, #9834 and #9394 already cover this. I'm closing this as a duplicate.

Feel free to mark one/all of the tickets mentioned above as blockers.


---

Comment by burcin created at 2010-09-21 06:22:06

Resolution: duplicate
