# Issue 2350: The 2.10.2 behavior of show(list) should instead be available via plot(list, array=True)

archive/issues_002350.json:
```json
{
    "body": "Assignee: was\n\nshow changed behavior in 2.10.2, which surprised lots of people.\n\n* revert show to the previous behavior.\n\n* plot(list) does what it currently does (i.e., superimpose the plots)\n\n* plot(list, array=True) does what show does in 2.10.2 (i.e., put the\nplots into an array).\n\n* change the docs to show() to more clearly reflect the purpose of the\nfunction.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2350\n\n",
    "created_at": "2008-02-29T01:45:04Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "The 2.10.2 behavior of show(list) should instead be available via plot(list, array=True)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2350",
    "user": "jason"
}
```
Assignee: was

show changed behavior in 2.10.2, which surprised lots of people.

* revert show to the previous behavior.

* plot(list) does what it currently does (i.e., superimpose the plots)

* plot(list, array=True) does what show does in 2.10.2 (i.e., put the
plots into an array).

* change the docs to show() to more clearly reflect the purpose of the
function.


Issue created by migration from https://trac.sagemath.org/ticket/2350





---

archive/issue_comments_015783.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-29T01:45:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2350#issuecomment-15783",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015784.json:
```json
{
    "body": "Changing assignee from was to jason.",
    "created_at": "2008-02-29T01:45:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2350#issuecomment-15784",
    "user": "jason"
}
```

Changing assignee from was to jason.



---

archive/issue_comments_015785.json:
```json
{
    "body": "The ticket that introduced the mentioned changes is #1908",
    "created_at": "2008-03-03T20:05:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2350#issuecomment-15785",
    "user": "jason"
}
```

The ticket that introduced the mentioned changes is #1908



---

archive/issue_comments_015786.json:
```json
{
    "body": "Attachment [show-revert.patch](tarball://root/attachments/some-uuid/ticket2350/show-revert.patch) by jason created at 2008-03-03 22:41:24",
    "created_at": "2008-03-03T22:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2350#issuecomment-15786",
    "user": "jason"
}
```

Attachment [show-revert.patch](tarball://root/attachments/some-uuid/ticket2350/show-revert.patch) by jason created at 2008-03-03 22:41:24



---

archive/issue_comments_015787.json:
```json
{
    "body": "show-revert.patch takes care of the first item listed above.  Please don't close this ticket, though, as I'd like to do the rest of the items too.",
    "created_at": "2008-03-03T22:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2350#issuecomment-15787",
    "user": "jason"
}
```

show-revert.patch takes care of the first item listed above.  Please don't close this ticket, though, as I'd like to do the rest of the items too.



---

archive/issue_comments_015788.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-03-03T22:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2350#issuecomment-15788",
    "user": "jason"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_015789.json:
```json
{
    "body": "see #2380 for the remainder of the items; you can close this one after applying the patch.",
    "created_at": "2008-03-03T22:59:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2350#issuecomment-15789",
    "user": "jason"
}
```

see #2380 for the remainder of the items; you can close this one after applying the patch.



---

archive/issue_comments_015790.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc1",
    "created_at": "2008-03-03T23:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2350#issuecomment-15790",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc1



---

archive/issue_comments_015791.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-03T23:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2350#issuecomment-15791",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015792.json:
```json
{
    "body": "Oops, forgot to change the status in the summary.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-04T00:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2350#issuecomment-15792",
    "user": "mabshoff"
}
```

Oops, forgot to change the status in the summary.

Cheers,

Michael
