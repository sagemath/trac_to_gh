# Issue 3498: make numpy the backend for matrices over CDF and RDF

Issue created by migration from https://trac.sagemath.org/ticket/3498

Original creator: jason

Original creation time: 2008-06-23 22:51:33

Assignee: was


```
[20:17] <wstein-3053> numpy is usually better.
[20:18] <jason--> okay; do you mind if we switch the determinant function to numpy for matrices over CDF?
[20:18] <wstein-3053> jason-- please do.
[20:19] <jason--> okay; ticket coming right up.
```




---

Comment by jason created at 2008-09-24 06:33:44

numpy.2.patch is an update.  RDF matrices seem to work all right, except for 4 doctest failures: a loads(dumps()) doctest and three other doctests that should be changed.  Apparently the SVD format returned is different than the GSL format, and numpy correctly recognizes a singular matrix and throws an error whereas GSL went ahead and tried to compute an inverse.


---

Attachment

The numpy-RDF-CDF.patch replaces all previous patches.

Basically, I factored out stuff that was common between RDF and CDF matrices (which turned out to be almost everything except the very initial part), stripped out GSL stuff, and wrote a few more doctests.

Oops, I just realized that I didn't delete a few pieces of cruft still hanging around from the GSL implementation.  I'll post a follow-up patch shortly.


---

Comment by jason created at 2008-09-26 01:37:47

apply on top of previous patch


---

Attachment

These patches are for 3.1.3alpha1.  With these patches, sage -t *.py and sage -t *.pyx both pass in the matrix/ directory.


---

Comment by mabshoff created at 2008-09-26 01:45:49

Hi Jason, 

any particular reason you delete the solve extension in setup.py, i.e.

```
604	606	#     matrix_padic_capped_relative_dense, 
605	 	     solve, 
606	607	
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-09-26 01:51:13

Jason,

just to make 100% sure: does this patch depend on any other patch?

Cheers,

Michael


---

Comment by jason created at 2008-09-26 01:58:36

Mabshoff: these patches do not depend on anything but a pristine 3.1.3alpha1

I deleted the solve module because it seemed like it was purely a helper module for RDF/CDF matrices.  That was the only place I could a reference to it in the sage codebase.  The functionality should be present in the RDF/CDF matrix codebase; numpy has a function which does all that that module does in just a line or two.  At least, that's how I understood it when I looked at it.


---

Comment by jason created at 2008-09-26 02:44:54

Some timings.  First, a bunch of commands in 3.1.3alpha1 without the patches, then with the patches.

The matrix below is from `m=random_matrix(RDF,30,min=-2<sup>32,max=2</sup>32)`.  I then copied the same matrix to the other session, so the timings below are for the exact same matrix.

before patches:

```
sage: timeit('Matrix(RDF, [[1,2],[3,4]])')
625 loops, best of 3: 152 µs per loop
sage: timeit('Matrix(CDF, [[1,2],[3,4]])')
625 loops, best of 3: 207 µs per loop
sage: m
30 x 30 dense matrix over Real Double Field
sage: timeit('m+m')
625 loops, best of 3: 32.1 µs per loop
sage: timeit('m*m')
625 loops, best of 3: 57.2 µs per loop
sage: timeit('~m')
625 loops, best of 3: 194 µs per loop
sage: timeit('m.det()')
625 loops, best of 3: 2.58 µs per loop
sage: timeit('m.transpose()')
625 loops, best of 3: 30.9 µs per loop
sage: timeit('m.LU()')
625 loops, best of 3: 368 µs per loop
sage: timeit('m.eigenspaces()')
5 loops, best of 3: 43.3 ms per loop
sage: timeit('m.SVD()')
625 loops, best of 3: 1.39 ms per loop
sage: timeit('m.QR()')
625 loops, best of 3: 197 µs per loop
sage: timeit('m.QR()')
625 loops, best of 3: 196 µs per loop
sage: b=vector(RDF,range(30))
sage: timeit('m.solve_left(b)')
625 loops, best of 3: 270 µs per loop
sage: timeit('m.solve_left_LU(b)')
625 loops, best of 3: 238 µs per loop
sage: 
```



after patches:

```
sage:  timeit('Matrix(RDF, [[1,2],[3,4]])')
625 loops, best of 3: 159 µs per loop
sage: timeit('Matrix(CDF, [[1,2],[3,4]])')
625 loops, best of 3: 176 µs per loop
sage: m
30 x 30 dense matrix over Real Double Field
sage: timeit('m+m')
625 loops, best of 3: 42.8 µs per loop
sage: timeit('m*m')
625 loops, best of 3: 67.2 µs per loop
sage: timeit('~m')
625 loops, best of 3: 452 µs per loop
sage: timeit('m.det()')
625 loops, best of 3: 200 µs per loop
sage: timeit('m.transpose()')
625 loops, best of 3: 34 µs per loop
sage: timeit('m.LU()')
625 loops, best of 3: 112 µs per loop
sage: timeit('m.eigenspaces()')
5 loops, best of 3: 50.4 ms per loop
sage: timeit('m.SVD()')
125 loops, best of 3: 3.52 ms per loop
sage: timeit('m.QR()')
625 loops, best of 3: 831 µs per loop
sage: b=vector(RDF,range(30))
sage: timeit('m.solve_left(b)')
625 loops, best of 3: 256 µs per loop
```



---

Comment by mabshoff created at 2008-09-26 03:18:06

Jason, 

since caching seems to affect the above numbers: can you turn off GSL caching and redo the numbers? Then open a ticket to add caching for the new numpy classes? As is there are some significant slowdowns.

Cheers,

Michael


---

Comment by jason created at 2008-09-26 03:21:40

Some more timings from respectably-sized matrices show that numpy is indeed way faster most of the time and neck-and-neck the rest of the time.  The GSL determinant speed below is most likely from from caching the LU decomposition that had been computed for something before and using that to compute the determinant.

Before patch

```
sage: # Before patches: GSL
sage: m=random_matrix(RDF,500,min=-2^32,max=2^32)
sage: timeit('m+m')
125 loops, best of 3: 7.2 ms per loop
sage: timeit('m*m')
5 loops, best of 3: 90.6 ms per loop
sage: timeit('~m')
5 loops, best of 3: 639 ms per loop
sage: timeit('m.det()')
625 loops, best of 3: 19.1 µs per loop
sage: timeit('m.transpose()')
125 loops, best of 3: 5.76 ms per loop
sage: timeit('m.LU()')
5 loops, best of 3: 97.6 ms per loop
sage: %time m.SVD()
CPU times: user 8.26 s, sys: 0.09 s, total: 8.35 s
Wall time: 9.16 s

