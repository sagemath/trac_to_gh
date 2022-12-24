# Issue 1472: [with optional spkg] gnuplotpy optional package doesn' t work with numpy

archive/issues_001472.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe optional gnuplotpy package doesn't work with numpy (requires Numeric). Luckily this is fixed by doing a global search an replace of Numeric with numpy. Having done that \n\nhttp://sage.math.washington.edu/home/jkantor/spkgs/gnuplotpy-1.7.p3.spkg\n\nnow works. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1472\n\n",
    "created_at": "2007-12-12T10:00:35Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "[with optional spkg] gnuplotpy optional package doesn' t work with numpy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1472",
    "user": "jkantor"
}
```
Assignee: @williamstein

The optional gnuplotpy package doesn't work with numpy (requires Numeric). Luckily this is fixed by doing a global search an replace of Numeric with numpy. Having done that 

http://sage.math.washington.edu/home/jkantor/spkgs/gnuplotpy-1.7.p3.spkg

now works. 



Issue created by migration from https://trac.sagemath.org/ticket/1472





---

archive/issue_comments_009473.json:
```json
{
    "body": "For the sake of the reviewer, could you give an example of a command sequence that fails with the current gnuplotpy package and works with the new one?",
    "created_at": "2007-12-15T04:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1472#issuecomment-9473",
    "user": "cwitty"
}
```

For the sake of the reviewer, could you give an example of a command sequence that fails with the current gnuplotpy package and works with the new one?



---

archive/issue_comments_009474.json:
```json
{
    "body": "Looks good to me.  Tested using sample code from http://www.math.washington.edu/~jkantor/Numerical_Sage/node13.html .",
    "created_at": "2007-12-15T05:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1472#issuecomment-9474",
    "user": "cwitty"
}
```

Looks good to me.  Tested using sample code from http://www.math.washington.edu/~jkantor/Numerical_Sage/node13.html .



---

archive/issue_comments_009475.json:
```json
{
    "body": "The optional spkg has been added to sagemath.org.",
    "created_at": "2007-12-15T05:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1472#issuecomment-9475",
    "user": "mabshoff"
}
```

The optional spkg has been added to sagemath.org.



---

archive/issue_comments_009476.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T05:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1472#issuecomment-9476",
    "user": "mabshoff"
}
```

Resolution: fixed
