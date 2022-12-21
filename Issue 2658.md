# Issue 2658: Matrix from a vector doesn't preserve the vector's parent ring automatically

Issue created by migration from Trac.

Original creator: dfdeshom

Original creation time: 2008-03-24 03:13:50

Assignee: was

Creating a matrix from a vector doesn't preserve the vector's parent ring automatically.:


```
sage: v = vector(RR,range(5)) ; v ; v.parent()
 (0.000000000000000, 1.00000000000000, 2.00000000000000, 3.00000000000000, 4.00000000000000)
 Vector space of dimension 5 over Real Field with 53 bits of precision

sage: M=matrix(v) ; M ; M.parent()
 [0 1 2 3 4]
 Full MatrixSpace of 1 by 5 dense matrices over Integer Ring
```


This works if you specify the ring explicitly (ie  `Matrix(RR,v)` ) but I don't see why sage can't do the "right" thing automatically.


---

Comment by jason created at 2008-03-24 20:08:19

The code tries to call v._matrix_(ZZ) and if this fails, it calls v._matrix_() (which gives the answer you want).

Is there a good reason for the code to call v._matrix_(ZZ) before trying v._matrix_()?


---

Comment by jason created at 2008-03-25 21:23:33

This is resolved in the matrix() rewrite in #2651.


---

Comment by jason created at 2008-03-25 21:23:33

Resolution: duplicate


---

Comment by mabshoff created at 2008-03-25 23:39:01

Resolution changed from duplicate to 


---

Comment by mabshoff created at 2008-03-25 23:39:01

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-03-25 23:39:01

This is not a duplicate and not fixed yet. Tickets like this get only closed when the original ticket is close. Reopened.

Cheers,

Michael


---

Comment by dfdeshom created at 2008-04-14 16:35:54

I'm glad mabshoff didn't close this. The matrix rewrite (#2651) missed some stuff:

```
sage: v = vector(IntegerModRing(2),range(5));v.parent()
Vector space of dimension 5 over Ring of integers modulo 2
sage: M=matrix(v) ;  M.parent()
Full MatrixSpace of 1 by 5 dense matrices over Integer Ring
}}} 

and :

{{{
sage: v = vector(QQ,range(5));v.parent()
Vector space of dimension 5 over Rational Field
sage: M=matrix(v) ;  M.parent()
Full MatrixSpace of 1 by 5 dense matrices over Integer Ring
}}}


---

Comment by jason created at 2008-04-14 18:25:53

Are you *sure* that the rewrite missed those things?  The rewrite was applied in 3.0alpha0.  You shouldn't get those results after applying #2651.

In fact, a doctest for the new matrix() rewrite is the following:


```
sage: matrix(vector(RR,[1,2,3])).parent() 
Full MatrixSpace of 1 by 3 dense matrices over Real Field with 53 bits of precision 
```


The fact that this doctest is not failing indicates that this issue is resolved.


---

Comment by dfdeshom created at 2008-04-14 18:43:22

Mea culpa :) . I do have 3.0alpha3 installed here, but I must have confused it with my 2.11 copy. Both of these examples above work for me. I think it's safe to close this one.


---

Comment by jason created at 2008-04-14 19:07:02

Resolution: fixed


---

Comment by jason created at 2008-04-14 19:07:02

Closing this since it has been fixed and doctested by #2651.
