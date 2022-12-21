# Issue 6553: fast slicing of sparse matrices

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-07-18 12:46:30

Assignee: was

CC:  rbeezer

Extracting a slice from a sparse matrix is insanely slow, as the code effectively treats the matrix as a dense matrix.


---

Comment by jason created at 2009-07-18 13:05:04

Before, I waited for several minutes before giving up.

AFTER:


```
sage: A=random_matrix(ZZ,100000,density=.00005,sparse=True)                  
sage: %time A[50000:,:50000]                                                 
CPU times: user 0.43 s, sys: 0.01 s, total: 0.44 s
Wall time: 0.47 s
50000 x 50000 sparse matrix over Integer Ring
```



Also:

BEFORE:


```
sage: A=random_matrix(ZZ,10000,density=.00005,sparse=True)     
sage: %time A[5000:,:5000]                                     
CPU times: user 8.32 s, sys: 0.02 s, total: 8.34 s
Wall time: 8.69 s
5000 x 5000 sparse matrix over Integer Ring
```


AFTER:


```
sage: A=random_matrix(ZZ,10000,density=.00005,sparse=True)
sage: %time A[5000:,:5000]                                
CPU times: user 0.04 s, sys: 0.00 s, total: 0.04 s
Wall time: 0.08 s
5000 x 5000 sparse matrix over Integer Ring
```



---

Comment by rbeezer created at 2009-07-20 02:18:00

Nicely done.  Three comments before giving this a positive review.

1.  The last test behaves differently for me, and the result seems "more correct" according to the density specified.  This is on 4.1.rc1 (which is the newest upgrade I could muster).


```
    sage: len(B.nonzero_positions())
Expected:
    14047
Got:
    100550
```


2.  Lists of non-integers (admittedly silly) fails silently and incorrectly.  It would appear that no entry of the new matrix gets set properly, so the result is the zero matrix of the correct size.


```
sage: A = random_matrix(ZZ, 20, 20, x=10, sparse=True)
sage: len(A.nonzero_positions())
353
sage: A.matrix_from_rows_and_columns([1.1, 2.1, 3.1, 4.1], [5.1, 6.1, 7.1, 8.1])

[0 0 0 0]
[0 0 0 0]
[0 0 0 0]
[0 0 0 0]
```


3.  I'd think the doctests would be improved if there were tests for 

(a) the condition in (2)

(b) the case of non-list input (raising the `TypeError` as implemented)


---

Comment by jason created at 2009-07-20 14:00:22

Thanks for reviewing these so quickly!

  1. Are you on a 64-bit system (maybe you are getting a different random matrix)?  That doctest quite definitely passes for me.  I agree that your answer seems more correct, though.

  2.  The error is in the sparse matrix indexing function, not in this function.  I've opened up #6569 to address this issue, with a relevant example.  I don't think that should hold back this code.

  3. The condition in (2) should be tested in #6569.  I've updated the patch to include a doctest for (b).


---

Comment by jason created at 2009-07-20 14:16:33

Also, the problem (1) above might be related to #3436.


---

Comment by rbeezer created at 2009-07-20 18:46:15

Yes, I'm testing on a 64-bit system.  What do you want to do with this doctest?  

I think that is all that needs to be addressed now, since you are right that the non-integer index and density behavior belong elsewhere.

Solve one problem and expose two more?  ;-)

Rob


---

Attachment

I've updated the patch again with both of our outputs.  It should pass your doctests now too.  Can you review it again?

Thanks!


---

Comment by rbeezer created at 2009-07-22 00:35:58

The fix on the one doctest works.  Passes tests for all of sage/matrix/*

Positive review.

PS The discrepancy here, and as illustrated in #3436, is troubling.


---

Comment by mvngu created at 2009-07-23 04:57:07

Resolution: fixed
