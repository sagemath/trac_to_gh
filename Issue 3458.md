# Issue 3458: parallel -- a very simple reference api for @parallel and parallel_eval

archive/issues_003458.json:
```json
{
    "body": "Assignee: yi\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3458\n\n",
    "created_at": "2008-06-18T03:14:08Z",
    "labels": [
        "dsage",
        "major",
        "enhancement"
    ],
    "title": "parallel -- a very simple reference api for @parallel and parallel_eval",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3458",
    "user": "was"
}
```
Assignee: yi



Issue created by migration from https://trac.sagemath.org/ticket/3458





---

archive/issue_comments_024379.json:
```json
{
    "body": "Attachment\n\nThis depends on #3453.",
    "created_at": "2008-06-18T03:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24379",
    "user": "was"
}
```

Attachment

This depends on #3453.



---

archive/issue_comments_024380.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-06-18T06:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24380",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_024381.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-06-18T08:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24381",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_024382.json:
```json
{
    "body": "first three patches have positive review",
    "created_at": "2008-06-19T00:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24382",
    "user": "was"
}
```

first three patches have positive review



---

archive/issue_comments_024383.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-06-19T01:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24383",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_024384.json:
```json
{
    "body": "Example test function:\n\n\n```\ndef MS1(N,k):\n    return ModularSymbols(N,k,sign=1).decomposition(10)[0]\n```\n\n\nTypical inputs:\n\n```\ntime v = MS1([(250,2), (11,2), (37,2)])\n```\n",
    "created_at": "2008-06-19T01:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24384",
    "user": "was"
}
```

Example test function:


```
def MS1(N,k):
    return ModularSymbols(N,k,sign=1).decomposition(10)[0]
```


Typical inputs:

```
time v = MS1([(250,2), (11,2), (37,2)])
```




---

archive/issue_comments_024385.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-06-19T02:47:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24385",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_024386.json:
```json
{
    "body": "patch 3 should not be used anymore since the p_iter implementation is in \n\n```\nsage.dsage.interface.parallel_iter\n```\n",
    "created_at": "2008-06-19T21:12:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24386",
    "user": "yi"
}
```

patch 3 should not be used anymore since the p_iter implementation is in 

```
sage.dsage.interface.parallel_iter
```




---

archive/issue_comments_024387.json:
```json
{
    "body": "patch 3 should still be applied since it changes things other then dsage.",
    "created_at": "2008-06-19T23:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24387",
    "user": "gfurnish"
}
```

patch 3 should still be applied since it changes things other then dsage.



---

archive/issue_comments_024388.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-06-20T01:30:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24388",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_024389.json:
```json
{
    "body": "Patch 6 does not apply for me after having applied the first 5 patches. Specifically, decorate.py, ncpus.py and multiprocessing.py result in .rej's. Can you post plain copies of those files?",
    "created_at": "2008-06-20T20:25:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24389",
    "user": "yi"
}
```

Patch 6 does not apply for me after having applied the first 5 patches. Specifically, decorate.py, ncpus.py and multiprocessing.py result in .rej's. Can you post plain copies of those files?



---

archive/issue_comments_024390.json:
```json
{
    "body": "This is a clean bundle that one can apply instead of all the patches.",
    "created_at": "2008-06-21T23:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24390",
    "user": "was"
}
```

This is a clean bundle that one can apply instead of all the patches.



---

archive/issue_comments_024391.json:
```json
{
    "body": "Attachment\n\nYi: bundle posted.",
    "created_at": "2008-06-21T23:53:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24391",
    "user": "was"
}
```

Attachment

Yi: bundle posted.



---

archive/issue_comments_024392.json:
```json
{
    "body": "Updated bundle which uses sage.dsage.interface.dsage_interface.BlockingDSage's parallel_iter instead of the one supplied in the bundle. This will only work after #3467 gets merged in.",
    "created_at": "2008-06-23T20:04:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24392",
    "user": "yi"
}
```

Updated bundle which uses sage.dsage.interface.dsage_interface.BlockingDSage's parallel_iter instead of the one supplied in the bundle. This will only work after #3467 gets merged in.



---

archive/issue_comments_024393.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-06-24T03:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24393",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_024394.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_wstein\".",
    "created_at": "2008-06-24T03:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24394",
    "user": "was"
}
```

Changing keywords from "" to "editor_wstein".



---

archive/issue_comments_024395.json:
```json
{
    "body": "Patch looks great. Doctests pass on 3.0.3 OS X 10.5.",
    "created_at": "2008-06-26T02:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24395",
    "user": "yi"
}
```

Patch looks great. Doctests pass on 3.0.3 OS X 10.5.



---

archive/issue_comments_024396.json:
```json
{
    "body": "Merged sage-3458-fixed.hg in Sage 3.0.4.alpha1",
    "created_at": "2008-06-26T04:22:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24396",
    "user": "mabshoff"
}
```

Merged sage-3458-fixed.hg in Sage 3.0.4.alpha1



---

archive/issue_comments_024397.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-26T04:22:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24397",
    "user": "mabshoff"
}
```

Resolution: fixed
