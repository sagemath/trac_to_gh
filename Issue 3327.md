# Issue 3327: missing .divides() implementation for FieldElement

archive/issues_003327.json:
```json
{
    "body": "Assignee: somebody\n\nThe generic .divides() implementation doesn't work for FieldElement; this causes the following problem:\n\n```\n  R.<a,b> = NumberField(x^2-3,'g')[]\n  S.<y> = R.fraction_field()[]\n  xgcd(y^2, a*y+b) \n```\n\ngoes BOOM (as reported by Ga\u00ebtan Bisson here: http://groups.google.com/group/sage-support/browse_thread/thread/5338608bd7508b00/76dd56341dc29b1b#76dd56341dc29b1b)\n\nThe attached patch adds the missing method and some doctests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3327\n\n",
    "created_at": "2008-05-29T03:18:28Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "missing .divides() implementation for FieldElement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3327",
    "user": "cwitty"
}
```
Assignee: somebody

The generic .divides() implementation doesn't work for FieldElement; this causes the following problem:

```
  R.<a,b> = NumberField(x^2-3,'g')[]
  S.<y> = R.fraction_field()[]
  xgcd(y^2, a*y+b) 
```

goes BOOM (as reported by Gaëtan Bisson here: http://groups.google.com/group/sage-support/browse_thread/thread/5338608bd7508b00/76dd56341dc29b1b#76dd56341dc29b1b)

The attached patch adds the missing method and some doctests.

Issue created by migration from https://trac.sagemath.org/ticket/3327





---

archive/issue_comments_023074.json:
```json
{
    "body": "Attachment [field_element_divides.patch](tarball://root/attachments/some-uuid/ticket3327/field_element_divides.patch) by cwitty created at 2008-05-29 03:20:22",
    "created_at": "2008-05-29T03:20:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3327#issuecomment-23074",
    "user": "cwitty"
}
```

Attachment [field_element_divides.patch](tarball://root/attachments/some-uuid/ticket3327/field_element_divides.patch) by cwitty created at 2008-05-29 03:20:22



---

archive/issue_comments_023075.json:
```json
{
    "body": "I tried it out and it works.  I read the code and it looks great!",
    "created_at": "2008-05-29T03:29:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3327#issuecomment-23075",
    "user": "@williamstein"
}
```

I tried it out and it works.  I read the code and it looks great!



---

archive/issue_comments_023076.json:
```json
{
    "body": "Agreed.  ++",
    "created_at": "2008-05-29T08:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3327#issuecomment-23076",
    "user": "@JohnCremona"
}
```

Agreed.  ++



---

archive/issue_comments_023077.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-29T13:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3327#issuecomment-23077",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023078.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha1",
    "created_at": "2008-05-29T13:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3327#issuecomment-23078",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.alpha1
