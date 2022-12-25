# Issue 2372: [with patch, needs review] speedup to matrix_from_rows_and_columns

archive/issues_002372.json:
```json
{
    "body": "Assignee: @dfdeshom\n\nWe make `matrix_from_rows_and_columns` a little faster by using well-known pyrex tricks.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2372\n\n",
    "created_at": "2008-03-03T05:32:28Z",
    "labels": [
        "component: linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with patch, needs review] speedup to matrix_from_rows_and_columns",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2372",
    "user": "https://github.com/dfdeshom"
}
```
Assignee: @dfdeshom

We make `matrix_from_rows_and_columns` a little faster by using well-known pyrex tricks.

Issue created by migration from https://trac.sagemath.org/ticket/2372





---

archive/issue_comments_015969.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-03T05:34:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2372#issuecomment-15969",
    "user": "https://github.com/dfdeshom"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015970.json:
```json
{
    "body": "Note: this is closely related to #2355, since speeding up  `matrix_from_rows_and_columns` will speed up `matrix.__getitem__()`",
    "created_at": "2008-03-03T15:23:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2372#issuecomment-15970",
    "user": "https://github.com/dfdeshom"
}
```

Note: this is closely related to #2355, since speeding up  `matrix_from_rows_and_columns` will speed up `matrix.__getitem__()`



---

archive/issue_comments_015971.json:
```json
{
    "body": "This patch looks cleaner(?)",
    "created_at": "2008-03-12T13:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2372#issuecomment-15971",
    "user": "https://github.com/jaapspies"
}
```

This patch looks cleaner(?)



---

archive/issue_comments_015972.json:
```json
{
    "body": "Attachment [trac_2490.patch](tarball://root/attachments/some-uuid/ticket2372/trac_2490.patch) by @jaapspies created at 2008-03-12 13:52:57\n\nSorry for the duplicate! I missed that. But I could not resist to send my patch!\n\nWhat do you think?\n\nCheers,\n\nJaap",
    "created_at": "2008-03-12T13:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2372#issuecomment-15972",
    "user": "https://github.com/jaapspies"
}
```

Attachment [trac_2490.patch](tarball://root/attachments/some-uuid/ticket2372/trac_2490.patch) by @jaapspies created at 2008-03-12 13:52:57

Sorry for the duplicate! I missed that. But I could not resist to send my patch!

What do you think?

Cheers,

Jaap



---

archive/issue_comments_015973.json:
```json
{
    "body": "Replying to [comment:4 jsp]:\n> Sorry for the duplicate! I missed that. But I could not resist to send my patch!\n> \n> What do you think?\n> \n> Cheers,\n> \n> Jaap\n> \n\nHi Jaap,\nI'm willing to sacrifice a little elegance for speed gains. My function seems to be faster so far:\n\n```\nsage:  w = random_matrix(ZZ,2000,2000)\n\nsage: %time w.matrix_from_rows_and_columns(range(1000),range(1300));\nCPU times: user 0.42 s, sys: 0.13 s, total: 0.55 s\nWall time: 0.55\n\nsage: %time w.matrix_from_rows_and_columns(range(1000),range(1300));\nCPU times: user 0.48 s, sys: 0.05 s, total: 0.53 s\nWall time: 0.54\n\nsage: %time w.matrix_from_rows_and_columns(range(1000),range(1300));\nCPU times: user 0.49 s, sys: 0.05 s, total: 0.54 s\nWall time: 0.53\n```\n\n\nvs\n\n```\nLoading SAGE library. Current Mercurial branch is: jaap\n\nsage:  w = random_matrix(ZZ,2000,2000)\n\nsage: %time w.matrix_from_rows_and_columns(range(1000),range(1300));\nCPU times: user 0.73 s, sys: 0.12 s, total: 0.84 s\nWall time: 0.84\n\nsage: %time w.matrix_from_rows_and_columns(range(1000),range(1300));\nCPU times: user 0.74 s, sys: 0.10 s, total: 0.84 s\nWall time: 0.84\n\nsage: %time w.matrix_from_rows_and_columns(range(1000),range(1300));\nCPU times: user 0.72 s, sys: 0.12 s, total: 0.84 s\nWall time: 0.83\n```\n\n\nAll times are on sage.math. If you can do better, great :)",
    "created_at": "2008-03-12T18:34:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2372#issuecomment-15973",
    "user": "https://github.com/dfdeshom"
}
```

Replying to [comment:4 jsp]:
> Sorry for the duplicate! I missed that. But I could not resist to send my patch!
> 
> What do you think?
> 
> Cheers,
> 
> Jaap
> 

Hi Jaap,
I'm willing to sacrifice a little elegance for speed gains. My function seems to be faster so far:

```
sage:  w = random_matrix(ZZ,2000,2000)

sage: %time w.matrix_from_rows_and_columns(range(1000),range(1300));
CPU times: user 0.42 s, sys: 0.13 s, total: 0.55 s
Wall time: 0.55

sage: %time w.matrix_from_rows_and_columns(range(1000),range(1300));
CPU times: user 0.48 s, sys: 0.05 s, total: 0.53 s
Wall time: 0.54

sage: %time w.matrix_from_rows_and_columns(range(1000),range(1300));
CPU times: user 0.49 s, sys: 0.05 s, total: 0.54 s
Wall time: 0.53
```


vs

```
Loading SAGE library. Current Mercurial branch is: jaap

sage:  w = random_matrix(ZZ,2000,2000)

sage: %time w.matrix_from_rows_and_columns(range(1000),range(1300));
CPU times: user 0.73 s, sys: 0.12 s, total: 0.84 s
Wall time: 0.84

sage: %time w.matrix_from_rows_and_columns(range(1000),range(1300));
CPU times: user 0.74 s, sys: 0.10 s, total: 0.84 s
Wall time: 0.84

sage: %time w.matrix_from_rows_and_columns(range(1000),range(1300));
CPU times: user 0.72 s, sys: 0.12 s, total: 0.84 s
Wall time: 0.83
```


All times are on sage.math. If you can do better, great :)



