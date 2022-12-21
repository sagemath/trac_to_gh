# Issue 5541: more formatting fixes for quaternion algebra docstring

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-03-17 03:43:08

Assignee: tba

Keywords: quaternion_algebra.py, sphinx, docstring

While reviewing ticket #5531 I noticed some further formatting issues in the docstring of `quaternion_algebra.py`. The objective is to make the docstring of that module look even prettier.


---

Comment by mvngu created at 2009-03-17 04:41:43

Make quaternion_algebra.py more prettier


---

Attachment

The patch *trac_5541-docstring-fixes.patch* fixes some more docstring formatting problems in `sage/algebras/quaternion_algebra.py`. It also resolves this indentation warning:

```
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
```

which I received after applying the patch for ticket #5531 and building the reference manual.


---

Comment by mvngu created at 2009-03-17 04:57:03

I should mention that this ticket depends on #5531.


---

Comment by jhpalmieri created at 2009-03-29 16:27:05

Looks good to me except for two very minor issues, which are taken care of in the referee's patch.

(By the way, see #5632 for a somewhat related ticket.)


---

Attachment


---

Comment by mvngu created at 2009-03-30 06:34:22

Replying to [comment:3 jhpalmieri]:
> Looks good to me except for two very minor issues, which are taken care of in the referee's patch.


Yep, looks good to me. Thanks for pointing that out.


---

Comment by mabshoff created at 2009-03-31 07:41:03

This patch needs to be rebased due to #5520:

```
sage-3.4.1.rc0/devel/sage$ patch -p1 --dry-run < trac_5541-docstring-fixes.patch 
patching file sage/algebras/quatalg/quaternion_algebra.py
Hunk #1 FAILED at 58.
Hunk #2 succeeded at 101 (offset 6 lines).
Hunk #3 FAILED at 125.
Hunk #4 succeeded at 152 (offset 6 lines).
Hunk #5 succeeded at 183 (offset 6 lines).
Hunk #6 succeeded at 195 (offset 6 lines).
Hunk #7 FAILED at 203.
Hunk #8 succeeded at 228 (offset 6 lines).
Hunk #9 succeeded at 242 (offset 6 lines).
Hunk #10 succeeded at 255 (offset 6 lines).
Hunk #11 succeeded at 268 (offset 6 lines).
Hunk #12 succeeded at 296 (offset 6 lines).
Hunk #13 succeeded at 305 (offset 6 lines).
Hunk #14 succeeded at 326 (offset 6 lines).
Hunk #15 succeeded at 348 (offset 6 lines).
Hunk #16 succeeded at 366 (offset 6 lines).
Hunk #17 succeeded at 379 (offset 6 lines).
Hunk #18 succeeded at 397 (offset 6 lines).
Hunk #19 succeeded at 424 (offset 6 lines).
Hunk #20 succeeded at 436 (offset 6 lines).
Hunk #21 succeeded at 454 (offset 6 lines).
Hunk #22 succeeded at 463 (offset 6 lines).
Hunk #23 succeeded at 476 (offset 6 lines).
Hunk #24 succeeded at 486 (offset 5 lines).
Hunk #25 succeeded at 518 (offset 5 lines).
Hunk #26 succeeded at 569 (offset 25 lines).
Hunk #27 succeeded at 606 (offset 43 lines).
Hunk #28 succeeded at 623 (offset 43 lines).
Hunk #29 succeeded at 640 with fuzz 1 (offset 43 lines).
Hunk #30 succeeded at 657 (offset 43 lines).
Hunk #31 succeeded at 683 (offset 43 lines).
Hunk #32 succeeded at 694 (offset 43 lines).
Hunk #33 FAILED at 742.
4 out of 33 hunks FAILED -- saving rejects to file sage/algebras/quatalg/quaternion_algebra.py.rej
```

Note that the file has moved from sage/algebras to sage/algebras/quatalg

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-03-31 15:40:17

Please see [my most recent comment on #5632](http://trac.sagemath.org/sage_trac/ticket/5632#comment:6) for a reference manual issue which is also relevant here.


---

Comment by jhpalmieri created at 2009-04-01 02:54:52

Here's a rebased version, plus more.  This includes all of mvngu's work, so he should obviously get a lot of credit for this; this covers the file up to line 700 or so. #5520 added a lot of code to this file with many of the same issues, so starting at line 741, there are new fixes.


---

Attachment

(this replaces both of the earlier patches)


---

Comment by jhpalmieri created at 2009-04-05 22:48:56

mvngu: the first half of my patch is just a rebased version of yours, and it already has a positive review.  If you are willing to review the second half, then that should do it for this ticket.


---

Comment by mvngu created at 2009-04-05 23:38:53

Replying to [comment:8 jhpalmieri]:
> mvngu: the first half of my patch is just a rebased version of yours, and it already has a positive review.  If you are willing to review the second half, then that should do it for this ticket.


jhpalmieri: I've read through the rebased patch. But I also want to (re)build at least the HTML version of the reference to make sure that the rebased patch fixes the problems it claims to fix. I'll give this patch a formal review sometime today.


---

Comment by mvngu created at 2009-04-17 02:18:59

REFEREE REPORT:



The following lines result in something weird when viewing the HTML version of the reference manual:

```
486	class QuaternionAlgebra_ab(QuaternionAlgebra_abstract): 
487	    """ 
488	    The quaternion algebra of the form `(a, b/K)`, where `i^2=a`, `j^2 = b`, 
489	    and `j*i = -i*j`.  ``K`` is a field not of characteristic 2 and ``a``, 
490	    ``b`` are nonzero elements of ``K``. 
491	 
492	    EXAMPLES:: 
493	 
494	    """ 
495	    def __init__(self, base_ring, a, b, names='i,j,k'):
```

See the [HTML version](http://sage.math.washington.edu/home/mvngu/reference/sage/algebras/quatalg/quaternion_algebra.html#sage.algebras.quatalg.quaternion_algebra.QuaternionAlgebra_ab) I've generated after applying the rebased patch. I think the problem is that there's a "EXAMPLES::" tag, which is not followed by any examples at all. Now by alphabetic order, the method `sage.algebras.quatalg.quaternion_algebra.QuaternionAlgebra_ab.QuaternionAlgebra_ab.discriminant()` is thus formatted in a weird way as

```
.. method:: QuaternionAlgebra_ab.discriminant()
```

in the HTML version.



How about some documentation for 

```
627	    def gen(self, i=0):
```

to explain what it does. At the moment, there are examples, but no explanation of what this method is supposed to do.



I think the maths expression in the following lines are typeset in a weird way:

```
1069	    def discriminant(self): 
1070	        r""" 
1071	        Return the discriminant of this order, which we define as 
1046	 	        $\sqrt( det ( Tr(e_i \bar(e_j) ) ) )$, where $\{e_i\}$ is the 
1072	        `\sqrt( det ( Tr(e_i \bar(e_j) ) ) )`, where `\{e_i\}` is the 
1073
```

See the [HTML version](http://sage.math.washington.edu/home/mvngu/reference/sage/algebras/quatalg/quaternion_algebra.html#sage.algebras.quatalg.quaternion_algebra.QuaternionOrder.discriminant) of the reference manual for a visual.



The maths expression in these lines

```
1481	        The normalized theta series is by definition 
1442	1482	 
1443	1483	        .. math: 
1444	1484	 
1445	 	        \theta_I(q)=\sum_{x \in I} q^{\frac{N(x)}{N(I)}} 
1446	 	         
 	1485	            \theta_I(q)=\sum_{x \in I} q^{\frac{N(x)}{N(I)}}
```

doesn't show up in the [HTML version](http://sage.math.washington.edu/home/mvngu/reference/sage/algebras/quatalg/quaternion_algebra.html#sage.algebras.quatalg.quaternion_algebra.QuaternionFractionalIdeal_rational.theta_series).


---

Attachment

apply on top of 5541-rebased.patch


---

Comment by jhpalmieri created at 2009-04-17 03:25:00

Oh, and mabshoff: this should fix the warnings for this file when building the reference manual.


---

Comment by mvngu created at 2009-04-17 05:53:20

REFEREE REPORT



I applied patches against sage-3.4.1.rc3 in this order:

 1. First, `5541-rebased.patch`
 1. Followed by `5541-second.patch`

All doctests passed with options `-t -long`. I rebuilt the HTML version of the reference manual and noticed that `5541-second.patch` has addressed all of my concerns above. Positive review.


---

Comment by mabshoff created at 2009-04-17 06:14:24

Ok, this should go into 3.4.1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-18 01:07:43

Resolution: fixed


---

Comment by mabshoff created at 2009-04-18 01:07:43

Merged  5541-rebased.patch and 5541-second.patch in Sage 3.4.1.rc4.

Cheers,

Michael
