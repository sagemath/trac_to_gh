# Issue 2320: sage -server, sage -worker, sage -dsage broken

archive/issues_002320.json:
```json
{
    "body": "Assignee: yi\n\nThese shorthands are broken right now because of changes to the dsage scripts. We need to either \n\n1) remove these shorthands\n2) fix them\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2320\n\n",
    "created_at": "2008-02-26T17:46:08Z",
    "labels": [
        "dsage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "sage -server, sage -worker, sage -dsage broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2320",
    "user": "yi"
}
```
Assignee: yi

These shorthands are broken right now because of changes to the dsage scripts. We need to either 

1) remove these shorthands
2) fix them



Issue created by migration from https://trac.sagemath.org/ticket/2320





---

archive/issue_comments_015428.json:
```json
{
    "body": "patch for SAGE_ROOT/local/bin/sage-sage",
    "created_at": "2008-02-29T06:38:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15428",
    "user": "yi"
}
```

patch for SAGE_ROOT/local/bin/sage-sage



---

archive/issue_comments_015429.json:
```json
{
    "body": "Attachment [sage-sage.patch](tarball://root/attachments/some-uuid/ticket2320/sage-sage.patch) by yi created at 2008-02-29 06:40:21\n\nI've attached the patch, after applying it make sure to chmod +x sage-dsage-*. This is against the hg_scripts repository.",
    "created_at": "2008-02-29T06:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15429",
    "user": "yi"
}
```

Attachment [sage-sage.patch](tarball://root/attachments/some-uuid/ticket2320/sage-sage.patch) by yi created at 2008-02-29 06:40:21

I've attached the patch, after applying it make sure to chmod +x sage-dsage-*. This is against the hg_scripts repository.



---

archive/issue_comments_015430.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-29T06:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15430",
    "user": "yi"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015431.json:
```json
{
    "body": "Reassigning to William for review since he's the man behind sage-sage :-)",
    "created_at": "2008-03-02T01:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15431",
    "user": "yi"
}
```

Reassigning to William for review since he's the man behind sage-sage :-)



---

archive/issue_comments_015432.json:
```json
{
    "body": "Changing assignee from yi to was.",
    "created_at": "2008-03-02T01:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15432",
    "user": "yi"
}
```

Changing assignee from yi to was.



---

archive/issue_comments_015433.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-03-02T01:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15433",
    "user": "yi"
}
```

Changing status from assigned to new.



---

archive/issue_comments_015434.json:
```json
{
    "body": "> Reassigning to William for review since he's the man behind sage-sage :-)\n\nWhat are you talking about?  sage-sage is an incomprehensible disaster :-)\n\n -- William",
    "created_at": "2008-03-02T08:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15434",
    "user": "was"
}
```

> Reassigning to William for review since he's the man behind sage-sage :-)

What are you talking about?  sage-sage is an incomprehensible disaster :-)

 -- William



---

archive/issue_comments_015435.json:
```json
{
    "body": "Patch looks good to me. Positive review. I assume I need to apply #2322 also to make this work.",
    "created_at": "2008-03-14T17:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15435",
    "user": "mabshoff"
}
```

Patch looks good to me. Positive review. I assume I need to apply #2322 also to make this work.



---

archive/issue_comments_015436.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T17:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15436",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015437.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T17:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2320#issuecomment-15437",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