(500 x 500 dense matrix over Real Double Field,
 500 x 500 dense matrix over Real Double Field,
 500 x 500 dense matrix over Real Double Field)
sage: %time m.QR()
CPU times: user 2.37 s, sys: 0.05 s, total: 2.42 s
Wall time: 2.68 s

(500 x 500 dense matrix over Real Double Field,
 500 x 500 dense matrix over Real Double Field)
sage: b=vector(RDF,range(500))
sage: timeit('m.solve_left(b)')
5 loops, best of 3: 72 ms per loop
sage: %time a=m.eigenspaces()
CPU times: user 26.61 s, sys: 0.42 s, total: 27.03 s
Wall time: 30.09 s
```


After patches

```
sage: # After patches: numpy
sage: m=random_matrix(RDF,500,min=-2^32,max=2^32)
sage: timeit('m+m')
125 loops, best of 3: 2.78 ms per loop
sage: timeit('m*m')
5 loops, best of 3: 89.2 ms per loop
sage: timeit('~m')
5 loops, best of 3: 224 ms per loop
sage: timeit('m.det()')
5 loops, best of 3: 62 ms per loop
sage: timeit('m.transpose()')
625 loops, best of 3: 32.9 µs per loop
sage: timeit('m.LU()')
5 loops, best of 3: 15.1 ms per loop
sage: timeit('m.SVD()')
5 loops, best of 3: 1.42 s per loop
sage: %time m.SVD()
CPU times: user 1.19 s, sys: 0.06 s, total: 1.25 s
Wall time: 1.42 s

(500 x 500 dense matrix over Real Double Field,
 500 x 500 dense matrix over Real Double Field,
 500 x 500 dense matrix over Real Double Field)
sage: %time m.QR()
CPU times: user 0.26 s, sys: 0.03 s, total: 0.28 s
Wall time: 0.32 s

(500 x 500 dense matrix over Real Double Field,
 500 x 500 dense matrix over Real Double Field)
sage: b=vector(RDF,range(500))
sage: timeit('m.solve_left(b)')
5 loops, best of 3: 68.6 ms per loop
sage: %time a=m.eigenspaces()
CPU times: user 27.52 s, sys: 0.31 s, total: 27.83 s
Wall time: 30.00 s
sage: 
```



---

Comment by malb created at 2008-09-27 19:28:49

*Review*
 * patch applies cleanly
 * I skimmed the code and it looks fine, I didn't thoroughly read it though
 * Is there any chance that we can get rid of the toplevel numpy imports (they were removed just recently and I wonder whether we can get away without them for startup time reasons)
 * doctests (64-bit Linux)

```
File "/home/malb/sage-3.1.3.alpha1/tmp/matrix_double_dense.py", line 854:
    sage: U*U.transpose()
