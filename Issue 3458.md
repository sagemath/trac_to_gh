# Issue 3458: parallel -- a very simple reference api for @parallel and parallel_eval

archive/issues_003458.json:
```json
{
    "body": "Assignee: @yqiang\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3458\n\n",
    "created_at": "2008-06-18T03:14:08Z",
    "labels": [
        "component: dsage"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "parallel -- a very simple reference api for @parallel and parallel_eval",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3458",
    "user": "https://github.com/williamstein"
}
```
Assignee: @yqiang



Issue created by migration from https://trac.sagemath.org/ticket/3458





---

archive/issue_comments_024330.json:
```json
{
    "body": "Attachment [sage-3458.patch](tarball://root/attachments/some-uuid/ticket3458/sage-3458.patch) by @williamstein created at 2008-06-18 03:15:04\n\nThis depends on #3453.",
    "created_at": "2008-06-18T03:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24330",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3458.patch](tarball://root/attachments/some-uuid/ticket3458/sage-3458.patch) by @williamstein created at 2008-06-18 03:15:04

This depends on #3453.



---

archive/issue_comments_024331.json:
```json
{
    "body": "Attachment [sage-3458-part2.patch](tarball://root/attachments/some-uuid/ticket3458/sage-3458-part2.patch) by @williamstein created at 2008-06-18 06:30:09",
    "created_at": "2008-06-18T06:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24331",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3458-part2.patch](tarball://root/attachments/some-uuid/ticket3458/sage-3458-part2.patch) by @williamstein created at 2008-06-18 06:30:09



---

archive/issue_comments_024332.json:
```json
{
    "body": "Attachment [sage-3458-part3.patch](tarball://root/attachments/some-uuid/ticket3458/sage-3458-part3.patch) by @williamstein created at 2008-06-18 08:52:06",
    "created_at": "2008-06-18T08:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24332",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3458-part3.patch](tarball://root/attachments/some-uuid/ticket3458/sage-3458-part3.patch) by @williamstein created at 2008-06-18 08:52:06



---

archive/issue_comments_024333.json:
```json
{
    "body": "first three patches have positive review",
    "created_at": "2008-06-19T00:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24333",
    "user": "https://github.com/williamstein"
}
```

first three patches have positive review



---

archive/issue_comments_024334.json:
```json
{
    "body": "Attachment [sage-3458-part4.patch](tarball://root/attachments/some-uuid/ticket3458/sage-3458-part4.patch) by @mwhansen created at 2008-06-19 01:33:45",
    "created_at": "2008-06-19T01:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24334",
    "user": "https://github.com/mwhansen"
}
```

Attachment [sage-3458-part4.patch](tarball://root/attachments/some-uuid/ticket3458/sage-3458-part4.patch) by @mwhansen created at 2008-06-19 01:33:45



---

archive/issue_events_007849.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-06-19T01:35:27Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "milestone": "sage-3.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3458#event-7849"
}
```



---

archive/issue_comments_024335.json:
```json
{
    "body": "Example test function:\n\n\n```\ndef MS1(N,k):\n    return ModularSymbols(N,k,sign=1).decomposition(10)[0]\n```\n\n\nTypical inputs:\n\n```\ntime v = MS1([(250,2), (11,2), (37,2)])\n```\n",
    "created_at": "2008-06-19T01:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24335",
    "user": "https://github.com/williamstein"
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

archive/issue_comments_024336.json:
```json
{
    "body": "Attachment [sage-3458-processing.patch](tarball://root/attachments/some-uuid/ticket3458/sage-3458-processing.patch) by @mwhansen created at 2008-06-19 02:47:09",
    "created_at": "2008-06-19T02:47:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24336",
    "user": "https://github.com/mwhansen"
}
```

Attachment [sage-3458-processing.patch](tarball://root/attachments/some-uuid/ticket3458/sage-3458-processing.patch) by @mwhansen created at 2008-06-19 02:47:09



---

archive/issue_comments_024337.json:
```json
{
    "body": "patch 3 should not be used anymore since the p_iter implementation is in \n\n```\nsage.dsage.interface.parallel_iter\n```\n",
    "created_at": "2008-06-19T21:12:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24337",
    "user": "https://github.com/yqiang"
}
```

patch 3 should not be used anymore since the p_iter implementation is in 

```
sage.dsage.interface.parallel_iter
```




---

archive/issue_comments_024338.json:
```json
{
    "body": "patch 3 should still be applied since it changes things other then dsage.",
    "created_at": "2008-06-19T23:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24338",
    "user": "https://github.com/garyfurnish"
}
```

patch 3 should still be applied since it changes things other then dsage.



---

archive/issue_comments_024339.json:
```json
{
    "body": "Attachment [sage-3458-part6.patch](tarball://root/attachments/some-uuid/ticket3458/sage-3458-part6.patch) by @williamstein created at 2008-06-20 01:30:36",
    "created_at": "2008-06-20T01:30:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24339",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3458-part6.patch](tarball://root/attachments/some-uuid/ticket3458/sage-3458-part6.patch) by @williamstein created at 2008-06-20 01:30:36



---

archive/issue_comments_024340.json:
```json
{
    "body": "Patch 6 does not apply for me after having applied the first 5 patches. Specifically, decorate.py, ncpus.py and multiprocessing.py result in .rej's. Can you post plain copies of those files?",
    "created_at": "2008-06-20T20:25:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24340",
    "user": "https://github.com/yqiang"
}
```

Patch 6 does not apply for me after having applied the first 5 patches. Specifically, decorate.py, ncpus.py and multiprocessing.py result in .rej's. Can you post plain copies of those files?



---

archive/issue_comments_024341.json:
```json
{
    "body": "This is a clean bundle that one can apply instead of all the patches.",
    "created_at": "2008-06-21T23:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24341",
    "user": "https://github.com/williamstein"
}
```

This is a clean bundle that one can apply instead of all the patches.



---

archive/issue_comments_024342.json:
```json
{
    "body": "Attachment [sage-3458.hg](tarball://root/attachments/some-uuid/ticket3458/sage-3458.hg) by @williamstein created at 2008-06-21 23:53:56\n\nYi: bundle posted.",
    "created_at": "2008-06-21T23:53:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24342",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3458.hg](tarball://root/attachments/some-uuid/ticket3458/sage-3458.hg) by @williamstein created at 2008-06-21 23:53:56

Yi: bundle posted.



---

archive/issue_comments_024343.json:
```json
{
    "body": "Updated bundle which uses sage.dsage.interface.dsage_interface.BlockingDSage's parallel_iter instead of the one supplied in the bundle. This will only work after #3467 gets merged in.",
    "created_at": "2008-06-23T20:04:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24343",
    "user": "https://github.com/yqiang"
}
```

Updated bundle which uses sage.dsage.interface.dsage_interface.BlockingDSage's parallel_iter instead of the one supplied in the bundle. This will only work after #3467 gets merged in.



---

archive/issue_comments_024344.json:
```json
{
    "body": "Attachment [sage-3458-fixed.hg](tarball://root/attachments/some-uuid/ticket3458/sage-3458-fixed.hg) by @williamstein created at 2008-06-24 03:04:45",
    "created_at": "2008-06-24T03:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24344",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3458-fixed.hg](tarball://root/attachments/some-uuid/ticket3458/sage-3458-fixed.hg) by @williamstein created at 2008-06-24 03:04:45



---

archive/issue_comments_024345.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_wstein\".",
    "created_at": "2008-06-24T03:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24345",
    "user": "https://github.com/williamstein"
}
```

Changing keywords from "" to "editor_wstein".



---

archive/issue_comments_024346.json:
```json
{
    "body": "Patch looks great. Doctests pass on 3.0.3 OS X 10.5.",
    "created_at": "2008-06-26T02:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24346",
    "user": "https://github.com/yqiang"
}
```

Patch looks great. Doctests pass on 3.0.3 OS X 10.5.



---

archive/issue_comments_024347.json:
```json
{
    "body": "Merged sage-3458-fixed.hg in Sage 3.0.4.alpha1",
    "created_at": "2008-06-26T04:22:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24347",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged sage-3458-fixed.hg in Sage 3.0.4.alpha1



---

archive/issue_comments_024348.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-26T04:22:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3458#issuecomment-24348",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_007850.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-26T04:22:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3458#event-7850"
}
```



---

archive/issue_events_007851.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-26T04:22:26Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "milestone": "sage-3.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3458#event-7851"
}
```



---

archive/issue_events_007852.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-26T04:22:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3458",
    "milestone": "sage-3.0.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3458#event-7852"
}
```
