# Issue 5953: sage/modular/modform/vm_basis.py is missing verbatim areas for doctests

Issue created by migration from https://trac.sagemath.org/ticket/5953

Original creator: mabshoff

Original creation time: 2009-05-01 05:03:46

Assignee: tba

This is what the ReST documentation looks like:

```
EXAMPLES:
sage: victor_miller_basis(1, 6) [] sage: victor_miller_basis(0, 6) [ 1 + O(q^6) ] sage: victor_miller_basis(2, 6) [] sage: victor_miller_basis(4, 6) [ 1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6) ]

sage: victor_miller_basis(6, 6, var=’w’) [ 1 - 504*w - 16632*w^2 - 122976*w^3 - 532728*w^4 - 1575504*w^5 + O(w^6) ]
```


Cheers,

Michael


---

Attachment


---

Comment by jhpalmieri created at 2009-05-01 05:43:49

I think that in INPUT and AUTHOR blocks, the lines shouldn't be indented. I'm attaching a referee's patch changing this, and also changing an instance of `$blah$` to ``blah``.  If you're happy with my patch, I'm happy with yours.


---

Comment by jhpalmieri created at 2009-05-01 05:44:09

referee's patch


---

Attachment

For the record: Reviewer patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-01 05:50:31

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-05-01 05:50:31

Changing assignee from tba to mabshoff.


---

Comment by mabshoff created at 2009-05-01 05:58:09

Merged both patches in Sage 3.4.2.final.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-01 05:58:09

Resolution: fixed
