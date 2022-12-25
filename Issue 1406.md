# Issue 1406: bug in coercion of multivariate polynomials (possibly libsingular related)

archive/issues_001406.json:
```json
{
    "body": "Assignee: somebody\n\nReducing a polynomial to the libsingular polynomials to GF(p^n) is buggy as the following examples all illustrate. \n\n\n```\nsage: R.<x,y> = QQ[]\nsage: S.<xx,yy> = GF(5)[]\nsage: S(5*x*y + x + 17*y)\n0*xx*yy + xx + 2*yy\nsage: R.<x,y> = ZZ[]\nsage: S.<xx,yy> = GF(5)[]\nsage: R.<x,y> = ZZ[]\nsage: S.<xx,yy> = GF(25,'a')[]\nsage: S(5*x*y + x + 17*y)\n0*xx*yy + xx + 2*yy\nsage: type(S(5*x*y + x + 17*y))\n<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>\nsage: R.<x,y> = ZZ[]\nsage: S.<xx,yy> = Integers(5)[]\nsage: S(5*x*y + x + 17*y)\nxx + 2*yy\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1406\n\n",
    "created_at": "2007-12-06T04:00:21Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "bug in coercion of multivariate polynomials (possibly libsingular related)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1406",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

Reducing a polynomial to the libsingular polynomials to GF(p^n) is buggy as the following examples all illustrate. 


```
sage: R.<x,y> = QQ[]
sage: S.<xx,yy> = GF(5)[]
sage: S(5*x*y + x + 17*y)
0*xx*yy + xx + 2*yy
sage: R.<x,y> = ZZ[]
sage: S.<xx,yy> = GF(5)[]
sage: R.<x,y> = ZZ[]
sage: S.<xx,yy> = GF(25,'a')[]
sage: S(5*x*y + x + 17*y)
0*xx*yy + xx + 2*yy
sage: type(S(5*x*y + x + 17*y))
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
sage: R.<x,y> = ZZ[]
sage: S.<xx,yy> = Integers(5)[]
sage: S(5*x*y + x + 17*y)
xx + 2*yy
```


Issue created by migration from https://trac.sagemath.org/ticket/1406





---

archive/issue_comments_009046.json:
```json
{
    "body": "I have a fix for this, but it causes a segfault in the testing of multi_polynomial_ideal.py .\n\n--Mike",
    "created_at": "2007-12-06T06:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1406#issuecomment-9046",
    "user": "https://github.com/mwhansen"
}
```

I have a fix for this, but it causes a segfault in the testing of multi_polynomial_ideal.py .

--Mike



---

archive/issue_comments_009047.json:
```json
{
    "body": "Changing assignee from somebody to @mwhansen.",
    "created_at": "2007-12-06T06:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1406#issuecomment-9047",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from somebody to @mwhansen.



---

archive/issue_comments_009048.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-06T06:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1406#issuecomment-9048",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009049.json:
```json
{
    "body": "Attachment [1406.patch](tarball://root/attachments/some-uuid/ticket1406/1406.patch) by @mwhansen created at 2007-12-06 08:28:44",
    "created_at": "2007-12-06T08:28:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1406#issuecomment-9049",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1406.patch](tarball://root/attachments/some-uuid/ticket1406/1406.patch) by @mwhansen created at 2007-12-06 08:28:44



---

archive/issue_comments_009050.json:
```json
{
    "body": "Attachment [trac-1406.patch](tarball://root/attachments/some-uuid/ticket1406/trac-1406.patch) by @williamstein created at 2007-12-06 15:55:33\n\nThis is a -- I think -- better version of the 1406.patch that mhansen attached -- use it instead.",
    "created_at": "2007-12-06T15:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1406#issuecomment-9050",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1406.patch](tarball://root/attachments/some-uuid/ticket1406/trac-1406.patch) by @williamstein created at 2007-12-06 15:55:33

This is a -- I think -- better version of the 1406.patch that mhansen attached -- use it instead.



---

archive/issue_comments_009051.json:
```json
{
    "body": "Bonus -- my patch doesn't cause segfaults in multi_polynomial_ideal.py... I think.",
    "created_at": "2007-12-06T16:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1406#issuecomment-9051",
    "user": "https://github.com/williamstein"
}
```

Bonus -- my patch doesn't cause segfaults in multi_polynomial_ideal.py... I think.



---

archive/issue_comments_009052.json:
```json
{
    "body": "Actually, it turns out that that segfault was there all along (with or without the patch).  See #1409 .",
    "created_at": "2007-12-06T19:48:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1406#issuecomment-9052",
    "user": "https://github.com/mwhansen"
}
```

Actually, it turns out that that segfault was there all along (with or without the patch).  See #1409 .



---

archive/issue_comments_009053.json:
```json
{
    "body": "Ok, looks good to me, merging William's patch.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-06T20:46:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1406#issuecomment-9053",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, looks good to me, merging William's patch.

Cheers,

Michael



---

archive/issue_events_003629.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-06T20:48:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1406",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1406#event-3629"
}
```



---

archive/issue_comments_009054.json:
```json
{
    "body": "Merged in 2.9.alpha1.",
    "created_at": "2007-12-06T20:48:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1406#issuecomment-9054",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.alpha1.



---

archive/issue_comments_009055.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-06T20:48:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1406#issuecomment-9055",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