Expected:
    [              1.0 2.13506512817e-16]
    [2.13506512817e-16               1.0]
Got:
    [              1.0 2.66876364757e-16]
    [2.66876364757e-16               1.0]
**********************************************************************
File "/home/malb/sage-3.1.3.alpha1/tmp/matrix_double_dense.py", line 859:
    sage: V*V.transpose()
Expected:
    [               1.0  2.02230810223e-16 -2.11947972194e-16]
    [ 2.02230810223e-16                1.0  7.09339271349e-17]
    [-2.11947972194e-16  7.09339271349e-17                1.0]
Got:
    [               1.0  5.94955942151e-17 -1.77117977403e-16]
    [ 5.94955942151e-17                1.0 -8.87690528723e-17]
    [-1.77117977403e-16 -8.87690528723e-17                1.0]
**********************************************************************
```



---

Comment by mabshoff created at 2008-09-27 19:38:47

Replying to [comment:10 malb]:

Hi malb,

> *Review*
>  * patch applies cleanly
>  * I skimmed the code and it looks fine, I didn't thoroughly read it though

I am valgrinding it right now. Jason and I spend four hours last night fixing problems with the new nump 1.2 and scip 0.7svn - see #4205.

>  * Is there any chance that we can get rid of the toplevel numpy imports (they were removed just recently and I wonder whether we can get away without them for startup time reasons)

Unfortunately not, but numpy 1.2 (which we are upgrading to in 3.1.3) imports in 0.2s or so on sage.math. 

>  * doctests (64-bit Linux)

Fixed in #4205. 

Cheers,

Michael


---

Comment by malb created at 2008-09-27 19:43:06

Hi, feel free to change to *positive review* when #4205 goes in.


---

Comment by mabshoff created at 2008-09-27 19:45:28

Replying to [comment:12 malb]:
> Hi, feel free to change to *positive review* when #4205 goes in.

Cool. We are still fighting some problems with scipy 0.7svn, but Mike Hansen and I are on it. Unless we can resolve those issue and if there are memory leaks in this patch I will throw the new numpy and scipy out of 3.1.3. That also makes it likely that this patch would miss 3.1.3, but so far I am hopeful.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-27 20:06:48

Ok, this is a problem:

```
==10940== LEAK SUMMARY:
==10940==    definitely lost: 13,108 bytes in 321 blocks.
==10940==      possibly lost: 303,196 bytes in 829 blocks.
==10940==    still reachable: 34,200,409 bytes in 198,999 blocks.
==10940==         suppressed: 340,122 bytes in 5,402 blocks.
==10940== Reachable blocks (those to which a pointer was found) are not shown.
==10940== To see them, rerun with: --leak-check=full --show-reachable=yes
```

This happens when valgrinding sage/modules/complex_double_vector.pyx. But the issue is not the code that Jason wrote, but that we leak not insignificant amounts of memory if we (re)import numpy. So I would suggest doing it once at the toplevel and killing all other import numpy statements. 

Another thing that concerns me is that the number of still reachable objects has gone up dramatically, i.e. contrast the above to the situation before:

```
==16395== LEAK SUMMARY:
==16395==    definitely lost: 612 bytes in 11 blocks.
==16395==      possibly lost: 312,717 bytes in 866 blocks.
==16395==    still reachable: 33,376,714 bytes in 193,940 blocks.
==16395==         suppressed: 329,948 bytes in 5,223 blocks.
==16395== Reachable blocks (those to which a pointer was found) are not shown.
==16395== To see them, rerun with: --leak-check=full --show-reachable=yes
```

One would need to run some longer tests to see if this is just additional, but constant crap from numpy or if the amount grows as we use it more.

Cheers,

Michael


---

Comment by was created at 2008-09-29 23:17:41

>> Malb: Is there any chance that we can get rid of the toplevel numpy imports (they were removed just recently and I wonder whether we can get away without them for startup time reasons)

> Mabshoff: Unfortunately not, but numpy 1.2 (which we are upgrading to in 3.1.3) imports in 0.2s or so on sage.math. 

For the record, it is absolutely definitely always possible to get rid of numpy imports.


---

Comment by malb created at 2008-09-30 08:29:04

Replying to [comment:15 was]:
> For the record, it is absolutely definitely always possible to get rid of numpy imports.

I was thinking about inheriting from a numpy type or cdef'ing some numpy type in some pxd file (don't know if that's even possible) Other than that, I can't think of any situation where one couldn't do it.


---

Comment by jason created at 2008-10-21 03:21:15

apply on top of previous patches


---

Attachment

I added numpy-3.patch (to be applied on top of the previous patches) which makes numpy *not* imported by default (imported lazily, though), and switches several functions from the numpy versions to the more careful/recommended scipy equivalents.

Earlier today, I ran valgrind on several examples and mabshoff indicated that things looked good to him.  He might do additional testing to see if things really are okay to merge.


---

Comment by jason created at 2008-10-21 03:31:47

These patches all apply on top of 3.1.4 and the doctests in matrix/*.pyx and matrix/*.py pass.


---

Comment by mabshoff created at 2008-10-21 20:26:22

The last patch repeatedly runs

```
import scipy.linalg
```

This import also needs to be done lazily.

Cheers,

Michael


---

Comment by jason created at 2008-10-22 00:18:49

After running some tests to see about leaking and the "import scipy.linalg" issue, mabshoff said on IRC that the output "looks good to me".  I don't have the logs on me, but I'm sure he can paste them in or comment if there is still an issue.


---

Comment by jason created at 2008-10-22 15:07:12

okay, copying the private review request here for posterity :)


```
Martin and Mike,

