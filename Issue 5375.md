# Issue 5375: [with patch, needs review] minor problems with ReST in geometry/lattice_polytope.py

archive/issues_005375.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nThis fixes the few open problems from ticket #4912.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5375\n\n",
    "created_at": "2009-02-26T00:22:43Z",
    "labels": [
        "component: geometry",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "[with patch, needs review] minor problems with ReST in geometry/lattice_polytope.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5375",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

This fixes the few open problems from ticket #4912.

Issue created by migration from https://trac.sagemath.org/ticket/5375





---

archive/issue_comments_041316.json:
```json
{
    "body": "Attachment [geom-rst.patch](tarball://root/attachments/some-uuid/ticket5375/geom-rst.patch) by @jhpalmieri created at 2009-02-26 00:37:33",
    "created_at": "2009-02-26T00:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5375#issuecomment-41316",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [geom-rst.patch](tarball://root/attachments/some-uuid/ticket5375/geom-rst.patch) by @jhpalmieri created at 2009-02-26 00:37:33



---

archive/issue_comments_041317.json:
```json
{
    "body": "Changing component from geometry to documentation.",
    "created_at": "2009-02-26T00:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5375#issuecomment-41317",
    "user": "https://github.com/jhpalmieri"
}
```

Changing component from geometry to documentation.



---

archive/issue_comments_041318.json:
```json
{
    "body": "REFEREE REPORT\n\n\n\nThe patch **geom-rst.patch** applied cleanly against 3.4.alpha0 and all doctests passed with the options `-t -long -optional`. The reference manual built fine with\n\n```\nsage -docbuild reference html\n```\nLooking at the relevant HTML file\n\n```\n/path/to/reference/sage/geometry/lattice_polytope.html\n```\nthe suggested patch fixed the problem it's intends to. So positive review on my part. Note that there are still a large number of typos in the file that **geom-rst.patch** touches, namely\n\n```\nsage/geometry/lattice_polytope.py\n```\nBut please open another ticket for that.",
    "created_at": "2009-02-27T07:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5375#issuecomment-41318",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
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

archive/issue_comments_041319.json:
```json
{
    "body": "Merged in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T16:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5375#issuecomment-41319",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.rc0.

Cheers,

Michael



---

archive/issue_comments_041320.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-28T16:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5375#issuecomment-41320",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_012527.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-28T16:24:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5375",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5375#event-12527"
}
```
