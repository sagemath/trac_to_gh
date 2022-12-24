# Issue 5972: [with patch; needs review] segfault in degenerate matrix multiply

archive/issues_005972.json:
```json
{
    "body": "Assignee: was\n\nOUCH:\n\n\n```\nwstein@sage:~$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nmatrix(QQ,2,0)sage: matrix(QQ,2,0)*matrix(QQ,0,2)\n| Sage Version 3.4.1, Release Date: 2009-04-21                       |\n| Type notebook() for the GUI, and license() for information.        |\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5972\n\n",
    "created_at": "2009-05-04T03:45:14Z",
    "labels": [
        "linear algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "[with patch; needs review] segfault in degenerate matrix multiply",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5972",
    "user": "was"
}
```
Assignee: was

OUCH:


```
wstein@sage:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
matrix(QQ,2,0)sage: matrix(QQ,2,0)*matrix(QQ,0,2)
| Sage Version 3.4.1, Release Date: 2009-04-21                       |
| Type notebook() for the GUI, and license() for information.        |

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

```


Issue created by migration from https://trac.sagemath.org/ticket/5972





---

archive/issue_comments_047364.json:
```json
{
    "body": "Attachment [trac_5972.patch](tarball://root/attachments/some-uuid/ticket5972/trac_5972.patch) by mabshoff created at 2009-05-04 04:05:05\n\nWilliam's patch rebased",
    "created_at": "2009-05-04T04:05:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5972#issuecomment-47364",
    "user": "mabshoff"
}
```

Attachment [trac_5972.patch](tarball://root/attachments/some-uuid/ticket5972/trac_5972.patch) by mabshoff created at 2009-05-04 04:05:05

William's patch rebased



---

archive/issue_comments_047365.json:
```json
{
    "body": "Nice catch.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T04:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5972#issuecomment-47365",
    "user": "mabshoff"
}
```

Nice catch.

Cheers,

Michael



---

archive/issue_comments_047366.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-04T04:19:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5972#issuecomment-47366",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_047367.json:
```json
{
    "body": "Merged in Sage 3.4.2.final.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T04:19:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5972#issuecomment-47367",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.final.

Cheers,

Michael



---

archive/issue_comments_047368.json:
```json
{
    "body": "the rebased patch michael posted doesn't work for me on 3.4.2.rc0, but this patch does, so I'm posting it.",
    "created_at": "2009-05-04T13:45:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5972#issuecomment-47368",
    "user": "was"
}
```

the rebased patch michael posted doesn't work for me on 3.4.2.rc0, but this patch does, so I'm posting it.
