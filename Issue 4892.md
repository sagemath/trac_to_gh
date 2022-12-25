# Issue 4892: Changing precision of a Complex can convert it to a real

archive/issues_004892.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: real complex precision\n\ngeorg.grafendorfer reported this to sage-support:\n\n```\nsage: a = CC(-5).n(prec=100)\nsage: b = ComplexField(100)(-5)\nsage: a == b\nTrue\nsage: type(a) == type(b)\nFalse\nsage: ln(a)\nNaN\nsage: ln(b)\n1.6094379124341003746007593332 + 3.1415926535897932384626433833*I\n```\n\nThe issue is that both a and b are equal to -5 (exactly, to 100 bit precision) but a is a Real while b is a Complex.  This happens because \n\n```\nLooking at the code for numerical_approx() in sage.misc.functional,\nthis happens because the attempt to coerce z into RealField(100)\nsucceeds.  To fix this (if it is agreed that it is a bug) that\nfunction would need to test the type of the input and return something\nof the same type (real/complex).\n```\n\nThe suggested fix is that the numerical_approx function should always return a complex number to the appropriate precsion if the input has type complex, even if the coercion into a real succeeded.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4892\n\n",
    "created_at": "2008-12-30T09:40:16Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Changing precision of a Complex can convert it to a real",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4892",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: somebody

Keywords: real complex precision

georg.grafendorfer reported this to sage-support:

```
sage: a = CC(-5).n(prec=100)
sage: b = ComplexField(100)(-5)
sage: a == b
True
sage: type(a) == type(b)
False
sage: ln(a)
NaN
sage: ln(b)
1.6094379124341003746007593332 + 3.1415926535897932384626433833*I
```

The issue is that both a and b are equal to -5 (exactly, to 100 bit precision) but a is a Real while b is a Complex.  This happens because 

```
Looking at the code for numerical_approx() in sage.misc.functional,
this happens because the attempt to coerce z into RealField(100)
succeeds.  To fix this (if it is agreed that it is a bug) that
function would need to test the type of the input and return something
of the same type (real/complex).
```

The suggested fix is that the numerical_approx function should always return a complex number to the appropriate precsion if the input has type complex, even if the coercion into a real succeeded.

Issue created by migration from https://trac.sagemath.org/ticket/4892





---

archive/issue_comments_037023.json:
```json
{
    "body": "Attachment [trac_4892-complex_approx.patch](tarball://root/attachments/some-uuid/ticket4892/trac_4892-complex_approx.patch) by @rlmill created at 2009-01-22 06:50:33",
    "created_at": "2009-01-22T06:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4892#issuecomment-37023",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_4892-complex_approx.patch](tarball://root/attachments/some-uuid/ticket4892/trac_4892-complex_approx.patch) by @rlmill created at 2009-01-22 06:50:33



---

archive/issue_comments_037024.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-22T06:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4892#issuecomment-37024",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to assigned.



---

archive/issue_comments_037025.json:
```json
{
    "body": "Changing assignee from somebody to @rlmill.",
    "created_at": "2009-01-22T06:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4892#issuecomment-37025",
    "user": "https://github.com/rlmill"
}
```

Changing assignee from somebody to @rlmill.



---

archive/issue_comments_037026.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-01-23T20:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4892#issuecomment-37026",
    "user": "https://github.com/aghitza"
}
```

Looks good to me.



---

archive/issue_comments_037027.json:
```json
{
    "body": "This patch causes the following doctest failure:\n\n```\nmabshoff@geom:/scratch/mabshoff/sage-3.3.alpha2$ ./sage -t -long devel/sage/sage/modules/vector_double_dense.pyx\nsage -t -long \"devel/sage/sage/modules/vector_double_dense.pyx\"\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/modules/vector_double_dense.pyx\", line 531:\n    sage: _.parent()\nExpected:\n    Vector space of dimension 3 over Real Field with 53 bits of precision\nGot:\n    Vector space of dimension 3 over Complex Field with 53 bits of precision\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/modules/vector_double_dense.pyx\", line 535:\n    sage: _.parent()\nExpected:\n    Vector space of dimension 3 over Real Field with 75 bits of precision\nGot:\n    Vector space of dimension 3 over Complex Field with 75 bits of precision\n**********************************************************************\n```\n\n\nGiven that this is vector_double_dense.pyx it seems odd.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-25T02:13:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4892#issuecomment-37027",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch causes the following doctest failure:

```
mabshoff@geom:/scratch/mabshoff/sage-3.3.alpha2$ ./sage -t -long devel/sage/sage/modules/vector_double_dense.pyx
sage -t -long "devel/sage/sage/modules/vector_double_dense.pyx"
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/modules/vector_double_dense.pyx", line 531:
    sage: _.parent()
Expected:
    Vector space of dimension 3 over Real Field with 53 bits of precision
Got:
    Vector space of dimension 3 over Complex Field with 53 bits of precision
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/modules/vector_double_dense.pyx", line 535:
    sage: _.parent()
Expected:
    Vector space of dimension 3 over Real Field with 75 bits of precision
Got:
    Vector space of dimension 3 over Complex Field with 75 bits of precision
**********************************************************************
```


Given that this is vector_double_dense.pyx it seems odd.

Cheers,

Michael



---

archive/issue_comments_037028.json:
```json
{
    "body": "Oops I should have tested modules/ during the review of rlm's patch.\n\nBut the doctests were indeed wrong to start with, the vector spaces *should* be complex.  I've added a trivial patch that fixes this.",
    "created_at": "2009-01-25T02:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4892#issuecomment-37028",
    "user": "https://github.com/aghitza"
}
```

Oops I should have tested modules/ during the review of rlm's patch.

But the doctests were indeed wrong to start with, the vector spaces *should* be complex.  I've added a trivial patch that fixes this.



---

archive/issue_comments_037029.json:
```json
{
    "body": "Attachment [trac_4892_1.patch](tarball://root/attachments/some-uuid/ticket4892/trac_4892_1.patch) by @aghitza created at 2009-01-25 02:31:04\n\napply after the other patch",
    "created_at": "2009-01-25T02:31:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4892#issuecomment-37029",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_4892_1.patch](tarball://root/attachments/some-uuid/ticket4892/trac_4892_1.patch) by @aghitza created at 2009-01-25 02:31:04

apply after the other patch



---

archive/issue_comments_037030.json:
```json
{
    "body": "+1 to the second patch",
    "created_at": "2009-01-25T21:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4892#issuecomment-37030",
    "user": "https://github.com/rlmill"
}
```

+1 to the second patch



---

archive/issue_comments_037031.json:
```json
{
    "body": "Merged both patches in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T15:23:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4892#issuecomment-37031",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_events_011285.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-28T15:23:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4892",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4892#event-11285"
}
```



---

archive/issue_events_011286.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-28T15:23:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4892",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4892#event-11286"
}
```



---

archive/issue_comments_037032.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T15:23:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4892#issuecomment-37032",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
