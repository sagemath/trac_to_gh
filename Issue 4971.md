# Issue 4971: make get_memory_usage() return a float on all platforms

archive/issues_004971.json:
```json
{
    "body": "Assignee: cwitty\n\nFrom http://groups.google.com/group/sage-support/t/58b8f491e4906f71\n\n```\nIf you know the limitations of get_memory_usage() you can work \naround them. Case in point from 3.2.3 right after startup: \n\n64 bit linux, i.e. sage.math: \nsage: get_memory_usage() \n668.32421875 \n---- \n32 bit OSX 10.5: \nsage: get_memory_usage() \n'131M+' \n---- \n64 bit OSX 10.5: \nsage: get_memory_usage() \n'171M+' \n--- \n32 bit Solaris/Sparc: \nsage: get_memory_usage() \n'81M' \n\nWhile there should be a difference between 32 and 64 bit, i.e 64 bit \ncode is larger and consumes more memory, the result from Linux is not \neven close to the truth, i.e. I don't think 32 bit Solaris is roughly \na magnitude more efficient than 64 bit Linux. \nEither way, the result of get_memory_usage() should be consistent \nacross platforms and not return a string in some cases and something \nelse on Linux. It should be a float of the memory used in MB. \n```\nWilliam then replied:\n\n```\n+1  Create a trac ticket.  This will be an easy point for the \n\"fix-the-most-trac-bugs-in-sage contest we're having next week. \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4971\n\n",
    "created_at": "2009-01-14T02:01:27Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "make get_memory_usage() return a float on all platforms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4971",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: cwitty

From http://groups.google.com/group/sage-support/t/58b8f491e4906f71

```
If you know the limitations of get_memory_usage() you can work 
around them. Case in point from 3.2.3 right after startup: 

64 bit linux, i.e. sage.math: 
sage: get_memory_usage() 
668.32421875 
---- 
32 bit OSX 10.5: 
sage: get_memory_usage() 
'131M+' 
---- 
64 bit OSX 10.5: 
sage: get_memory_usage() 
'171M+' 
--- 
32 bit Solaris/Sparc: 
sage: get_memory_usage() 
'81M' 

While there should be a difference between 32 and 64 bit, i.e 64 bit 
code is larger and consumes more memory, the result from Linux is not 
even close to the truth, i.e. I don't think 32 bit Solaris is roughly 
a magnitude more efficient than 64 bit Linux. 
Either way, the result of get_memory_usage() should be consistent 
across platforms and not return a string in some cases and something 
else on Linux. It should be a float of the memory used in MB. 
```
William then replied:

```
+1  Create a trac ticket.  This will be an easy point for the 
"fix-the-most-trac-bugs-in-sage contest we're having next week. 
```

Issue created by migration from https://trac.sagemath.org/ticket/4971





---

archive/issue_comments_037786.json:
```json
{
    "body": "Attachment [trac_4971.patch](tarball://root/attachments/some-uuid/ticket4971/trac_4971.patch) by @williamstein created at 2009-01-24 16:05:41",
    "created_at": "2009-01-24T16:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4971#issuecomment-37786",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_4971.patch](tarball://root/attachments/some-uuid/ticket4971/trac_4971.patch) by @williamstein created at 2009-01-24 16:05:41



---

archive/issue_comments_037787.json:
```json
{
    "body": "Nice. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T16:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4971#issuecomment-37787",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nice. Positive review.

Cheers,

Michael



---

archive/issue_events_011499.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T17:14:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4971",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4971#event-11499"
}
```



---

archive/issue_comments_037788.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T17:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4971#issuecomment-37788",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_comments_037789.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T17:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4971#issuecomment-37789",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
