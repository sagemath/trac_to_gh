# Issue 4811: doctesting line numbers in report are now completely broken.  They were fine ins age-3.2.1

archive/issues_004811.json:
```json
{
    "body": "Assignee: mabshoff\n\nTry breaking any doctest and you get stuff like this:\n\n```\nwas@sage:~/build/sage-3.2.2.alpha2$ ./sage -t devel/sage/sage/matrix/matrix_modn_dense.pyx\nsage -t  \"devel/sage/sage/matrix/matrix_modn_dense.pyx\"     \n**********************************************************************\nFile \"/home/was/build/sage-3.2.2.alpha2/devel/sage/sage/matrix/matrix_modn_dense.pyx\", line 276, in __main__.example_6\nFailed example:\n    m###line 554:_sage_    >>> m\n\n```\n\n\nNotice the line 276 there.   In the old sage:\n\n```\nwas@sage:~/d/sage/matrix$ sage -t matrix_modn_dense.pyx\nsage -t  \"devel/sage-main/sage/matrix/matrix_modn_dense.pyx\"**********************************************************************\nFile \"/home/was/s/devel/sage-main/sage/matrix/matrix_modn_dense.pyx\", line 554:\n    sage: m\nExpected:\n    [19 18 17]\n    [16 15 14]\n    [13 12 11]\nGot:\n```\n\n}}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/4811\n\n",
    "created_at": "2008-12-16T07:25:21Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "doctesting line numbers in report are now completely broken.  They were fine ins age-3.2.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4811",
    "user": "was"
}
```
Assignee: mabshoff

Try breaking any doctest and you get stuff like this:

```
was@sage:~/build/sage-3.2.2.alpha2$ ./sage -t devel/sage/sage/matrix/matrix_modn_dense.pyx
sage -t  "devel/sage/sage/matrix/matrix_modn_dense.pyx"     
**********************************************************************
File "/home/was/build/sage-3.2.2.alpha2/devel/sage/sage/matrix/matrix_modn_dense.pyx", line 276, in __main__.example_6
Failed example:
    m###line 554:_sage_    >>> m

```


Notice the line 276 there.   In the old sage:

```
was@sage:~/d/sage/matrix$ sage -t matrix_modn_dense.pyx
sage -t  "devel/sage-main/sage/matrix/matrix_modn_dense.pyx"**********************************************************************
File "/home/was/s/devel/sage-main/sage/matrix/matrix_modn_dense.pyx", line 554:
    sage: m
Expected:
    [19 18 17]
    [16 15 14]
    [13 12 11]
Got:
```

}}}

Issue created by migration from https://trac.sagemath.org/ticket/4811





---

archive/issue_comments_036473.json:
```json
{
    "body": "Attachment [trac_4811_bin.patch](tarball://root/attachments/some-uuid/ticket4811/trac_4811_bin.patch) by gfurnish created at 2008-12-16 07:37:39",
    "created_at": "2008-12-16T07:37:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4811#issuecomment-36473",
    "user": "gfurnish"
}
```

Attachment [trac_4811_bin.patch](tarball://root/attachments/some-uuid/ticket4811/trac_4811_bin.patch) by gfurnish created at 2008-12-16 07:37:39



---

archive/issue_comments_036474.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-16T07:37:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4811#issuecomment-36474",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036475.json:
```json
{
    "body": "Changing assignee from mabshoff to gfurnish.",
    "created_at": "2008-12-16T07:37:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4811#issuecomment-36475",
    "user": "gfurnish"
}
```

Changing assignee from mabshoff to gfurnish.



---

archive/issue_comments_036476.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-17T04:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4811#issuecomment-36476",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_036477.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-17T14:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4811#issuecomment-36477",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036478.json:
```json
{
    "body": "Merged in Sage 3.2.2.rc1",
    "created_at": "2008-12-17T14:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4811#issuecomment-36478",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.rc1
