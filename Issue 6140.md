# Issue 6140: Upgrade numpy to 1.3.0

archive/issues_006140.json:
```json
{
    "body": "Assignee: mabshoff\n\nHere is an spkg: http://sage.math.washington.edu/home/jason/numpy-1.3.0.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/6140\n\n",
    "created_at": "2009-05-27T21:20:16Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "Upgrade numpy to 1.3.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6140",
    "user": "https://github.com/jasongrout"
}
```
Assignee: mabshoff

Here is an spkg: http://sage.math.washington.edu/home/jason/numpy-1.3.0.spkg

Issue created by migration from https://trac.sagemath.org/ticket/6140





---

archive/issue_comments_048933.json:
```json
{
    "body": "This is related to #3391.  Also, #4205 can likely be closed once this ticket is closed.",
    "created_at": "2009-05-27T21:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6140#issuecomment-48933",
    "user": "https://github.com/jasongrout"
}
```

This is related to #3391.  Also, #4205 can likely be closed once this ticket is closed.



---

archive/issue_comments_048934.json:
```json
{
    "body": "Attachment [numpy-1.3.0-update.patch](tarball://root/attachments/some-uuid/ticket6140/numpy-1.3.0-update.patch) by @jasongrout created at 2009-05-27 22:11:17\n\nThere are a few minor doctest updates that need to be done.  See above for a patch which addresses at least some of these.\n\nWhen doing all doctests on 4.0.rc0, I get failures in:\n\n\n```\nThe following tests failed:\n\n        sage -t  devel/sage/sage/misc/banner.py # 5 doctests failed\n        sage -t  devel/sage/sage/matrix/matrix_symbolic_dense.pyx # 3 doctests failed\n        sage -t  devel/sage/sage/matrix/tests.py # 1 doctests failed\n        sage -t  devel/sage/sage/rings/polynomial/polynomial_element.pyx # 2 doctests failed\n        sage -t  devel/sage/sage/calculus/functions.py # 1 doctests failed\n        sage -t  devel/sage/sage/plot/plot_field.py # 1 doctests failed\n----------------------------------------------------------------------\n```\n\n\nHowever, some of these failures are from rc0, not from the numpy update.  The patch above corrects the failures that I know are from the numpy updated.  Please let me know if there are any other doctests that need to be updated in this ticket.",
    "created_at": "2009-05-27T22:11:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6140#issuecomment-48934",
    "user": "https://github.com/jasongrout"
}
```

Attachment [numpy-1.3.0-update.patch](tarball://root/attachments/some-uuid/ticket6140/numpy-1.3.0-update.patch) by @jasongrout created at 2009-05-27 22:11:17

There are a few minor doctest updates that need to be done.  See above for a patch which addresses at least some of these.

When doing all doctests on 4.0.rc0, I get failures in:


```
The following tests failed:

        sage -t  devel/sage/sage/misc/banner.py # 5 doctests failed
        sage -t  devel/sage/sage/matrix/matrix_symbolic_dense.pyx # 3 doctests failed
        sage -t  devel/sage/sage/matrix/tests.py # 1 doctests failed
        sage -t  devel/sage/sage/rings/polynomial/polynomial_element.pyx # 2 doctests failed
        sage -t  devel/sage/sage/calculus/functions.py # 1 doctests failed
        sage -t  devel/sage/sage/plot/plot_field.py # 1 doctests failed
----------------------------------------------------------------------
```


However, some of these failures are from rc0, not from the numpy update.  The patch above corrects the failures that I know are from the numpy updated.  Please let me know if there are any other doctests that need to be updated in this ticket.



---

archive/issue_comments_048935.json:
```json
{
    "body": "Everything looks good, except I get one trivial test failure. As you can see its just the difference between +0 and -0. It should probably be fixed. Positive review pending a fix of that. \n\nsage -t  \"devel/sage-main/sage/rings/polynomial/polynomial_element.pyx\"\n**********************************************************************\nFile \"/home/jkantor/sage-4.0/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx\", line 4059:\n    sage: p.roots(ring=RR)\nExpected:\n    [(0.000000000000000, 1)]\nGot:\n    [(-0.000000000000000, 1)]\n**********************************************************************",
    "created_at": "2009-06-01T08:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6140#issuecomment-48935",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

Everything looks good, except I get one trivial test failure. As you can see its just the difference between +0 and -0. It should probably be fixed. Positive review pending a fix of that. 

sage -t  "devel/sage-main/sage/rings/polynomial/polynomial_element.pyx"
**********************************************************************
File "/home/jkantor/sage-4.0/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx", line 4059:
    sage: p.roots(ring=RR)
Expected:
    [(0.000000000000000, 1)]
Got:
    [(-0.000000000000000, 1)]
**********************************************************************



---

archive/issue_comments_048936.json:
```json
{
    "body": "Also, #5090 might be able to be closed after this is merged.",
    "created_at": "2009-06-03T02:20:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6140#issuecomment-48936",
    "user": "https://github.com/jasongrout"
}
```

Also, #5090 might be able to be closed after this is merged.



---

archive/issue_comments_048937.json:
```json
{
    "body": "This looks good. I'm attaching a second patch for that one doctest failure. \n\nFor the record, this spkg and the two patches have been merged in `4.0.2.alpha0` -- but I want to take a few minutes and carefully close all the appropriate tickets linked in the discussion above, so I'll officially close this tomorrow.\n\nI'm going to be bold and say that my one-character patch doesn't really need a review; if someone wants to agree that it's fine, that wouldn't be bad.",
    "created_at": "2009-06-11T09:37:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6140#issuecomment-48937",
    "user": "https://github.com/craigcitro"
}
```

This looks good. I'm attaching a second patch for that one doctest failure. 

For the record, this spkg and the two patches have been merged in `4.0.2.alpha0` -- but I want to take a few minutes and carefully close all the appropriate tickets linked in the discussion above, so I'll officially close this tomorrow.

I'm going to be bold and say that my one-character patch doesn't really need a review; if someone wants to agree that it's fine, that wouldn't be bad.



---

archive/issue_comments_048938.json:
```json
{
    "body": "Attachment [trac-6140-pt2.patch](tarball://root/attachments/some-uuid/ticket6140/trac-6140-pt2.patch) by @craigcitro created at 2009-06-11 09:38:03\n\napply after spkg and patch above",
    "created_at": "2009-06-11T09:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6140#issuecomment-48938",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-6140-pt2.patch](tarball://root/attachments/some-uuid/ticket6140/trac-6140-pt2.patch) by @craigcitro created at 2009-06-11 09:38:03

apply after spkg and patch above



---

archive/issue_events_006389.json:
```json
{
    "actor": "@craigcitro",
    "created_at": "2009-06-12T06:56:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6140",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6140#event-6389"
}
```



---

archive/issue_comments_048939.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-12T06:56:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6140#issuecomment-48939",
    "user": "https://github.com/craigcitro"
}
```

Resolution: fixed



---

archive/issue_comments_048940.json:
```json
{
    "body": "spkg and patches merged in 4.0.2.alpha0.",
    "created_at": "2009-06-12T06:56:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6140#issuecomment-48940",
    "user": "https://github.com/craigcitro"
}
```

spkg and patches merged in 4.0.2.alpha0.
