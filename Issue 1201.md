# Issue 1201: add gramm-schmidt to sage

archive/issues_001201.json:
```json
{
    "body": "Assignee: was*\n\nAdd function to do gramm schmidt orthogonalization and also to verify the LLL criterion to Sage.\n\nNOTE: I have mostly done this.  This trac is just so I have a place to submit a patch.  So you shouldn't do this :-).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1201\n\n",
    "created_at": "2007-11-18T21:50:48Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "add gramm-schmidt to sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1201",
    "user": "https://github.com/williamstein"
}
```
Assignee: was*

Add function to do gramm schmidt orthogonalization and also to verify the LLL criterion to Sage.

NOTE: I have mostly done this.  This trac is just so I have a place to submit a patch.  So you shouldn't do this :-).


Issue created by migration from https://trac.sagemath.org/ticket/1201





---

archive/issue_comments_007418.json:
```json
{
    "body": "Attachment [trac1201.patch](tarball://root/attachments/some-uuid/ticket1201/trac1201.patch) by @williamstein created at 2007-11-19 03:35:53",
    "created_at": "2007-11-19T03:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1201#issuecomment-7418",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac1201.patch](tarball://root/attachments/some-uuid/ticket1201/trac1201.patch) by @williamstein created at 2007-11-19 03:35:53



---

archive/issue_comments_007419.json:
```json
{
    "body": "NOTE -- this is a generic implementation.  There is surely a vastly faster implementation in the case of an RDF or CDF base field (by calling to numpy).",
    "created_at": "2007-11-19T03:38:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1201#issuecomment-7419",
    "user": "https://github.com/williamstein"
}
```

NOTE -- this is a generic implementation.  There is surely a vastly faster implementation in the case of an RDF or CDF base field (by calling to numpy).



---

archive/issue_comments_007420.json:
```json
{
    "body": "From David Joyner:\n\n```\nI looked at it but can't figure out how to apply it to a cloned version\nof SAGE. It seems to make sense but I'd like to test it out.\nSorry for the delay. I had a final to type up and lots of grading.\n```",
    "created_at": "2007-11-21T12:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1201#issuecomment-7420",
    "user": "https://github.com/williamstein"
}
```

From David Joyner:

```
I looked at it but can't figure out how to apply it to a cloned version
of SAGE. It seems to make sense but I'd like to test it out.
Sorry for the delay. I had a final to type up and lots of grading.
```



---

archive/issue_events_003201.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-11-26T06:37:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1201",
    "milestone": "sage-2.8.15",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1201#event-3201"
}
```



---

archive/issue_comments_007421.json:
```json
{
    "body": "also apply this patch (after the first)",
    "created_at": "2007-11-26T06:40:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1201#issuecomment-7421",
    "user": "https://github.com/williamstein"
}
```

also apply this patch (after the first)



---

archive/issue_comments_007422.json:
```json
{
    "body": "Attachment [7421.patch](tarball://root/attachments/some-uuid/ticket1201/7421.patch) by @mwhansen created at 2007-12-01 17:12:17",
    "created_at": "2007-12-01T17:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1201#issuecomment-7422",
    "user": "https://github.com/mwhansen"
}
```

Attachment [7421.patch](tarball://root/attachments/some-uuid/ticket1201/7421.patch) by @mwhansen created at 2007-12-01 17:12:17



---

archive/issue_comments_007423.json:
```json
{
    "body": "I think this can go in.",
    "created_at": "2007-12-02T05:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1201#issuecomment-7423",
    "user": "https://github.com/mwhansen"
}
```

I think this can go in.



---

archive/issue_events_003202.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-02T05:54:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1201",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1201#event-3202"
}
```



---

archive/issue_comments_007424.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T05:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1201#issuecomment-7424",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007425.json:
```json
{
    "body": "Merged in 2.8.15.alpha2.",
    "created_at": "2007-12-02T05:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1201#issuecomment-7425",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.alpha2.
