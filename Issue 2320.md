# Issue 2320: sage -server, sage -worker, sage -dsage broken

archive/issues_002320.json:
```json
{
    "body": "Assignee: @yqiang\n\nThese shorthands are broken right now because of changes to the dsage scripts. We need to either \n\n1) remove these shorthands\n2) fix them\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2320\n\n",
    "created_at": "2008-02-26T17:46:08Z",
    "labels": [
        "component: dsage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "sage -server, sage -worker, sage -dsage broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2320",
    "user": "https://github.com/yqiang"
}
```
Assignee: @yqiang

These shorthands are broken right now because of changes to the dsage scripts. We need to either 

1) remove these shorthands
2) fix them



Issue created by migration from https://trac.sagemath.org/ticket/2320





---

archive/issue_comments_015394.json:
```json
{
    "body": "patch for SAGE_ROOT/local/bin/sage-sage",
    "created_at": "2008-02-29T06:38:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15394",
    "user": "https://github.com/yqiang"
}
```

patch for SAGE_ROOT/local/bin/sage-sage



---

archive/issue_comments_015395.json:
```json
{
    "body": "Attachment [sage-sage.patch](tarball://root/attachments/some-uuid/ticket2320/sage-sage.patch) by @yqiang created at 2008-02-29 06:40:21\n\nI've attached the patch, after applying it make sure to chmod +x sage-dsage-*. This is against the hg_scripts repository.",
    "created_at": "2008-02-29T06:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15395",
    "user": "https://github.com/yqiang"
}
```

Attachment [sage-sage.patch](tarball://root/attachments/some-uuid/ticket2320/sage-sage.patch) by @yqiang created at 2008-02-29 06:40:21

I've attached the patch, after applying it make sure to chmod +x sage-dsage-*. This is against the hg_scripts repository.



---

archive/issue_comments_015396.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-29T06:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15396",
    "user": "https://github.com/yqiang"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015397.json:
```json
{
    "body": "Reassigning to William for review since he's the man behind sage-sage :-)",
    "created_at": "2008-03-02T01:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15397",
    "user": "https://github.com/yqiang"
}
```

Reassigning to William for review since he's the man behind sage-sage :-)



---

archive/issue_comments_015398.json:
```json
{
    "body": "Changing assignee from @yqiang to @williamstein.",
    "created_at": "2008-03-02T01:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15398",
    "user": "https://github.com/yqiang"
}
```

Changing assignee from @yqiang to @williamstein.



---

archive/issue_comments_015399.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-03-02T01:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15399",
    "user": "https://github.com/yqiang"
}
```

Changing status from assigned to new.



---

archive/issue_comments_015400.json:
```json
{
    "body": "> Reassigning to William for review since he's the man behind sage-sage :-)\n\nWhat are you talking about?  sage-sage is an incomprehensible disaster :-)\n\n -- William",
    "created_at": "2008-03-02T08:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15400",
    "user": "https://github.com/williamstein"
}
```

> Reassigning to William for review since he's the man behind sage-sage :-)

What are you talking about?  sage-sage is an incomprehensible disaster :-)

 -- William



---

archive/issue_comments_015401.json:
```json
{
    "body": "Patch looks good to me. Positive review. I assume I need to apply #2322 also to make this work.",
    "created_at": "2008-03-14T17:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15401",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. Positive review. I assume I need to apply #2322 also to make this work.



---

archive/issue_events_002496.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-14T17:41:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2320#event-2496"
}
```



---

archive/issue_comments_015402.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T17:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15402",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015403.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T17:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15403",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
