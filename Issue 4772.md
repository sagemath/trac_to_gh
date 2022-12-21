# Issue 4772: make determinants of matrices over GF(2) way faster

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-12 19:26:24

Assignee: was

This is sad:

```
was`@`sage:~/build/sage-3.2.2.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: w = random_matrix(GF(2),100)
sage: time w.determinant()
CPU times: user 0.18 s, sys: 0.00 s, total: 0.18 s
Wall time: 0.19 s
0
sage: w = random_matrix(GF(3),100)
sage: time w.determinant()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
0
```

| Sage Version 3.2.2.alpha1, Release Date: 2008-12-10                |
| Type notebook() for the GUI, and license() for information.        |
The fix - just compute the rank of the matrix, and if it is less than the nrows, then det is 0.  Otherwise det is 1.  Easy.  Right now, stupid generic code is being used. 


---

Comment by was created at 2008-12-12 19:40:46

BEFORE:

```
sage: w = random_matrix(GF(2),1000)
sage: time w.determinant()
CPU times: user 174.27 s, sys: 0.01 s, total: 174.29 s
Wall time: 174.30 s
0
```


AFTER:

```
sage: w = random_matrix(GF(2),1000)
sage: timeit('w._clear_cache(); w.determinant()')
125 loops, best of 3: 5.48 ms per loop
```


For a speedup of a factor of a factor of over THIRTY THOUSAND (!):

```
sage: 174/(5.48*10^(-3))
31751.8248175182
```



---

Attachment

Very nice speedup!  Positive review.  Doctests pass in the file.


---

Comment by mabshoff created at 2008-12-13 09:07:36

Merged in Sage 3.2.2.alpha2


---

Comment by mabshoff created at 2008-12-13 09:07:36

Resolution: fixed
