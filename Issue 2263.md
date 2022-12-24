# Issue 2263: Sage 2.10.2.rc0: numerical noise doctest failure in calculus/calculus.py

archive/issues_002263.json:
```json
{
    "body": "Assignee: failure\n\nCraig Citro reported:\n\n```\n**********************************************************************\nFile \"calculus.py\", line \n    sage: f.find_maximum_on_interval(0,5, tol=0.1, maxfun=10)\nExpected:\n    (0.56109032345808163, 0.857926501456)\nGot:\n    (0.56109032345808174, 0.857926501456)\n********************************************************************** \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2263\n\n",
    "created_at": "2008-02-22T19:15:32Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Sage 2.10.2.rc0: numerical noise doctest failure in calculus/calculus.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2263",
    "user": "mabshoff"
}
```
Assignee: failure

Craig Citro reported:

```
**********************************************************************
File "calculus.py", line 
    sage: f.find_maximum_on_interval(0,5, tol=0.1, maxfun=10)
Expected:
    (0.56109032345808163, 0.857926501456)
Got:
    (0.56109032345808174, 0.857926501456)
********************************************************************** 
```


Issue created by migration from https://trac.sagemath.org/ticket/2263





---

archive/issue_comments_014991.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-22T19:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2263#issuecomment-14991",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014992.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-02-22T19:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2263#issuecomment-14992",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_014993.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2008-02-22T19:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2263#issuecomment-14993",
    "user": "mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_014994.json:
```json
{
    "body": "Numerical noise makes sense here, since behind the scenes this is double arithmetic\ndone in FORTRAN in scipy.   So we should just change the expected output to \n\n(0.561090323458081..., 0.857926501456)",
    "created_at": "2008-02-22T21:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2263#issuecomment-14994",
    "user": "was"
}
```

Numerical noise makes sense here, since behind the scenes this is double arithmetic
done in FORTRAN in scipy.   So we should just change the expected output to 

(0.561090323458081..., 0.857926501456)



---

archive/issue_comments_014995.json:
```json
{
    "body": "Attachment [trac_2263.patch](tarball://root/attachments/some-uuid/ticket2263/trac_2263.patch) by mabshoff created at 2008-02-22 21:16:21",
    "created_at": "2008-02-22T21:16:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2263#issuecomment-14995",
    "user": "mabshoff"
}
```

Attachment [trac_2263.patch](tarball://root/attachments/some-uuid/ticket2263/trac_2263.patch) by mabshoff created at 2008-02-22 21:16:21



---

archive/issue_comments_014996.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-22T22:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2263#issuecomment-14996",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014997.json:
```json
{
    "body": "Merged in Sage 2.10.2.final",
    "created_at": "2008-02-22T22:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2263#issuecomment-14997",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.final
