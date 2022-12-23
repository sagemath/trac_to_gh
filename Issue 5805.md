# Issue 5805: numerical noise in "devel/sage/sage/modular/dirichlet.py"

archive/issues_005805.json:
```json
{
    "body": "Assignee: craigcitro\n\nOn Fedora 9, 32 bit:\n\n\n\n```\nsage -t  \"devel/sage/sage/modular/dirichlet.py\"             \n**********************************************************************\nFile \"/home/jaap/downloads/sage-3.4.1.rc0/devel/sage/sage/modular/dirichlet.py\", line 1044:\n    sage: e.kloosterman_sum_numerical()\nExpected:\n    7.21644966006e-16 + 1.73205080757*I\nGot:\n    6.66133814775e-16 + 1.73205080757*I\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_29\n***Test Failed*** 1 failures.\n\n```\n\n\n\nCheers,\n\nJaap\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5805\n\n",
    "created_at": "2009-04-16T21:02:12Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "title": "numerical noise in \"devel/sage/sage/modular/dirichlet.py\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5805",
    "user": "jsp"
}
```
Assignee: craigcitro

On Fedora 9, 32 bit:



```
sage -t  "devel/sage/sage/modular/dirichlet.py"             
**********************************************************************
File "/home/jaap/downloads/sage-3.4.1.rc0/devel/sage/sage/modular/dirichlet.py", line 1044:
    sage: e.kloosterman_sum_numerical()
Expected:
    7.21644966006e-16 + 1.73205080757*I
Got:
    6.66133814775e-16 + 1.73205080757*I
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_29
***Test Failed*** 1 failures.

```



Cheers,

Jaap



Issue created by migration from https://trac.sagemath.org/ticket/5805





---

archive/issue_comments_045561.json:
```json
{
    "body": "Changing component from modular forms to doctest.",
    "created_at": "2009-04-17T10:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5805#issuecomment-45561",
    "user": "mabshoff"
}
```

Changing component from modular forms to doctest.



---

archive/issue_comments_045562.json:
```json
{
    "body": "Changing assignee from craigcitro to mabshoff.",
    "created_at": "2009-04-17T10:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5805#issuecomment-45562",
    "user": "mabshoff"
}
```

Changing assignee from craigcitro to mabshoff.



---

archive/issue_comments_045563.json:
```json
{
    "body": "Another datapoint from 3.4.1.rc3 on Solaris 10/x86-64 running in 32 bit mode:\n\n```\nsage -t -long devel/sage/sage/modular/dirichlet.py\n**********************************************************************\nFile \"/home/mabshoff/build-3.4.1.rc2/sage-3.4.1.rc2-fulvia-gcc-4.3.3/\ndevel/sage-main/sage/modular/dirichlet.py\", line 10\n44:\n    sage: e.kloosterman_sum_numerical()\nExpected:\n    7.21644966006e-16 + 1.73205080757*I\nGot:\n    6.66133814775e-16 + 1.73205080757*I\n**********************************************************************\n```\n",
    "created_at": "2009-04-17T10:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5805#issuecomment-45563",
    "user": "mabshoff"
}
```

Another datapoint from 3.4.1.rc3 on Solaris 10/x86-64 running in 32 bit mode:

```
sage -t -long devel/sage/sage/modular/dirichlet.py
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc2/sage-3.4.1.rc2-fulvia-gcc-4.3.3/
devel/sage-main/sage/modular/dirichlet.py", line 10
44:
    sage: e.kloosterman_sum_numerical()
Expected:
    7.21644966006e-16 + 1.73205080757*I
Got:
    6.66133814775e-16 + 1.73205080757*I
**********************************************************************
```




---

archive/issue_comments_045564.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-17T10:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5805#issuecomment-45564",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045565.json:
```json
{
    "body": "Add the Sage release, make it clear it is a blocker. \n\nCheers,\n\nMichael",
    "created_at": "2009-04-17T11:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5805#issuecomment-45565",
    "user": "mabshoff"
}
```

Add the Sage release, make it clear it is a blocker. 

Cheers,

Michael



---

archive/issue_comments_045566.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-04-17T11:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5805#issuecomment-45566",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_045567.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-18T08:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5805#issuecomment-45567",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_045568.json:
```json
{
    "body": "Patch looks good to me, applied ok to 3.4.1.rc3 and passed test on 32- and 64-bit.",
    "created_at": "2009-04-18T14:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5805#issuecomment-45568",
    "user": "cremona"
}
```

Patch looks good to me, applied ok to 3.4.1.rc3 and passed test on 32- and 64-bit.



---

archive/issue_comments_045569.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-18T23:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5805#issuecomment-45569",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_045570.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc4.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T23:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5805#issuecomment-45570",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc4.

Cheers,

Michael
