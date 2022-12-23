# Issue 1919: improve base fields of DualAbelainGroup

archive/issues_001919.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  tscrim jhpalmieri\n\nIn sage/groups/abelian_gps/dual_abelian_group_element.py, the __call__\nmethod uses some code which must be modified if the base field is finite.\nSpecifically, \"zeta = F.gen()\" must be changed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1919\n\n",
    "created_at": "2008-01-25T02:41:58Z",
    "labels": [
        "group theory",
        "minor",
        "enhancement"
    ],
    "title": "improve base fields of DualAbelainGroup",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1919",
    "user": "wdj"
}
```
Assignee: joyner

CC:  tscrim jhpalmieri

In sage/groups/abelian_gps/dual_abelian_group_element.py, the __call__
method uses some code which must be modified if the base field is finite.
Specifically, "zeta = F.gen()" must be changed.

Issue created by migration from https://trac.sagemath.org/ticket/1919





---

archive/issue_comments_012163.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-09-13T19:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1919#issuecomment-12163",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_012164.json:
```json
{
    "body": "New commits:",
    "created_at": "2017-09-13T19:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1919#issuecomment-12164",
    "user": "chapoton"
}
```

New commits:



---

archive/issue_comments_012165.json:
```json
{
    "body": "another interesting one, simple enough",
    "created_at": "2017-09-20T18:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1919#issuecomment-12165",
    "user": "chapoton"
}
```

another interesting one, simple enough



---

archive/issue_comments_012166.json:
```json
{
    "body": "LGTM.",
    "created_at": "2017-09-20T21:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1919#issuecomment-12166",
    "user": "tscrim"
}
```

LGTM.



---

archive/issue_comments_012167.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-09-20T21:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1919#issuecomment-12167",
    "user": "tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_012168.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-09-24T13:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1919#issuecomment-12168",
    "user": "vbraun"
}
```

Resolution: fixed
