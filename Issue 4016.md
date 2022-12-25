# Issue 4016: [with patch, needs review] improve doctests to schemes/generic/scheme.py

archive/issues_004016.json:
```json
{
    "body": "Assignee: mabshoff\n\nBrings coverage up to 96% (sorry, I have no idea what's going on with the one remaining function).\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4016\n\n",
    "created_at": "2008-08-31T07:52:18Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] improve doctests to schemes/generic/scheme.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4016",
    "user": "https://github.com/aghitza"
}
```
Assignee: mabshoff

Brings coverage up to 96% (sorry, I have no idea what's going on with the one remaining function).



Issue created by migration from https://trac.sagemath.org/ticket/4016





---

archive/issue_comments_028910.json:
```json
{
    "body": "All the doctests look sane to me, and mabshoff is verifying that they all pass.",
    "created_at": "2008-08-31T08:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4016#issuecomment-28910",
    "user": "https://github.com/robertwb"
}
```

All the doctests look sane to me, and mabshoff is verifying that they all pass.



---

archive/issue_comments_028911.json:
```json
{
    "body": "One slight problem in tut.tex:\n\n```\nsage -t -long devel/doc/tut/tut.tex\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/tmp/tut.py\", line 2178:\n    : D\nExpected:\n    Affine Curve over Rational Field defined by\n       x^5 + x^3*y^2 + x^2*y^3 + y^5 - x^3 - y^3 - x^2 - y^2 + 1\nGot:\n    Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:\n      x^5 + x^3*y^2 + x^2*y^3 + y^5 - x^3 - y^3 - x^2 - y^2 + 1\n**********************************************************************\n```\n",
    "created_at": "2008-08-31T08:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4016#issuecomment-28911",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

One slight problem in tut.tex:

```
sage -t -long devel/doc/tut/tut.tex
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/tmp/tut.py", line 2178:
    : D
Expected:
    Affine Curve over Rational Field defined by
       x^5 + x^3*y^2 + x^2*y^3 + y^5 - x^3 - y^3 - x^2 - y^2 + 1
Got:
    Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
      x^5 + x^3*y^2 + x^2*y^3 + y^5 - x^3 - y^3 - x^2 - y^2 + 1
**********************************************************************
```




---

archive/issue_comments_028912.json:
```json
{
    "body": "Attachment [4016-doctest_scheme.patch](tarball://root/attachments/some-uuid/ticket4016/4016-doctest_scheme.patch) by @aghitza created at 2008-08-31 12:08:04",
    "created_at": "2008-08-31T12:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4016#issuecomment-28912",
    "user": "https://github.com/aghitza"
}
```

Attachment [4016-doctest_scheme.patch](tarball://root/attachments/some-uuid/ticket4016/4016-doctest_scheme.patch) by @aghitza created at 2008-08-31 12:08:04



---

archive/issue_comments_028913.json:
```json
{
    "body": "Sorry Michael, I should have tested the docs as well...  anyway, it just required a small fix in plane_curves/curve.py.  I have replaced the patch with one that adds that small fix.",
    "created_at": "2008-08-31T12:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4016#issuecomment-28913",
    "user": "https://github.com/aghitza"
}
```

Sorry Michael, I should have tested the docs as well...  anyway, it just required a small fix in plane_curves/curve.py.  I have replaced the patch with one that adds that small fix.



---

archive/issue_comments_028914.json:
```json
{
    "body": "Thanks Alex, I see it is the same fix as in sage/schemes/generic/algebraic_scheme.py. I know that Robert won't be online today, but hopefully he can take a quick look on Monday. Assuming it passes doctests I plan to merge this patch in the near future.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T02:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4016#issuecomment-28914",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Thanks Alex, I see it is the same fix as in sage/schemes/generic/algebraic_scheme.py. I know that Robert won't be online today, but hopefully he can take a quick look on Monday. Assuming it passes doctests I plan to merge this patch in the near future.

Cheers,

Michael



---

archive/issue_comments_028915.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha4",
    "created_at": "2008-09-01T02:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4016#issuecomment-28915",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha4



---

archive/issue_comments_028916.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-01T02:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4016#issuecomment-28916",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004246.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-09-01T02:56:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4016",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4016#event-4246"
}
```
