# Issue 4387: [with patch, needs review] Fix memory leak in si2sa_ZZ in sage/libs/singular/singular.pyx

archive/issues_004387.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @malb\n\nWe currently leak on mpz in si2sa_ZZ:\n\n```\n==696== 104 bytes in 13 blocks are definitely lost in loss record 11,644 of 19,410\n==696==    at 0x4A1BE1B: malloc (vg_replace_malloc.c:207)\n==696==    by 0x6760947: __gmpz_init (in /scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/libgmp.so.3.4.1)\n==696==    by 0x15E05AAE: __pyx_f_4sage_4libs_8singular_8singular_10Conversion_si2sa_ZZ (singular.cpp:2513)\n==696==    by 0x15E07C85: __pyx_f_4sage_4libs_8singular_8singular_10Conversion_si2sa (singular.cpp:4803)\n==696==    by 0x1572034D: __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular_coefficients(_object*, _object*) (multi_polynomial_libsingular.cpp:25706)\n==696==    by 0x415832: PyObject_Call (abstract.c:1861)\n==696==    by 0x15735A21: __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular_gcd(_object*, _object*, _object*) (multi_polynomial_libsingular.cpp:23546)\n```\n\nThe attached patch fixes that.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4387\n\n",
    "created_at": "2008-10-30T05:10:54Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, needs review] Fix memory leak in si2sa_ZZ in sage/libs/singular/singular.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4387",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @malb

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

Issue created by migration from https://trac.sagemath.org/ticket/4387





---

archive/issue_comments_032231.json:
```json
{
    "body": "Attachment [trac_4387.patch](tarball://root/attachments/some-uuid/ticket4387/trac_4387.patch) by @craigcitro created at 2008-10-30 05:17:25\n\nNotice that the `mpz_init` happens twice -- this is definitely the right fix.",
    "created_at": "2008-10-30T05:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4387#issuecomment-32231",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_4387.patch](tarball://root/attachments/some-uuid/ticket4387/trac_4387.patch) by @craigcitro created at 2008-10-30 05:17:25

Notice that the `mpz_init` happens twice -- this is definitely the right fix.



---

archive/issue_comments_032232.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-30T05:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4387#issuecomment-32232",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha2



---

archive/issue_events_004632.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-30T05:20:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4387",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4387#event-4632"
}
```



---

archive/issue_comments_032233.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-30T05:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4387#issuecomment-32233",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032234.json:
```json
{
    "body": "CCed malb so he knows about the issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-30T05:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4387#issuecomment-32234",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

CCed malb so he knows about the issue.

Cheers,

Michael
