# Issue 6521: replace .copy() with .__copy__() in matrix/matrix0.pyx

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-07-13 10:20:55

Assignee: was

See also #111, where this originates.



---

Comment by kcrisman created at 2009-08-26 19:41:28

Based on 4.1.1


---

Attachment

This passed all doctests in sage.matrix, sage.modules, and sage.groups.matrix_gps, so hopefully I got all of them.


---

Comment by jason created at 2009-09-15 04:39:25

Is there a deprecation warning now on .copy()?  I didn't see one on this patch.


---

Comment by kcrisman created at 2009-09-15 12:14:04

Replying to [comment:2 jason]:
> Is there a deprecation warning now on .copy()?  I didn't see one on this patch.
Does there need to be?  I don't recall that in #111 there was, but maybe there is supposed to be?


---

Comment by jason created at 2009-09-15 15:11:25

Replying to [comment:3 kcrisman]:
> Replying to [comment:2 jason]:
> > Is there a deprecation warning now on .copy()?  I didn't see one on this patch.
> Does there need to be?  I don't recall that in #111 there was, but maybe there is supposed to be?  

Yes, there does need to be a deprecation warning.  #111 was *way* before we had the deprecation warning policy, so that's why it wasn't mentioned there.  Unfortunately, I think a lot of code (including my code!) has used the .copy() function since then that would break.  We need to give us poor folks a warning that things are changing.


---

Comment by kcrisman created at 2009-09-15 15:18:57

Replying to [comment:4 jason]:
> Replying to [comment:3 kcrisman]:
> > Replying to [comment:2 jason]:
> > > Is there a deprecation warning now on .copy()?  I didn't see one on this patch.
> > Does there need to be?  I don't recall that in #111 there was, but maybe there is supposed to be?  
> 
> Yes, there does need to be a deprecation warning.  #111 was *way* before we had the deprecation warning policy, so that's why it wasn't mentioned there.  Unfortunately, I think a lot of code (including my code!) has used the .copy() function since then that would break.  We need to give us poor folks a warning that things are changing.
Unfortunately, the patch for #111 was only merged a few weeks ago, and is new in 4.1.1!   That means that you should probably open a followup patch for putting deprecation warnings in for all of those.   And then opening another patch that says to remove them in 6 months...


---

Comment by jason created at 2009-09-15 15:41:51

Replying to [comment:5 kcrisman]:

> Unfortunately, the patch for #111 was only merged a few weeks ago, and is new in 4.1.1!   That means that you should probably open a followup patch for putting deprecation warnings in for all of those.   And then opening another patch that says to remove them in 6 months...

Ouch, okay.  I'll post a quick patch to this ticket (since I know at least some of my stuff will break) and open up a follow-up ticket for the rest of the stuff in #111.


---

Attachment

apply on top of previous patch


---

Comment by jason created at 2009-09-15 16:43:42

positive review for kcrisman's patch.

kcrisman, can you review my patch?  It adds the deprecation warning.


---

Comment by kcrisman created at 2009-09-15 17:13:07

Looks okay, passes relevant tests.  I hadn't seen that doctest:...: thing before, it's good to know about.


---

Comment by mvngu created at 2009-09-16 00:25:47

I got the following doctest failures. Except for the twist.py related failure, these are all a direct consequence of having deprecated the method `.copy()`.

```
sage -t -long devel/sage/sage/server/simple/twist.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/server/simple/twist.py", line 51:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))
Expected:
    {
    "status": "done",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    4
Got:
    {
    "status": "done",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    <BLANKLINE>
    4
    �e0
**********************************************************************
1 items had failures:
   1 of  24 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.2.alpha1/tmp/.doctest_twist.py
	 [8.5 s]

<SNIP>

sage -t -long devel/sage/sage/geometry/lattice_polytope.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/geometry/lattice_polytope.py", line 233:
    sage: p = LatticePolytope(m, "A lattice polytope with WRONG vertices",
                            compute_vertices=False)
Expected nothing
Got:
    doctest:259: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)
**********************************************************************
1 items had failures:
   1 of  18 in __main__.example_3
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.2.alpha1/tmp/.doctest_lattice_polytope.py
	 [11.9 s]

<SNIP>

sage -t -long devel/sage/sage/plot/plot3d/base.pyx
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/plot/plot3d/base.pyx", line 1509:
    sage: T.get_matrix()
Expected:
    [100.0   0.0   0.0   0.0]
    [  0.0 100.0   0.0   0.0]
    [  0.0   0.0 100.0   0.0]
    [  0.0   0.0   0.0   1.0]
Got:
    doctest:1172: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)
    [100.0   0.0   0.0   0.0]
    [  0.0 100.0   0.0   0.0]
    [  0.0   0.0 100.0   0.0]
    [  0.0   0.0   0.0   1.0]
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_55
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.2.alpha1/tmp/.doctest_base.py
	 [8.0 s]
	 
<SNIP>

sage -t -long devel/sage/sage/crypto/mq/sbox.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/crypto/mq/sbox.py", line 420:
    sage: S.maximal_difference_probability_absolute()
Expected:
    2
Got:
    doctest:1: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)
    2
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/crypto/mq/sbox.py", line 440:
    sage: S.maximal_difference_probability()
Expected:
    0.25
Got:
    doctest:443: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)
    0.25
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/crypto/mq/sbox.py", line 518:
    sage: S.maximal_linear_bias_absolute()
Expected:
    2
Got:
    doctest:1: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)
    2
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/crypto/mq/sbox.py", line 533:
    sage: S.maximal_linear_bias_relative()
Expected:
    0.25
Got:
    doctest:536: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)
    0.25
**********************************************************************
4 items had failures:
   1 of   4 in __main__.example_14
   1 of   4 in __main__.example_15
   1 of   4 in __main__.example_17
   1 of   4 in __main__.example_18
***Test Failed*** 4 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.2.alpha1/tmp/.doctest_sbox.py
	 [3.0 s]
```



---

Attachment

apply on top of previous patches


---

Comment by jason created at 2009-09-17 08:40:12

The -fixes.patch should take care of all of those doctest failures.


---

Comment by mvngu created at 2009-09-17 10:08:16

Resolution: fixed


---

Comment by mvngu created at 2009-09-17 10:08:16

Merged patches in this order:

 1. `trac_6521-copy-matrix.patch`
 1. `trac_6521-deprecation.patch`
 1. `trac_6521-deprecation-fixes.patch`

All doctests pass.
