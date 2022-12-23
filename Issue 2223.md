# Issue 2223: sage-2.10.2.alpha1 -- bessel_J -- precision errors

Issue created by migration from https://trac.sagemath.org/ticket/2223

Original creator: was

Original creation time: 2008-02-20 06:54:22

Assignee: somebody

On OSX 

```
sage -t  devel/sage-main/sage/functions/special.py          **********************************************************************
File "special.py", line 506:
    sage: bessel_J(3,10,"scipy")
Expected:
    0.0583793793052... - 1.65905485529...e-17*I
Got:
    0.0583793793052000 - 2.93425242844000e-17*I
**********************************************************************
1 items had failures:
```


Thoughts:

It's likely a theorem that bessel_J is always real
for integer first argument?  If so, let's just return
the real part and be done with these weird imaginary
part issues:

```
sage: bessel_J(3,10,"scipy")
0.0583793793052000 - 2.93425242844000e-17*I
sage: bessel_J(4,10,"scipy")
9.69299109301000e-17*I - 0.219602686102000
sage: bessel_J(5,10,"scipy")
1.11203257018000e-16*I - 0.234061528187000
sage: bessel_J(10,10,"scipy")
0.207486106633000 - 1.17732704470000e-16*I
sage: bessel_J(10,20,"scipy")
0.186482558024000 - 2.10019326787000e-16*I
```



---

Comment by wdj created at 2008-02-20 11:30:16

I assumed (stupdly) that ...e-(large) would be parsed as 0. I can replace all terms with
e-(large) by 0.000... if that seems reasonable.


---

Comment by wdj created at 2008-02-20 11:46:23

More precisely: I can replace all terms with e-(large)*I by 
(a) "0.000...*I" (to indicate that the user might get a small number returned from scipy) or 
(b) "0.0*I" or 
(c) nothing (as William stated), 
whichever seems more reasonable.


---

Attachment


---

Comment by wdj created at 2008-02-21 00:00:35

The attached patch fixes the problem referred to above. It replaces *e-(large)*I by nothing in the docstring. Paases sage -t. sage -testall has lots of failures, but none seem related to this patch.


---

Comment by mabshoff created at 2008-02-21 00:08:38

David, the patch you posted only removes one space. You probably need to export at least one commit prior to that.

Cheers,

Michael


---

Comment by wdj created at 2008-02-21 01:09:56

Sorry. I don't know what I did wrong. I thin this new patch is better.


---

Attachment

William's pat


---

Comment by mabshoff created at 2008-02-22 01:03:14

As is the patch doesn't apply:

```
sage$ patch -p1 --dry-run < trac_2223.patch
patching file sage/functions/special.py
Hunk #1 FAILED at 5.
Hunk #2 succeeded at 500 (offset 7 lines).
Hunk #3 FAILED at 514.
Hunk #4 succeeded at 537 with fuzz 2 (offset 10 lines).
2 out of 4 hunks FAILED -- saving rejects to file sage/functions/special.py.rej
```

I guess the only important hunk is the third one, so I will probably merge that one manually.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-22 01:06:16

Resolution: fixed


---

Comment by mabshoff created at 2008-02-22 01:06:16

Merged hunk 3 manually in Sage 2.10.2.rc0
