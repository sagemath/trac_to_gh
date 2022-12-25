# Issue 6622: substitution of a dict into a symbolic expression modifies the dict

archive/issues_006622.json:
```json
{
    "body": "Assignee: @burcin\n\n\n```\nsage: var('v t')\nsage: f = v*t\nsage: D = {v: 2}\nsage: f(D, t=3)\n6\nsage: D\n{v: 2, t: 3}\n```\n\n\nAfter the call above, D should *not* be changed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6622\n\n",
    "created_at": "2009-07-25T20:05:50Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "substitution of a dict into a symbolic expression modifies the dict",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6622",
    "user": "https://github.com/williamstein"
}
```
Assignee: @burcin


```
sage: var('v t')
sage: f = v*t
sage: D = {v: 2}
sage: f(D, t=3)
6
sage: D
{v: 2, t: 3}
```


After the call above, D should *not* be changed.

Issue created by migration from https://trac.sagemath.org/ticket/6622





---

archive/issue_comments_054156.json:
```json
{
    "body": "Here's how to workaround it (namely, put \"dict(constants)\" instead of \"constants\").  In the code for __call__ or subs, something similar should be done. \n\n\n```\nsage: var('v t')\nsage: f = v*t\nsage: s = {v: 2}\nsage: f(dict(s), t=3)\n6\nsage: s\n{v: 2}\n```\n",
    "created_at": "2009-07-25T20:07:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6622#issuecomment-54156",
    "user": "https://github.com/williamstein"
}
```

Here's how to workaround it (namely, put "dict(constants)" instead of "constants").  In the code for __call__ or subs, something similar should be done. 


```
sage: var('v t')
sage: f = v*t
sage: s = {v: 2}
sage: f(dict(s), t=3)
6
sage: s
{v: 2}
```




---

archive/issue_comments_054157.json:
```json
{
    "body": "Attachment [trac_6622.patch](tarball://root/attachments/some-uuid/ticket6622/trac_6622.patch) by wcauchois created at 2009-07-29 00:44:15\n\nbased on sage 4.1.1.alpha1",
    "created_at": "2009-07-29T00:44:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6622#issuecomment-54157",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Attachment [trac_6622.patch](tarball://root/attachments/some-uuid/ticket6622/trac_6622.patch) by wcauchois created at 2009-07-29 00:44:15

based on sage 4.1.1.alpha1



---

archive/issue_comments_054158.json:
```json
{
    "body": "This was a simple fix.",
    "created_at": "2009-07-29T00:44:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6622#issuecomment-54158",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

This was a simple fix.



---

archive/issue_events_006862.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-08-03T06:34:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6622",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6622#event-6862"
}
```



---

archive/issue_comments_054159.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-03T06:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6622#issuecomment-54159",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
