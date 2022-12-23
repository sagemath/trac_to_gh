# Issue 3243: [with patch; needs review] cygwin -- get it to work on cygwin

archive/issues_003243.json:
```json
{
    "body": "Assignee: mabshoff\n\nWrap log2 in a function so it will work in cygwin.  In cygwin log2 is a macro:\n\n```\nsh-3.2$ grep log2 *.h\nmath.h:#define log2(x) (log (x) / M_LOG2_E)\nmath.h:#define log2f(x) (logf (x) / (float) M_LOG2_E)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3243\n\n",
    "created_at": "2008-05-17T20:44:59Z",
    "labels": [
        "porting: Cygwin",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] cygwin -- get it to work on cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3243",
    "user": "was"
}
```
Assignee: mabshoff

Wrap log2 in a function so it will work in cygwin.  In cygwin log2 is a macro:

```
sh-3.2$ grep log2 *.h
math.h:#define log2(x) (log (x) / M_LOG2_E)
math.h:#define log2f(x) (logf (x) / (float) M_LOG2_E)
```



Issue created by migration from https://trac.sagemath.org/ticket/3243





---

archive/issue_comments_022454.json:
```json
{
    "body": "Attachment\n\nThe same issue pops up on Solaris 9. Solaris 10 is fine.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-17T21:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3243#issuecomment-22454",
    "user": "mabshoff"
}
```

Attachment

The same issue pops up on Solaris 9. Solaris 10 is fine.

Cheers,

Michael



---

archive/issue_comments_022455.json:
```json
{
    "body": "Patch is good, positive review. With the patch applied doctests pass.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-18T12:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3243#issuecomment-22455",
    "user": "mabshoff"
}
```

Patch is good, positive review. With the patch applied doctests pass.

Cheers,

Michael



---

archive/issue_comments_022456.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-18T12:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3243#issuecomment-22456",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.alpha1



---

archive/issue_comments_022457.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-18T12:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3243#issuecomment-22457",
    "user": "mabshoff"
}
```

Resolution: fixed
