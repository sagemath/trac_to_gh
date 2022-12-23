# Issue 2093: floats - sage is inconsistant at times

archive/issues_002093.json:
```json
{
    "body": "Assignee: moretti\n\nThis is really confusing to calculus level students:\n\n```\nsage: x(x+1)\nx + 1\n```\n\n\nThere may be no good fix here, but one idea is to override __call__() on SmybolicVariable to raise an exception.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2093\n\n",
    "created_at": "2008-02-08T01:07:37Z",
    "labels": [
        "calculus",
        "minor",
        "bug"
    ],
    "title": "floats - sage is inconsistant at times",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2093",
    "user": "moretti"
}
```
Assignee: moretti

This is really confusing to calculus level students:

```
sage: x(x+1)
x + 1
```


There may be no good fix here, but one idea is to override __call__() on SmybolicVariable to raise an exception.

Issue created by migration from https://trac.sagemath.org/ticket/2093





---

archive/issue_comments_013529.json:
```json
{
    "body": "We sort of thought about this awhile ago, and it does raise an exception in cases there the thing being called is a constant.\n\n\n```\nsage: (sqrt(2) + 17)(x+2)\n---------------------------------------------------------------------------\n<type 'exceptions.ValueError'>            Traceback (most recent call last)\n\n/opt/sage-2.10.1.rc0/devel/sage-main/sage/<ipython console> in <module>()\n\n/opt/sage-2.10.1.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.py in __call__(self, *args, **kwargs)\n   3778 \n   3779             if len(args) > self.number_of_arguments():\n-> 3780                 raise ValueError, \"the number of arguments must be less than or equal to %s\"%self.number_of_arguments()\n   3781             \n   3782             new_ops = []\n\n<type 'exceptions.ValueError'>: the number of arguments must be less than or equal to 0\n```\n\n\nThere is a fair amount of functionality that would be lost by removing function calls on symbolic  objects.",
    "created_at": "2008-02-08T01:57:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2093#issuecomment-13529",
    "user": "mhansen"
}
```

We sort of thought about this awhile ago, and it does raise an exception in cases there the thing being called is a constant.


```
sage: (sqrt(2) + 17)(x+2)
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/opt/sage-2.10.1.rc0/devel/sage-main/sage/<ipython console> in <module>()

/opt/sage-2.10.1.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.py in __call__(self, *args, **kwargs)
   3778 
   3779             if len(args) > self.number_of_arguments():
-> 3780                 raise ValueError, "the number of arguments must be less than or equal to %s"%self.number_of_arguments()
   3781             
   3782             new_ops = []

<type 'exceptions.ValueError'>: the number of arguments must be less than or equal to 0
```


There is a fair amount of functionality that would be lost by removing function calls on symbolic  objects.



---

archive/issue_comments_013530.json:
```json
{
    "body": "Changing assignee from moretti to mhansen.",
    "created_at": "2008-02-08T01:57:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2093#issuecomment-13530",
    "user": "mhansen"
}
```

Changing assignee from moretti to mhansen.



---

archive/issue_comments_013531.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-08T01:57:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2093#issuecomment-13531",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013532.json:
```json
{
    "body": "Should this be closed as not a bug?",
    "created_at": "2008-07-14T10:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2093#issuecomment-13532",
    "user": "gfurnish"
}
```

Should this be closed as not a bug?



---

archive/issue_comments_013533.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-16T13:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2093#issuecomment-13533",
    "user": "burcin"
}
```

Resolution: fixed



---

archive/issue_comments_013534.json:
```json
{
    "body": "This was fixed by #5413. This call behavior is deprecated in 3.4.1.",
    "created_at": "2009-04-16T13:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2093#issuecomment-13534",
    "user": "burcin"
}
```

This was fixed by #5413. This call behavior is deprecated in 3.4.1.
