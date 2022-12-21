# Issue 4387: [with patch, needs review] Fix memory leak in si2sa_ZZ in sage/libs/singular/singular.pyx

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-10-30 05:10:54

Assignee: mabshoff

CC:  malb

We currently leak on mpz in si2sa_ZZ:

```
==696== 104 bytes in 13 blocks are definitely lost in loss record 11,644 of 19,410
==696==    at 0x4A1BE1B: malloc (vg_replace_malloc.c:207)
==696==    by 0x6760947: __gmpz_init (in /scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/libgmp.so.3.4.1)
==696==    by 0x15E05AAE: __pyx_f_4sage_4libs_8singular_8singular_10Conversion_si2sa_ZZ (singular.cpp:2513)
==696==    by 0x15E07C85: __pyx_f_4sage_4libs_8singular_8singular_10Conversion_si2sa (singular.cpp:4803)
==696==    by 0x1572034D: __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular_coefficients(_object*, _object*) (multi_polynomial_libsingular.cpp:25706)
==696==    by 0x415832: PyObject_Call (abstract.c:1861)
==696==    by 0x15735A21: __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular_gcd(_object*, _object*, _object*) (multi_polynomial_libsingular.cpp:23546)
```

The attached patch fixes that.

Cheers,

Michael


---

Attachment

Notice that the `mpz_init` happens twice -- this is definitely the right fix.


---

Comment by mabshoff created at 2008-10-30 05:20:27

Merged in Sage 3.2.alpha2


---

Comment by mabshoff created at 2008-10-30 05:20:27

Resolution: fixed


---

Comment by mabshoff created at 2008-10-30 05:20:59

CCed malb so he knows about the issue.

Cheers,

Michael
