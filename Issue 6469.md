# Issue 6469: sage-4.1.rc0: numerical noise in graph.py

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-07-06 17:33:15

Assignee: tbd


```
sage -t  "devel/sage/sage/graphs/graph.py"
**********************************************************************
File "/home/jaap/downloads/sage-4.1.alpha2/devel/sage/sage/graphs/graph.py", line 7144:
     sage: T.spectrum()
Expected:
     [1, -0.500000000000000? + 0.866025403784439?*I, -0.500000000000000? - 0.866025403784439?*I]
Got:
     [1, -0.50000000000000000? + 0.866025403784439?*I, -0.500000000000000? - 0.866025403784439?*I]
**********************************************************************
File "/home/jaap/downloads/sage-4.1.alpha2/devel/sage/sage/graphs/graph.py", line 7272:
     sage: T.eigenvectors()
Expected:
     [(1, [
     (1, 1, 1)
     ], 1), (-0.500000000000000? - 0.866025403784439?*I, [(1, -0.500000000000000? - 0.866025403784439?*I, -0.500000000000000? + 0.866025403784439?*I)], 1),
(-0.500000000000000? + 0.866025403784439?*I, [(1, -0.500000000000000? + 0.866025403784439?*I, -0.500000000000000? - 0.866025403784439?*I)], 1)]
Got:
     [(1, [
     (1, 1, 1)
     ], 1), (-0.500000000000000? - 0.866025403784439?*I, [(1, -0.500000000000000? - 0.866025403784439?*I, -0.500000000000000? + 0.866025403784439?*I)], 1),
(-0.50000000000000000? + 0.866025403784439?*I, [(1, -0.50000000000000000? + 0.866025403784439?*I, -0.50000000000000000? - 0.866025403784439?*I)], 1)]
********************************************************************** 
```



---

Attachment

Doctests added in #6258 are failing on some systems due to slightly different degrees of accuracy.  This patch truncates each non-integer value to 10 digits in these doctests.  Documentation builds fine, and sage/graphs/graph.py passes all tests on 64-bit Ubuntu 9.04 on Intel.


---

Comment by aginiewicz created at 2009-07-07 09:05:48

with patch graph testing passes on 32 bit Arch, so probably also on other platforms where it was failing


---

Comment by rlm created at 2009-07-07 19:57:45

Resolution: fixed
