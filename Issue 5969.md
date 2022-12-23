# Issue 5969: implement computation of rational cuspidal subgroups of modular abelian varieties

Issue created by migration from https://trac.sagemath.org/ticket/5969

Original creator: was

Original creation time: 2009-05-03 05:49:30

Assignee: was

CC:  boothby

This will depend on #5882.


---

Attachment


---

Attachment


---

Comment by was created at 2010-01-26 01:29:24

Hi,

Note that trac-5969-part4.patch removes the abvarsub modular symbols functions for torsion, since I found that they are buggy and not finished.  The same functionality is already available in the modular abelian varieties code anyways, so this is no real loss.


---

Comment by was created at 2010-01-26 01:29:24

Changing status from new to needs_review.


---

Attachment

I just checked that all four patches apply fine to sage-4.3.5 still with no rebasing necessary.


---

Comment by AlexGhitza created at 2010-04-03 05:26:00

The "part2" patch changes some things in `matrix/matrix_integer_dense.pyx`, and that causes two doctest failures:


```

sage -t -long "devel/sage/sage/modules/fg_pid/fgp_module.py"
**********************************************************************
File "/mnt/usb1/scratch/ghitza/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/devel/sage/sage/modules/fg_pid/fgp_module.py", line 1131:
    sage: phi = Q.hom([0,V.0,V.1]); phi
Expected:
    Morphism from module over Integer Ring with invariants (2, 0, 0) to module with invariants (0, 0, 0) that sends the generators to [(0, 0, 0), (0, 0, 1), (0, 1, 0)]
Got:
    Morphism from module over Integer Ring with invariants (2, 0, 0) to module with invariants (0, 0, 0) that sends the generators to [(0, 0, 0), (1, 0, 0), (0, 1, 0)]
**********************************************************************
File "/mnt/usb1/scratch/ghitza/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/devel/sage/sage/modules/fg_pid/fgp_module.py", line 1139:
    sage: phi(Q.1)
Expected:
    (0, 0, 1)
Got:
    (1, 0, 0)
**********************************************************************
```


It was not obvious to me whether this was harmless or an actual problem.

The rest looks good, there are a couple of docstring fixes but I have a reviewer patch that can take care of them.


---

Comment by AlexGhitza created at 2010-04-03 05:26:00

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-04-23 23:36:57

Changing status from needs_work to needs_review.


---

Attachment

It turns out that part 2 fixes a *MAJOR* bug in SNF for matrices over ZZ in an edge case.  The doctest in finitely generated modules was just wrong (ouch).    I carefully checked through this with Robert Bradshaw, and posted a patch that updates the doctest.


---

Comment by AlexGhitza created at 2010-04-24 23:16:36

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2010-04-24 23:16:36

This looks good to me, and passes tests.

Note that the part1 patch applies with some fuzz to sage-4.4.rc0, but it's fine.


---

Comment by was created at 2010-04-29 05:13:21

Resolution: fixed
