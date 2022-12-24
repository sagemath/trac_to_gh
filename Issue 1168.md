# Issue 1168: asinh/acosh/atanh are only partially known to sage

archive/issues_001168.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: asinh(1)\n<type 'exceptions.NameError'>: name 'asinh' is not defined\nsage: asinh(x)\n<type 'exceptions.NameError'>: name 'asinh' is not defined\n```\n\nbut:\n\n```\nsage: integrate(1/sqrt(9+x^2), x)\nasinh(x/3)\nsage: (1.0).asinh()\n0.881373587019543\n```\n\nThe same holds for acosh and atanh.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1168\n\n",
    "created_at": "2007-11-13T22:58:42Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "asinh/acosh/atanh are only partially known to sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1168",
    "user": "zimmerma"
}
```
Assignee: was


```
sage: asinh(1)
<type 'exceptions.NameError'>: name 'asinh' is not defined
sage: asinh(x)
<type 'exceptions.NameError'>: name 'asinh' is not defined
```

but:

```
sage: integrate(1/sqrt(9+x^2), x)
asinh(x/3)
sage: (1.0).asinh()
0.881373587019543
```

The same holds for acosh and atanh.

Issue created by migration from https://trac.sagemath.org/ticket/1168





---

archive/issue_comments_007160.json:
```json
{
    "body": "This was fixed in an earlier patch.\n\n```\nsage: asinh(1)\nasinh(1)\nsage: asinh(x)\nasinh(x)\nsage: acosh(x)\nacosh(x)\nsage: atanh(x)\natanh(x)\n```\n",
    "created_at": "2007-11-30T23:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1168#issuecomment-7160",
    "user": "mhansen"
}
```

This was fixed in an earlier patch.

```
sage: asinh(1)
asinh(1)
sage: asinh(x)
asinh(x)
sage: acosh(x)
acosh(x)
sage: atanh(x)
atanh(x)
```




---

archive/issue_comments_007161.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-30T23:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1168#issuecomment-7161",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007162.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2007-11-30T23:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1168#issuecomment-7162",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_007163.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-30T23:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1168#issuecomment-7163",
    "user": "mhansen"
}
```

Resolution: fixed
