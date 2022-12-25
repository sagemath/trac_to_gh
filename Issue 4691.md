# Issue 4691: Minor docstring change for timeout on notebook

archive/issues_004691.json:
```json
{
    "body": "Assignee: boothby\n\nFrom sage-support:\n\n> > c) could easily. Did you set the timeout parameter for the server? \n> >       timeout       -- (default: 0) seconds until idle worksheet sessions \n> >                              automatically timeout, i.e., the corresponding \n> >                              Sage session terminates.  0 means 'never timeout'. \n\n> That seems to have been the other main problem, and we fixed it. \n\n\nCare to open a ticket to update the docstring? I think it would be \ngood to mention that on low memory systems one should set some timeout \nsince otherwise Sage will gobble up all available memory if there are \nmany users. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4691\n\n",
    "created_at": "2008-12-04T01:38:59Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "Minor docstring change for timeout on notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4691",
    "user": "https://github.com/kcrisman"
}
```
Assignee: boothby

From sage-support:

> > c) could easily. Did you set the timeout parameter for the server? 
> >       timeout       -- (default: 0) seconds until idle worksheet sessions 
> >                              automatically timeout, i.e., the corresponding 
> >                              Sage session terminates.  0 means 'never timeout'. 

> That seems to have been the other main problem, and we fixed it. 


Care to open a ticket to update the docstring? I think it would be 
good to mention that on low memory systems one should set some timeout 
since otherwise Sage will gobble up all available memory if there are 
many users. 


Issue created by migration from https://trac.sagemath.org/ticket/4691





---

archive/issue_comments_035290.json:
```json
{
    "body": "Attachment [sage_trac_4691.patch](tarball://root/attachments/some-uuid/ticket4691/sage_trac_4691.patch) by @dandrake created at 2008-12-04 05:34:58",
    "created_at": "2008-12-04T05:34:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4691#issuecomment-35290",
    "user": "https://github.com/dandrake"
}
```

Attachment [sage_trac_4691.patch](tarball://root/attachments/some-uuid/ticket4691/sage_trac_4691.patch) by @dandrake created at 2008-12-04 05:34:58



---

archive/issue_comments_035291.json:
```json
{
    "body": "Patch uploaded. I also edited http://wiki.sagemath.org/StartingTheNotebook .",
    "created_at": "2008-12-04T05:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4691#issuecomment-35291",
    "user": "https://github.com/dandrake"
}
```

Patch uploaded. I also edited http://wiki.sagemath.org/StartingTheNotebook .



---

archive/issue_comments_035292.json:
```json
{
    "body": "Thanks, Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-04T08:24:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4691#issuecomment-35292",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Thanks, Positive review.

Cheers,

Michael



---

archive/issue_comments_035293.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha0",
    "created_at": "2008-12-04T14:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4691#issuecomment-35293",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.alpha0



---

archive/issue_comments_035294.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-04T14:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4691#issuecomment-35294",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004937.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-12-04T14:10:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4691",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4691#event-4937"
}
```
