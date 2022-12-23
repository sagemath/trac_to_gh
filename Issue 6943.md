# Issue 6943: Make @parallel work for callable objects

archive/issues_006943.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  was craigcitro rlm\n\nThe following should work:\n\n\n```\n@parallel\n@cached_function\ndef foo(x):\n    return x+1\n```\n\n\nhowever, when we attempt to evaluate foo...\n\n\n```\nsage: for k in foo(range(200)):\n...       print k\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/home/boothby/.sage/sage_notebook/worksheets/admin/69/code/995.py\", line 7, in <module>\n    for k in foo(range(_sage_const_200 )):\\u000a    print k\n  File \"\", line 1, in <module>\n    \n  File \"/scratch/boothby/sage/local/lib/python2.6/site-packages/sage/parallel/multiprocessing.py\", line 63, in parallel_iter\n    fp = pickle_function(f)\n  File \"fpickle.pyx\", line 60, in sage.misc.fpickle.pickle_function (sage/misc/fpickle.c:746)\nAttributeError: 'CachedFunction' object has no attribute 'func_code'\n```\n\n\nIf any callable object is picklable, it should work with the parallel decorator.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6943\n\n",
    "created_at": "2009-09-16T02:07:16Z",
    "labels": [
        "misc",
        "critical",
        "bug"
    ],
    "title": "Make @parallel work for callable objects",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6943",
    "user": "boothby"
}
```
Assignee: boothby

CC:  was craigcitro rlm

The following should work:


```
@parallel
@cached_function
def foo(x):
    return x+1
```


however, when we attempt to evaluate foo...


```
sage: for k in foo(range(200)):
...       print k
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/boothby/.sage/sage_notebook/worksheets/admin/69/code/995.py", line 7, in <module>
    for k in foo(range(_sage_const_200 )):\u000a    print k
  File "", line 1, in <module>
    
  File "/scratch/boothby/sage/local/lib/python2.6/site-packages/sage/parallel/multiprocessing.py", line 63, in parallel_iter
    fp = pickle_function(f)
  File "fpickle.pyx", line 60, in sage.misc.fpickle.pickle_function (sage/misc/fpickle.c:746)
AttributeError: 'CachedFunction' object has no attribute 'func_code'
```


If any callable object is picklable, it should work with the parallel decorator.

Issue created by migration from https://trac.sagemath.org/ticket/6943





---

archive/issue_comments_057410.json:
```json
{
    "body": "depends on #6927 and #6937",
    "created_at": "2009-09-20T04:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6943#issuecomment-57410",
    "user": "boothby"
}
```

depends on #6927 and #6937



---

archive/issue_comments_057411.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-09-28T03:43:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6943#issuecomment-57411",
    "user": "mvngu"
}
```

Attachment



---

archive/issue_comments_057412.json:
```json
{
    "body": "Attachment\n\nRebased on referee patch of #6927. Depends on #6927. Apply this patch only",
    "created_at": "2009-11-30T16:49:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6943#issuecomment-57412",
    "user": "timdumol"
}
```

Attachment

Rebased on referee patch of #6927. Depends on #6927. Apply this patch only



---

archive/issue_comments_057413.json:
```json
{
    "body": "Things work perfectly and as advertised. Positive review on my part, but my referee patch must be reviewed by someone else.",
    "created_at": "2009-11-30T16:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6943#issuecomment-57413",
    "user": "timdumol"
}
```

Things work perfectly and as advertised. Positive review on my part, but my referee patch must be reviewed by someone else.



---

archive/issue_comments_057414.json:
```json
{
    "body": "Hi,\n\nThis asks for:\n (1) not pickling args, and (2) timeouts. \n\n#6967 also does both as a biproduct.",
    "created_at": "2010-01-21T16:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6943#issuecomment-57414",
    "user": "was"
}
```

Hi,

This asks for:
 (1) not pickling args, and (2) timeouts. 

#6967 also does both as a biproduct.



---

archive/issue_comments_057415.json:
```json
{
    "body": "Should we close this ticket as fixed?",
    "created_at": "2010-01-31T03:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6943#issuecomment-57415",
    "user": "mpatel"
}
```

Should we close this ticket as fixed?



---

archive/issue_comments_057416.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-31T18:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6943#issuecomment-57416",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057417.json:
```json
{
    "body": "Close as fixed by #6967.",
    "created_at": "2010-01-31T18:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6943#issuecomment-57417",
    "user": "mvngu"
}
```

Close as fixed by #6967.
