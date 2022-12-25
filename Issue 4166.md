# Issue 4166: Separate resource for @interact

archive/issues_004166.json:
```json
{
    "body": "Assignee: @itolkov\n\nThere is a new resource for the initial evaluation and later updates.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4166\n\n",
    "created_at": "2008-09-22T02:15:26Z",
    "labels": [
        "component: interact"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Separate resource for @interact",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4166",
    "user": "https://github.com/itolkov"
}
```
Assignee: @itolkov

There is a new resource for the initial evaluation and later updates.

Issue created by migration from https://trac.sagemath.org/ticket/4166





---

archive/issue_comments_030187.json:
```json
{
    "body": "Attachment [trac4166_1.patch](tarball://root/attachments/some-uuid/ticket4166/trac4166_1.patch) by @williamstein created at 2008-09-24 22:49:02\n\nGood, works, but has one problem, which is that it creates a serious security vulnerability.  It needs code like this or something like in the Worksheet_eval Resource:\n\n```\n        if owner != '_sage_':\n            if W.owner() != self.username and not (self.username in W.collaborators()):\n               return InvalidPage(msg = \"can't evaluate worksheet cells\", username = self.username\\\n)\n```\n\n\nOnce this is resolved, it will get a positive review. \n\nIt might also be nice if there were a comment that explains why we are creating this new resource.  E.g., \"make code cleaner\"?  \"because it will be needed later for something else\nthat is planned?\"",
    "created_at": "2008-09-24T22:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4166#issuecomment-30187",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac4166_1.patch](tarball://root/attachments/some-uuid/ticket4166/trac4166_1.patch) by @williamstein created at 2008-09-24 22:49:02

Good, works, but has one problem, which is that it creates a serious security vulnerability.  It needs code like this or something like in the Worksheet_eval Resource:

```
        if owner != '_sage_':
            if W.owner() != self.username and not (self.username in W.collaborators()):
               return InvalidPage(msg = "can't evaluate worksheet cells", username = self.username\
)
```


Once this is resolved, it will get a positive review. 

It might also be nice if there were a comment that explains why we are creating this new resource.  E.g., "make code cleaner"?  "because it will be needed later for something else
that is planned?"



---

archive/issue_events_009462.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4166",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4166#event-9462"
}
```



---

archive/issue_events_009463.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4166",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4166#event-9463"
}
```



---

archive/issue_events_009464.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4166",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4166#event-9464"
}
```



---

archive/issue_events_009465.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4166",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4166#event-9465"
}
```



---

archive/issue_events_009466.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4166",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4166#event-9466"
}
```



---

archive/issue_events_009467.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4166",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4166#event-9467"
}
```



---

archive/issue_events_009468.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4166",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4166#event-9468"
}
```
