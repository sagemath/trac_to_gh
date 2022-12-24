# Issue 6007: Bring plot/primitive.py to 100% coverage

archive/issues_006007.json:
```json
{
    "body": "Assignee: mabshoff\n\nBring plot/primitive.py to 100% coverage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6007\n\n",
    "created_at": "2009-05-08T16:43:54Z",
    "labels": [
        "doctest",
        "minor",
        "enhancement"
    ],
    "title": "Bring plot/primitive.py to 100% coverage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6007",
    "user": "kcrisman"
}
```
Assignee: mabshoff

Bring plot/primitive.py to 100% coverage.

Issue created by migration from https://trac.sagemath.org/ticket/6007





---

archive/issue_comments_047794.json:
```json
{
    "body": "Attachment [trac_6007.patch](tarball://root/attachments/some-uuid/ticket6007/trac_6007.patch) by kcrisman created at 2009-05-08 16:44:19",
    "created_at": "2009-05-08T16:44:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6007#issuecomment-47794",
    "user": "kcrisman"
}
```

Attachment [trac_6007.patch](tarball://root/attachments/some-uuid/ticket6007/trac_6007.patch) by kcrisman created at 2009-05-08 16:44:19



---

archive/issue_comments_047795.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-08T16:45:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6007#issuecomment-47795",
    "user": "kcrisman"
}
```

Changing status from new to assigned.



---

archive/issue_comments_047796.json:
```json
{
    "body": "Please see [http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43](http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43) for explanation of why there is no loads(dumps()) test.",
    "created_at": "2009-05-08T16:45:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6007#issuecomment-47796",
    "user": "kcrisman"
}
```

Please see [http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43](http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43) for explanation of why there is no loads(dumps()) test.



---

archive/issue_comments_047797.json:
```json
{
    "body": "Changing assignee from mabshoff to kcrisman.",
    "created_at": "2009-05-08T16:45:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6007#issuecomment-47797",
    "user": "kcrisman"
}
```

Changing assignee from mabshoff to kcrisman.



---

archive/issue_comments_047798.json:
```json
{
    "body": "Changing component from doctest to documentation.",
    "created_at": "2009-05-09T02:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6007#issuecomment-47798",
    "user": "kcrisman"
}
```

Changing component from doctest to documentation.



---

archive/issue_comments_047799.json:
```json
{
    "body": "reviewer patch; add consistency to the whole module",
    "created_at": "2009-05-09T03:22:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6007#issuecomment-47799",
    "user": "mvngu"
}
```

reviewer patch; add consistency to the whole module



---

archive/issue_comments_047800.json:
```json
{
    "body": "Attachment [trac_6007-reviewer.patch](tarball://root/attachments/some-uuid/ticket6007/trac_6007-reviewer.patch) by mvngu created at 2009-05-09 03:34:05\n\nREFEREE REPORT\n\n\n\nThe patch `trac_6007.patch` applies fine against the \"post-final\" version sage-3.4.2, all doctests pass with the options `-t -long`, and the doctest coverage is 100% as claimed. The reference manual built OK, but note that `sage/plot/primitive.py` is not included in the reference manual, so you can't search for the module in it.\n\n\n\nOn the side of pedantry, the patch introduces a trivial inconsistency in how \"two-dimensional\" and \"three-dimensional\" are abbreviated. So all such references in the module `sage/plot/primitive.py` now follow the forms `2D` and `3D`. Apart from this trivial issue of inconsistency which is fixed in `trac_6007-reviewer.patch`, positive review for kcrisman's patch. Only my patch needs to be reviewed.",
    "created_at": "2009-05-09T03:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6007#issuecomment-47800",
    "user": "mvngu"
}
```

Attachment [trac_6007-reviewer.patch](tarball://root/attachments/some-uuid/ticket6007/trac_6007-reviewer.patch) by mvngu created at 2009-05-09 03:34:05

REFEREE REPORT



The patch `trac_6007.patch` applies fine against the "post-final" version sage-3.4.2, all doctests pass with the options `-t -long`, and the doctest coverage is 100% as claimed. The reference manual built OK, but note that `sage/plot/primitive.py` is not included in the reference manual, so you can't search for the module in it.



On the side of pedantry, the patch introduces a trivial inconsistency in how "two-dimensional" and "three-dimensional" are abbreviated. So all such references in the module `sage/plot/primitive.py` now follow the forms `2D` and `3D`. Apart from this trivial issue of inconsistency which is fixed in `trac_6007-reviewer.patch`, positive review for kcrisman's patch. Only my patch needs to be reviewed.



---

archive/issue_comments_047801.json:
```json
{
    "body": "> Only my patch needs to be reviewed.\n\nLooks good.",
    "created_at": "2009-05-09T20:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6007#issuecomment-47801",
    "user": "jhpalmieri"
}
```

> Only my patch needs to be reviewed.

Looks good.



---

archive/issue_comments_047802.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-11T08:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6007#issuecomment-47802",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_047803.json:
```json
{
    "body": "Merged both patches in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T08:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6007#issuecomment-47803",
    "user": "mabshoff"
}
```

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael
