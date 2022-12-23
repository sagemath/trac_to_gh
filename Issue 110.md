# Issue 110: srange should accept negative step value

archive/issues_000110.json:
```json
{
    "body": "Assignee: somebody\n\nIt should work more like Python's ordinary `range`, not like this:\n\n\n```\nsage: srange(1, 5, -1)\n---------------------------------------------------------------------------\nexceptions.ValueError                                Traceback (most recent call last)\n\n/home/dmharvey/sage-1.3.7.3.3/<ipython console> \n\n/home/dmharvey/sage/local/lib/python2.4/site-packages/sage/misc/misc.py in srange(a, b, step, include_endpoint)\n    630         \n    631     if step <= 0:\n--> 632         raise ValueError, \"step (=%s) must be positive\"%step\n    633     num_steps = int(float((b-a)/step)) + 1\n    634     v = [a] + [a + k*step for k in range(1,num_steps)]\n\nValueError: step (=-1) must be positive\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/110\n\n",
    "created_at": "2006-10-04T23:15:38Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "title": "srange should accept negative step value",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/110",
    "user": "dmharvey"
}
```
Assignee: somebody

It should work more like Python's ordinary `range`, not like this:


```
sage: srange(1, 5, -1)
---------------------------------------------------------------------------
exceptions.ValueError                                Traceback (most recent call last)

/home/dmharvey/sage-1.3.7.3.3/<ipython console> 

/home/dmharvey/sage/local/lib/python2.4/site-packages/sage/misc/misc.py in srange(a, b, step, include_endpoint)
    630         
    631     if step <= 0:
--> 632         raise ValueError, "step (=%s) must be positive"%step
    633     num_steps = int(float((b-a)/step)) + 1
    634     v = [a] + [a + k*step for k in range(1,num_steps)]

ValueError: step (=-1) must be positive
```



Issue created by migration from https://trac.sagemath.org/ticket/110





---

archive/issue_comments_000515.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-10-05T07:44:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/110#issuecomment-515",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_000516.json:
```json
{
    "body": "I fixed this for sage-1.4",
    "created_at": "2006-10-05T07:44:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/110#issuecomment-516",
    "user": "was"
}
```

I fixed this for sage-1.4
