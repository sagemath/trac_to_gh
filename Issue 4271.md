# Issue 4271: [with patch, needs review] improve coverage test of ell_generic.py to 100%, and fix typos

Issue created by migration from https://trac.sagemath.org/ticket/4271

Original creator: zimmerma

Original creation time: 2008-10-12 20:07:22

Assignee: mabshoff


```
bash-3.00$ sage -t ell_generic.py
sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_generic.py
         [74.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 74.0 seconds
bash-3.00$ sage -coverage ell_generic.py
----------------------------------------------------------------------
ell_generic.py
SCORE ell_generic.py: 100% (60 of 60)
----------------------------------------------------------------------
```



---

Attachment


---

Comment by cremona created at 2008-10-13 11:47:06

The patch is good.  It apples cleanly to 3.1.3.alpha3 and works as advertised.  Thanks, Paul -- almost all those typos were due to me!

John (in his lunch break in Bordeaux)

Michael: this only affects docstrings so should have no effect outside this one file.


---

Comment by mabshoff created at 2008-10-13 12:40:12

Replying to [comment:1 cremona]:
> Michael: this only affects docstrings so should have no effect outside this one file.

Hi John,

you actually beat me to a review and I was also convinced that this patch has 0% risk, so I will merge it into 3.1.3.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-14 12:31:16

Resolution: fixed


---

Comment by mabshoff created at 2008-10-14 12:31:16

Merged in Sage 3.1.3.final
