# Issue 2537: a.frac() should return x-x.floor()

archive/issues_002537.json:
```json
{
    "body": "Assignee: @rishikesha\n\nfrac(-2.9) should be .1\n\nIssue created by migration from https://trac.sagemath.org/ticket/2537\n\n",
    "created_at": "2008-03-16T01:09:45Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "a.frac() should return x-x.floor()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2537",
    "user": "https://github.com/rishikesha"
}
```
Assignee: @rishikesha

frac(-2.9) should be .1

Issue created by migration from https://trac.sagemath.org/ticket/2537





---

archive/issue_comments_017271.json:
```json
{
    "body": "Attachment [real.patch](tarball://root/attachments/some-uuid/ticket2537/real.patch) by mabshoff created at 2008-03-16 01:11:42",
    "created_at": "2008-03-16T01:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2537#issuecomment-17271",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [real.patch](tarball://root/attachments/some-uuid/ticket2537/real.patch) by mabshoff created at 2008-03-16 01:11:42



---

archive/issue_comments_017272.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-03-16T01:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2537#issuecomment-17272",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Resolution: invalid



---

archive/issue_events_002718.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/cwitty",
    "created_at": "2008-03-16T01:32:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2537",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2537#event-2718"
}
```



---

archive/issue_comments_017273.json:
```json
{
    "body": "There is apparently no consensus on the meaning of frac() (see http://mathworld.wolfram.com/FractionalPart.html for some discussion of the issues and the different definitions).  Since Sage's RR is mostly a wrapper for MPFR, I would prefer to stay with the current definition (which also matches my intuition for what \"fractional part\" should mean); this is also the definition used by the majority of a statistically meaningless sampling from a google search.\n\nIf you feel strongly about the issue, I suggest taking it to sage-devel to get a broader sampling of opinions on the question.",
    "created_at": "2008-03-16T01:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2537#issuecomment-17273",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

There is apparently no consensus on the meaning of frac() (see http://mathworld.wolfram.com/FractionalPart.html for some discussion of the issues and the different definitions).  Since Sage's RR is mostly a wrapper for MPFR, I would prefer to stay with the current definition (which also matches my intuition for what "fractional part" should mean); this is also the definition used by the majority of a statistically meaningless sampling from a google search.

If you feel strongly about the issue, I suggest taking it to sage-devel to get a broader sampling of opinions on the question.
