# Issue 565: memleak in matrix_rational_sparse_allocate_mpq_vector exposed by ModularSymbols(n,sign=1).decomposition()

Issue created by migration from https://trac.sagemath.org/ticket/565

Original creator: mabshoff

Original creation time: 2007-09-02 00:22:06

Assignee: mabshoff

Hello folks,

```
for n in range(10,100): a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()
```

causes (among other things) the following:

```
==5107== 4,536,112 bytes in 567,014 blocks are definitely lost in loss record 2,943 of 2,944
==5107==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==5107==    by 0x94AD2C1: __gmpq_init (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)
==5107==    by 0x210C44C3: __pyx_f_22matrix_rational_sparse_allocate_mpq_vector (matrix_rational_sparse.c:5358)
==5107==    by 0x210C6041: __pyx_f_22matrix_rational_sparse_mpq_vector_set_entry (matrix_rational_sparse.c:6542)
==5107==    by 0x210C6367: __pyx_f_22matrix_rational_sparse_22Matrix_rational_sparse_set_unsafe (matrix_rational_sparse.c:84
63)
==5107==    by 0x1E21D176: __pyx_mp_ass_subscript_7matrix0_Matrix (matrix0.c:2277)
==5107==    by 0x480E96: PyEval_EvalFrameEx (ceval.c:1497)
==5107==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)
==5107==    by 0x4845B3: PyEval_EvalFrameEx (ceval.c:3660)
==5107==    by 0x485025: PyEval_EvalFrameEx (ceval.c:3650)
==5107==    by 0x485025: PyEval_EvalFrameEx (ceval.c:3650)
==5107==    by 0x485025: PyEval_EvalFrameEx (ceval.c:3650)
```

Cheers,

Tagged for 2.8.4

Michael


---

Comment by mabshoff created at 2007-09-02 00:30:36

Changing status from new to assigned.


---

Attachment

this patch fixes a memleak when setting an entry to 0 in a sparse vector


---

Comment by was created at 2007-09-03 15:47:54

This is a pretty shocking before and after example!

BEFORE

```
age: get_memory_usage()
372.22265625
sage: m = random_matrix(ZZ, 300, sparse=True)
sage: get_memory_usage()
376.92578125
sage: for i in range(300):
....:     for j in range(300):
....:         m[i,j] = 0
....:

sage: get_memory_usage()
786.4765625
```



A 300 MB memleak!!!

AFTER:


```
sage: get_memory_usage()
372.23046875
sage: m = random_matrix(ZZ, 300, sparse=True)
sage: get_memory_usage()
376.921875
sage: for i in range(300):
....:     for j in range(300):
....:         m[i,j] = 0
....:
sage: get_memory_usage()
376.921875
```



---

Comment by mabshoff created at 2007-09-03 17:28:53

Resolution: fixed


---

Comment by mabshoff created at 2007-09-03 17:28:53

William has fixed the huge memleak mentioned above. The patch has also been pushed out to the public repo.

There is another smaller issue left in add_mpz_vector_init and once we find a proper testcase we will open another ticket for it.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-03 20:07:04

#533 seems related to this ticket.

Cheers,

Michael
