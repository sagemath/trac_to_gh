# Issue 5121: major bug in plot command

archive/issues_005121.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: E = EllipticCurve('37a')\nsage: plot(E)\nsage: plot(E, xmin=25,xmax=25)\nTraceback (most recent call last):\n...\nAttributeError: 'SymbolicEquation' object has no attribute '_fast_float_'\n```\n\n\nThis broke David Hansen's thesis.  It also caused me a lot of embarasement during my talk at Sage Days 12!!!\n\nIt is a new bug introduced by some plot refactoring recently. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5121\n\n",
    "created_at": "2009-01-28T20:07:18Z",
    "labels": [
        "graphics",
        "blocker",
        "bug"
    ],
    "title": "major bug in plot command",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5121",
    "user": "was"
}
```
Assignee: was


```
sage: E = EllipticCurve('37a')
sage: plot(E)
sage: plot(E, xmin=25,xmax=25)
Traceback (most recent call last):
...
AttributeError: 'SymbolicEquation' object has no attribute '_fast_float_'
```


This broke David Hansen's thesis.  It also caused me a lot of embarasement during my talk at Sage Days 12!!!

It is a new bug introduced by some plot refactoring recently. 

Issue created by migration from https://trac.sagemath.org/ticket/5121





---

archive/issue_comments_039153.json:
```json
{
    "body": "Apparently a block of code was not indented correctly.  I'll post up a patch momentarily.",
    "created_at": "2009-01-28T21:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5121#issuecomment-39153",
    "user": "jason"
}
```

Apparently a block of code was not indented correctly.  I'll post up a patch momentarily.



---

archive/issue_comments_039154.json:
```json
{
    "body": "This broke in the commit http://www.sagemath.org/hg/sage-main/diff/ed11b267ec9f/sage/plot/plot.py",
    "created_at": "2009-01-28T21:56:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5121#issuecomment-39154",
    "user": "jason"
}
```

This broke in the commit http://www.sagemath.org/hg/sage-main/diff/ed11b267ec9f/sage/plot/plot.py



---

archive/issue_comments_039155.json:
```json
{
    "body": "Attachment [trac_5121.patch](tarball://root/attachments/some-uuid/ticket5121/trac_5121.patch) by was created at 2009-01-28 23:14:17",
    "created_at": "2009-01-28T23:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5121#issuecomment-39155",
    "user": "was"
}
```

Attachment [trac_5121.patch](tarball://root/attachments/some-uuid/ticket5121/trac_5121.patch) by was created at 2009-01-28 23:14:17



---

archive/issue_comments_039156.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-29T00:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5121#issuecomment-39156",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_039157.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-29T00:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5121#issuecomment-39157",
    "user": "mabshoff"
}
```

Resolution: fixed
