# Issue 3837: Performance regression in sha.py due to #3674

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-08-13 17:14:08

Assignee: cremona

Thew new code uses symbolic sqrt, ceil and floor. Hence doctest timing of sha.py go from 22 to 45 seconds and the long version goes from 4 minutes to 10.5. Most of the time is spend in Maxima.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-13 17:14:15

Changing priority from major to blocker.


---

Comment by cremona created at 2008-08-13 22:04:30

I did not change sha.py.  I did delete some imports from ell_point.py which were not used in that file.  If the author of sha.py wants or needs some functions, they should import them!

John


---

Comment by mabshoff created at 2008-08-13 22:23:40

The following seems to be the offending code: In trac_3674_sage-trac3674new.patch

```
+++ b/sage/schemes/elliptic_curves/ell_point.py Thu Aug 07 22:02:56 2008 +0100
`@``@` -54,7 +54,6 `@``@` AUTHORS:
 #                  http://www.gnu.org/licenses/
 #*****************************************************************************
 
-from math import ceil, floor, sqrt
```

And then

```
--- a/sage/schemes/elliptic_curves/ell_rational_field.py        Wed Jul 30 06:34:58 2008 -0700
+++ b/sage/schemes/elliptic_curves/ell_rational_field.py        Thu Aug 07 22:02:56 2008 +0100
`@``@` -11,6 +11,8 `@``@` AUTHORS:
    -- Christian Wuthrich (2007): added padic sha computation
    -- David Roe (2007-9): moved sha, l-series and p-adic functionality to separate files.
    -- John Cremona (2008-01)
+   -- Tobias Nagel & Michael Mardaus (2008-07): added integral_points
+   -- John Cremona (2008-07): further work on integral_points
 """
 
 #*****************************************************************************
`@``@` -55,7 +57,7 `@``@` import sage.databases.cremona
 import sage.databases.cremona
 from   sage.libs.pari.all import pari
 import sage.functions.transcendental as transcendental
-import math
+from sage.calculus.calculus import sqrt, floor, ceil
```

So we end up (indirectly) calling Maxima in sha.py.

William and I discussed the problem and it seems that the new code requires higher precision as the double values provided by the Python math library. The goal is not to blame you three, but to sort out how we can avoid calling Maxima without breaking the new code. :)

Cheers,

Michael


---

Attachment


---

Attachment

The first patch really belongs to #3674 but I put it here:  I increased the default precision for elliptic_logarithm() from 53 to 100 bits and added a doctest showing how 53 bits is insufficient for a curve in the databse.

The second one sorts out the ceil/floor/sqrt confusion.  I hope.

In Michael and Tobias's original code they used sqrt (etc) from calculus, since they went looking for those functions and found them there first, without knowing that these were bad to use as they involved maxima, and low precision.  The math.sqrt (etc) functions were not good enough for our new code as we need to have more precision, and I rewrote it to use the syntax a.sqrt() instead of sqrt(a) as this involves no imports and guarantees that you use the right version of sqrt!  (I omitted a few which I have now converted like this, so I no longer need to import ceil or floor).  When I had done that I intended to delete their imports from calculus, but left one in by mistake, which managed to get used instead of the math ones.

I hope this is sorted now.  I take 8.9s to doctest sha.py (or 180s with -long) .

John


---

Comment by cremona created at 2008-08-14 14:45:47

Thanks -- I'm sure I changed the tag to "needs review" but apparently not!


---

Comment by mabshoff created at 2008-08-14 23:55:10

Hi John,

with both patches applied I am getting 

```
sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.rc0/tmp/ell_rational_field.py", line 3827:
    sage: a=E.integral_points([P1,P2,P3,P4,P5]); len(a)  # long time (400s!)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_100[12]>", line 1, in <module>
        a=E.integral_points([P1,P2,P3,P4,P5]); len(a)  # long time (400s!)###line 3827:
    sage: a=E.integral_points([P1,P2,P3,P4,P5]); len(a)  # long time (400s!)
      File "/scratch/mabshoff/release-cycle/sage-3.1.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 4161, in integral_points
        low_bound = R((sqrt(d_L_0 - Q) - T)/c)
    OverflowError: math range error
**********************************************************************
1 items had failures:
   1 of  13 in __main__.example_100
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.rc0/tmp/.doctest_ell_rational_field.py
         [69.0 s]
```

on sage.math.

Cheers,

Michael


---

Attachment


---

Comment by cremona created at 2008-08-15 08:20:47

Sorry about that, it is now fixed.

In one place I used sqrt(xxx) instead of xxx.sqrt(), in a place where sqrt was math.sqrt but xxx was some very large RealField element.  I have now vowed to never *ever* use floating point functions except via xxx.foo() since with foo(x) you never know what will happen -- someone else might add an import statement which meas that you will pick up the wrong foo().  Which is what caused this ticket in the first place.

Extra patch fixes this (I tested this doctest).


---

Comment by mabshoff created at 2008-08-15 09:16:04

Excellent, the three patches pass doctest, the changes are great Positive review. William also glanced at the changes.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-15 09:16:15

Merged in Sage 3.1.rc0


---

Comment by mabshoff created at 2008-08-15 09:16:15

Resolution: fixed
