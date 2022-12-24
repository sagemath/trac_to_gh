# Issue 9946: output bug in GiNaC

archive/issues_009946.json:
```json
{
    "body": "Assignee: @burcin\n\n\n```\nsage: a.imag()\nsin(1/2*arctan2(0, -88* + 1))*sqrt(abs(4*(sqrt(3) - 5)*(sqrt(3) + 5) + 1))\n```\n\nSee the output of the second argument of `arctan2`.\nSee also #9913.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9947\n\n",
    "created_at": "2010-09-19T08:26:08Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "output bug in GiNaC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9946",
    "user": "@zimmermann6"
}
```
Assignee: @burcin


```
sage: a.imag()
sin(1/2*arctan2(0, -88* + 1))*sqrt(abs(4*(sqrt(3) - 5)*(sqrt(3) + 5) + 1))
```

See the output of the second argument of `arctan2`.
See also #9913.

Issue created by migration from https://trac.sagemath.org/ticket/9947





---

archive/issue_comments_099177.json:
```json
{
    "body": "add doctest",
    "created_at": "2010-09-24T11:04:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99177",
    "user": "@burcin"
}
```

add doctest



---

archive/issue_comments_099178.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-09-24T11:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99178",
    "user": "@burcin"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_099179.json:
```json
{
    "body": "Changing keywords from \"\" to \"pynac\".",
    "created_at": "2010-09-24T11:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99179",
    "user": "@burcin"
}
```

Changing keywords from "" to "pynac".



---

archive/issue_comments_099180.json:
```json
{
    "body": "Changing component from calculus to symbolics.",
    "created_at": "2010-09-24T11:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99180",
    "user": "@burcin"
}
```

Changing component from calculus to symbolics.



---

archive/issue_comments_099181.json:
```json
{
    "body": "Attachment [trac_9947-add_eval.patch](tarball://root/attachments/some-uuid/ticket9947/trac_9947-add_eval.patch) by @burcin created at 2010-09-24 11:10:54\n\nThis was fixed in GiNaC by Richard Kreckel. Here is the relevant patch:\n\nhttp://www.ginac.de/ginac.git?p=ginac.git;a=commitdiff;h=e08cda1854bdb82f6706ec269233577690ae00e4\n\nI applied the patch to pynac, so this will be fixed in the next release.",
    "created_at": "2010-09-24T11:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99181",
    "user": "@burcin"
}
```

Attachment [trac_9947-add_eval.patch](tarball://root/attachments/some-uuid/ticket9947/trac_9947-add_eval.patch) by @burcin created at 2010-09-24 11:10:54

This was fixed in GiNaC by Richard Kreckel. Here is the relevant patch:

http://www.ginac.de/ginac.git?p=ginac.git;a=commitdiff;h=e08cda1854bdb82f6706ec269233577690ae00e4

I applied the patch to pynac, so this will be fixed in the next release.



---

archive/issue_comments_099182.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-05-09T15:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99182",
    "user": "@burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099183.json:
```json
{
    "body": "New pynac package with the fix is at #11317.",
    "created_at": "2011-05-09T15:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99183",
    "user": "@burcin"
}
```

New pynac package with the fix is at #11317.



---

archive/issue_comments_099184.json:
```json
{
    "body": "Looks ok.  Same comment as at #9891.\n\nFor instance, one could then allow an spkg maintainer to review the upstream fix.  But that's not exactly what we want.",
    "created_at": "2011-05-09T18:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99184",
    "user": "@kcrisman"
}
```

Looks ok.  Same comment as at #9891.

For instance, one could then allow an spkg maintainer to review the upstream fix.  But that's not exactly what we want.



---

archive/issue_comments_099185.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-05-09T18:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99185",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099186.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-27T12:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99186",
    "user": "@jdemeyer"
}
```

Resolution: fixed
