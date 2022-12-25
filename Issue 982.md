# Issue 982: abs(x) returns incorrect LaTex

archive/issues_000982.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: f = abs(x)\nsage: latex(f)\n\\abs \\left( x \\right)\n```\n\n\nbut it should be\n\n\n```\nsage: latex(f)\n\\mathrm{abs} \\left| x \\right|\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/982\n\n",
    "created_at": "2007-10-24T17:39:00Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "abs(x) returns incorrect LaTex",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/982",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @williamstein


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

archive/issue_comments_005989.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-10-24T17:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/982#issuecomment-5989",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_005990.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-24T17:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/982#issuecomment-5990",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005991.json:
```json
{
    "body": "Oops.  I mean to write, it should be:\n\n```\nsage: latex(abs)\n\\mathrm{abs}\nsage: latex(abs(x))\n\\left| x \\right|\n```\n",
    "created_at": "2007-10-24T17:42:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/982#issuecomment-5991",
    "user": "https://github.com/mwhansen"
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

archive/issue_comments_005992.json:
```json
{
    "body": "Attachment [982.patch](tarball://root/attachments/some-uuid/ticket982/982.patch) by @mwhansen created at 2007-10-24 17:50:02",
    "created_at": "2007-10-24T17:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/982#issuecomment-5992",
    "user": "https://github.com/mwhansen"
}
```

Attachment [982.patch](tarball://root/attachments/some-uuid/ticket982/982.patch) by @mwhansen created at 2007-10-24 17:50:02



---

archive/issue_comments_005993.json:
```json
{
    "body": "Replying to [comment:1 mhansen]:",
    "created_at": "2007-10-24T17:50:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/982#issuecomment-5993",
    "user": "https://github.com/mwhansen"
}
```

Replying to [comment:1 mhansen]:



---

archive/issue_comments_005994.json:
```json
{
    "body": "applied to 2.8.9.alpha1",
    "created_at": "2007-10-24T19:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/982#issuecomment-5994",
    "user": "https://github.com/malb"
}
```

applied to 2.8.9.alpha1



---

archive/issue_comments_005995.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-24T19:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/982#issuecomment-5995",
    "user": "https://github.com/malb"
}
```

Resolution: fixed
