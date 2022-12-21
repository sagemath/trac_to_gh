# Issue 5817: Update FLINT to 1.2.5 (latest upstream release)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-04-18 23:20:28

Assignee: mabshoff


```
I've release FLINT 1.2.5. This fixes a serious error that existed in
zn_poly-0.8. Unbeknownst to me, David Harvey had already fixed this
issue in zn_poly-0.9 but I had not realised that had been released,
due to him changing institutions and me not updating my link to his
webpage in my frequently visited tabs list. FLINT now uses zn_poly-0.9
by default for polynomial arithmetic over Z/nZ in zmod_poly.

There is still an issue with z_factor which fails to factor some
numbers very rarely (it prints a message to say it has failed). Tom
Boothby is working on a fix, and this should also speed up the
factorisation function noticeably.

Bill. 
```



---

Comment by mabshoff created at 2009-04-18 23:20:40

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-04-20 07:05:49

While I am at it: Please also add this fix to make the check target work on OSX, too:

```
diff -r fc2eb24f71a2 spkg-check
--- a/spkg-check        Thu Apr 09 00:29:11 2009 -0400
+++ b/spkg-check        Mon Apr 20 00:04:56 2009 -0700
`@``@` -17,6 +17,11 `@``@`
    FLINT_TUNE=" -fPIC -funroll-loops  "
 fi
 
+if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
+   echo "64 bit MacIntel"
+   FLINT_TUNE=" -fPIC -m64 -funroll-loops"
+fi
+
 export FLINT_TUNE
 
 FLINT_GMP_INCLUDE_DIR="$SAGE_LOCAL"/include/
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 08:13:35

The spkg is at 

  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.2/rc0/flint-1.2.5.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 08:29:16

Ok, this spkg needs a patch to module_list.py due to header changes for zn_poly.h. Bumping it to 4.0.

Cheers,

Mcihael


---

Comment by mabshoff created at 2009-04-30 08:58:56

Fixed the issue with headers, but monsky still has a small problem:

```
sage -t -long devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py
**********************************************************************
File "/scratch/mabshoff/sage-3.4.2.alpha0/devel/sage-main/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1562:
    sage: B.det()                                               # long time
Expected:
    11 + 484*t^2 + 451*t^3 + O(t^4)
Got:
    245 + 240*t + 724*t^2 + 808*t^3 + O(t^4)
**********************************************************************
```


The spkg is now at http://sage.math.washington.edu/home/mabshoff/spkgs/flint-1.2.5.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-11 07:26:56

FYI: Turning off znpoly in FLINT makes the doctest pass.

Cheers,

Michael


---

Comment by dmharvey created at 2009-05-28 15:47:10

I couldn't build the spkg on linux/opteron. I tried vanilla sage 3.4.2 with spkg/standard/flint-1.2.4.p2.spkg replaced by flint-1.2.5.spkg, building from scratch. It breaks at


```
fmpz.c:40:29: error: zn_poly/zn_poly.h: No such file or directory
```


while building FLINT. Am I doing this incorrectly, or is there some problem with the spkg?


---

Comment by dmharvey created at 2009-05-28 16:03:54

Ok, for some reason fmpz.c has

#include "zn_poly/zn_poly.h"

whereas all the other files have

#include "zn_poly/src/zn_poly.h"

When I change fmpz.c to the latter, the spkg builds.


---

Comment by dmharvey created at 2009-05-29 15:08:39

After fixing the build problem above, I can replicate mabshoff's doctest failure.

However, if one tries the computation directly, it gives the correct answer:


```
sage: S.<t> = PowerSeriesRing(Integers(1331), default_prec=4)
sage: B = Matrix([[1144 + 264*t + 841*t^2 + 1025*t^3 + O(t^4), 176 + 1052*t + 216*t^2 + 523*t^3 + O(t^4)], [847 + 668*t + 81*t^2 + 424*t^3 + O(t^4), 185 + 341*t + 171*t^2 + 642*t^3 + O(t^4)]])sage: B.det()11 + 484*t^2 + 451*t^3 + O(t^4)
```


Still investigating...


---

Comment by dmharvey created at 2009-05-29 15:56:24

Here is a simpler failure case:


```
sage: S.<t> = PolynomialRing(Integers(14641))
sage: f = 1 + 9581*t
sage: g = 1 + 4334*t
sage: R = PolynomialRing(Integers(1331), "t")
sage: ff = f.change_ring(R)
sage: gg = g.change_ring(R)
sage: ff
264*t + 1
sage: gg
341*t + 1
sage: ff * gg
925*t^2 + 605*t + 1
sage: (264 * 341) % 1331
847
```


So the `t^2` coefficient is wrong.


---

Comment by dmharvey created at 2009-05-29 16:05:52

The output of `change_ring` (in the previous example) is not of type `Polynomial_zmod_flint` as it should be, it ends up being `Polynomial_generic_dense`. The multiplication ff * gg is actually calling the generic karatsuba code in the Sage library, it's not calling FLINT or `zn_poly` as far as I can tell. Each input to `do_karatsuba()` is a list containing a single polynomial, instead of a list of coefficients.

Probably making `change_ring` return the correct type of object will fix all this mess. I don't think it has anything to do with FLINT or `zn_poly`. Maybe it's a coercion problem.


---

Comment by dmharvey created at 2009-05-29 16:28:04

Sorry, I'm an idiot. That code snippet above is using `change_ring` incorrectly. Here is a better example:


```
sage: S.<t> = PolynomialRing(Integers(14641))
sage: f = 1 + 9581*t
sage: g = 1 + 4334*t
sage: R = Integers(1331)
sage: ff = f.change_ring(R)
sage: gg = g.change_ring(R)
sage: ff
264*t + 1
sage: gg
341*t + 1
sage: ff * gg
925*t^2 + 605*t + 1
sage: (264 * 341) % 1331
847
```


Both ff and gg now have the correct type, but the answer is still wrong. Still investigating...


---

Comment by dmharvey created at 2009-05-29 19:01:28

Somewhere some coefficients are not being reduced properly:


```
sage: R.<x> = PolynomialRing(Integers(121))
sage: S.<y> = PolynomialRing(Integers(11))
sage: S(50*x)
6*y
sage: R(S(50*x))
50*x     # !!!!!!
```


This happens for both the flint-1.2.4.p2 and flint-1.2.5 spkgs.


---

Comment by dmharvey created at 2009-05-31 05:43:58

I have made a more specific ticket at #6168.


---

Comment by kedlaya created at 2009-06-02 01:41:11

I applied the ticket at #6168 against 4.0, and then built the spkg (on sage.math). It now passes all doctests in sage/schemes and sage/rings. Positive review.


---

Comment by mhansen created at 2009-06-03 20:23:05

Merged flint-1.2.5.spkg in 4.0.1.rc0.  Note that testing is enabled.  I'll make a ticket to disable it for the final release.


---

Comment by mhansen created at 2009-06-03 20:23:05

Resolution: fixed
