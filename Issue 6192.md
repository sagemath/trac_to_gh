# Issue 6192: numerical noise on x86 fedora core 8 (cicero on skynet)

archive/issues_006192.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage -t  \"devel/sage/sage/calculus/calculus.py\"\n**********************************************************************\nFile \"/home/wstein/build-4.4.0/cicero/sage-4.0.1.alpha0/devel/sage/sage/calculus/calculus.py\", line 700:\n    sage: numerical_integral(f, 0, 1)\nExpected:\n    (0.52848223225314706, 6.8392846084921134e-07)\nGot:\n    (0.52848223225314706, 6.8392846078917534e-07)\n**********************************************************************\n1 items had failures:\n   1 of  16 in __main__.example_2\n```\n\n\nNoise or a bug?\n\n```\nsage -t  \"devel/sage/sage/rings/number_field/number_field_element.pyx\"\n**********************************************************************\nFile \"/home/wstein/build-4.4.0/cicero/sage-4.0.1.alpha0/devel/sage/sage/rings/number_field/number_field_element.pyx\", line \n766:\n    sage: CDF(a)\nExpected:\n    1.0*I\nGot:\n    -2.88668828424e-18 - 1.0*I\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_21\n***Test Failed*** 1 failures.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6192\n\n",
    "created_at": "2009-06-02T21:56:13Z",
    "labels": [
        "algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "numerical noise on x86 fedora core 8 (cicero on skynet)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6192",
    "user": "@williamstein"
}
```
Assignee: tbd


```
sage -t  "devel/sage/sage/calculus/calculus.py"
**********************************************************************
File "/home/wstein/build-4.4.0/cicero/sage-4.0.1.alpha0/devel/sage/sage/calculus/calculus.py", line 700:
    sage: numerical_integral(f, 0, 1)
Expected:
    (0.52848223225314706, 6.8392846084921134e-07)
Got:
    (0.52848223225314706, 6.8392846078917534e-07)
**********************************************************************
1 items had failures:
   1 of  16 in __main__.example_2
```


Noise or a bug?

```
sage -t  "devel/sage/sage/rings/number_field/number_field_element.pyx"
**********************************************************************
File "/home/wstein/build-4.4.0/cicero/sage-4.0.1.alpha0/devel/sage/sage/rings/number_field/number_field_element.pyx", line 
766:
    sage: CDF(a)
Expected:
    1.0*I
Got:
    -2.88668828424e-18 - 1.0*I
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_21
***Test Failed*** 1 failures.
```


Issue created by migration from https://trac.sagemath.org/ticket/6192





---

archive/issue_comments_049456.json:
```json
{
    "body": "The second issue is because the roots of x^2+1 are \"sorted\" as complex numbers, and because of numerical noise, the roots are swapped.",
    "created_at": "2009-06-02T22:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6192#issuecomment-49456",
    "user": "@williamstein"
}
```

The second issue is because the roots of x^2+1 are "sorted" as complex numbers, and because of numerical noise, the roots are swapped.



---

archive/issue_comments_049457.json:
```json
{
    "body": "Attachment [trac_6192.patch](tarball://root/attachments/some-uuid/ticket6192/trac_6192.patch) by @williamstein created at 2009-06-02 22:04:42",
    "created_at": "2009-06-02T22:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6192#issuecomment-49457",
    "user": "@williamstein"
}
```

Attachment [trac_6192.patch](tarball://root/attachments/some-uuid/ticket6192/trac_6192.patch) by @williamstein created at 2009-06-02 22:04:42



---

archive/issue_comments_049458.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T06:29:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6192#issuecomment-49458",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_049459.json:
```json
{
    "body": "Looks good to me.\n\nMerged in 4.0.1.rc0.",
    "created_at": "2009-06-04T06:29:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6192#issuecomment-49459",
    "user": "@mwhansen"
}
```

Looks good to me.

Merged in 4.0.1.rc0.
