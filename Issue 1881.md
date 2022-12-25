# Issue 1881: Sage 2.10.1.alpha0: tut.tex doctes failure with factorize()

archive/issues_001881.json:
```json
{
    "body": "Assignee: mabshoff\n\nInitially reported by Jaap:\n\n```\nsage -t  tut.tex                                            \n**********************************************************************\nFile \"tut.py\", line 3574:\n    : factor(f)\nExpected:\n    9 * (-x^5 + y^2)^2 * (x^6 - 2*x^3*y^2 - x^2*y^3 + y^4)\nGot:\n    (9) * (-x^5 + y^2)^2 * (x^6 - 2*x^3*y^2 - x^2*y^3 + y^4)\n**********************************************************************\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1881\n\n",
    "created_at": "2008-01-21T22:00:18Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "Sage 2.10.1.alpha0: tut.tex doctes failure with factorize()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1881",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Initially reported by Jaap:

```
sage -t  tut.tex                                            
**********************************************************************
File "tut.py", line 3574:
    : factor(f)
Expected:
    9 * (-x^5 + y^2)^2 * (x^6 - 2*x^3*y^2 - x^2*y^3 + y^4)
Got:
    (9) * (-x^5 + y^2)^2 * (x^6 - 2*x^3*y^2 - x^2*y^3 + y^4)
**********************************************************************
```



Issue created by migration from https://trac.sagemath.org/ticket/1881





---

archive/issue_comments_011870.json:
```json
{
    "body": "This is likely the \"fault\" of Ncalexan's recent changes to factorize.py.  \nI'm not sure this change is bad though -- it's probably good using parens for\nthe unit part.  Though it looks dumb in this case.",
    "created_at": "2008-01-21T22:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1881#issuecomment-11870",
    "user": "https://github.com/williamstein"
}
```

This is likely the "fault" of Ncalexan's recent changes to factorize.py.  
I'm not sure this change is bad though -- it's probably good using parens for
the unit part.  Though it looks dumb in this case.



---

archive/issue_comments_011871.json:
```json
{
    "body": "Attachment [Sage-2.10.1.alpha0-fix-doctest-1881.patch](tarball://root/attachments/some-uuid/ticket1881/Sage-2.10.1.alpha0-fix-doctest-1881.patch) by mabshoff created at 2008-01-21 22:25:25\n\nYou are right, it does look dumb, but this seems to be fallout from #1391, i.e. \"bug in unit part of factorizations of multivariate polynomials\". At least malb did fix a doctest in that patch in the same fashion. Care to review this trivial patch?\n\nCheers,\n\nMichael",
    "created_at": "2008-01-21T22:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1881#issuecomment-11871",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.10.1.alpha0-fix-doctest-1881.patch](tarball://root/attachments/some-uuid/ticket1881/Sage-2.10.1.alpha0-fix-doctest-1881.patch) by mabshoff created at 2008-01-21 22:25:25

You are right, it does look dumb, but this seems to be fallout from #1391, i.e. "bug in unit part of factorizations of multivariate polynomials". At least malb did fix a doctest in that patch in the same fashion. Care to review this trivial patch?

Cheers,

Michael



---

archive/issue_comments_011872.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-22T01:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1881#issuecomment-11872",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha1



---

archive/issue_comments_011873.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-22T01:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1881#issuecomment-11873",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
