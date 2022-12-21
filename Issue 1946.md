# Issue 1946: Tate's algorithm has NO DOCTESTS!  See sage/schemes/elliptic_curves/ell_number_field.py

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-27 02:36:59

Assignee: was

I'm sure -- after a bit of a glance, for example, at scale_curve,
that lots of this code is broken as a result of having no doctests!


---

Comment by was created at 2008-01-27 15:09:09

Changing status from new to assigned.


---

Comment by cremona created at 2008-01-28 06:28:25

patch for elliptic_curve and number_field stuff


---

Attachment

Lots of doctests for elliptic curves with many bug fixes for bugs revealed by them.

Several new functions for changing models:  thought still needed on how to return the isomorphism as well as the new model;  if not Magma style then by storing the map as an attribute of the new curve as is done for number fields?

Joint work by John Cremona and William Stein.


---

Comment by cremona created at 2008-01-31 05:17:08

The previous patch left some failing doctests in number_field_ideal_rel.py.
This patch 8090.patch fixed those with some substantial reworking of the classes NumberFieldIdeal, NumberFieldFractionalIdeal and NumberFieldFractionalIdeal_rel. 

Please would people with experience of the elliptic curve classes review 8089.patch and someone who knows the number field code review 8090.patch (which should be applied after 8089.patch.

By the way, I have checked all doctest in both number_field/ and elliptic_curve/ directories (and have added lots to these), and also the doc and const directories (where a couple of changes were needed).


---

Comment by ncalexan created at 2008-02-15 05:09:04

8090 looks fine to me, lots of good doctests.  I can't view 8089.


---

Comment by cremona created at 2008-02-18 08:57:33

8090.patch has a positive review but 8089 has not yet been reviewed.  I don't know why it cannot be viewed directly from the trac page!


---

Comment by mabshoff created at 2008-02-18 19:24:47

Replying to [comment:5 cremona]:
>  8090.patch has a positive review but 8089 has not yet been reviewed.  I don't know why it cannot be viewed directly from the trac page!
> 

The parent of the patch is in 2.10.2.alpha0 and the trac installations uses the release branch. You can still download the patch and look at it "manually".

Cheers,

Michael


---

Attachment

This replaces Cremona's previous version; but has a comment and applies cleanly.


---

Comment by was created at 2008-02-19 17:22:24

Changing assignee from was to cremona.


---

Comment by was created at 2008-02-19 17:22:24

Changing status from assigned to new.


---

Comment by was created at 2008-02-19 17:22:24

REFEREE REPORT:

1. I applied both patches to sage-2.10.1.alpha0.  There is one rejected hunk
in the second patch (8090.patch).  I replaced 8090.patch by one that works without
any problems.

2. After applying both patches all doctests in elliptic curves and number fields pass. 

3. I fixed a number of formating issues with the new docstrings. See the third patch 3.

4. This patch rocks!  It is a major significant contribution to improving the doctest coverage and quality of the sage elliptic curve code. Very positive review.


---

Attachment

apply all three patches, including this one


---

Comment by mabshoff created at 2008-02-19 17:35:27

I am getting more rejects if I apply against my current version of 2.10.2.alpha1 (which will be alpha2 in about 30 minutes):

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/devel/sage$ patch -p1 --dry-run < 8089.patch
patching file sage/rings/ideal.py
patching file sage/rings/number_field/all.py
Hunk #1 succeeded at 6 with fuzz 1.
patching file sage/rings/number_field/number_field.py
Hunk #1 succeeded at 162 (offset 5 lines).
Hunk #2 succeeded at 1248 (offset 24 lines).
Hunk #3 succeeded at 1259 (offset 24 lines).
Hunk #4 succeeded at 1289 (offset 24 lines).
patching file sage/rings/number_field/number_field_element.pyx
Hunk #1 succeeded at 1550 (offset 12 lines).
Hunk #2 succeeded at 1563 with fuzz 1 (offset 12 lines).
patching file sage/rings/number_field/number_field_ideal.py
patching file sage/rings/number_field/number_field_ideal_rel.py
patching file sage/schemes/elliptic_curves/cm.py
patching file sage/schemes/elliptic_curves/ell_field.py
patching file sage/schemes/elliptic_curves/ell_finite_field.py
Hunk #1 FAILED at 42.
Hunk #2 FAILED at 66.
Hunk #3 FAILED at 81.
Hunk #4 FAILED at 142.
Hunk #5 FAILED at 211.
Hunk #6 FAILED at 241.
Hunk #7 FAILED at 298.
Hunk #8 FAILED at 400.
Hunk #9 succeeded at 783 with fuzz 2 (offset 359 lines).
Hunk #10 FAILED at 801.
9 out of 10 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_finite_field.py.rej
patching file sage/schemes/elliptic_curves/ell_generic.py
Hunk #3 succeeded at 1483 (offset 23 lines).
Hunk #4 succeeded at 1629 (offset 23 lines).
patching file sage/schemes/elliptic_curves/ell_number_field.py
patching file sage/schemes/elliptic_curves/ell_rational_field.py
Hunk #2 succeeded at 1519 (offset 11 lines).
Hunk #3 succeeded at 1574 (offset 11 lines).
Hunk #4 succeeded at 1607 (offset 11 lines).
Hunk #5 succeeded at 1680 (offset 11 lines).
Hunk #6 succeeded at 2176 (offset 11 lines).
Hunk #7 succeeded at 2886 (offset 46 lines).
patching file sage/schemes/elliptic_curves/padics.py
Hunk #1 succeeded at 36 (offset 1 line).
Hunk #2 succeeded at 1195 (offset 210 lines).
Hunk #3 succeeded at 1244 (offset 210 lines).
patching file sage/schemes/elliptic_curves/weierstrass_morphism.py
```

I suggest rebasing against 2.10.2.alpha2.

Cheers,

Michael


---

Comment by was created at 2008-02-19 17:45:14

Gees!  This all applies cleanly to alpha0.  Here's an hg bundle that I made by applying all three patches cleanly to alpha 0 and doing hg_sage.send:

http://sage.math.washington.edu/home/was/tmp/1946.hg


---

Comment by mabshoff created at 2008-02-21 13:19:33

Replying to [comment:9 was]:
> Gees!  This all applies cleanly to alpha0.  Here's an hg bundle that I made by applying all three patches cleanly to alpha 0 and doing hg_sage.send:
> 
> http://sage.math.washington.edu/home/was/tmp/1946.hg

Even that bundle does not apply cleanly against my 2.10.2.a1 or 2.10.2.a2. It looks like a whole bunch of trivial, white space related rejects. One exception is the fixed doctest, but that is easy to fix.

Cheers,

Michael


---

Comment by was created at 2008-02-21 15:14:06

This is a new bundle rebased against alpha2.  It also contains one additional patch that fixes two doctest failures (one in elliptic_curve/padic.py and one number field
ideal doctest). 

http://sage.math.washington.edu/home/was/patches/sage-1946.hg


---

Comment by mabshoff created at 2008-02-21 15:17:45

Merged sage-1946.hg in Sage 2.10.2.rc0


---

Comment by mabshoff created at 2008-02-21 15:17:45

Resolution: fixed
