# Issue 1472: [with optional spkg] gnuplotpy optional package doesn' t work with numpy

archive/issues_001472.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe optional gnuplotpy package doesn't work with numpy (requires Numeric). Luckily this is fixed by doing a global search an replace of Numeric with numpy. Having done that \n\nhttp://sage.math.washington.edu/home/jkantor/spkgs/gnuplotpy-1.7.p3.spkg\n\nnow works. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1472\n\n",
    "created_at": "2007-12-12T10:00:35Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "[with optional spkg] gnuplotpy optional package doesn' t work with numpy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1472",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```
Assignee: @williamstein

The optional gnuplotpy package doesn't work with numpy (requires Numeric). Luckily this is fixed by doing a global search an replace of Numeric with numpy. Having done that 

http://sage.math.washington.edu/home/jkantor/spkgs/gnuplotpy-1.7.p3.spkg

now works. 



Issue created by migration from https://trac.sagemath.org/ticket/1472





---

archive/issue_events_003743.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-12T18:42:06Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1472",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1472#event-3743"
}
```



---

archive/issue_comments_009448.json:
```json
{
    "body": "For the sake of the reviewer, could you give an example of a command sequence that fails with the current gnuplotpy package and works with the new one?",
    "created_at": "2007-12-15T04:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1472#issuecomment-9448",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

For the sake of the reviewer, could you give an example of a command sequence that fails with the current gnuplotpy package and works with the new one?



---

archive/issue_comments_009449.json:
```json
{
    "body": "Looks good to me.  Tested using sample code from http://www.math.washington.edu/~jkantor/Numerical_Sage/node13.html .",
    "created_at": "2007-12-15T05:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1472#issuecomment-9449",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Looks good to me.  Tested using sample code from http://www.math.washington.edu/~jkantor/Numerical_Sage/node13.html .



---

archive/issue_comments_009450.json:
```json
{
    "body": "The optional spkg has been added to sagemath.org.",
    "created_at": "2007-12-15T05:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1472#issuecomment-9450",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The optional spkg has been added to sagemath.org.



---

archive/issue_events_003744.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-15T05:45:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1472",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1472#event-3744"
}
```



---

archive/issue_comments_009451.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T05:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1472#issuecomment-9451",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
