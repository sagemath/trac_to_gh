# Issue 6058: Add basic statistics functionality at the top level

archive/issues_006058.json:
```json
{
    "body": "Assignee: jkantor\n\nSage should provide basic statistics functionality at the top level.  These functions might use scipy.stats or R or a new native implementation.  For graphics in particular we should probably bypass R.  \n\nThis ticket will merely start this process with one patch, but will not completely address the needed functionality.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6058\n\n",
    "created_at": "2009-05-17T21:02:12Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Add basic statistics functionality at the top level",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6058",
    "user": "mhampton"
}
```
Assignee: jkantor

Sage should provide basic statistics functionality at the top level.  These functions might use scipy.stats or R or a new native implementation.  For graphics in particular we should probably bypass R.  

This ticket will merely start this process with one patch, but will not completely address the needed functionality.

Issue created by migration from https://trac.sagemath.org/ticket/6058





---

archive/issue_comments_048232.json:
```json
{
    "body": "A baby step towards top-level statistics",
    "created_at": "2009-05-17T21:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6058#issuecomment-48232",
    "user": "mhampton"
}
```

A baby step towards top-level statistics



---

archive/issue_comments_048233.json:
```json
{
    "body": "Attachment [trac_6058_basic_stats1.patch](tarball://root/attachments/some-uuid/ticket6058/trac_6058_basic_stats1.patch) by mhampton created at 2009-05-17 21:19:07\n\nComments are welcome on this very initial effort.",
    "created_at": "2009-05-17T21:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6058#issuecomment-48233",
    "user": "mhampton"
}
```

Attachment [trac_6058_basic_stats1.patch](tarball://root/attachments/some-uuid/ticket6058/trac_6058_basic_stats1.patch) by mhampton created at 2009-05-17 21:19:07

Comments are welcome on this very initial effort.



---

archive/issue_comments_048234.json:
```json
{
    "body": "Changing assignee from jkantor to mhampton.",
    "created_at": "2009-05-17T21:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6058#issuecomment-48234",
    "user": "mhampton"
}
```

Changing assignee from jkantor to mhampton.



---

archive/issue_comments_048235.json:
```json
{
    "body": "Changing component from numerical to statistics.",
    "created_at": "2009-05-17T21:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6058#issuecomment-48235",
    "user": "mhampton"
}
```

Changing component from numerical to statistics.



---

archive/issue_comments_048236.json:
```json
{
    "body": "Two quick comments:\n\n* With the mean function, dividing by `len(a_list)` is **really** dangerous -- for instance, if you give the function a collection of Python `int`s, then it will do Python `int` division -- so `3/2 = 1`, etc. Bad news.\n\n* Do we want to use the name `std` for standard deviation? Since the other systems (e.g. R) use that, we should have it available, but I would also like to have the full `standard_deviation` available (especially since we have `variance` as opposed to just `var`, for obvious reasons).",
    "created_at": "2009-05-17T22:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6058#issuecomment-48236",
    "user": "@craigcitro"
}
```

Two quick comments:

* With the mean function, dividing by `len(a_list)` is **really** dangerous -- for instance, if you give the function a collection of Python `int`s, then it will do Python `int` division -- so `3/2 = 1`, etc. Bad news.

* Do we want to use the name `std` for standard deviation? Since the other systems (e.g. R) use that, we should have it available, but I would also like to have the full `standard_deviation` available (especially since we have `variance` as opposed to just `var`, for obvious reasons).



---

archive/issue_comments_048237.json:
```json
{
    "body": "This apparently was done at around the same time as this was posted by #7197, and no one noticed.  Sorry, Marshall :( but on the plus side we have had this since Sage 4.3 :)\n\nTo release manager - this is invalid/dup.",
    "created_at": "2012-06-01T18:42:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6058#issuecomment-48237",
    "user": "@kcrisman"
}
```

This apparently was done at around the same time as this was posted by #7197, and no one noticed.  Sorry, Marshall :( but on the plus side we have had this since Sage 4.3 :)

To release manager - this is invalid/dup.



---

archive/issue_comments_048238.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-06-01T18:42:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6058#issuecomment-48238",
    "user": "@kcrisman"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_048239.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-06-02T12:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6058#issuecomment-48239",
    "user": "@jdemeyer"
}
```

Resolution: duplicate
