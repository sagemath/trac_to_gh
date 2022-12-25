# Issue 9357: Unhandled SIGFPE: in number_field_element_quadratic

archive/issues_009357.json:
```json
{
    "body": "Assignee: @aghitza\n\nKeywords: SIGFPE, ZeroDivisionError\n\n\n```\nsage: d=QQ[i](0)\nsage: ~d\n\n\n------------------------------------------------------------\nUnhandled SIGFPE: An unhandled floating point exception occurred in Sage.\nThis probably occurred because a *compiled* component\nof Sage has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate (sorry).\n------------------------------------------------------------\n\n```\n\n\nThe code dos not check if the element to be inverted is zero or not and does not handle the exception that ocurred in the c extension.\n\nThere is a trivial patch that checks if the input is zero or not. I am not sure if the sourronding code should have some _sig_on _sig_off to made it more robust. _sig_on _sig_off would avoid the sage crash but would raise a RunTime exception.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9357\n\n",
    "created_at": "2010-06-28T16:18:05Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Unhandled SIGFPE: in number_field_element_quadratic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9357",
    "user": "https://github.com/lftabera"
}
```
Assignee: @aghitza

Keywords: SIGFPE, ZeroDivisionError


```
sage: d=QQ[i](0)
sage: ~d


------------------------------------------------------------
Unhandled SIGFPE: An unhandled floating point exception occurred in Sage.
This probably occurred because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------

```


The code dos not check if the element to be inverted is zero or not and does not handle the exception that ocurred in the c extension.

There is a trivial patch that checks if the input is zero or not. I am not sure if the sourronding code should have some _sig_on _sig_off to made it more robust. _sig_on _sig_off would avoid the sage crash but would raise a RunTime exception.

Issue created by migration from https://trac.sagemath.org/ticket/9357





---

archive/issue_comments_088700.json:
```json
{
    "body": "Attachment [trac_9357.patch](tarball://root/attachments/some-uuid/ticket9357/trac_9357.patch) by @lftabera created at 2010-06-28 16:45:24",
    "created_at": "2010-06-28T16:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9357#issuecomment-88700",
    "user": "https://github.com/lftabera"
}
```

Attachment [trac_9357.patch](tarball://root/attachments/some-uuid/ticket9357/trac_9357.patch) by @lftabera created at 2010-06-28 16:45:24



---

archive/issue_comments_088701.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-30T07:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9357#issuecomment-88701",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088702.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-30T07:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9357#issuecomment-88702",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_023088.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-20T09:31:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9357",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9357#event-23088"
}
```



---

archive/issue_comments_088703.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T09:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9357#issuecomment-88703",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