I'm emailing you two since you've both already looked at the patches at http://trac.sagemath.org/sage_trac/ticket/3498.  Martin, you almost gave it a positive review, pending resolution of the deprecation warnings.  I think mabshoff fixed the deprecation warnings without applying #4205.  Mike, you expressed some concerns over leaks.  I took care of the global numpy import issue and ran some tests with valgrind and, based on those, mabshoff said today on IRC: "Someone other than me needs to (re)review. Blessing from me on memory issues AFAIK :)"


Michael also said he was still a bit suspicious, though, and it seems like he'd like to run valgrind on it himself as well.


So, would either of you like to (re)review the patches at #3498, especially for the mathematical content?  Michael can run valgrind on it again if he wants as well.

Thanks,

Jason
```



---

Comment by robertwb created at 2008-10-24 04:32:39

Is there any reason you still have the `gsl_matrix` field in the new class? Also, have you looked into using the new buffer interface, e.g., for element access (see http://wiki.cython.org/tutorials/numpy )? Perhaps this should be a separate ticket though.


---

Comment by jason created at 2008-10-24 11:30:30

I don't believe there is any gsl_matrix field in the new class.  Where are you seeing it (after applying the patches)?

Also, yes, I have looked at using the new buffer interface.  However, for some reason, I didn't think we had current enough numpy/cython to be able to use it, and even if we did, it seemed like it was still under development.  I was going to wait until there was a clear, complete implementation.  I'm excited about it, though!

I agree it ought to be a separate ticket.


---

Attachment

apply on top of previous patches


---

Comment by jason created at 2008-10-24 11:36:09

Okay, I see two places where I still import gsl.pxi.  I've deleted those with remove-gsl-import.patch.  Apply that patch on top of all the previous patches.

Is that what you were talking about, Robert?


---

Comment by jason created at 2008-10-27 20:32:02

robertwb: Here's a ping about reviewing this ticket, if you have time.  I think I corrected the problems you pointed out.


---

Comment by robertwb created at 2008-10-28 18:08:29

Yes, this is what I was talking about.


---

Comment by jason created at 2008-10-30 02:06:51

robertwb: does that mean you give this another positive review?  I'm not trying to push for a positive review, just trying to help the review process along.


---

Comment by robertwb created at 2008-10-30 02:17:49

I haven't looked into this enough to give it a positive review, but what I have looked at looks good. I'll give it a more thorough look during bug day tomorrow.


---

Comment by jason created at 2008-10-30 03:14:06

Thanks!!  I've started working moving RDF/CDF vectors to numpy too, but that's another trac ticket.


---

Comment by jason created at 2008-11-03 21:57:35

robertwb: Did you have time to look at this patch on bug day?


---

Comment by robertwb created at 2008-11-04 07:03:21

Hmm... what's up with 


```
-sage: from scipy import linsolve   
+sage: from scipy.sparse.linalg.dsolve import linsolve
```

in sage/numerical/test.py? Does scipy.linsolve not work anymore?


---

Comment by robertwb created at 2008-11-04 07:05:43

Sorry, that was in reference to #4205. 

I did look some at this on bug day, and the code looks solid and well written. I also say positive review, pending #4205.


---

Comment by jason created at 2008-11-04 11:33:16

To my understanding, this patch does not depend on #4205.  #4205 was to resolve some issues with upgrading to numpy 1.2.  That upgrade has already happened.  mabshoff took care of the warnings in question by modifying the numpy 1.2 code to not give the warnings, so it was a temporary fix.  However, that issue is separate from this patch.

In other words, this patch depends on numpy 1.2, which has already been upgraded in Sage.  Dealing with the deprecations in numpy 1.2 is a separate issue from this ticket, and should not be considered a prerequisite for this ticket.

robertwb: given that, does this patch earn a positive review?


---

Comment by jason created at 2008-11-04 11:36:31

(of course, that's assuming that this patch actually applies and doctests run smoothly without applying #4205; I think it does, but can't check it again right now.  robertwb, did you *have* to apply #4205 before this patch would apply?)


---

Comment by robertwb created at 2008-11-04 19:50:09

No, I did not have to apply #4205. I was deferring to malb that there was some (unknown to me) reason that #4205 should be first. But it does look good to me, so I'm giving this a positive review.


---

Comment by jason created at 2008-11-04 21:16:19

Thanks.  At that time, it was unclear what to do about the deprecation warnings in numpy/scipy, so #4205 was probably a prerequisite then.  As explained above, it is no longer a prerequisite, but should still be taken care of soon (i.e., before the next update of numpy/scipy).


---

Comment by mabshoff created at 2008-11-05 18:13:31

The patch needs to be rebased - likely due to #799. 3.2.alpha2 should be out shortly, so I would suggest using that.

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha3/devel/sage$ patch -p1 < trac_3498_part_1_numpy-RDF-CDF.patch 
patching file sage/ext/numpy.pxd
patching file sage/matrix/change_ring.pyx
patching file sage/matrix/constructor.py
patching file sage/matrix/matrix_complex_double_dense.pxd
patching file sage/matrix/matrix_complex_double_dense.pyx
Hunk #3 FAILED at 83.
1 out of 3 hunks FAILED -- saving rejects to file sage/matrix/matrix_complex_double_dense.pyx.rej
patching file sage/matrix/matrix_double_dense.pxd
patching file sage/matrix/matrix_double_dense.pyx
patching file sage/matrix/matrix_real_double_dense.pxd
patching file sage/matrix/matrix_real_double_dense.pyx
Hunk #5 FAILED at 81.
1 out of 5 hunks FAILED -- saving rejects to file sage/matrix/matrix_real_double_dense.pyx.rej
patching file sage/matrix/solve.pyx
patching file setup.py
Hunk #2 succeeded at 488 (offset 2 lines).
Hunk #3 succeeded at 601 (offset 2 lines).
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-11-05 18:15:05

Oh yeah: While you are at is also please fold all four patches into one and add a proper license statemant to the file sage/ext/numpy.pxd.

Cheers,

Michael


---

Comment by jason created at 2008-11-08 06:43:07

ignore all previous files; this reverts the relevant parts of #4439 and then #778, which no longer apply to the affected files since the code has been factored out to matrix_double_dense.pyx.


---

Attachment

apply on top of revert-trac_4439_778.patch


---

Comment by jason created at 2008-11-08 06:47:42

Apply revert-trac_4439_778.patch and then numpy-RDF-CDF-final.patch to mabshoff's current (as of right now; this timestamp) 3.1.4rc0 tree.

I think all comments have been addressed (finally! :).


---

Comment by mabshoff created at 2008-11-09 18:14:02

There are some numerical noise issues to fix:

```
sage -t -long devel/sage/sage/matrix/matrix_double_dense.pyx
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc0/devel/sage/sage/matrix/matrix_double_dense.pyx", line 887:
    sage: U*U.transpose()
Expected:
    [              1.0 2.13506512817e-16]
    [2.13506512817e-16               1.0]
Got:
    [              1.0 2.66876364757e-16]
    [2.66876364757e-16               1.0]
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc0/devel/sage/sage/matrix/matrix_double_dense.pyx", line 892:
    sage: V*V.transpose()
Expected:
    [               1.0  2.02230810223e-16 -2.11947972194e-16]
    [ 2.02230810223e-16                1.0  7.09339271349e-17]
    [-2.11947972194e-16  7.09339271349e-17                1.0]
Got:
    [               1.0  5.94955942151e-17 -1.77117977403e-16]
    [ 5.94955942151e-17                1.0 -8.87690528723e-17]
    [-1.77117977403e-16 -8.87690528723e-17                1.0]
**********************************************************************
```



---

Comment by mabshoff created at 2008-11-09 18:20:27

Merged revert-trac_4439_778.patch and numpy-RDF-CDF-final.patch in Sage 3.2.rc0.

I will fix the numerical noise in a referee patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-09 18:20:27

Resolution: fixed
