# Issue 4048: [with patch, positive review] missing minpoly for GF(p)

archive/issues_004048.json:
```json
{
    "body": "Assignee: @williamstein\n\nNick Alexander reports in https://groups.google.com/group/sage-devel/browse_thread/thread/e5538e40d2b89002\n\n```\nsage: GF(241^2, 'a')(1).minpoly() \nx + 240 \nsage: GF(241, 'a')(1).minpoly() \n--------------------------------------------------------------------------- \nAttributeError                            Traceback (most recent call   \nlast) \n... \nAttributeError: 'sage.rings.integer_mod.IntegerMod_int' object has no   \nattribute 'minpoly' \n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4048\n\n",
    "closed_at": "2009-01-24T17:13:57Z",
    "created_at": "2008-09-03T17:43:18Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, positive review] missing minpoly for GF(p)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4048",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

Nick Alexander reports in https://groups.google.com/group/sage-devel/browse_thread/thread/e5538e40d2b89002

```
sage: GF(241^2, 'a')(1).minpoly() 
x + 240 
sage: GF(241, 'a')(1).minpoly() 
--------------------------------------------------------------------------- 
AttributeError                            Traceback (most recent call   
last) 
... 
AttributeError: 'sage.rings.integer_mod.IntegerMod_int' object has no   
attribute 'minpoly' 
```



Issue created by migration from https://trac.sagemath.org/ticket/4048





---

archive/issue_comments_029132.json:
```json
{
    "body": "Attachment [trac_4048.patch](tarball://root/attachments/some-uuid/ticket4048/trac_4048.patch) by @aghitza created at 2009-01-22 01:21:29",
    "created_at": "2009-01-22T01:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4048#issuecomment-29132",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_4048.patch](tarball://root/attachments/some-uuid/ticket4048/trac_4048.patch) by @aghitza created at 2009-01-22 01:21:29



---

archive/issue_comments_029133.json:
```json
{
    "body": "See the attached patch.",
    "created_at": "2009-01-22T01:22:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4048#issuecomment-29133",
    "user": "https://github.com/aghitza"
}
```

See the attached patch.



---

archive/issue_comments_029134.json:
```json
{
    "body": "works for me",
    "created_at": "2009-01-23T10:51:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4048#issuecomment-29134",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

works for me



---

archive/issue_events_009247.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T17:13:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4048",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4048#event-9247"
}
```



---

archive/issue_events_009248.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T17:13:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4048",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4048#event-9248"
}
```



---

archive/issue_comments_029135.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T17:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4048#issuecomment-29135",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_comments_029136.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T17:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4048",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4048#issuecomment-29136",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
