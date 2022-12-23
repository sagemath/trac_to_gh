# Issue 2206: Factorizations

Issue created by migration from https://trac.sagemath.org/ticket/2206

Original creator: jason

Original creation time: 2008-02-18 21:24:31

Assignee: somebody

A few miscellaneous improvements/fixes to Factorizations from mhansen's patches at 2028.


---

Attachment


---

Comment by ncalexan created at 2008-02-19 00:30:45

Looks good to me.  I assume a factorization with powers > maximum integer is not supported?  Because we're converting via int(...).

Apply.


---

Comment by was created at 2008-02-19 00:35:52

> I assume a factorization with powers > maximum integer is 
> not supported? Because we're converting via int(...).

What is "maximum integer"?   In pure python code int(...)
is arbitrary precision. 

William


---

Comment by mabshoff created at 2008-02-19 15:05:16


```
sage$ patch -p1 --dry-run < trac_2206_factorization.patch
patching file sage/structure/factorization.py
Hunk #3 FAILED at 261.
Hunk #4 FAILED at 280.
Hunk #5 FAILED at 291.
3 out of 5 hunks FAILED -- saving rejects to file sage/structure/factorization.py.rej
```


Please rebase and resubmit the patch. It would also be good to change the subject line to something more descriptive.

Cheers,

Michael


---

Attachment

Rebased against 2.10.2.


---

Comment by mabshoff created at 2008-02-25 04:17:52

Resolution: fixed


---

Comment by mabshoff created at 2008-02-25 04:17:52

Merged factorization.2.patch in Sage 2.10.3.alpha0
