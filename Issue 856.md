# Issue 856: strange behaviour when converting a numpy matrix to a sage one

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2007-10-12 02:43:28

Assignee: mhansen


```
sage: import numpy
sage: numpy.array([[1,2,3],[4,5,6],[7,8,9]],'f')

array([[ 1.,  2.,  3.],
      [ 4.,  5.,  6.],
      [ 7.,  8.,  9.]], dtype=float32)
sage: a=numpy.array([[1,2,3],[4,5,6],[7,8,9]],'f')
sage: matrix(a)

[     2.00000047311      512.000122547       8192.0019722]
[     131072.031677 9.87267348858e-312 1.48958728182e-263]
[6.36598737141e-314  6.6976282025e-316 3.40280828847e-313]
sage:

```


------------------------------------
Are you running a 64-bit machine?

I looked at the code, and the problem seems to come from the fact that
it is doing a naive check on the type of the numpy array; it is
currently assuming that your float32 array is a float64 array which is
why you are getting the strange results you are.  See below:


```
sage: a = numpy.array([[1,2,3],[4,5,6],[7,8,9]],float)
sage: a.dtype
dtype('float64')
sage: matrix(a)

[1.0 2.0 3.0]
[4.0 5.0 6.0]
[7.0 8.0 9.0]
sage: a = numpy.array([[1,2,3],[4,5,6],[7,8,9]],'float64')
sage: a.dtype
dtype('float64')
sage: matrix(a)

[1.0 2.0 3.0]
[4.0 5.0 6.0]
[7.0 8.0 9.0]
sage: a = numpy.array([[1,2,3],[4,5,6],[7,8,9]],'float32')
sage: a.dtype
dtype('float32')
sage: matrix(a)

[     2.00000047311      512.000122547       8192.0019722]
[     131072.031677 2.34082748762e-310                0.0]
[3.16202013338e-322 4.74797085653e-321 4.94065645841e-324]

```



---

Attachment

patch needs testing on 32-bit machines


---

Comment by mhansen created at 2007-10-12 04:48:07

Changing status from new to assigned.


---

Comment by was created at 2007-10-13 07:31:45

Resolution: fixed
