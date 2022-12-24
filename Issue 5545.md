# Issue 5545: bug in sage's Cython dependency tracker

archive/issues_005545.json:
```json
{
    "body": "Assignee: mabshoff\n\nTo reproduce: Start with Sage 3.4.  Apply the attached patch (dependency-tracker-bug-testcase.patch).  Rebuild with \"sage -b\", then run Sage.  Type:\n\n```\nsage: import sage.rings.polynomial.real_roots\n```\n\nYou will get an error:\n\n```\nTypeError: sage.rings.real_mpfi.RealIntervalField is not a type object\n```\n\nBut if you touch real_roots.pyx and rebuild, the error goes away.\n\nSo somehow real_roots.pyx depends on real_mpfi.pyx in a way that the dependency tracker doesn't catch.  (It's not obvious how, because real_roots.pyx never even mentions `mpfi`.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/5545\n\n",
    "created_at": "2009-03-17T06:22:21Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bug in sage's Cython dependency tracker",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5545",
    "user": "cwitty"
}
```
Assignee: mabshoff

To reproduce: Start with Sage 3.4.  Apply the attached patch (dependency-tracker-bug-testcase.patch).  Rebuild with "sage -b", then run Sage.  Type:

```
sage: import sage.rings.polynomial.real_roots
```

You will get an error:

```
TypeError: sage.rings.real_mpfi.RealIntervalField is not a type object
```

But if you touch real_roots.pyx and rebuild, the error goes away.

So somehow real_roots.pyx depends on real_mpfi.pyx in a way that the dependency tracker doesn't catch.  (It's not obvious how, because real_roots.pyx never even mentions `mpfi`.)

Issue created by migration from https://trac.sagemath.org/ticket/5545





---

archive/issue_comments_043135.json:
```json
{
    "body": "Attachment [dependency-tracker-bug-testcase.patch](tarball://root/attachments/some-uuid/ticket5545/dependency-tracker-bug-testcase.patch) by jdemeyer created at 2013-08-13 15:35:53",
    "created_at": "2013-08-13T15:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5545#issuecomment-43135",
    "user": "jdemeyer"
}
```

Attachment [dependency-tracker-bug-testcase.patch](tarball://root/attachments/some-uuid/ticket5545/dependency-tracker-bug-testcase.patch) by jdemeyer created at 2013-08-13 15:35:53



---

archive/issue_comments_043136.json:
```json
{
    "body": "worksforme:\n\n```\njdemeyer@tamiyo:/usr/local/src/sage-git$ touch src/sage/rings/real_mpfi.pxd\njdemeyer@tamiyo:/usr/local/src/sage-git$ ./sage -b\nscons: `install' is up to date.\nUpdating Cython code....\nEnabling Cython debugging support\nCompiling sage/rings/complex_interval.pyx because it depends on ./sage/rings/real_mpfi.pxd.\nCompiling sage/rings/real_mpfi.pyx because it depends on sage/rings/real_mpfi.pxd.\nCompiling sage/rings/polynomial/real_roots.pyx because it depends on ./sage/rings/real_mpfi.pxd.\n[...]\n```\n",
    "created_at": "2014-09-02T09:19:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5545#issuecomment-43136",
    "user": "jdemeyer"
}
```

worksforme:

```
jdemeyer@tamiyo:/usr/local/src/sage-git$ touch src/sage/rings/real_mpfi.pxd
jdemeyer@tamiyo:/usr/local/src/sage-git$ ./sage -b
scons: `install' is up to date.
Updating Cython code....
Enabling Cython debugging support
Compiling sage/rings/complex_interval.pyx because it depends on ./sage/rings/real_mpfi.pxd.
Compiling sage/rings/real_mpfi.pyx because it depends on sage/rings/real_mpfi.pxd.
Compiling sage/rings/polynomial/real_roots.pyx because it depends on ./sage/rings/real_mpfi.pxd.
[...]
```




---

archive/issue_comments_043137.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-09-02T09:19:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5545#issuecomment-43137",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_043138.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-09-02T09:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5545#issuecomment-43138",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_043139.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2014-09-09T14:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5545#issuecomment-43139",
    "user": "vbraun"
}
```

Resolution: worksforme
