# Issue 982: abs(x) returns incorrect LaTex

archive/issues_000982.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: f = abs(x)\nsage: latex(f)\n\\abs \\left( x \\right)\n```\n\n\nbut it should be\n\n\n```\nsage: latex(f)\n\\mathrm{abs} \\left| x \\right|\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/982\n\n",
    "created_at": "2007-10-24T17:39:00Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "abs(x) returns incorrect LaTex",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/982",
    "user": "mhansen"
}
```
Assignee: was


```
sage: f = abs(x)
sage: latex(f)
\abs \left( x \right)
```


but it should be


```
sage: latex(f)
\mathrm{abs} \left| x \right|
```


Issue created by migration from https://trac.sagemath.org/ticket/982





---

archive/issue_comments_006009.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2007-10-24T17:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/982#issuecomment-6009",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_006010.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-24T17:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/982#issuecomment-6010",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006011.json:
```json
{
    "body": "Oops.  I mean to write, it should be:\n\n```\nsage: latex(abs)\n\\mathrm{abs}\nsage: latex(abs(x))\n\\left| x \\right|\n```\n",
    "created_at": "2007-10-24T17:42:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/982#issuecomment-6011",
    "user": "mhansen"
}
```

Oops.  I mean to write, it should be:

```
sage: latex(abs)
\mathrm{abs}
sage: latex(abs(x))
\left| x \right|
```




---

archive/issue_comments_006012.json:
```json
{
    "body": "Attachment [982.patch](tarball://root/attachments/some-uuid/ticket982/982.patch) by mhansen created at 2007-10-24 17:50:02",
    "created_at": "2007-10-24T17:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/982#issuecomment-6012",
    "user": "mhansen"
}
```

Attachment [982.patch](tarball://root/attachments/some-uuid/ticket982/982.patch) by mhansen created at 2007-10-24 17:50:02



---

archive/issue_comments_006013.json:
```json
{
    "body": "Replying to [comment:1 mhansen]:",
    "created_at": "2007-10-24T17:50:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/982#issuecomment-6013",
    "user": "mhansen"
}
```

Replying to [comment:1 mhansen]:



---

archive/issue_comments_006014.json:
```json
{
    "body": "applied to 2.8.9.alpha1",
    "created_at": "2007-10-24T19:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/982#issuecomment-6014",
    "user": "malb"
}
```

applied to 2.8.9.alpha1



---

archive/issue_comments_006015.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-24T19:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/982#issuecomment-6015",
    "user": "malb"
}
```

Resolution: fixed
