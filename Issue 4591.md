# Issue 4591: magma -- EllipticCurve('37a').three_selmer_rank() fails in Magma 2.14

Issue created by migration from https://trac.sagemath.org/ticket/4591

Original creator: was

Original creation time: 2008-11-23 04:22:13

Assignee: was

In Magma 2.13 this works:

```
EllipticCurve('37a').three_selmer_rank()
```

but in Magma 2.14 it doesn't (tested on osx and linux):

```
sage: EllipticCurve('37a').three_selmer_rank()
```


This is implemented by a script I ship that is a modified versin of a magma script.
I thus need to fix this.  


---

Comment by was created at 2008-11-23 07:32:58

this totally fixes the problem, and is much simpler and better doctested code.  it also is much faster and works with both magma 2.13 and 2.14.


---

Attachment


---

Comment by was created at 2008-11-23 07:37:56

it is very important to delete the whole directory data/extcode/magma/stoll, even if hg doesn't do that.  check it!


---

Attachment

Positive review. wstein explained the reasons behind the switch to Magma code in detail, so I am happy.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-23 08:05:46

Unfortunately there are slight reject issues:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage$ patch -p1 --dry-run < trac_4591_sage-4591.patch 
patching file sage/interfaces/magma.py
Hunk #1 FAILED at 744.
1 out of 1 hunk FAILED -- saving rejects to file sage/interfaces/magma.py.rej
patching file sage/schemes/elliptic_curves/ell_rational_field.py
patching file sage/schemes/elliptic_curves/magma_3descent.py
```


Cheers,

Michael


---

Attachment

rebased version.


---

Comment by mabshoff created at 2008-11-23 08:18:19

Resolution: fixed


---

Comment by mabshoff created at 2008-11-23 08:18:19

Merged in Sage 3.2.1.alpha0
