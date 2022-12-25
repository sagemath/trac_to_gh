# Issue 1436: FLINT 1.01 doesn't pass test suite on OSX 10.5.1

archive/issues_001436.json:
```json
{
    "body": "Assignee: mabshoff\n\nI got the following on bsd:\n\n```\nTesting _fmpz_poly_scalar_mul_si()... ok\nTesting fmpz_poly_scalar_mul_si()... ok\nTesting _fmpz_poly_scalar_mul_fmpz()... ok\nTesting fmpz_poly_scalar_mul_fmpz()... ./spkg-check: line 16: 94786\nFloating point exception./fmpz_poly-test\n\nreal    4m39.394s\nuser    4m44.254s\nsys     0m6.256s\nsage: An error occurred while installing flint-1.01\n```\n\n\nFLINT 1.0 build and tested fine.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1436\n\n",
    "created_at": "2007-12-09T16:12:45Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "FLINT 1.01 doesn't pass test suite on OSX 10.5.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1436",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

I got the following on bsd:

```
Testing _fmpz_poly_scalar_mul_si()... ok
Testing fmpz_poly_scalar_mul_si()... ok
Testing _fmpz_poly_scalar_mul_fmpz()... ok
Testing fmpz_poly_scalar_mul_fmpz()... ./spkg-check: line 16: 94786
Floating point exception./fmpz_poly-test

real    4m39.394s
user    4m44.254s
sys     0m6.256s
sage: An error occurred while installing flint-1.01
```


FLINT 1.0 build and tested fine.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1436





---

archive/issue_events_003680.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-10T04:02:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1436",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1436#event-3680"
}
```



---

archive/issue_comments_009252.json:
```json
{
    "body": "Fixed by updating to FLINT 1.02. Merged in 2.9.alpha3.",
    "created_at": "2007-12-10T04:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1436#issuecomment-9252",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed by updating to FLINT 1.02. Merged in 2.9.alpha3.



---

archive/issue_comments_009253.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-10T04:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1436#issuecomment-9253",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
