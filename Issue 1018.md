# Issue 1018: Change prod() to used balanced tree

Issue created by migration from https://trac.sagemath.org/ticket/1018

Original creator: robertwb

Original creation time: 2007-10-28 08:09:45

Assignee: somebody

Computing a*b*c*d as (a*b)*(c*d) rather than ((a*b)*c)*d can take better advantage of asymptotically fast multiplication. On the other hand the latter can take better advantage of inplace operators and has less overhead. 


---

Comment by robertwb created at 2007-10-28 08:16:28

Changing assignee from somebody to robertwb.


---

Comment by robertwb created at 2007-10-28 08:16:28

This patch computes the product in a balanced way down to a certain level (default 5) and can be much faster. Only associativity (not commutativity) is assumed. 


```
sage: time a = prod([1..50000])
CPU times: user 0.08 s, sys: 0.01 s, total: 0.08 s
Wall time: 0.08
sage: time L = [1..50000]
CPU times: user 0.02 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.03

```


vs a generator (which is multiplied in order)


```
sage: time a = prod(1..50000)
CPU times: user 1.11 s, sys: 0.00 s, total: 1.12 s
Wall time: 1.12
sage: time L = list(1..50000)
CPU times: user 0.18 s, sys: 0.00 s, total: 0.19 s
Wall time: 0.19
```


There is also a class sage.misc.misc_c.NonAssociative to see the exact product tree. 

```
sage: from sage.misc.misc_c import NonAssociative
sage: L = [NonAssociative(label) for label in 'abcdef']
sage: prod(L)
(((a*b)*c)*((d*e)*f))
```



---

Attachment


---

Comment by cwitty created at 2007-10-28 18:08:31

Resolution: fixed
