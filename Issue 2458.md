# Issue 2458: bug in linbox's spkg-install: ${SAGE_LCOAL}

archive/issues_002458.json:
```json
{
    "body": "Assignee: mabshoff\n\nFrancois noted in http://groups.google.com/group/sage-devel/browse_thread/thread/4a902c07ebb7c45d that\n\n```\nIn linbox in the spkg-install file on line 41 we have an interesting\nreference to ${SAGE_LCOAL}. \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2458\n\n",
    "created_at": "2008-03-10T14:47:59Z",
    "labels": [
        "component: linbox",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "bug in linbox's spkg-install: ${SAGE_LCOAL}",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2458",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Francois noted in http://groups.google.com/group/sage-devel/browse_thread/thread/4a902c07ebb7c45d that

```
In linbox in the spkg-install file on line 41 we have an interesting
reference to ${SAGE_LCOAL}. 
```


Issue created by migration from https://trac.sagemath.org/ticket/2458





---

archive/issue_comments_016609.json:
```json
{
    "body": "An updated spkg which removes that elif case (since it is useless and leads to potential misdetection) can be found at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.3/rc4/linbox-1.1.5rc2.p2.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-03-10T14:53:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2458#issuecomment-16609",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

An updated spkg which removes that elif case (since it is useless and leads to potential misdetection) can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.3/rc4/linbox-1.1.5rc2.p2.spkg

Cheers,

Michael



---

archive/issue_comments_016610.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-10T14:53:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2458#issuecomment-16610",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016611.json:
```json
{
    "body": "Looks good to me, in that nothing new that is bad is introduced and it fixes the typo.  Of course I'm not saying linbox*spkg is perfect...",
    "created_at": "2008-03-10T15:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2458#issuecomment-16611",
    "user": "https://github.com/williamstein"
}
```

Looks good to me, in that nothing new that is bad is introduced and it fixes the typo.  Of course I'm not saying linbox*spkg is perfect...



---

archive/issue_comments_016612.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-10T17:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2458#issuecomment-16612",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016613.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc4",
    "created_at": "2008-03-10T17:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2458#issuecomment-16613",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc4



---

archive/issue_events_005793.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-10T17:17:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2458",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2458#event-5793"
}
```
