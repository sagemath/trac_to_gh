# Issue 769: Matrix_mod2_dense._echelon_strassen gives fals results sometimes

Issue created by migration from https://trac.sagemath.org/ticket/769

Original creator: malb

Original creation time: 2007-10-01 04:21:25

Assignee: was

Even though this method is probably not be used anyway, it is worth noticing that it gives False results from time to time:

```
sage: for i in range(10): 
....:   A = random_matrix(GF(2),20,20);
....:   B = A.echelon_form();
....:   A._clear_cache(); 
....:   A._echelon_strassen(cutoff=10); 
....:   A == B
False
True
True
False
True
False
True
True
True
False
```



```
sage: for i in range(10): 
....:   A = random_matrix(GF(7),20,20);
....:   B = A.echelon_form();
....:   A._clear_cache(); 
....:   A._echelon_strassen(cutoff=10); 
....:   A == B
True
True
True
False
True
True
True
True
True
True
```



---

Comment by was created at 2007-10-04 15:54:05

I tested 1000 STrassen echelons over QQ with no problems.  I tested 100 over GF(389), i.e., a fairly big
prime, and even there it fails.  It must be that either:
    (1) matrix windows are buggy mod p, or
    (2) the echelon algorithm itself is wrong mod p.

I just tested with *generic* windows, and the *algorithm* is buggy, not the implementation of windows. 

--- 

I have modified 

William


---

Comment by was created at 2007-10-04 15:54:05

Resolution: fixed


---

Comment by robertwb created at 2007-10-04 21:22:51

Resolution changed from fixed to 


---

Comment by robertwb created at 2007-10-04 21:22:51

Changing status from closed to reopened.


---

Comment by robertwb created at 2007-10-04 21:22:51

Changing priority from minor to critical.


---

Comment by robertwb created at 2007-10-04 21:22:51

I fixed the algorithm, it was forgetting to clear some pivots in some cases on full rank (where it was jumping to the end 'cause it knew it everything but the diagonal was 0's) 

I have tested this on 1000's of matrices of varying sizes and primes.


---

Comment by was created at 2007-10-05 02:16:07

Resolution: fixed


---

Attachment


---

Comment by was created at 2007-10-05 02:16:07

Changing component from algebraic geometry to linear algebra.
