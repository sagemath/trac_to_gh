# Issue 8540: ** BLOCKER ** very simple basic sqrt simplification totally broken bad

archive/issues_008540.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @robertwb @mwhansen\n\n\n```\nsage: a = 3/4\nsage: b = a^(-1/2)\nsage: b^2\n12\n```\n\n\nBut it should be 4/3.  \n\nReported by Paul Nelson, a grad student at Caltech.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8540\n\n",
    "created_at": "2010-03-15T05:17:30Z",
    "labels": [
        "symbolics",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "** BLOCKER ** very simple basic sqrt simplification totally broken bad",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8540",
    "user": "@williamstein"
}
```
Assignee: @burcin

CC:  @robertwb @mwhansen


```
sage: a = 3/4
sage: b = a^(-1/2)
sage: b^2
12
```


But it should be 4/3.  

Reported by Paul Nelson, a grad student at Caltech.

Issue created by migration from https://trac.sagemath.org/ticket/8540





---

archive/issue_comments_077200.json:
```json
{
    "body": "This serious bug is present in sage-4.0, but not in 3.4.2, so it was caused in the switch to Pynac.",
    "created_at": "2010-03-16T03:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8540#issuecomment-77200",
    "user": "@williamstein"
}
```

This serious bug is present in sage-4.0, but not in 3.4.2, so it was caused in the switch to Pynac.



---

archive/issue_comments_077201.json:
```json
{
    "body": "Even earlier than the square:\n\n\n```\nsage: (3/4)^(-1/2)\n6*sqrt(1/3)\nsage: n((.75)^(-1/2))\n1.15470053837925\nsage: n(6*sqrt(1/3))\n3.46410161513775\n```\n",
    "created_at": "2010-03-16T05:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8540#issuecomment-77201",
    "user": "@jasongrout"
}
```

Even earlier than the square:


```
sage: (3/4)^(-1/2)
6*sqrt(1/3)
sage: n((.75)^(-1/2))
1.15470053837925
sage: n(6*sqrt(1/3))
3.46410161513775
```




---

archive/issue_comments_077202.json:
```json
{
    "body": "During the push for the switch, some code was added to simplify these cases (where the base and exponent are rational, but the result is not exact) further than what ginac can do. See `sage.rings.rational.rational_power_parts` for example.\n\nI am taking a look at this right now, but I don't have much time, so I can't promise any results.",
    "created_at": "2010-03-16T09:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8540#issuecomment-77202",
    "user": "@burcin"
}
```

During the push for the switch, some code was added to simplify these cases (where the base and exponent are rational, but the result is not exact) further than what ginac can do. See `sage.rings.rational.rational_power_parts` for example.

I am taking a look at this right now, but I don't have much time, so I can't promise any results.



---

archive/issue_comments_077203.json:
```json
{
    "body": "Changing component from symbolics to basic arithmetic.",
    "created_at": "2010-03-16T12:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8540#issuecomment-77203",
    "user": "@burcin"
}
```

Changing component from symbolics to basic arithmetic.



---

archive/issue_comments_077204.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-16T12:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8540#issuecomment-77204",
    "user": "@burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077205.json:
```json
{
    "body": "Attachment [trac_8540-rational_power.patch](tarball://root/attachments/some-uuid/ticket8540/trac_8540-rational_power.patch) by @burcin created at 2010-03-16 12:14:11\n\nattachment:trac_8540-rational_power.patch fixes the problem, please review.",
    "created_at": "2010-03-16T12:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8540#issuecomment-77205",
    "user": "@burcin"
}
```

Attachment [trac_8540-rational_power.patch](tarball://root/attachments/some-uuid/ticket8540/trac_8540-rational_power.patch) by @burcin created at 2010-03-16 12:14:11

attachment:trac_8540-rational_power.patch fixes the problem, please review.



---

archive/issue_comments_077206.json:
```json
{
    "body": "Looks good.",
    "created_at": "2010-03-16T18:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8540#issuecomment-77206",
    "user": "@mwhansen"
}
```

Looks good.



---

archive/issue_comments_077207.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-16T18:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8540#issuecomment-77207",
    "user": "@mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077208.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-17T06:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8540#issuecomment-77208",
    "user": "mvngu"
}
```

Resolution: fixed
