# Issue 2798: probably easy-to-fix ptest issue

archive/issues_002798.json:
```json
{
    "body": "Assignee: gfurnish\n\n\n```\n09:56 < wstein> I just got this from ptest:\n09:56 -!- Irssi: Pasting 5 lines to #sage-devel. Press Ctrl-K if you wish to do this or Ctrl-C to cancel.\n09:56 < wstein>   File \"/Users/was/build/sage-2.10.4/local/bin/sage-ptest\", line 74, in run\n09:56 < wstein>     if e==-2:\n09:56 < wstein> UnboundLocalError: local variable 'e' referenced before assignment\n09:56 < wstein>  \n09:56 < wstein> but then it worked...\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2798\n\n",
    "created_at": "2008-04-04T16:57:05Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "probably easy-to-fix ptest issue",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2798",
    "user": "was"
}
```
Assignee: gfurnish


```
09:56 < wstein> I just got this from ptest:
09:56 -!- Irssi: Pasting 5 lines to #sage-devel. Press Ctrl-K if you wish to do this or Ctrl-C to cancel.
09:56 < wstein>   File "/Users/was/build/sage-2.10.4/local/bin/sage-ptest", line 74, in run
09:56 < wstein>     if e==-2:
09:56 < wstein> UnboundLocalError: local variable 'e' referenced before assignment
09:56 < wstein>  
09:56 < wstein> but then it worked...
```


Issue created by migration from https://trac.sagemath.org/ticket/2798





---

archive/issue_comments_019213.json:
```json
{
    "body": "Attachment [trac_2798.patch](tarball://root/attachments/some-uuid/ticket2798/trac_2798.patch) by gfurnish created at 2008-04-04 18:47:09",
    "created_at": "2008-04-04T18:47:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2798#issuecomment-19213",
    "user": "gfurnish"
}
```

Attachment [trac_2798.patch](tarball://root/attachments/some-uuid/ticket2798/trac_2798.patch) by gfurnish created at 2008-04-04 18:47:09



---

archive/issue_comments_019214.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-04T18:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2798#issuecomment-19214",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_019215.json:
```json
{
    "body": "Patch looks good to me. It doesn't really address the issue wstein encountered, but it will print a proper error message the next time somebody hits the bug that caused the problem in the first place. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-04T19:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2798#issuecomment-19215",
    "user": "mabshoff"
}
```

Patch looks good to me. It doesn't really address the issue wstein encountered, but it will print a proper error message the next time somebody hits the bug that caused the problem in the first place. Positive review.

Cheers,

Michael



---

archive/issue_comments_019216.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T19:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2798#issuecomment-19216",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019217.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-04T19:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2798#issuecomment-19217",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha1
