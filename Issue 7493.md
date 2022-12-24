# Issue 7493: Implement sage -t --time

archive/issues_007493.json:
```json
{
    "body": "Assignee: tbd\n\nWhen a test file takes time to execute, it would be handy to have a quick overview of which specific tests take long. \n\nSomething like:\n\n```\n    sage -t --verbose --time bla.py\n    Trying: \n        1+1\n    Expecting:\n        2\n    ok [0.1ms]\n    Trying: \n        factor(....)\n    Expecting:\n        ...\n    ok [10s] warning: please use # long time\n    Trying: \n        factor(.....) # long time\n    Expecting:\n        ...\n    ok [10s]\n    Trying: \n        factor(........)\n    Expecting:\n        ...\n    ok [300s] warning: this is too long!\n```\n\n\nAnd in non verbose mode:\n\n\n```\n    sage -t --time bla.py\n    Warning: factor(....) line 30 takes 10s: please use # long time\n    Warning: factor(........) line 50 takes 300s: this is too long!\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7493\n\n",
    "created_at": "2009-11-19T11:22:25Z",
    "labels": [
        "doctest coverage",
        "major",
        "enhancement"
    ],
    "title": "Implement sage -t --time",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7493",
    "user": "nthiery"
}
```
Assignee: tbd

When a test file takes time to execute, it would be handy to have a quick overview of which specific tests take long. 

Something like:

```
    sage -t --verbose --time bla.py
    Trying: 
        1+1
    Expecting:
        2
    ok [0.1ms]
    Trying: 
        factor(....)
    Expecting:
        ...
    ok [10s] warning: please use # long time
    Trying: 
        factor(.....) # long time
    Expecting:
        ...
    ok [10s]
    Trying: 
        factor(........)
    Expecting:
        ...
    ok [300s] warning: this is too long!
```


And in non verbose mode:


```
    sage -t --time bla.py
    Warning: factor(....) line 30 takes 10s: please use # long time
    Warning: factor(........) line 50 takes 300s: this is too long!
```



Issue created by migration from https://trac.sagemath.org/ticket/7493





---

archive/issue_comments_063297.json:
```json
{
    "body": "Here is a patch which sorts of do the job. It is not intended to be merged, but to make you crave enough for the feature to actually implement it right:\n\n```\nzephyr-~s/categories>sage -t -time coxeter_groups.py    \nsage -t -time \"4.3/devel/sage-combinat/sage/categories/coxeter_groups.py\"\n...\nFile \"/opt/sage-4.3/devel/sage-combinat/sage/categories/coxeter_groups.py\", line 1010:\n    sage: for u in P4:\n          for v in P4:\n              assert u.bruhat_lequal(v) == P4toW(u).bruhat_le(P4toW(v))\nExpected nothing\nGot:\n    Warning: test took 8.1s > 1s. Please use # long time\nTotal time for all tests: 24.0 seconds\n```\n",
    "created_at": "2010-01-20T10:30:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7493#issuecomment-63297",
    "user": "nthiery"
}
```

Here is a patch which sorts of do the job. It is not intended to be merged, but to make you crave enough for the feature to actually implement it right:

```
zephyr-~s/categories>sage -t -time coxeter_groups.py    
sage -t -time "4.3/devel/sage-combinat/sage/categories/coxeter_groups.py"
...
File "/opt/sage-4.3/devel/sage-combinat/sage/categories/coxeter_groups.py", line 1010:
    sage: for u in P4:
          for v in P4:
              assert u.bruhat_lequal(v) == P4toW(u).bruhat_le(P4toW(v))
Expected nothing
Got:
    Warning: test took 8.1s > 1s. Please use # long time
Total time for all tests: 24.0 seconds
```




---

archive/issue_comments_063298.json:
```json
{
    "body": "Nicolas, can you actually attach your toy patch to this ticket?  I've now been in a few situations where I'm staring at the output of sage -t -verbose, and having *anything* automated for this would be a great help to my sanity.",
    "created_at": "2010-01-23T22:50:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7493#issuecomment-63298",
    "user": "AlexGhitza"
}
```

Nicolas, can you actually attach your toy patch to this ticket?  I've now been in a few situations where I'm staring at the output of sage -t -verbose, and having *anything* automated for this would be a great help to my sanity.



---

archive/issue_comments_063299.json:
```json
{
    "body": "Attachment [trac_7493-check-long-time.patch](tarball://root/attachments/some-uuid/ticket7493/trac_7493-check-long-time.patch) by nthiery created at 2010-01-23 22:59:26",
    "created_at": "2010-01-23T22:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7493#issuecomment-63299",
    "user": "nthiery"
}
```

Attachment [trac_7493-check-long-time.patch](tarball://root/attachments/some-uuid/ticket7493/trac_7493-check-long-time.patch) by nthiery created at 2010-01-23 22:59:26



---

archive/issue_comments_063300.json:
```json
{
    "body": "Replying to [comment:2 AlexGhitza]:\n> Nicolas, can you actually attach your toy patch to this ticket?  I've now been in a few situations where I'm staring at the output of sage -t -verbose, and having *anything* automated for this would be a great help to my sanity.\n\nOops, there it is.\n\nEh eh, maybe my strategy is going to work :-)",
    "created_at": "2010-01-23T23:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7493#issuecomment-63300",
    "user": "nthiery"
}
```

Replying to [comment:2 AlexGhitza]:
> Nicolas, can you actually attach your toy patch to this ticket?  I've now been in a few situations where I'm staring at the output of sage -t -verbose, and having *anything* automated for this would be a great help to my sanity.

Oops, there it is.

Eh eh, maybe my strategy is going to work :-)



---

archive/issue_comments_063301.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-02-22T21:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7493#issuecomment-63301",
    "user": "jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_comments_063302.json:
```json
{
    "body": "This is essentially all implemented in #12415.",
    "created_at": "2013-02-22T21:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7493#issuecomment-63302",
    "user": "jdemeyer"
}
```

This is essentially all implemented in #12415.
