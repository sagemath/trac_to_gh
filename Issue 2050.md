# Issue 2050: disallow *generic* matrix eigenspaces for inexact fields (very easy to implement)

Issue created by migration from https://trac.sagemath.org/ticket/2050

Original creator: was

Original creation time: 2008-02-05 05:00:28

Assignee: was

CC:  ncalexander@gmail.com

Instead of lying the following code should just raise a NotImplementedError.  Basically use the `is_exact()` method on rings to determine if the ring is not exact, and if so, raise an error on eigenspaces computation.  Some generic algorithms suck for inexact rings.   One thing, the error message for RR and CC could suggest using RDF or CDF... and maybe when prec <= 53, the code could use RDF or CDF (?). 


```
sage: R=RealField(30)
sage: M=matrix(R,2,[2,1,1,1])
sage: M.eigenspaces()

[
(2.6180340, [

]),
(0.38196601, [

])
]
```



---

Comment by was created at 2008-02-05 05:00:42

See #1706 for a related ticket.


---

Attachment


---

Comment by mhansen created at 2008-02-27 18:43:38

I get the following against 2.10.3.alpha0:


```
cd "/home/mhansen/sage-2.10.3.alpha0/devel/sage" && hg status
cd "/home/mhansen/sage-2.10.3.alpha0/devel/sage" && hg status
cd "/home/mhansen/sage-2.10.3.alpha0/devel/sage" && hg import   "/home/mhansen/.sage/temp/sage/15288/tmp_0.patch"
applying /home/mhansen/.sage/temp/sage/15288/tmp_0.patch
patching file sage/matrix/matrix2.pyx
Hunk #4 succeeded at 2130 with fuzz 2 (offset 0 lines).
Hunk #5 FAILED at 2146
Hunk #6 FAILED at 2163
2 out of 7 hunks FAILED -- saving rejects to file sage/matrix/matrix2.pyx.rej
abort: patch failed to apply
```



---

Attachment


---

Comment by mhansen created at 2008-02-27 22:58:58

I've made a patch 2050 which applies cleanly after #2299 .  All tests pass so things look good to me.


---

Comment by mabshoff created at 2008-02-28 00:57:07

Merged 2050.patch in Sage 2.10.3.rc0


---

Comment by mabshoff created at 2008-02-28 00:57:07

Resolution: fixed
