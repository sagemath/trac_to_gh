# Issue 6011: Bring plot/arrow.py to 100% coverage

archive/issues_006011.json:
```json
{
    "body": "Assignee: mabshoff\n\nBring plot/arrow.py to 100% coverage\n\nIssue created by migration from https://trac.sagemath.org/ticket/6011\n\n",
    "created_at": "2009-05-09T02:45:35Z",
    "labels": [
        "doctest",
        "minor",
        "enhancement"
    ],
    "title": "Bring plot/arrow.py to 100% coverage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6011",
    "user": "kcrisman"
}
```
Assignee: mabshoff

Bring plot/arrow.py to 100% coverage

Issue created by migration from https://trac.sagemath.org/ticket/6011





---

archive/issue_comments_047832.json:
```json
{
    "body": "Attachment\n\nAlso adds tiny plot3d enhancement (original doctest only tested Graphics.plot3d).\n\nPlease see [http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43](http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43) for why there is no loads(dumps()) test.  Yet.",
    "created_at": "2009-05-09T02:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6011#issuecomment-47832",
    "user": "kcrisman"
}
```

Attachment

Also adds tiny plot3d enhancement (original doctest only tested Graphics.plot3d).

Please see [http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43](http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43) for why there is no loads(dumps()) test.  Yet.



---

archive/issue_comments_047833.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-09T02:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6011#issuecomment-47833",
    "user": "kcrisman"
}
```

Changing status from new to assigned.



---

archive/issue_comments_047834.json:
```json
{
    "body": "Changing assignee from mabshoff to kcrisman.",
    "created_at": "2009-05-09T02:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6011#issuecomment-47834",
    "user": "kcrisman"
}
```

Changing assignee from mabshoff to kcrisman.



---

archive/issue_comments_047835.json:
```json
{
    "body": "Changing component from doctest to documentation.",
    "created_at": "2009-05-09T02:52:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6011#issuecomment-47835",
    "user": "kcrisman"
}
```

Changing component from doctest to documentation.



---

archive/issue_comments_047836.json:
```json
{
    "body": "Attachment\n\nreviewer patch; add consistency to the whole module",
    "created_at": "2009-05-09T04:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6011#issuecomment-47836",
    "user": "mvngu"
}
```

Attachment

reviewer patch; add consistency to the whole module



---

archive/issue_comments_047837.json:
```json
{
    "body": "REFEREE REPORT\n\n\n\nThe patch `trac_6011.patch` applies OK against the \"post-final\" version sage-3.4.2, all doctests pass with the options `-t -long`, and the doctest coverage is now 100% as claimed. Note that `sage/plot/arrow.py` is not included in the reference manual, so you can't search for it in order to view the documentation for `sage/plot/arrow.py`.\n\n\n\nThe patch adds some trivial inconsistencies in how \"two-dimensional\" and \"three-dimensional\" are abbreviated. These and other inconsistencies are fixed in the reviewer patch `trac_6011-reviewer.patch`. Apart from the issue of consistency throughout the whole module, positive review for kcrisman's patch. Only my patch needs to be reviewed.",
    "created_at": "2009-05-09T04:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6011#issuecomment-47837",
    "user": "mvngu"
}
```

REFEREE REPORT



The patch `trac_6011.patch` applies OK against the "post-final" version sage-3.4.2, all doctests pass with the options `-t -long`, and the doctest coverage is now 100% as claimed. Note that `sage/plot/arrow.py` is not included in the reference manual, so you can't search for it in order to view the documentation for `sage/plot/arrow.py`.



The patch adds some trivial inconsistencies in how "two-dimensional" and "three-dimensional" are abbreviated. These and other inconsistencies are fixed in the reviewer patch `trac_6011-reviewer.patch`. Apart from the issue of consistency throughout the whole module, positive review for kcrisman's patch. Only my patch needs to be reviewed.



---

archive/issue_comments_047838.json:
```json
{
    "body": "Merged both patches in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T09:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6011#issuecomment-47838",
    "user": "mabshoff"
}
```

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_047839.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-11T09:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6011#issuecomment-47839",
    "user": "mabshoff"
}
```

Resolution: fixed
