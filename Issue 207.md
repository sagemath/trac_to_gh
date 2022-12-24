# Issue 207: log in waaay slower than python's math.log

archive/issues_000207.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: time x = [log(n) for n in range(1, 100000)]\nCPU times: user 2.68 s, sys: 0.08 s, total: 2.75 s\nWall time: 2.76\n\nsage: import math\nsage: time x = [math.log(n) for n in range(1, 100000)]\nCPU times: user 0.15 s, sys: 0.01 s, total: 0.17 s\nWall time: 0.17\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/207\n\n",
    "created_at": "2007-01-23T14:17:33Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-1.9",
    "title": "log in waaay slower than python's math.log",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/207",
    "user": "dmharvey"
}
```
Assignee: somebody


```
sage: time x = [log(n) for n in range(1, 100000)]
CPU times: user 2.68 s, sys: 0.08 s, total: 2.75 s
Wall time: 2.76

sage: import math
sage: time x = [math.log(n) for n in range(1, 100000)]
CPU times: user 0.15 s, sys: 0.01 s, total: 0.17 s
Wall time: 0.17
```



Issue created by migration from https://trac.sagemath.org/ticket/207





---

archive/issue_comments_000933.json:
```json
{
    "body": "Improved for sage-1.9:\n\n```\n\nsage: time x = [math.log(n) for n in range(1, 100000)]\nCPU times: user 0.07 s, sys: 0.01 s, total: 0.08 s\nWall time: 0.08\nsage: time x = [log(n) for n in range(1, 100000)]\nCPU times: user 0.37 s, sys: 0.01 s, total: 0.38 s\nWall time: 0.39\n```\n\n\nNote that the SAGE log does much more than the math one, since\nit allows for calling a log method of the object (testing for\npresense of already takes more time than math.log).  Also, it \nreturns a native SAGE object -- in this case I've changed it to\nreturn an RDF element, which is pretty logical. \n\nWilliam",
    "created_at": "2007-01-23T19:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/207#issuecomment-933",
    "user": "was"
}
```

Improved for sage-1.9:

```

sage: time x = [math.log(n) for n in range(1, 100000)]
CPU times: user 0.07 s, sys: 0.01 s, total: 0.08 s
Wall time: 0.08
sage: time x = [log(n) for n in range(1, 100000)]
CPU times: user 0.37 s, sys: 0.01 s, total: 0.38 s
Wall time: 0.39
```


Note that the SAGE log does much more than the math one, since
it allows for calling a log method of the object (testing for
presense of already takes more time than math.log).  Also, it 
returns a native SAGE object -- in this case I've changed it to
return an RDF element, which is pretty logical. 

William



---

archive/issue_comments_000934.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-23T19:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/207#issuecomment-934",
    "user": "was"
}
```

Resolution: fixed
