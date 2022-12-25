# Issue 2293: [with patch at #2292, positive review] word_problem error in AbelianGroup

archive/issues_002293.json:
```json
{
    "body": "Assignee: joyner\n\n```\nsage: sage: A.<a,b,c,d,e> = AbelianGroup(5,[4, 5, 5, 7, 8])\nsage: wp = word_problem([a,b,c,d,e],a); wp\n[[a, 1]]\n```\nis okay but all these are wrong:\n\n```\nsage: wp = word_problem([a,b,c,d,e],b); wp\n[[a, 1]]\nsage: wp = word_problem([a,b,c,d,e],c); wp\n[[a, 1]]\nsage: wp = word_problem([a,b,c,d,e],d); wp\n[[a, 1]]\nsage: wp = word_problem([a,b,c,d,e],e); wp\n[[a, 1]]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2293\n\n",
    "closed_at": "2008-02-27T23:10:18Z",
    "created_at": "2008-02-24T15:33:04Z",
    "labels": [
        "component: group theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[with patch at #2292, positive review] word_problem error in AbelianGroup",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2293",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: joyner

```
sage: sage: A.<a,b,c,d,e> = AbelianGroup(5,[4, 5, 5, 7, 8])
sage: wp = word_problem([a,b,c,d,e],a); wp
[[a, 1]]
```
is okay but all these are wrong:

```
sage: wp = word_problem([a,b,c,d,e],b); wp
[[a, 1]]
sage: wp = word_problem([a,b,c,d,e],c); wp
[[a, 1]]
sage: wp = word_problem([a,b,c,d,e],d); wp
[[a, 1]]
sage: wp = word_problem([a,b,c,d,e],e); wp
[[a, 1]]
```


Issue created by migration from https://trac.sagemath.org/ticket/2293





---

archive/issue_comments_015180.json:
```json
{
    "body": "Please see\nhttp://trac.sagemath.org/sage_trac/ticket/2292\nfor the patch.",
    "created_at": "2008-02-24T18:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2293#issuecomment-15180",
    "user": "https://github.com/wdjoyner"
}
```

Please see
http://trac.sagemath.org/sage_trac/ticket/2292
for the patch.



---

archive/issue_events_005414.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-24T19:08:34Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2293",
    "milestone": "sage-2.10.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2293#event-5414"
}
```



---

archive/issue_comments_015181.json:
```json
{
    "body": "The patch for #2292 fixes this.",
    "created_at": "2008-02-27T22:20:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2293#issuecomment-15181",
    "user": "https://github.com/mwhansen"
}
```

The patch for #2292 fixes this.



---

archive/issue_comments_015182.json:
```json
{
    "body": "Fixed due to the patch at #2292 merged in Sage 2.10.3.rc0",
    "created_at": "2008-02-27T23:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2293#issuecomment-15182",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed due to the patch at #2292 merged in Sage 2.10.3.rc0



---

archive/issue_comments_015183.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-27T23:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2293#issuecomment-15183",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005415.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-27T23:10:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2293",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2293#event-5415"
}
```
