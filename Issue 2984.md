# Issue 2984: ITANIUM (RHEL 5) -- turn off all unaligned access messages

archive/issues_002984.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\n20:30 < wstein|afk> See this page: http://kbase.redhat.com/faq/FAQ_105_9111.shtm\n20:30 < wstein|afk> It says \"These messages are informative only. When any application performs an unaligned \n                    access, the processor traps into the kernel and the kernel emulates the unaligned access. \n                    The program will work correctly however there will be a performance hit, as emulating the \n                    unaligned memory access is a software operation and not a hardware operation.\"\n20:30 < mabshoff> ok\n```\n\n\nThis will not be needed once #2209 is done, I hope. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2984\n\n",
    "created_at": "2008-04-21T03:37:37Z",
    "labels": [
        "Cygwin",
        "blocker",
        "bug"
    ],
    "title": "ITANIUM (RHEL 5) -- turn off all unaligned access messages",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2984",
    "user": "was"
}
```
Assignee: mabshoff


```
20:30 < wstein|afk> See this page: http://kbase.redhat.com/faq/FAQ_105_9111.shtm
20:30 < wstein|afk> It says "These messages are informative only. When any application performs an unaligned 
                    access, the processor traps into the kernel and the kernel emulates the unaligned access. 
                    The program will work correctly however there will be a performance hit, as emulating the 
                    unaligned memory access is a software operation and not a hardware operation."
20:30 < mabshoff> ok
```


This will not be needed once #2209 is done, I hope. 

Issue created by migration from https://trac.sagemath.org/ticket/2984





---

archive/issue_comments_020546.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-21T04:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2984#issuecomment-20546",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020547.json:
```json
{
    "body": "Changing component from Cygwin to porting.",
    "created_at": "2008-04-21T04:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2984#issuecomment-20547",
    "user": "mabshoff"
}
```

Changing component from Cygwin to porting.



---

archive/issue_comments_020548.json:
```json
{
    "body": "I am testing the fix, but this will take a while.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-21T04:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2984#issuecomment-20548",
    "user": "mabshoff"
}
```

I am testing the fix, but this will take a while.

Cheers,

Michael



---

archive/issue_comments_020549.json:
```json
{
    "body": "Patch up here:\n  http://sage.math.washington.edu/home/was/patches/gap-4.4.10.p7.spkg",
    "created_at": "2008-04-21T05:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2984#issuecomment-20549",
    "user": "was"
}
```

Patch up here:
  http://sage.math.washington.edu/home/was/patches/gap-4.4.10.p7.spkg



---

archive/issue_comments_020550.json:
```json
{
    "body": "Spkg looks good to me, the fix works. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-21T06:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2984#issuecomment-20550",
    "user": "mabshoff"
}
```

Spkg looks good to me, the fix works. Positive review.

Cheers,

Michael



---

archive/issue_comments_020551.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-21T06:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2984#issuecomment-20551",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020552.json:
```json
{
    "body": "Merged in Sage 3.0.rc1",
    "created_at": "2008-04-21T06:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2984#issuecomment-20552",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.rc1
