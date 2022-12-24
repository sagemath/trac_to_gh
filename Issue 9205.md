# Issue 9205: Discrete logs to composite bases

archive/issues_009205.json:
```json
{
    "body": "Assignee: @williamstein\n\nAt present, we have a discrete log function which claims to work for Z/NZ when this group is cyclic, but it can be wrong when N is not prime, as in this example:\n\n```\nsage: Mod(5,9).log(Mod(2, 9))\n6\nsage: sage: discrete_log(Mod(5, 9), Mod(2, 9))\n5\n```\n\n\nThe first answer is totally wrong, because Pari's znlog function is intended to be used with a prime modulus and silently returns junk in the non-prime case.\n\nI need to be able to express elements of Z/NZ* in terms of generators in the non-cyclic case anway, so I will fix this in the process.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9205\n\n",
    "created_at": "2010-06-10T14:11:02Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Discrete logs to composite bases",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9205",
    "user": "@loefflerd"
}
```
Assignee: @williamstein

At present, we have a discrete log function which claims to work for Z/NZ when this group is cyclic, but it can be wrong when N is not prime, as in this example:

```
sage: Mod(5,9).log(Mod(2, 9))
6
sage: sage: discrete_log(Mod(5, 9), Mod(2, 9))
5
```


The first answer is totally wrong, because Pari's znlog function is intended to be used with a prime modulus and silently returns junk in the non-prime case.

I need to be able to express elements of Z/NZ* in terms of generators in the non-cyclic case anway, so I will fix this in the process.

Issue created by migration from https://trac.sagemath.org/ticket/9205





---

archive/issue_comments_086158.json:
```json
{
    "body": "patch against 4.4.4.alpha0",
    "created_at": "2010-06-10T14:41:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9205#issuecomment-86158",
    "user": "@loefflerd"
}
```

patch against 4.4.4.alpha0



---

archive/issue_comments_086159.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-10T14:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9205#issuecomment-86159",
    "user": "@loefflerd"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086160.json:
```json
{
    "body": "Attachment [trac_9205-discrete_log.patch](tarball://root/attachments/some-uuid/ticket9205/trac_9205-discrete_log.patch) by @loefflerd created at 2010-06-10 14:43:26\n\nHere's a patch. It fixes the \"log\" method so it returns the right answer when the multiplicative group is cyclic, and adds a new method (I called this \"generalised log\" -- I didn't know what else to call it) which returns a vector of exponents with respect to the generators of the unit group.",
    "created_at": "2010-06-10T14:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9205#issuecomment-86160",
    "user": "@loefflerd"
}
```

Attachment [trac_9205-discrete_log.patch](tarball://root/attachments/some-uuid/ticket9205/trac_9205-discrete_log.patch) by @loefflerd created at 2010-06-10 14:43:26

Here's a patch. It fixes the "log" method so it returns the right answer when the multiplicative group is cyclic, and adds a new method (I called this "generalised log" -- I didn't know what else to call it) which returns a vector of exponents with respect to the generators of the unit group.



---

archive/issue_comments_086161.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-23T16:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9205#issuecomment-86161",
    "user": "@JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086162.json:
```json
{
    "body": "Looks fine, applies to 4.4.4.alpha1 also and tests in rings/finite_rings pass.",
    "created_at": "2010-06-23T16:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9205#issuecomment-86162",
    "user": "@JohnCremona"
}
```

Looks fine, applies to 4.4.4.alpha1 also and tests in rings/finite_rings pass.



---

archive/issue_comments_086163.json:
```json
{
    "body": "apply over previous patch",
    "created_at": "2010-06-30T19:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9205#issuecomment-86163",
    "user": "@loefflerd"
}
```

apply over previous patch



---

archive/issue_comments_086164.json:
```json
{
    "body": "Attachment [trac_9205-doctest.patch](tarball://root/attachments/some-uuid/ticket9205/trac_9205-doctest.patch) by @loefflerd created at 2010-06-30 19:04:11\n\nReplying to [comment:2 cremona]:\n> Looks fine, applies to 4.4.4.alpha1 also and tests in rings/finite_rings pass.\n\n... but one of the doctest in sage/functions/log doesn't. Here's a tiny patch that fixes that.",
    "created_at": "2010-06-30T19:04:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9205#issuecomment-86164",
    "user": "@loefflerd"
}
```

Attachment [trac_9205-doctest.patch](tarball://root/attachments/some-uuid/ticket9205/trac_9205-doctest.patch) by @loefflerd created at 2010-06-30 19:04:11

Replying to [comment:2 cremona]:
> Looks fine, applies to 4.4.4.alpha1 also and tests in rings/finite_rings pass.

... but one of the doctest in sage/functions/log doesn't. Here's a tiny patch that fixes that.



---

archive/issue_comments_086165.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T07:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9205#issuecomment-86165",
    "user": "@qed777"
}
```

Resolution: fixed
