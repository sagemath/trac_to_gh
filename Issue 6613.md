# Issue 6613: patch from #6393 should also demonstrate that bug is fixed

Issue created by migration from https://trac.sagemath.org/ticket/6613

Original creator: mvngu

Original creation time: 2009-07-24 14:33:13

Assignee: craigcitro

CC:  revans@ucsd.edu

At this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/84bdf37a75345bb5/2a86396377e1c81d) thread, Ron Evans provided a test case to demonstrate that the function `jacobi_sum()` in Sage 4.1 provided wrong answers:

```
sage: G=DirichletGroup(5); X=G.list(); Y=X[0]; Z=X[1];  #Y is trivial and Z is quartic

sage: sum([Y(x)*Z(1-x) for x in IntegerModRing(5)])
 -1
sage: # The value -1 above is the correct value of the Jacobi sum J(Y, Z).

sage: Y.jacobi_sum(Z);    Z.jacobi_sum(Y)
0
0
sage: #The 0 values above are incorrect values of J(Y, Z).
```

The patch at #6393 fixed the reported bug, but left out the test case. The reported test case should be included to demonstrate that the bug has been fixed.


---

Comment by mvngu created at 2009-07-24 14:38:01

depends on #6393


---

Attachment


---

Comment by schilly created at 2009-07-24 16:02:22

i confirm that the doctests correctly repesents the given testcase.


---

Comment by mvngu created at 2009-07-24 22:29:59

Resolution: fixed
