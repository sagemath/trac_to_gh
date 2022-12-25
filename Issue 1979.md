# Issue 1979: doctest fall out from #740 in tut.tex

archive/issues_001979.json:
```json
{
    "body": "Assignee: failure\n\nThe following happens while doctesting `tut.tex`:\n\n```\nsage -t  tut.tex\n**********************************************************************\nFile \"tut.py\", line 1676:\n    : EllipticCurve(5)\nExpected:\n    Elliptic Curve defined by y^2 + x*y  = x^3 + 36/1723*x + 1/1723\n                over Rational Field\nGot:\n    Elliptic Curve defined by y^2  = x^3 + 25845*x - 29687290 over Rational Field\n**********************************************************************\nFile \"tut.py\", line 1722:\n    : factor(F.conductor())\nExpected:\n    2^6 * 37\nGot:\n    2^6 * 3^2 * 37^2\n**********************************************************************\nFile \"tut.py\", line 1730:\n    : G = F.quadratic_twist(2); G\nExpected:\n    Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field\nGot:\n    Elliptic Curve defined by y^2 + y = x^3 - 12321*x - 341908 over Rational Field\n**********************************************************************\nFile \"tut.py\", line 1732:\n    : G.conductor()\nExpected:\n    37\nGot:\n    12321\n**********************************************************************\n```\nWilliam says:\n\n```\n[04:56] <mabshoff> william_stein: #740 seems to create different results in various places, i.e. doc test failures.\n[04:56] <william_stein> hmmm\n[04:57] <mabshoff> File \"tut.py\", line 1676:\n[04:57] <mabshoff>     : EllipticCurve(5)\n[04:57] <mabshoff> Expected:\n[04:57] <mabshoff>     Elliptic Curve defined by y^2 + x*y  = x^3 + 36/1723*x + 1/1723\n[04:57] <mabshoff>                 over Rational Field\n[04:57] <mabshoff> Got:\n[04:57] <mabshoff>     Elliptic Curve defined by y^2  = x^3 + 25845*x - 29687290 over Rational Field\n[04:57] <william_stein> mabshoff -- not surprising.\n[04:57] <william_stein> NOBODY has doctested testall after applying that.\n[04:57] <mabshoff> ok\n[04:57] <william_stein> The new output in tut.py is right, by the way.\n[04:57] <mabshoff> :)\n[04:57] <william_stein> It's a different curve with that j-invariant -- a better one.\n```\nPatch coming up.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1979\n\n",
    "created_at": "2008-01-30T05:10:33Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "doctest fall out from #740 in tut.tex",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1979",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: failure

The following happens while doctesting `tut.tex`:

```
sage -t  tut.tex
**********************************************************************
File "tut.py", line 1676:
    : EllipticCurve(5)
Expected:
    Elliptic Curve defined by y^2 + x*y  = x^3 + 36/1723*x + 1/1723
                over Rational Field
Got:
    Elliptic Curve defined by y^2  = x^3 + 25845*x - 29687290 over Rational Field
**********************************************************************
File "tut.py", line 1722:
    : factor(F.conductor())
Expected:
    2^6 * 37
Got:
    2^6 * 3^2 * 37^2
**********************************************************************
File "tut.py", line 1730:
    : G = F.quadratic_twist(2); G
Expected:
    Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
Got:
    Elliptic Curve defined by y^2 + y = x^3 - 12321*x - 341908 over Rational Field
**********************************************************************
File "tut.py", line 1732:
    : G.conductor()
Expected:
    37
Got:
    12321
**********************************************************************
```
William says:

```
[04:56] <mabshoff> william_stein: #740 seems to create different results in various places, i.e. doc test failures.
[04:56] <william_stein> hmmm
[04:57] <mabshoff> File "tut.py", line 1676:
[04:57] <mabshoff>     : EllipticCurve(5)
[04:57] <mabshoff> Expected:
[04:57] <mabshoff>     Elliptic Curve defined by y^2 + x*y  = x^3 + 36/1723*x + 1/1723
[04:57] <mabshoff>                 over Rational Field
[04:57] <mabshoff> Got:
[04:57] <mabshoff>     Elliptic Curve defined by y^2  = x^3 + 25845*x - 29687290 over Rational Field
[04:57] <william_stein> mabshoff -- not surprising.
[04:57] <william_stein> NOBODY has doctested testall after applying that.
[04:57] <mabshoff> ok
[04:57] <william_stein> The new output in tut.py is right, by the way.
[04:57] <mabshoff> :)
[04:57] <william_stein> It's a different curve with that j-invariant -- a better one.
```
Patch coming up.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1979





---

archive/issue_comments_012797.json:
```json
{
    "body": "Attachment [Sage-2.10.1.rc3-fix-doctest-fallout-from_trac-740.patch](tarball://root/attachments/some-uuid/ticket1979/Sage-2.10.1.rc3-fix-doctest-fallout-from_trac-740.patch) by mabshoff created at 2008-01-30 05:18:12",
    "created_at": "2008-01-30T05:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1979#issuecomment-12797",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.10.1.rc3-fix-doctest-fallout-from_trac-740.patch](tarball://root/attachments/some-uuid/ticket1979/Sage-2.10.1.rc3-fix-doctest-fallout-from_trac-740.patch) by mabshoff created at 2008-01-30 05:18:12



---

archive/issue_comments_012798.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc3. This ticket should be reopened if it turns out that the fix is incorrect.",
    "created_at": "2008-01-30T09:42:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1979#issuecomment-12798",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.rc3. This ticket should be reopened if it turns out that the fix is incorrect.



---

archive/issue_events_004781.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-30T09:42:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1979",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1979#event-4781"
}
```



---

archive/issue_comments_012799.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-30T09:42:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1979#issuecomment-12799",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012800.json:
```json
{
    "body": "Looks good to me (and Cremona said the same in email).",
    "created_at": "2008-01-30T13:05:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1979#issuecomment-12800",
    "user": "https://github.com/williamstein"
}
```

Looks good to me (and Cremona said the same in email).



---

archive/issue_comments_012801.json:
```json
{
    "body": "Attachment [ec740.patch](tarball://root/attachments/some-uuid/ticket1979/ec740.patch) by mabshoff created at 2008-01-30 15:24:06\n\nThis is a corrected patch of my patch, so I am reverting my patch an applying this one",
    "created_at": "2008-01-30T15:24:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1979#issuecomment-12801",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [ec740.patch](tarball://root/attachments/some-uuid/ticket1979/ec740.patch) by mabshoff created at 2008-01-30 15:24:06

This is a corrected patch of my patch, so I am reverting my patch an applying this one



---

archive/issue_comments_012802.json:
```json
{
    "body": "Merged ec740.patch in Sage 2.10.1.rc4 after reverting the original patch",
    "created_at": "2008-01-30T15:25:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1979#issuecomment-12802",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged ec740.patch in Sage 2.10.1.rc4 after reverting the original patch
