# Issue 2201: [with patch, needs review] doctest failure on 2.10.2.alpha0: number_field.py

archive/issues_002201.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @jaapspies\n\nJaap reported the following doctest failure on sage-devel:\n\n\n```\njaap@paix sage-2.10.2.alpha0]$ ./sage -t  devel/sage-main/sage/rings/number_field/number_field.py\nsage -t  devel/sage-main/sage/rings/number_field/number_field.py**********************************************************************\nFile \"number_field.py\", line 2087:\n    sage: F.reduced_basis()\nExpected:\n    [1, alpha, alpha^2 - 15*alpha + 1, alpha^3 - 16*alpha^2 + 469*alpha + 267109]\nGot:\n    [1, alpha, alpha^2 - 15*alpha, alpha^3 - 16*alpha^2 + 469*alpha + 267109]\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_60\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_number_field.py\n         [33.8 s]\nexit code: 256\n```\n\n\nThis is due to different precision getting used to compute an embedding somewhere -- the fix was to add an optional `prec` argument, which is useful in its own right, and then make the doctests call with a specific precision. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2201\n\n",
    "created_at": "2008-02-18T01:24:56Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch, needs review] doctest failure on 2.10.2.alpha0: number_field.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2201",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

CC:  @jaapspies

Jaap reported the following doctest failure on sage-devel:


```
jaap@paix sage-2.10.2.alpha0]$ ./sage -t  devel/sage-main/sage/rings/number_field/number_field.py
sage -t  devel/sage-main/sage/rings/number_field/number_field.py**********************************************************************
File "number_field.py", line 2087:
    sage: F.reduced_basis()
Expected:
    [1, alpha, alpha^2 - 15*alpha + 1, alpha^3 - 16*alpha^2 + 469*alpha + 267109]
Got:
    [1, alpha, alpha^2 - 15*alpha, alpha^3 - 16*alpha^2 + 469*alpha + 267109]
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_60
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_number_field.py
         [33.8 s]
exit code: 256
```


This is due to different precision getting used to compute an embedding somewhere -- the fix was to add an optional `prec` argument, which is useful in its own right, and then make the doctests call with a specific precision. 

Issue created by migration from https://trac.sagemath.org/ticket/2201





---

archive/issue_comments_014454.json:
```json
{
    "body": "Attachment [trac-2201.patch](tarball://root/attachments/some-uuid/ticket2201/trac-2201.patch) by @craigcitro created at 2008-02-18 01:25:27",
    "created_at": "2008-02-18T01:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2201#issuecomment-14454",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-2201.patch](tarball://root/attachments/some-uuid/ticket2201/trac-2201.patch) by @craigcitro created at 2008-02-18 01:25:27



---

archive/issue_comments_014455.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-18T01:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2201#issuecomment-14455",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014456.json:
```json
{
    "body": "I just realized that this patch is against 2.10.1 + patches from 1085 -- I don't think this should cause any trouble, since it only touches one file, but if it does, I'll rebase it.",
    "created_at": "2008-02-18T01:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2201#issuecomment-14456",
    "user": "https://github.com/craigcitro"
}
```

I just realized that this patch is against 2.10.1 + patches from 1085 -- I don't think this should cause any trouble, since it only touches one file, but if it does, I'll rebase it.



---

archive/issue_comments_014457.json:
```json
{
    "body": "Couldn't apply the patch tos sage-2.10.2.alpha.\n\nJaap",
    "created_at": "2008-02-18T11:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2201#issuecomment-14457",
    "user": "https://github.com/jaapspies"
}
```

Couldn't apply the patch tos sage-2.10.2.alpha.

Jaap



---

archive/issue_comments_014458.json:
```json
{
    "body": "Just applied the patch by hand and it works:\n\n\n```\n\n[jaap@paix sage-2.10.2.alpha0]$ ./sage -t  devel/sage-main/sage/rings/number_field/number_field.py\nsage -t  devel/sage-main/sage/rings/number_field/number_field.py\n         [21.3 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 21.3 seconds\n\n```\n",
    "created_at": "2008-02-18T12:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2201#issuecomment-14458",
    "user": "https://github.com/jaapspies"
}
```

Just applied the patch by hand and it works:


```

[jaap@paix sage-2.10.2.alpha0]$ ./sage -t  devel/sage-main/sage/rings/number_field/number_field.py
sage -t  devel/sage-main/sage/rings/number_field/number_field.py
         [21.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 21.3 seconds

```




---

archive/issue_comments_014459.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-18T13:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2201#issuecomment-14459",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002367.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-18T13:34:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2201",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2201#event-2367"
}
```



---

archive/issue_comments_014460.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-18T13:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2201#issuecomment-14460",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha1



---

archive/issue_comments_014461.json:
```json
{
    "body": "FYI: This patch fixes the doctest issue on sage.math, too.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-18T17:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2201#issuecomment-14461",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

FYI: This patch fixes the doctest issue on sage.math, too.

Cheers,

Michael
