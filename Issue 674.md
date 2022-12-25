# Issue 674: Solaris 10: sympow is broken

archive/issues_000674.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  drkirkby\n\nKeywords: Solaris 10, sympow\n\n\n```\n-bash-3.00$ sympow\nsympow 1.018 RELEASE  (c) Mark Watkins -**ERROR** QD_check failed at x[1]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/674\n\n",
    "created_at": "2007-09-17T00:36:38Z",
    "labels": [
        "component: packages",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Solaris 10: sympow is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/674",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: somebody

CC:  drkirkby

Keywords: Solaris 10, sympow


```
-bash-3.00$ sympow
sympow 1.018 RELEASE  (c) Mark Watkins -**ERROR** QD_check failed at x[1]
```


Issue created by migration from https://trac.sagemath.org/ticket/674





---

archive/issue_comments_003478.json:
```json
{
    "body": "I have a fixed Sympow build that passes doctests now on Solaris 10.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-15T06:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/674#issuecomment-3478",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I have a fixed Sympow build that passes doctests now on Solaris 10.

Cheers,

Michael



---

archive/issue_comments_003479.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-15T06:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/674#issuecomment-3479",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003480.json:
```json
{
    "body": "Changing assignee from somebody to mabshoff.",
    "created_at": "2009-01-15T06:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/674#issuecomment-3480",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from somebody to mabshoff.



---

archive/issue_comments_003481.json:
```json
{
    "body": "Changing component from packages to solaris.",
    "created_at": "2009-01-15T06:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/674#issuecomment-3481",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from packages to solaris.



---

archive/issue_comments_003482.json:
```json
{
    "body": "I'm cc:ing Dr. Kirkby on this since he is likely to have a way to test this easily.  Unfortunately, it seems this fix - whatever it was - was never integrated.",
    "created_at": "2009-12-30T04:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/674#issuecomment-3482",
    "user": "https://github.com/kcrisman"
}
```

I'm cc:ing Dr. Kirkby on this since he is likely to have a way to test this easily.  Unfortunately, it seems this fix - whatever it was - was never integrated.



---

archive/issue_comments_003483.json:
```json
{
    "body": "If the subject lines is to believed, then this was Solaris 10 x86. I do not have such a system. I've got Open Solaris (Solaris 11) on x86 and Solaris 10 on SPARC. But I do not have any Solaris 10 x86 system. I could install Solaris 10 on a virtual machine, but I don't have it running just now and would rather concentrate on Solaris 11 (Open Solaris). \n\nI'm not getting any doctest failures with the name *sympow* in them. I know nothing about this package, but I do not see anything obviously wrong on Solaris 10 SPARC. \n\n\n```\nkirkby@t2:[~/sage-4.3] $ ./sage -sh\n\nStarting subshell with Sage environment variables set.\nBe sure to exit when you are done and do not do anything\nwith other copies of Sage!\n\nBypassing shell configuration files ...\n\n/rootpool2/local/kirkby/sage-4.3\nsage subshell$ sympow\nsympow 1.018 RELEASE  (c) Mark Watkins --- see README and COPYING for details\n```\n\n\nThere is a copy of Sage 4.3 at /rootpool2/local/kirkby/sage-4.3 on 't2'. If you are able to test that there, it would be helpful, but I do not see the obvious crash. But x86 could be a different matter of course. \n\ndave",
    "created_at": "2009-12-30T15:01:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/674#issuecomment-3483",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

If the subject lines is to believed, then this was Solaris 10 x86. I do not have such a system. I've got Open Solaris (Solaris 11) on x86 and Solaris 10 on SPARC. But I do not have any Solaris 10 x86 system. I could install Solaris 10 on a virtual machine, but I don't have it running just now and would rather concentrate on Solaris 11 (Open Solaris). 

I'm not getting any doctest failures with the name *sympow* in them. I know nothing about this package, but I do not see anything obviously wrong on Solaris 10 SPARC. 


```
kirkby@t2:[~/sage-4.3] $ ./sage -sh

Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!

Bypassing shell configuration files ...

/rootpool2/local/kirkby/sage-4.3
sage subshell$ sympow
sympow 1.018 RELEASE  (c) Mark Watkins --- see README and COPYING for details
```


There is a copy of Sage 4.3 at /rootpool2/local/kirkby/sage-4.3 on 't2'. If you are able to test that there, it would be helpful, but I do not see the obvious crash. But x86 could be a different matter of course. 

dave



---

archive/issue_comments_003484.json:
```json
{
    "body": "Closed due to #9703",
    "created_at": "2010-08-26T20:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/674#issuecomment-3484",
    "user": "https://github.com/mwhansen"
}
```

Closed due to #9703



---

archive/issue_comments_003485.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-08-26T20:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/674#issuecomment-3485",
    "user": "https://github.com/mwhansen"
}
```

Resolution: duplicate



---

archive/issue_events_000742.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-08-26T20:35:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/674",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/674#event-742"
}
```



---

archive/issue_comments_003486.json:
```json
{
    "body": "Thank you for closing this Mike. It's nice to know I fixed a 3-year old bug!\n\nDave",
    "created_at": "2010-08-26T21:14:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/674#issuecomment-3486",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Thank you for closing this Mike. It's nice to know I fixed a 3-year old bug!

Dave



---

archive/issue_comments_003487.json:
```json
{
    "body": ":-)",
    "created_at": "2010-08-26T21:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/674#issuecomment-3487",
    "user": "https://github.com/mwhansen"
}
```

:-)
