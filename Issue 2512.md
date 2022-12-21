# Issue 2512: implement condition number for matrices

Issue created by migration from Trac.

Original creator: schilly

Original creation time: 2008-03-13 22:33:26

Assignee: was

implement [condition number (wikipedia)](http://en.wikipedia.org/wiki/Condition_number) for matrices. 

something like:

```
def condition(m,p=2):
    return norm(m.inverse(),p) * norm(m,p)
```


depends on #1763


---

Comment by dfdeshom created at 2008-03-14 19:19:07

Condition numbers for any norm can be expensive, since they involve computing the inverse of a matrix. If our matrix is singular, this is even worse. I would propose:
 * Computing the condition number for norms 1,2,inf. This can be done reasonably efficiently in gsl and lapack
 * Computing condition estimators for other norms or when matrices get very large.

Is there any case that we would want compute a condition for norms other than 1,2 and inf? I'm curious


---

Comment by spice created at 2011-03-22 23:41:56

A one-line implementation of the condition number, which computes A.norm()*A.inverse().norm().


---

Comment by spice created at 2011-03-22 23:44:51

Changing keywords from "" to "matrix, condition number".


---

Comment by spice created at 2011-03-22 23:44:51

Changing status from new to needs_review.


---

Attachment

The patch implements a very simple .condition_number() method, based on a matrix's .norm() method. As such it only works for p = 1,2,Infinity or the Frobenius norm.

Suggestions/comments welcome. Written on sage 4.6.2.


---

Comment by schilly created at 2011-03-23 00:00:48

wow, this still exists. The doctest looks fine, is it possible to indent the options for the argument? Apart from that I strongly suggest to use numpy for that. They solve the 2-norm special case via svd and all the others might be faster. They also have a -infinity case.


```
sage: from numpy.linalg.linalg import cond     
sage: A = matrix([[1,2,4],[5,3,9],[7,8,6]])    
sage: cond(A)                              
13.139632629120618
sage: cond(A, 1)                           
22.88636363636364
sage: cond(A, 'fro')                       
14.21690371493278
sage: import numpy as np                   
sage: cond(A, np.inf)                      
19.090909090909093
sage: cond(A, -np.inf)                     
2.5454545454545454
```


complex also works


```
sage: A = matrix([[1+2j, 1+3j], [1+1j, 0.5-0.5j]])
sage: cond(A, np.inf)                             
4.2200687516284452
sage: cond(A)        
3.2255049266776936
```



---

Comment by rbeezer created at 2011-03-23 00:16:13

Hi Simon,

Could you compare timings against #10837?  (I didn't know #2512 existed.)

Rob


---

Comment by spice created at 2011-03-23 00:55:46

Turns out Rob Beezer has implemented condition numbers by directly wrapping the NumPy cond() command in patch #10837.

Some timings:

Patch 2512:


```
sage: A = matrix([[1,2,4],[5,3,9],[7,8,6]])
sage: timeit('A.condition_number(2)')
125 loops, best of 3: 1.96 ms per loop
sage: timeit('A.condition_number(Infinity)')
625 loops, best of 3: 1.31 ms per loop
sage: timeit('A.condition_number("frob")')
625 loops, best of 3: 949 µs per loop

sage: A = MatrixSpace(CC,50).random_element()
sage: timeit('A.condition_number(2)')
5 loops, best of 3: 389 ms per loop
sage: timeit('A.condition_number(1)')
5 loops, best of 3: 380 ms per loop
sage: timeit('A.condition_number("frob")')
5 loops, best of 3: 358 ms per loop
```


Patch 10837:


```
sage: A = matrix(RDF,[[1,2,4],[5,3,9],[7,8,6]])
sage: timeit('A.condition(2)')
625 loops, best of 3: 282 µs per loop
sage: timeit('A.condition(Infinity)')
625 loops, best of 3: 123 µs per loop
sage: timeit('A.condition("frob")')
625 loops, best of 3: 203 µs per loop

sage: A = MatrixSpace(CDF,50).random_element()
sage: timeit('A.condition(1)')
625 loops, best of 3: 968 µs per loop
sage: timeit('A.condition(2)')
125 loops, best of 3: 2.97 ms per loop
sage: timeit('A.condition("frob")')
625 loops, best of 3: 942 µs per loop
```


I vote we go for Rob's patch.


---

Comment by spice created at 2011-03-23 00:55:46

Resolution: duplicate


---

Comment by rbeezer created at 2011-03-23 01:17:00

> I vote we go for Rob's patch.

Yep, looks like 3 to 10 times faster.  I might steal your code for a verification doctest on #10837.

Thanks for the timing tests.
