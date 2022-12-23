# Issue 788: a doctest change: random low order bits

Issue created by migration from https://trac.sagemath.org/ticket/788

Original creator: was

Original creation time: 2007-10-02 14:23:57

Assignee: failure

All doctests in sage like this

```
 sage: numerical thing   # random low order bits
 1.234283409283408238 + 19190.9393*I
```

should be changed to

```
 sage: numerical thing
 1.234283409283408... + 19190.93...*I
```

where the ... goes for the ambiguity in low order bits. 

There are 44 such cases (at least).  See them by typing

```
sage: search_src('random low')
```



---

Comment by mabshoff created at 2008-07-31 04:21:39

Changing assignee from failure to mabshoff.


---

Comment by mabshoff created at 2008-07-31 04:21:39

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-31 04:21:39

There now seem to be quite a number of those. I will post a patch here to attempt to wipe them out.

Cheers,

Michael


---

Comment by anakha created at 2008-10-24 05:13:48

Changing assignee from mabshoff to anakha.


---

Comment by anakha created at 2008-10-24 05:13:48

Changing status from assigned to new.


---

Comment by anakha created at 2008-10-24 05:13:48

This patch needs to be tested on a lot of machines with either sage -testall or


```
sage -t sage/calculus/calculus.py sage/calculus/functional.py sage/calculus/wester.py sage/graphs/graph.py sage/gsl/dft.py sage/matrix/matrix_complex_double_dense.pyx sage/matrix/matrix_real_double_dense.pyx sage/modular/modform/numerical.py sage/modules/real_double_vector.pyx sage/rings/number_field/number_field.py sage/rings/number_field/totallyreal_data.pyx sage/rings/polynomial/polynomial_element.pyx sage/rings/real_double.pyx sage/schemes/elliptic_curves/sha_tate.py
```


which tests only the modified files.

Do not mark as positive unless there is about 3 different architectures tested ({x86, ppc, sparc} x {32-bit, 64-bit})

Please report on what architecture you did the test.


---

Attachment

The patches apply, and everything works except for one doctest:

```
sage -t  devel/sage-main/sage/rings/polynomial/polynomial_element.pyx**********************************************************************
File "/opt/sage-3.2.alpha0/tmp/polynomial_element.py", line 1940:
    sage: f.factor()
Expected:
    (1.0*x - 1.00000... + 1.0000...*I) * (1.0*x - 1.00000... + 0.999989...*I) * (1.0*x - 0.9999... + 1.00000...*I) * (1.0*x + 0.99999... - 1.00000...*I) * (1.0*x + 0.999996... - 0.99998...*I) * (1.0*x + 1.00001... - 1.00000...*I)
Got:
    (1.0*x - 1.00000621124 + 1.00000779481*I) * (1.0*x - 1.00000364483 + 0.999990723518*I) * (1.0*x - 0.99999014393 + 1.00000148167*I) * (1.0*x + 0.99999217079 - 1.00000864146*I) * (1.0*x + 0.999996430878 - 0.999988898998*I) * (1.0*x + 1.00001139833 - 1.00000245954*I)
**********************************************************************
1 items had failures:
   1 of  74 in __main__.example_46
***Test Failed*** 1 failures.
For whitespace errors, see the file /opt/sage-3.2.alpha0/tmp/.doctest_polynomial_element.py
	 [6.7 s]
```

This is on Ubuntu Intrepid amd64, on a Core 2 Quad processor. The doctest fails every time, and no other test does. It looks like the `0.999989` in the second factor should be `0.0.99999`.


---

Comment by ddrake created at 2008-10-25 01:26:36

Replying to [comment:3 ddrake]:
I applied the patches on an Intel Core 2 Duo OS X machine (10.5) and got the same failure in polynomial_element:

```
File "/Applications/sage/tmp/polynomial_element.py", line 1947:
    sage: f.factor()
Expected:
    (1.0*x - 1.00000... + 1.0000...*I) * (1.0*x - 1.00000... + 0.999989...*I) * (1.0*x - 0.9999... + 1.00000...*I) * (1.0*x + 0.99999... - 1.00000...*I) * (1.0*x + 0.999996... - 0.99998...*I) * (1.0*x + 1.00001... - 1.00000...*I)
Got:
    (1.0*x - 1.00001180498 + 0.999999639235*I) * (1.0*x - 0.999994409957 + 1.00001040378*I) * (1.0*x - 0.999993785062 + 0.999989956987*I) * (1.0*x + 0.999991652054 - 1.00000998012*I) * (1.0*x + 0.999995530902 - 0.999987780431*I) * (1.0*x + 1.00001281704 - 1.00000223945*I)
**********************************************************************
```

(There were other failures as well, but (1) the new files were compiled with gcc 4.01, a known buggy compiler, and (2) the first patch didn't apply cleanly against 3.1.2, so until we hear otherwise, we should perhaps blame me and my laptop and not the doctests.)


---

Attachment


---

Comment by anakha created at 2008-10-25 06:09:56

Changing status from new to assigned.


---

Comment by anakha created at 2008-10-25 06:09:56

Patch updated (same name) to fix the failures you've seen.

About your two points, 

(1) I do all my builds with "gcc version 4.0.1 (Apple Inc. build 5484)" and I never had any problem (on PPC though)

(2) Yes that is your fault, these patches are against 3.1.4.

So if you try again with 3.1.4 as the base and still get the other failures, I would be interested.

By the way we now have tests report for x86, x84_64 and PPC 32 now.  I would still like tests on sparc or another architecture, but if the current patch does not get any failures, then I would consider it ready to go in.


---

Comment by mabshoff created at 2008-10-30 04:26:39

Patch looks good to me. I did not merge the hunk in sage/rings/polynomial/polynomial_element.pyx around line 1942. That can be taken care of down the road. 

Since we will do an alpha2 shortly any numerical noise doctest failure can be fixed before rc0, so positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-30 04:26:53

Resolution: fixed


---

Comment by mabshoff created at 2008-10-30 04:26:53

Merged in Sage 3.2.alpha2
