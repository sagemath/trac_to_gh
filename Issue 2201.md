# Issue 2201: [with patch, needs review] doctest failure on 2.10.2.alpha0: number_field.py

archive/issues_002201.json:
```json
{
    "body": "Assignee: craigcitro\n\nCC:  jsp\n\nJaap reported the following doctest failure on sage-devel:\n\n\n```\njaap@paix sage-2.10.2.alpha0]$ ./sage -t  devel/sage-main/sage/rings/number_field/number_field.py\nsage -t  devel/sage-main/sage/rings/number_field/number_field.py**********************************************************************\nFile \"number_field.py\", line 2087:\n    sage: F.reduced_basis()\nExpected:\n    [1, alpha, alpha^2 - 15*alpha + 1, alpha^3 - 16*alpha^2 + 469*alpha + 267109]\nGot:\n    [1, alpha, alpha^2 - 15*alpha, alpha^3 - 16*alpha^2 + 469*alpha + 267109]\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_60\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_number_field.py\n         [33.8 s]\nexit code: 256\n```\n\n\nThis is due to different precision getting used to compute an embedding somewhere -- the fix was to add an optional `prec` argument, which is useful in its own right, and then make the doctests call with a specific precision. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2201\n\n",
    "created_at": "2008-02-18T01:24:56Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] doctest failure on 2.10.2.alpha0: number_field.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2201",
    "user": "craigcitro"
}
```
Assignee: craigcitro

CC:  jsp

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

archive/issue_comments_014485.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-18T01:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2201#issuecomment-14485",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_014486.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-18T01:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2201#issuecomment-14486",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014487.json:
```json
{
    "body": "I just realized that this patch is against 2.10.1 + patches from 1085 -- I don't think this should cause any trouble, since it only touches one file, but if it does, I'll rebase it.",
    "created_at": "2008-02-18T01:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2201#issuecomment-14487",
    "user": "craigcitro"
}
```

I just realized that this patch is against 2.10.1 + patches from 1085 -- I don't think this should cause any trouble, since it only touches one file, but if it does, I'll rebase it.



---

archive/issue_comments_014488.json:
```json
{
    "body": "Couldn't apply the patch tos sage-2.10.2.alpha.\n\nJaap",
    "created_at": "2008-02-18T11:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2201#issuecomment-14488",
    "user": "jsp"
}
```

Couldn't apply the patch tos sage-2.10.2.alpha.

Jaap



---

archive/issue_comments_014489.json:
```json
{
    "body": "Just applied the patch by hand and it works:\n\n\n```\n\n[jaap@paix sage-2.10.2.alpha0]$ ./sage -t  devel/sage-main/sage/rings/number_field/number_field.py\nsage -t  devel/sage-main/sage/rings/number_field/number_field.py\n         [21.3 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 21.3 seconds\n\n```\n",
    "created_at": "2008-02-18T12:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2201#issuecomment-14489",
    "user": "jsp"
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

archive/issue_comments_014490.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-18T13:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2201#issuecomment-14490",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014491.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-18T13:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2201#issuecomment-14491",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha1



---

archive/issue_comments_014492.json:
```json
{
    "body": "FYI: This patch fixes the doctest issue on sage.math, too.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-18T17:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2201#issuecomment-14492",
    "user": "mabshoff"
}
```

FYI: This patch fixes the doctest issue on sage.math, too.

Cheers,

Michael
