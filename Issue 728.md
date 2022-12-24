# Issue 728: sage_inspect broken

archive/issues_000728.json:
```json
{
    "body": "Assignee: was\n\nThis is SAGE 2.8.5:\n\n\n```\nsage: A = random_matrix(ZZ,3,3)\nsage: A.lll?\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n ... File \"/usr/local/sage-2.8.1/local/lib/python2.5/site-packages/sage/misc/sageinspect.py\", line 252, in sage_getargspec\n    args, varargs, varkw = inspect.getargs(func_obj.func_code)\nUnboundLocalError: local variable 'func_obj' referenced before assignment\nsage: e = 1\nsage: e.additive_order?\n\n  File \"<stdin>\", line 1, in <module>\n ... File \"/usr/local/sage-2.8.1/local/lib/python2.5/site-packages/sage/misc/sageinspect.py\", line 252, in sage_getargspec\n    args, varargs, varkw = inspect.getargs(func_obj.func_code)\nUnboundLocalError: local variable 'func_obj' referenced before assignment\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/728\n\n",
    "created_at": "2007-09-21T13:38:10Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.6",
    "title": "sage_inspect broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/728",
    "user": "malb"
}
```
Assignee: was

This is SAGE 2.8.5:


```
sage: A = random_matrix(ZZ,3,3)
sage: A.lll?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
 ... File "/usr/local/sage-2.8.1/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 252, in sage_getargspec
    args, varargs, varkw = inspect.getargs(func_obj.func_code)
UnboundLocalError: local variable 'func_obj' referenced before assignment
sage: e = 1
sage: e.additive_order?

  File "<stdin>", line 1, in <module>
 ... File "/usr/local/sage-2.8.1/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 252, in sage_getargspec
    args, varargs, varkw = inspect.getargs(func_obj.func_code)
UnboundLocalError: local variable 'func_obj' referenced before assignment
```


Issue created by migration from https://trac.sagemath.org/ticket/728





---

archive/issue_comments_004275.json:
```json
{
    "body": "What platform do these errors occur on?\n\nBoth of the examples work fine for me on 64-bit Linux.",
    "created_at": "2007-09-26T20:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/728#issuecomment-4275",
    "user": "mhansen"
}
```

What platform do these errors occur on?

Both of the examples work fine for me on 64-bit Linux.



---

archive/issue_comments_004276.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T18:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/728#issuecomment-4276",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_004277.json:
```json
{
    "body": "I fixed this; it happened on os x.",
    "created_at": "2007-10-04T18:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/728#issuecomment-4277",
    "user": "was"
}
```

I fixed this; it happened on os x.
