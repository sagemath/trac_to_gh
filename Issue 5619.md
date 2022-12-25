# Issue 5619: doctests for error messages in groebner_fan.py

archive/issues_005619.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  mhampton\n\nKeywords: groebner_fan.py, doctest\n\nThis is a follow-up to ticket #5465. Here, we add some doctests to check the error messages being raised.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5619\n\n",
    "created_at": "2009-03-27T02:48:38Z",
    "labels": [
        "component: geometry",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "doctests for error messages in groebner_fan.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5619",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mhampton

CC:  mhampton

Keywords: groebner_fan.py, doctest

This is a follow-up to ticket #5465. Here, we add some doctests to check the error messages being raised.

Issue created by migration from https://trac.sagemath.org/ticket/5619





---

archive/issue_comments_043796.json:
```json
{
    "body": "The patch **trac_5619-doctests.patch** adds two doctests to `groebner_fan.py`. The doctests check the error messages that can be raised by the functions `render()` and `render3d()`. Currently, these error messages are of the `NotImplementedError` type. This patch depends on ticket #5465.",
    "created_at": "2009-03-27T03:40:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5619#issuecomment-43796",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch **trac_5619-doctests.patch** adds two doctests to `groebner_fan.py`. The doctests check the error messages that can be raised by the functions `render()` and `render3d()`. Currently, these error messages are of the `NotImplementedError` type. This patch depends on ticket #5465.



---

archive/issue_comments_043797.json:
```json
{
    "body": "Attachment [trac_5619-doctests.patch](tarball://root/attachments/some-uuid/ticket5619/trac_5619-doctests.patch) by mhampton created at 2009-05-20 23:51:52\n\nThese make sense, and appear to work.  Positive review.",
    "created_at": "2009-05-20T23:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5619#issuecomment-43797",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_5619-doctests.patch](tarball://root/attachments/some-uuid/ticket5619/trac_5619-doctests.patch) by mhampton created at 2009-05-20 23:51:52

These make sense, and appear to work.  Positive review.



---

archive/issue_events_013224.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-21T00:31:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5619",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5619#event-13224"
}
```



---

archive/issue_events_013225.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-21T00:31:01Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5619",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5619#event-13225"
}
```



---

archive/issue_comments_043798.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-21T00:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5619#issuecomment-43798",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_043799.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-21T00:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5619#issuecomment-43799",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
