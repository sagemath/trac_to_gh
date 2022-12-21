# Issue 2255: matrix transpose does not maintain subdivision information

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-02-22 05:43:57

Assignee: was

CC:  ncalexander@gmail.com

Keywords: matrix transpose subdivision subdivide


```
sage: tau = CC(I)*matrix(2, 2, [2, 0, 0, 2])
sage: B = block_matrix([tau, tau, tau, tau], 2, 2)
sage: B

[2.00000000000000*I                  0|2.00000000000000*I                  0]
[                 0 2.00000000000000*I|                 0 2.00000000000000*I]
[-------------------------------------+-------------------------------------]
[2.00000000000000*I                  0|2.00000000000000*I                  0]
[                 0 2.00000000000000*I|                 0 2.00000000000000*I]
sage: B.transpose()

[2.00000000000000*I                  0 2.00000000000000*I                  0]
[                 0 2.00000000000000*I                  0 2.00000000000000*I]
[2.00000000000000*I                  0 2.00000000000000*I                  0]
[                 0 2.00000000000000*I                  0 2.00000000000000*I]
```



---

Comment by ncalexan created at 2008-03-06 08:36:47

Resolution: duplicate


---

Comment by ncalexan created at 2008-03-06 08:36:47

This is essentially a duplicate of #2142.
