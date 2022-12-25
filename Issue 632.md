# Issue 632: bug in command line time function and something -- very weird

archive/issues_000632.json:
```json
{
    "body": "Assignee: somebody\n\nNotice that the second timing below is \"0 seconds\", which is clearly completely wrong.\nThe notation \"3r\" means the unpreparsed 3, i.e., the Python *integer* 3.  There\nis a *noticeable amount of time* that passes when the input is given.  So something\nis very very wrong.  This happens on intel os x and on 64-bit opteron linux (and\nprobably all other os's). \n\n```\nsage: time n=int(3)**int(999999)\nCPU times: user 0.76 s, sys: 0.00 s, total: 0.76 s\nWall time: 0.76\nsage: time n= 3r ** 999999r\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n\nsage: preparse('time n= 3r ** 999999r')\n'time n= 3 ** 999999'\nsage: preparse('time n=int(3)**int(999999)')\n'time n=int(Integer(3))**int(Integer(999999))'\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/632\n\n",
    "created_at": "2007-09-09T23:27:42Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "bug in command line time function and something -- very weird",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/632",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

Notice that the second timing below is "0 seconds", which is clearly completely wrong.
The notation "3r" means the unpreparsed 3, i.e., the Python *integer* 3.  There
is a *noticeable amount of time* that passes when the input is given.  So something
is very very wrong.  This happens on intel os x and on 64-bit opteron linux (and
probably all other os's). 

```
sage: time n=int(3)**int(999999)
CPU times: user 0.76 s, sys: 0.00 s, total: 0.76 s
Wall time: 0.76
sage: time n= 3r ** 999999r
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00

sage: preparse('time n= 3r ** 999999r')
'time n= 3 ** 999999'
sage: preparse('time n=int(3)**int(999999)')
'time n=int(Integer(3))**int(Integer(999999))'
```

Issue created by migration from https://trac.sagemath.org/ticket/632





---

archive/issue_comments_003240.json:
```json
{
    "body": "The \"time\" IPython operator compiles the code, and then carefully times how long it takes to run the compiled code.\n\nThe Python compiler does some constant folding.  In this case, when IPython tries to compile \"n = 3 ** 999999\", the Python compiler evaluates the exponentiation (before IPython starts timing).\n\nI can't think of a good way to fix this, if we even decide it's a bug.  Maybe one of the less-bad ways is to change the preprocessor, so that \"3r\" maps to \"int(3)\" instead of \"3\".",
    "created_at": "2007-10-07T17:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/632#issuecomment-3240",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

The "time" IPython operator compiles the code, and then carefully times how long it takes to run the compiled code.

The Python compiler does some constant folding.  In this case, when IPython tries to compile "n = 3 ** 999999", the Python compiler evaluates the exponentiation (before IPython starts timing).

I can't think of a good way to fix this, if we even decide it's a bug.  Maybe one of the less-bad ways is to change the preprocessor, so that "3r" maps to "int(3)" instead of "3".



---

archive/issue_comments_003241.json:
```json
{
    "body": "For the record:\n\nWilliam Stein, Fernando Perez, and I corresponded about this.  In the next version of IPython (0.8.2), the \"time\" command will time the compilation separately, and report this time if it's more than 0.1 seconds.\n\nI suppose this bug should stay open until that version of IPython is included in SAGE; then it can be closed.",
    "created_at": "2007-10-12T01:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/632#issuecomment-3241",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

For the record:

William Stein, Fernando Perez, and I corresponded about this.  In the next version of IPython (0.8.2), the "time" command will time the compilation separately, and report this time if it's more than 0.1 seconds.

I suppose this bug should stay open until that version of IPython is included in SAGE; then it can be closed.



---

archive/issue_comments_003242.json:
```json
{
    "body": "This is fixed in 3.1.4 at least:\n\n```\nsage: time n= 3r ** 999999r\nCPU times: user 0.17 s, sys: 0.01 s, total: 0.17 s\nWall time: 0.19 s\n```\n\nAnd we are already at 0.8.4 for IPython.",
    "created_at": "2008-10-23T23:33:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/632#issuecomment-3242",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

This is fixed in 3.1.4 at least:

```
sage: time n= 3r ** 999999r
CPU times: user 0.17 s, sys: 0.01 s, total: 0.17 s
Wall time: 0.19 s
```

And we are already at 0.8.4 for IPython.



---

archive/issue_events_001684.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-24T10:35:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/632",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/632#event-1684"
}
```



---

archive/issue_comments_003243.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-24T10:35:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/632#issuecomment-3243",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_003244.json:
```json
{
    "body": "Fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-24T10:35:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/632#issuecomment-3244",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed.

Cheers,

Michael
