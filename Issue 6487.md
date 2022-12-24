# Issue 6487: Plethysm with the zero symmetric function causes a segfault

archive/issues_006487.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  mhansen\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage:\nsage: sage: s = SFASchur(QQ)\nsage: sage: s([2]).plethysm(s.zero_element())\nsage.bin:\n| Sage Version 4.1.rc1, Release Date: 2009-07-07                     |\n| Type notebook() for the GUI, and license() for information.        |\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\nThis problem also exists with sage-4.0.2.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6487\n\n",
    "created_at": "2009-07-08T19:17:28Z",
    "labels": [
        "combinatorics",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Plethysm with the zero symmetric function causes a segfault",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6487",
    "user": "saliola"
}
```
Assignee: mhansen

CC:  mhansen


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage:
sage: sage: s = SFASchur(QQ)
sage: sage: s([2]).plethysm(s.zero_element())
sage.bin:
| Sage Version 4.1.rc1, Release Date: 2009-07-07                     |
| Type notebook() for the GUI, and license() for information.        |
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```

This problem also exists with sage-4.0.2.

Issue created by migration from https://trac.sagemath.org/ticket/6487





---

archive/issue_comments_052460.json:
```json
{
    "body": "This appears to be fixed in sage-4.4.\n\n```\nsage: sage: sage: s = SFASchur(QQ)\nsage: sage: sage: s([2]).plethysm(s.zero_element())\n0\n```\n",
    "created_at": "2010-05-06T15:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6487#issuecomment-52460",
    "user": "jbandlow"
}
```

This appears to be fixed in sage-4.4.

```
sage: sage: sage: s = SFASchur(QQ)
sage: sage: sage: s([2]).plethysm(s.zero_element())
0
```




---

archive/issue_comments_052461.json:
```json
{
    "body": "I'll mark this as invalid then.",
    "created_at": "2010-05-06T16:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6487#issuecomment-52461",
    "user": "mhansen"
}
```

I'll mark this as invalid then.



---

archive/issue_comments_052462.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-05-06T16:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6487#issuecomment-52462",
    "user": "mhansen"
}
```

Resolution: invalid
