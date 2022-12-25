# Issue 945: preparser should ignore "    ....:" when it ignores "sage:"

archive/issues_000945.json:
```json
{
    "body": "Assignee: @williamstein\n\nHere's a test case.  First I define a function:\n\n```\nsage: def foo(x):\n....:     return x+3\n....: \n```\n\n\nThen I copy/paste the above session:\n\n```\nsage: sage: def foo(x):\n....:     ....:     return x+3\n------------------------------------------------------------\n<type 'exceptions.IndentationError'>: expected an indented block (<ipython console>, line 2)\n\nsage: \n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/945\n\n",
    "created_at": "2007-10-20T17:15:06Z",
    "labels": [
        "component: user interface",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "preparser should ignore \"    ....:\" when it ignores \"sage:\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/945",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

Here's a test case.  First I define a function:

```
sage: def foo(x):
....:     return x+3
....: 
```


Then I copy/paste the above session:

```
sage: sage: def foo(x):
....:     ....:     return x+3
------------------------------------------------------------
<type 'exceptions.IndentationError'>: expected an indented block (<ipython console>, line 2)

sage: 
```



Issue created by migration from https://trac.sagemath.org/ticket/945





---

archive/issue_comments_005756.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-05-24T17:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/945#issuecomment-5756",
    "user": "https://github.com/tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_events_002608.json:
```json
{
    "actor": "https://github.com/tscrim",
    "created_at": "2013-05-24T17:59:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/945",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/945#event-2608"
}
```



---

archive/issue_comments_005757.json:
```json
{
    "body": "This was fixed at some point (tested on `5.10.beta2`):\n\n```\nsage: def foo(x):\n....:     return x\n....: \nsage: sage: def foo(x):        \n....:     ....:     return x\n....: ....: \nsage: \nsage: def foo(x):\n....:     ....:     return x\n....: \n```\n",
    "created_at": "2013-05-24T17:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/945#issuecomment-5757",
    "user": "https://github.com/tscrim"
}
```

This was fixed at some point (tested on `5.10.beta2`):

```
sage: def foo(x):
....:     return x
....: 
sage: sage: def foo(x):        
....:     ....:     return x
....: ....: 
sage: 
sage: def foo(x):
....:     ....:     return x
....: 
```




---

archive/issue_comments_005758.json:
```json
{
    "body": "I confirm that this works, hence i put a positive review. I do not know who shoud be the author though. Maybe ipython ?",
    "created_at": "2013-06-01T13:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/945#issuecomment-5758",
    "user": "https://trac.sagemath.org/admin/accounts/users/tmonteil"
}
```

I confirm that this works, hence i put a positive review. I do not know who shoud be the author though. Maybe ipython ?



---

archive/issue_comments_005759.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-01T13:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/945#issuecomment-5759",
    "user": "https://trac.sagemath.org/admin/accounts/users/tmonteil"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_005760.json:
```json
{
    "body": "For duplicate tickets, there is no author since there is no patch to be merged.",
    "created_at": "2013-06-01T15:04:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/945#issuecomment-5760",
    "user": "https://github.com/tscrim"
}
```

For duplicate tickets, there is no author since there is no patch to be merged.



---

archive/issue_events_002609.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-06-03T13:07:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/945",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/945#event-2609"
}
```



---

archive/issue_comments_005761.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-06-03T13:07:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/945#issuecomment-5761",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme



---

archive/issue_comments_005762.json:
```json
{
    "body": "See also #14665 for a related bug.",
    "created_at": "2013-06-03T15:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/945#issuecomment-5762",
    "user": "https://github.com/vbraun"
}
```

See also #14665 for a related bug.
