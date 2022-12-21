# Issue 4981: [with patch, needs review] clean up polynomial_ring.py

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2009-01-15 13:17:33

Assignee: burcin

CC:  malb

The way element classes are chosen in `sage/rings/polynomial/polynomial_ring.py` goes very much against object oriented design, and is basically ugly. :)

Attached patch tries to clean up this file, moves the decision of element classes to the immediate parents, adds some tests, and unifies the `__call__` methods. This also makes it much easier to add support for specialized polynomial classes.


---

Comment by cremona created at 2009-01-18 17:58:30

Review:  Patch applies cleanly to 3.2.3.  All looks very sensible to me, and I trust burcin to know what he is doing, though I cannot say that I followed through all the logic.  All doctests in rings/polynomial pass, so I think that this is good to go.


---

Comment by mabshoff created at 2009-01-19 03:28:43

This patch causes the following trivial to fix doctest failure:

```
mabshoff`@`geom:/scratch/mabshoff/sage-3.3.alpha0$ ./sage -t -long devel/sage/sage/calculus/calculus.py
sage -t -long "devel/sage/sage/calculus/calculus.py"        
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha0/devel/sage/sage/calculus/calculus.py", line 1912:
    sage: type(a)
Expected:
    <type 'sage.rings.polynomial.polynomial_element.Polynomial_generic_dense'>
Got:
    <class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_generic_dense_field'>
**********************************************************************
```

Unfortunately the following test

```
Trying:
    Integer(2)*P + Integer(2)*Q # indirect doctest###line 208:_sage_    >>> 2*P + 2*Q # indirect doctest
Expecting:
    (x^2 - 2*x + 1, y - 3/2*a*x + 1/2*a)
```

in sage/schemes/hyperelliptic_curves/jacobian_morphism.py seems to loop forever - at least I killed it after it used 22 minutes of CPU time on the new sage.math.

Cheers,

Michael


---

Comment by burcin created at 2009-01-21 08:15:53

A new patch which fixes the doctests is attached.


---

Comment by ncalexan created at 2009-01-21 19:04:20

Code wise: this looks great!  I heartily agree with the sentiment and implementation.

Testing wise: I tested this on sage.math and think that it works.


---

Comment by mabshoff created at 2009-01-23 02:41:08

Unfortunately this has been broken due to other merges, probably #4965:

```
mabshoff`@`geom:/scratch/mabshoff/sage-3.3.alpha1/devel/sage$ patch -p1 < trac_4981_polynomial_ring.patch 
patching file sage/calculus/calculus.py
patching file sage/misc/classgraph.py
patching file sage/rings/polynomial/polynomial_ring.py
Hunk #2 succeeded at 86 with fuzz 2 (offset 2 lines).
Hunk #3 succeeded at 102 (offset 2 lines).
Hunk #4 succeeded at 111 (offset 2 lines).
Hunk #5 succeeded at 156 (offset 2 lines).
Hunk #6 succeeded at 167 (offset 2 lines).
Hunk #7 succeeded at 231 (offset 2 lines).
Hunk #8 succeeded at 277 (offset 2 lines).
Hunk #9 succeeded at 490 (offset 2 lines).
Hunk #10 FAILED at 504.
Hunk #11 succeeded at 968 (offset 2 lines).
Hunk #12 succeeded at 983 (offset 2 lines).
Hunk #13 FAILED at 1125.
2 out of 13 hunks FAILED -- saving rejects to file sage/rings/polynomial/polynomial_ring.py.rej
patching file sage/rings/polynomial/polynomial_template.pxi
Hunk #1 FAILED at 85.
1 out of 1 hunk FAILED -- saving rejects to file sage/rings/polynomial/polynomial_template.pxi.rej
```

Please rebase for 3.3.alpha1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 17:33:27

I fixed a tiny doctesting issue in the second patch:

```
sage -t -long "devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py", line 84:
    sage: A.<y> = PolynomialRing(GF(2)); A
Expected:
    Univariate Polynomial Ring in y over Finite Field of size 2
Got:
    Univariate Polynomial Ring in y over Finite Field of size 2 (using NTL)
**********************************************************************
1 items had failures:
```

Burcin explained how he fixed the hang, positive review.

Cheers,

Michael


---

Comment by burcin created at 2009-01-24 17:36:47

clean up polynomial_ring.py (take 4)


---

Comment by mabshoff created at 2009-01-24 17:45:36

Resolution: fixed


---

Attachment

Merged polynomial_ring.py (take 4) in Sage 3.3.alpha2
