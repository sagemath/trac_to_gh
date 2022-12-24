# Issue 6874: #4135 follow-up: fix typos and docbuild warnings

archive/issues_006874.json:
```json
{
    "body": "Assignee: tba\n\nCC:  ddrake timdumol\n\nAfter merging the patch `trac_4135.5.patch` at #4135, rebuilding the reference manual results in a warning:\n\n```\nWARNING: <autodoc>:0: (ERROR/3) Error in \"module\" directive:\nno content permitted.\n\n.. module:: sage.server.notebook.twist\n\n    TESTS::\n\n    It is important that this file never be imported by default on\n    startup by Sage, since it is very expensive, since importing Twisted\n    is expensive. This doctest verifies that twist.py isn't imported on\n    startup.\n\n    sage: os.system(\"sage -startuptime | grep twisted\\.web2 1>/dev/null\") != 0  # !=0 means not found\n    True\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6874\n\n",
    "created_at": "2009-09-03T10:27:09Z",
    "labels": [
        "documentation",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "#4135 follow-up: fix typos and docbuild warnings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6874",
    "user": "mvngu"
}
```
Assignee: tba

CC:  ddrake timdumol

After merging the patch `trac_4135.5.patch` at #4135, rebuilding the reference manual results in a warning:

```
WARNING: <autodoc>:0: (ERROR/3) Error in "module" directive:
no content permitted.

.. module:: sage.server.notebook.twist

    TESTS::

    It is important that this file never be imported by default on
    startup by Sage, since it is very expensive, since importing Twisted
    is expensive. This doctest verifies that twist.py isn't imported on
    startup.

    sage: os.system("sage -startuptime | grep twisted\.web2 1>/dev/null") != 0  # !=0 means not found
    True
```



Issue created by migration from https://trac.sagemath.org/ticket/6874





---

archive/issue_comments_056750.json:
```json
{
    "body": "depends on #4135",
    "created_at": "2009-09-03T10:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6874#issuecomment-56750",
    "user": "mvngu"
}
```

depends on #4135



---

archive/issue_comments_056751.json:
```json
{
    "body": "Attachment [trac_6874-fix-typos.patch](tarball://root/attachments/some-uuid/ticket6874/trac_6874-fix-typos.patch) by mvngu created at 2009-09-03 10:37:48",
    "created_at": "2009-09-03T10:37:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6874#issuecomment-56751",
    "user": "mvngu"
}
```

Attachment [trac_6874-fix-typos.patch](tarball://root/attachments/some-uuid/ticket6874/trac_6874-fix-typos.patch) by mvngu created at 2009-09-03 10:37:48



---

archive/issue_comments_056752.json:
```json
{
    "body": "Looks good. Positive review.",
    "created_at": "2009-09-03T12:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6874#issuecomment-56752",
    "user": "ddrake"
}
```

Looks good. Positive review.



---

archive/issue_comments_056753.json:
```json
{
    "body": "Changing assignee from tba to mvngu.",
    "created_at": "2009-09-03T12:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6874#issuecomment-56753",
    "user": "ddrake"
}
```

Changing assignee from tba to mvngu.



---

archive/issue_comments_056754.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-03T21:38:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6874#issuecomment-56754",
    "user": "mvngu"
}
```

Resolution: fixed
