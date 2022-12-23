# Issue 5845: Fix precision bug in hilbert_class_polynomial()

Issue created by migration from https://trac.sagemath.org/ticket/5845

Original creator: cremona

Original creation time: 2009-04-21 10:41:47

Assignee: tbd

Keywords: hilbert class polynomial quadratic form

The code introduced in #4990 uses an incorrect precision bound in a paper of Enge.  Enge has supplied a corrected bound, and the code fixed to use it.  At the same time, 
    * The code has been extended to non-fundamental discriminants
    * It has been moved to sage/schemes/elliptic_curves/cm.py which had a similar function requiring Magma;  the method for number fields now calls this.
    * The function elliptic_j has been added to sage/functions/special.py
    * A new method is_primitive() has been added for integral binary quadratic forms, as well as a primitive_only flag to the function `BinaryQF_reduced_representatives`.
    * Last but not least, sage/schemes/elliptic_curves/cm.py has been ReST-ified and added to the reference manual

This started out as just a conversion of one small file with only 3 functions in it to ReST!


---

Comment by cremona created at 2009-04-21 10:45:10

Applies to 3.4.1.rc4


---

Attachment


---

Comment by stankewicz created at 2009-05-23 17:45:47

All doctests pass. It works very well and is a sorely needed addition to sage.

One minor point: In the patch the paper of Enge calls for a constant of log(2*10.163) while the code has a typo which sets this constant to log(2*10.63). This makes no difference whatsoever in the output of the program(indeed there's no difference in the operation of the code for h<~24) but it's worth noting.


---

Comment by cremona created at 2009-05-23 18:49:34

Thanks for the report.  I don't have access to Enge's paper at the moment but I'll see him in person tomorrow so I can perhaps check up on that type (recall that one of his papers had a lot of typos in it, and I took the "official" bounds from correspondence with him).


---

Comment by mhansen created at 2009-06-01 04:28:14

This needs to rebased against 4.0 since functions/special.py has changed.  The elliptic_j function should be written to match those.


---

Comment by cremona created at 2009-06-01 08:01:53

Replying to [comment:5 mhansen]:
> This needs to rebased against 4.0 since functions/special.py has changed.  The elliptic_j function should be written to match those.
Will do -- John


---

Attachment

Rebased to 4.0 (replace previous)


---

Comment by cremona created at 2009-06-01 08:22:45

I have done the rebasing -- not sure whether it's ok to put back "with positive review" to I have marked it "needs review" again.


---

Comment by AlexGhitza created at 2009-06-01 11:15:05

Good.


---

Comment by ncalexan created at 2009-06-13 21:12:28

Resolution: fixed
