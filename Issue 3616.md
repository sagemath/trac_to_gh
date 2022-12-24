# Issue 3616: flint hangs on itanium

archive/issues_003616.json:
```json
{
    "body": "Assignee: somebody\n\nUsing sage-3.0.4.rc0 on ia64 SUSE we have:\n\n```\n            sage: P.<x> = PolynomialRing(ZZ)\n            sage: F = (x^2 + 2)*x^3; G = (x^2+2)*(x-3)\n            sage: g, u, v = F.xgcd(G)\nHANG\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3616\n\n",
    "created_at": "2008-07-08T19:13:57Z",
    "labels": [
        "basic arithmetic",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "flint hangs on itanium",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3616",
    "user": "was"
}
```
Assignee: somebody

Using sage-3.0.4.rc0 on ia64 SUSE we have:

```
            sage: P.<x> = PolynomialRing(ZZ)
            sage: F = (x^2 + 2)*x^3; G = (x^2+2)*(x-3)
            sage: g, u, v = F.xgcd(G)
HANG
```


Issue created by migration from https://trac.sagemath.org/ticket/3616





---

archive/issue_comments_025521.json:
```json
{
    "body": "Recompiling with -O0 does *not* fix the problem.  The flint test suite *fails* on\nitanium even with -O0:\n\n\n```\nTesting fmpz_CRT_ui()... FAIL!\nTesting fmpz_sqrtrem()... ok\n\nAt least one test FAILED!\n```\n\n\nThat's the first failure.\n\nThis is flint-1.010.\n\nwilliam",
    "created_at": "2008-07-08T19:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3616#issuecomment-25521",
    "user": "was"
}
```

Recompiling with -O0 does *not* fix the problem.  The flint test suite *fails* on
itanium even with -O0:


```
Testing fmpz_CRT_ui()... FAIL!
Testing fmpz_sqrtrem()... ok

At least one test FAILED!
```


That's the first failure.

This is flint-1.010.

william



---

archive/issue_comments_025522.json:
```json
{
    "body": "More test failures on iras (itanium box):\n\n\n```\nTesting fmpz_poly_CRT_unsigned()... FAIL!\nTesting fmpz_poly_CRT()... FAIL!\n```\n",
    "created_at": "2008-07-08T19:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3616#issuecomment-25522",
    "user": "was"
}
```

More test failures on iras (itanium box):


```
Testing fmpz_poly_CRT_unsigned()... FAIL!
Testing fmpz_poly_CRT()... FAIL!
```




---

archive/issue_comments_025523.json:
```json
{
    "body": "Due to the hard work by Bill Hard we now have a 1.0.11 spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/flint-1.011.spkg\n\nI turned on spkg-check per default. Builds and tests fine on x86-64 and Itanium.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-09T16:04:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3616#issuecomment-25523",
    "user": "mabshoff"
}
```

Due to the hard work by Bill Hard we now have a 1.0.11 spkg at

http://sage.math.washington.edu/home/mabshoff/flint-1.011.spkg

I turned on spkg-check per default. Builds and tests fine on x86-64 and Itanium.

Cheers,

Michael



---

archive/issue_comments_025524.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-09T16:22:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3616#issuecomment-25524",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_025525.json:
```json
{
    "body": "Merged in Sage 3.0.4.rc2",
    "created_at": "2008-07-09T16:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3616#issuecomment-25525",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.rc2
