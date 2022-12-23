# Issue 2609: [with patch, needs review] generators for congruence subgroups

Issue created by migration from https://trac.sagemath.org/ticket/2609

Original creator: rlm

Original creation time: 2008-03-20 08:56:45

Assignee: was

Generators for Gamma0, Gamma1 and GammaH.


---

Comment by cremona created at 2008-03-22 18:15:29

This looks fine mathematically.  I don't much like seeing three almost identical functions, though (for Gamma0, Gamma1 and GammaH).  Can it not be written in such a way that all three call a common core function which has the list of coset reps as a parameter?

Even better would be a function to do this more generally, given generators for a big group and coset reps for a subgroup -- but I do realise that one would also need toprovide functions to return the coset rep for any give element of the big group.


---

Comment by was created at 2008-03-22 18:17:57

Yes, I agree, those three functions *definitely* need to be refactored into a single function.


---

Comment by was created at 2008-03-22 19:55:32

Since you're doing just arithmetic, it just occurred to me that in the interest of speed one could use the specialized 2x2 integer matrix class that Robert Bradshaw wrote, which is ten times faster.  For example: 


```
sage: import sage.matrix.matrix_integer_2x2
sage: A = sage.matrix.matrix_integer_2x2.Matrix_integer_2x2(MatrixSpace(ZZ,2),[1,2,3,4],False,False)
sage: time for _ in xrange(10^5): B = A*A
CPU times: user 0.23 s, sys: 0.00 s, total: 0.23 s
Wall time: 0.24
sage: A = matrix(ZZ,2,[1,2,3,4])sage: time for _ in xrange(10^5): B = A*A
CPU times: user 1.81 s, sys: 0.21 s, total: 2.02 s
Wall time: 2.04
```



---

Comment by cremona created at 2008-03-22 20:41:23

The replacement patch certainly answers my point made earlier.  So I would have said: OK, merge this in -- until I saw was's comment.  rlm, how about trying that out and seeing if is is as much faster as hoped?


---

Comment by rlm created at 2008-03-23 00:00:13

was:

```
sage: time L = Gamma0(389).generators()
CPU times: user 0.50 s, sys: 0.04 s, total: 0.54 s
Wall time: 0.54
```

is:

```
sage: time L = Gamma0(389).generators()
CPU times: user 0.04 s, sys: 0.00 s, total: 0.04 s
Wall time: 0.05
```



---

Comment by cremona created at 2008-03-23 10:25:43

Fantastic!  

This patch provides very useful functionality, and in a very efficient way.  It should definitely be included.


---

Attachment

Merged in Sage 2.11.alpha2


---

Comment by mabshoff created at 2008-03-23 20:35:53

Resolution: fixed