---

archive/issue_comments_015974.json:
```json
{
    "body": "Ok, time is money. So I better give a positive review.\n\nOne question before I do so:\nwhy not cdef i an j?\n\n```\n        cdef Py_ssize_t nrows, ncols,i,j,k,r\n\n```\n\n\nAll test in deve/sage/sage/matrix passed.",
    "created_at": "2008-03-14T13:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2372#issuecomment-15974",
    "user": "https://github.com/jaapspies"
}
```

Ok, time is money. So I better give a positive review.

One question before I do so:
why not cdef i an j?

```
        cdef Py_ssize_t nrows, ncols,i,j,k,r

```


All test in deve/sage/sage/matrix passed.



---

archive/issue_comments_015975.json:
```json
{
    "body": "Attachment [2372.patch](tarball://root/attachments/some-uuid/ticket2372/2372.patch) by @dfdeshom created at 2008-03-14 14:36:27",
    "created_at": "2008-03-14T14:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2372#issuecomment-15975",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [2372.patch](tarball://root/attachments/some-uuid/ticket2372/2372.patch) by @dfdeshom created at 2008-03-14 14:36:27



---

archive/issue_comments_015976.json:
```json
{
    "body": "Replying to [comment:6 jsp]:\n> why not cdef i an j?\n> {{{\n>         cdef Py_ssize_t nrows, ncols,i,j,k,r\n> \n> }}}\n\nGood point. I've added these declarations and updated the patch (2372.patch). All tests in sage/matrix pass.",
    "created_at": "2008-03-14T14:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2372#issuecomment-15976",
    "user": "https://github.com/dfdeshom"
}
```

Replying to [comment:6 jsp]:
> why not cdef i an j?
> {{{
>         cdef Py_ssize_t nrows, ncols,i,j,k,r
> 
> }}}

Good point. I've added these declarations and updated the patch (2372.patch). All tests in sage/matrix pass.



---

archive/issue_comments_015977.json:
```json
{
    "body": "I had that tested already :)",
    "created_at": "2008-03-14T18:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2372#issuecomment-15977",
    "user": "https://github.com/jaapspies"
}
```

I had that tested already :)



---

archive/issue_comments_015978.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-16T00:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2372#issuecomment-15978",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002549.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-16T00:01:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2372",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2372#event-2549"
}
```



---

archive/issue_comments_015979.json:
```json
{
    "body": "Merged 2372.patch in Sage 2.10.4.rc0",
    "created_at": "2008-03-16T00:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2372#issuecomment-15979",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 2372.patch in Sage 2.10.4.rc0
