# Issue 4610: "sage -tp X"L Move certain long doctests to the start of the list of files to test

Issue created by migration from https://trac.sagemath.org/ticket/4610

Original creator: mabshoff

Original creation time: 2008-11-25 01:06:11

Assignee: mabshoff

There are various doctests in Sage that take a while, chief among those is

```
sage -t -long devel/sage/sage/crypto/mq/sr.py
	 [630.4 s]
```

When running -tp with a high number of parallel threads those tests end up running at the end and making the user wait a while until that test finishes:

```
Total time for all tests: 1287.6 seconds
```

Moving this and a couple other files to the beginning of the list to doctest in local/bin/sage-ptest would likely result in a more even utilization of the cores. This also annoys me personally since I run -tp 8 -long after each patch merged in sage.math and it would shave probably 4 minutes off the total time of each run.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-25 01:06:25

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-11-29 02:58:32

The following doctest take more than 100 seconds on sage.math with the current 3.2.1.a2:

```
devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
devel/sage/sage/rings/qqbar.py
devel/sage/sage/schemes/elliptic_curves/sha_tate.py
devel/sage/sage/functions/piecewise.py
devel/sage/sage/graphs/graph_generators.py
devel/sage/sage/groups/perm_gps/partn_ref/refinement_binary.pyx
devel/sage/sage/groups/matrix_gps/matrix_group.py
devel/sage/sage/graphs/graph.py
devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx
devel/sage/sage/groups/perm_gps/partn_ref/refinement_graphs.pyx
devel/sage/sage/combinat/root_system/weyl_characters.py
devel/sage/sage/combinat/root_system/weyl_characters.py
devel/sage/sage/calculus/calculus.py
devel/sage/sage/crypto/mq/sr.py
```


Cheers,

Michael


---

Attachment


---

Comment by gfurnish created at 2008-12-05 04:07:39

Changing assignee from mabshoff to gfurnish.


---

Comment by gfurnish created at 2008-12-05 04:07:39

This patch autotracks timing of files so that they test in the right order.


---

Comment by gfurnish created at 2008-12-05 04:07:39

Changing status from assigned to new.


---

Comment by mabshoff created at 2008-12-05 05:51:48

Nice work, positive review. I am adding some tiny additional print statements to keep the user informed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-05 06:36:21

Merged in Sage 3.2.2.alpha0


---

Comment by mabshoff created at 2008-12-05 06:36:21

Resolution: fixed
