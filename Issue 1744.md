# Issue 1744: FLINT 1.05 "make check" failure on Linux/Itanium

archive/issues_001744.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe following issue has been reported by two independent parties with vastly different setups, but both using gcc 4.2.2:\n\nThe `make check` in FLINT fails with\n\n```\nTesting _fmpz_poly_mul_KS()... GNU MP: Cannot reallocate memory\n(old_size=8 new_size=4294959128)\n./spkg-check: line 51: 13014 Aborted                 ./fmpz_poly-test \n```\nThis indicates a potential bug in gmp, but so far nobody has figured out what causes it. Bill Hart is investigating.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1744\n\n",
    "created_at": "2008-01-10T06:51:38Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "FLINT 1.05 \"make check\" failure on Linux/Itanium",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1744",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

The following issue has been reported by two independent parties with vastly different setups, but both using gcc 4.2.2:

The `make check` in FLINT fails with

```
Testing _fmpz_poly_mul_KS()... GNU MP: Cannot reallocate memory
(old_size=8 new_size=4294959128)
./spkg-check: line 51: 13014 Aborted                 ./fmpz_poly-test 
```
This indicates a potential bug in gmp, but so far nobody has figured out what causes it. Bill Hart is investigating.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1744





---

archive/issue_comments_010989.json:
```json
{
    "body": "This bug appears to have been caused by the builtin functions in gcc for counting the number of bits in an unsigned long x. FLINT 1.0.6 hopefully fixes this issue by dealing with the special case of x == 0 at which point the bug occurred. The fix has been tested on one of the systems which failed.\n\nSAGE should upgrade to FLINT 1.0.6 to rectify this.\n\nBill.",
    "created_at": "2008-01-19T05:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1744#issuecomment-10989",
    "user": "https://trac.sagemath.org/admin/accounts/users/wbhart"
}
```

This bug appears to have been caused by the builtin functions in gcc for counting the number of bits in an unsigned long x. FLINT 1.0.6 hopefully fixes this issue by dealing with the special case of x == 0 at which point the bug occurred. The fix has been tested on one of the systems which failed.

SAGE should upgrade to FLINT 1.0.6 to rectify this.

Bill.



---

archive/issue_comments_010990.json:
```json
{
    "body": "The problem has been solved via #1821.",
    "created_at": "2008-01-24T09:16:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1744#issuecomment-10990",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The problem has been solved via #1821.



---

archive/issue_comments_010991.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-24T09:16:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1744#issuecomment-10991",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004222.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-24T09:16:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1744",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1744#event-4222"
}
```
