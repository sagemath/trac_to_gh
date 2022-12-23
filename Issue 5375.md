# Issue 5375: [with patch, needs review] minor problems with ReST in geometry/lattice_polytope.py

archive/issues_005375.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nThis fixes the few open problems from ticket #4912.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5375\n\n",
    "created_at": "2009-02-26T00:22:43Z",
    "labels": [
        "geometry",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] minor problems with ReST in geometry/lattice_polytope.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5375",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

This fixes the few open problems from ticket #4912.

Issue created by migration from https://trac.sagemath.org/ticket/5375





---

archive/issue_comments_041398.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-02-26T00:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5375#issuecomment-41398",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_041399.json:
```json
{
    "body": "Changing component from geometry to documentation.",
    "created_at": "2009-02-26T00:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5375#issuecomment-41399",
    "user": "jhpalmieri"
}
```

Changing component from geometry to documentation.



---

archive/issue_comments_041400.json:
```json
{
    "body": "REFEREE REPORT\n\n\n\nThe patch **geom-rst.patch** applied cleanly against 3.4.alpha0 and all doctests passed with the options `-t -long -optional`. The reference manual built fine with\n\n```\nsage -docbuild reference html\n```\n\nLooking at the relevant HTML file\n\n```\n/path/to/reference/sage/geometry/lattice_polytope.html\n```\n\nthe suggested patch fixed the problem it's intends to. So positive review on my part. Note that there are still a large number of typos in the file that **geom-rst.patch** touches, namely\n\n```\nsage/geometry/lattice_polytope.py\n```\n\nBut please open another ticket for that.",
    "created_at": "2009-02-27T07:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5375#issuecomment-41400",
    "user": "mvngu"
}
```

REFEREE REPORT



The patch **geom-rst.patch** applied cleanly against 3.4.alpha0 and all doctests passed with the options `-t -long -optional`. The reference manual built fine with

```
sage -docbuild reference html
```

Looking at the relevant HTML file

```
/path/to/reference/sage/geometry/lattice_polytope.html
```

the suggested patch fixed the problem it's intends to. So positive review on my part. Note that there are still a large number of typos in the file that **geom-rst.patch** touches, namely

```
sage/geometry/lattice_polytope.py
```

But please open another ticket for that.



---

archive/issue_comments_041401.json:
```json
{
    "body": "Merged in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T16:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5375#issuecomment-41401",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.rc0.

Cheers,

Michael



---

archive/issue_comments_041402.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-28T16:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5375#issuecomment-41402",
    "user": "mabshoff"
}
```

Resolution: fixed
