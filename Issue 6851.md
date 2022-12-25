# Issue 6851: hashes for derivatives of symbolic functions still collide

archive/issues_006851.json:
```json
{
    "body": "Assignee: @burcin\n\nIt seems that #6243 didn't fix things properly:\n\n```\nThanks to those who worked on closing ticket 6243 regarding\nderivatives as dictionary keys for the release of Sage 4.1.1.  It\nappears that there's still a bug, though (see below).\n\nAlex\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: f= function('f',x)\nsage: d= {}\nsage: for i in [1..5]:\n....:     print diff(f,x,i)\n....:     d[diff(f,x,i)] = i\n....:\nD[0](f)(x)\nD[0, 0](f)(x)\n<boom>\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6851\n\n",
    "created_at": "2009-08-31T12:02:12Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "hashes for derivatives of symbolic functions still collide",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6851",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

It seems that #6243 didn't fix things properly:

```
Thanks to those who worked on closing ticket 6243 regarding
derivatives as dictionary keys for the release of Sage 4.1.1.  It
appears that there's still a bug, though (see below).

Alex

----------------------------------------------------------------------
----------------------------------------------------------------------
sage: f= function('f',x)
sage: d= {}
sage: for i in [1..5]:
....:     print diff(f,x,i)
....:     d[diff(f,x,i)] = i
....:
D[0](f)(x)
D[0, 0](f)(x)
<boom>
```

Issue created by migration from https://trac.sagemath.org/ticket/6851





---

archive/issue_comments_056391.json:
```json
{
    "body": "Attachment [trac_6851-fderivative_hash_collision.patch](tarball://root/attachments/some-uuid/ticket6851/trac_6851-fderivative_hash_collision.patch) by @burcin created at 2009-09-19 15:14:23\n\nI hope I have the right fix in pynac this time. attachment:trac_6851-fderivative_hash_collision.patch contains doctests for Sage.\n\nI will post a new pynac package and review instructions soon.",
    "created_at": "2009-09-19T15:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6851#issuecomment-56391",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_6851-fderivative_hash_collision.patch](tarball://root/attachments/some-uuid/ticket6851/trac_6851-fderivative_hash_collision.patch) by @burcin created at 2009-09-19 15:14:23

I hope I have the right fix in pynac this time. attachment:trac_6851-fderivative_hash_collision.patch contains doctests for Sage.

I will post a new pynac package and review instructions soon.



---

archive/issue_comments_056392.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-19T15:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6851#issuecomment-56392",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_056393.json:
```json
{
    "body": "New pynac package available at #6993.",
    "created_at": "2009-09-22T19:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6851#issuecomment-56393",
    "user": "https://github.com/burcin"
}
```

New pynac package available at #6993.



---

archive/issue_comments_056394.json:
```json
{
    "body": "This works fine.  Positive review, pending of course review of the package.",
    "created_at": "2009-09-23T19:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6851#issuecomment-56394",
    "user": "https://github.com/kcrisman"
}
```

This works fine.  Positive review, pending of course review of the package.



---

archive/issue_comments_056395.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-25T22:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6851#issuecomment-56395",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_016122.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-25T22:45:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6851",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6851#event-16122"
}
```



---

archive/issue_comments_056396.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6851#issuecomment-56396",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
