# Issue 5783: [with patch, needs review]  Lazy attributes: fix infinite recursion bug + support for cpdefs methods

archive/issues_005783.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  sage-combinat\n\nThe summary says it all.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5783\n\n",
    "created_at": "2009-04-14T06:55:25Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, needs review]  Lazy attributes: fix infinite recursion bug + support for cpdefs methods",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5783",
    "user": "nthiery"
}
```
Assignee: cwitty

CC:  sage-combinat

The summary says it all.

Issue created by migration from https://trac.sagemath.org/ticket/5783





---

archive/issue_comments_045268.json:
```json
{
    "body": "Changing assignee from cwitty to nthiery.",
    "created_at": "2009-05-18T03:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5783#issuecomment-45268",
    "user": "nthiery"
}
```

Changing assignee from cwitty to nthiery.



---

archive/issue_comments_045269.json:
```json
{
    "body": "Attachment [lazy_attributes-fixes-5783-final.patch](tarball://root/attachments/some-uuid/ticket5783/lazy_attributes-fixes-5783-final.patch) by nthiery created at 2009-05-19 06:19:22",
    "created_at": "2009-05-19T06:19:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5783#issuecomment-45269",
    "user": "nthiery"
}
```

Attachment [lazy_attributes-fixes-5783-final.patch](tarball://root/attachments/some-uuid/ticket5783/lazy_attributes-fixes-5783-final.patch) by nthiery created at 2009-05-19 06:19:22



---

archive/issue_comments_045270.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-19T06:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5783#issuecomment-45270",
    "user": "nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045271.json:
```json
{
    "body": "Updated patch:\n- fix ReST doc (indentation, ::, ...)\n- fix introspection\n- adds a hook for this in sage.misc.sageinspect.sage_getsourcelines",
    "created_at": "2009-05-19T06:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5783#issuecomment-45271",
    "user": "nthiery"
}
```

Updated patch:
- fix ReST doc (indentation, ::, ...)
- fix introspection
- adds a hook for this in sage.misc.sageinspect.sage_getsourcelines



---

archive/issue_comments_045272.json:
```json
{
    "body": "Adds lots of good documentation, fixes some problems, though additional feature requests remain.  Positive review.",
    "created_at": "2009-05-19T08:00:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5783#issuecomment-45272",
    "user": "roed"
}
```

Adds lots of good documentation, fixes some problems, though additional feature requests remain.  Positive review.



---

archive/issue_comments_045273.json:
```json
{
    "body": "David,\n\nplease remember to change the summary if you do reviews of tickets.\n\nMichael",
    "created_at": "2009-05-19T15:06:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5783#issuecomment-45273",
    "user": "mabshoff"
}
```

David,

please remember to change the summary if you do reviews of tickets.

Michael



---

archive/issue_comments_045274.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T19:21:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5783#issuecomment-45274",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_045275.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-19T19:21:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5783#issuecomment-45275",
    "user": "mabshoff"
}
```

Resolution: fixed
