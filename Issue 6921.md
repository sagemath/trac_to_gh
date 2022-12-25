# Issue 6921: MATLAB crashes on Snow Leopard due to library conflicts

archive/issues_006921.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhen using the MATLAB interface in Sage MATLAB crashes on startup. This is due to library conflicts with Sage.\n\nI have created a (minor) patch to use sage-native-execute when starting MATLAB. This fixes the problems on my machine (OS X 10.6) and the interface now passes all doctests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6921\n\n",
    "created_at": "2009-09-11T04:28:16Z",
    "labels": [
        "component: interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "MATLAB crashes on Snow Leopard due to library conflicts",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6921",
    "user": "https://trac.sagemath.org/admin/accounts/users/jjh"
}
```
Assignee: @williamstein

When using the MATLAB interface in Sage MATLAB crashes on startup. This is due to library conflicts with Sage.

I have created a (minor) patch to use sage-native-execute when starting MATLAB. This fixes the problems on my machine (OS X 10.6) and the interface now passes all doctests.

Issue created by migration from https://trac.sagemath.org/ticket/6921





---

archive/issue_comments_057025.json:
```json
{
    "body": "Attachment [matlab-native-execute.patch](tarball://root/attachments/some-uuid/ticket6921/matlab-native-execute.patch) by jjh created at 2009-09-11 04:33:51",
    "created_at": "2009-09-11T04:33:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6921#issuecomment-57025",
    "user": "https://trac.sagemath.org/admin/accounts/users/jjh"
}
```

Attachment [matlab-native-execute.patch](tarball://root/attachments/some-uuid/ticket6921/matlab-native-execute.patch) by jjh created at 2009-09-11 04:33:51



---

archive/issue_comments_057026.json:
```json
{
    "body": "I can't test the exact setup, but in all cases using sage-native-execute is a good idea, and this does work on Linux, so positive review.",
    "created_at": "2009-09-22T14:49:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6921#issuecomment-57026",
    "user": "https://github.com/williamstein"
}
```

I can't test the exact setup, but in all cases using sage-native-execute is a good idea, and this does work on Linux, so positive review.



---

archive/issue_events_016253.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-23T06:36:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6921",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6921#event-16253"
}
```



---

archive/issue_comments_057027.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-23T06:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6921#issuecomment-57027",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_016254.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-23T06:36:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6921",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6921#event-16254"
}
```



---

archive/issue_comments_057028.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T09:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6921#issuecomment-57028",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
