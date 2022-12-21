# Issue 564: memleak in matrix_integer_sparse_allocate_mpz_vector exposed by ModularSymbols(n,sign=1).decomposition()

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-02 00:21:14

Assignee: mabshoff

Hello folks,

```
for n in range(10,100): a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()
```

causes (among other things) the following:

```
==5107== 90,320 bytes in 11,290 blocks are definitely lost in loss record 2,811 of 2,944
==5107==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==5107==    by 0x94A2697: __gmpz_init (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)
==5107==    by 0x20A67143: __pyx_f_21matrix_integer_sparse_allocate_mpz_vector (matrix_integer_sparse.c:1202)
==5107==    by 0x20A684BF: __pyx_f_21matrix_integer_sparse_add_mpz_vector_init (matrix_integer_sparse.c:1315)
==5107==    by 0x20A6D054: __pyx_f_21matrix_integer_sparse_21Matrix_integer_sparse__add_c_impl (matrix_integer_sparse.c:6549
)
==5107==    by 0xDFE08FD: __pyx_f_7element_13ModuleElement__add_c (element.c:3986)
==5107==    by 0xDFCF2E8: __pyx_f_7element_13ModuleElement___add__ (element.c:3888)
==5107==    by 0x41596C: binary_op1 (abstract.c:398)
==5107==    by 0x416ADB: PyNumber_InPlaceAdd (abstract.c:744)
==5107==    by 0x27D10EBA: __pyx_f_4misc_matrix_rational_echelon_form_multimodular (misc.c:12816)
==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==5107==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)

```

Cheers,

Tagged for 2.8.4

Michael


---

Comment by mabshoff created at 2007-09-02 00:30:28

Changing status from new to assigned.


---

Attachment

This fixes the memleak in + or - for sparse matrix arithmetic.


---

Comment by mabshoff created at 2007-09-03 15:37:46


```
[17:17] <mabshoff> I am running the above with range(10,30) to save some time.
[17:22] <mabshoff> It works:
[17:22] <mabshoff> Without the patch:
[17:22] <mabshoff> ==8165== LEAK SUMMARY:
[17:22] <mabshoff> ==8165==    definitely lost: 144,790 bytes in 12,251 blocks.
[17:22] <mabshoff> ==8165==    indirectly lost: 22,800 bytes in 532 blocks.
[17:22] <mabshoff> ==8165==      possibly lost: 392,214 bytes in 1,010 blocks.
[17:22] <mabshoff> With the patch:
[17:22] <mabshoff> ==8132== LEAK SUMMARY:
[17:22] <mabshoff> ==8132==    definitely lost: 141,107 bytes in 11,827 blocks.
[17:22] <mabshoff> ==8132==    indirectly lost: 22,155 bytes in 531 blocks.
[17:22] <mabshoff> ==8132==      possibly lost: 392,982 bytes in 1,012 blocks.
```

This ticket should be closed.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-03 17:27:18

Resolution: fixed


---

Comment by mabshoff created at 2007-09-03 17:27:18

There is another smaller issue left in add_mpz_vector_init and once we find a proper testcase we will open another ticket for it.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-03 20:06:49

#533 seems related to this ticket.

Cheers,

Michael
