# Issue 9946: output bug in GiNaC

archive/issues_009946.json:
```json
{
    "body": "Assignee: @burcin\n\n\n```\nsage: a.imag()\nsin(1/2*arctan2(0, -88* + 1))*sqrt(abs(4*(sqrt(3) - 5)*(sqrt(3) + 5) + 1))\n```\n\nSee the output of the second argument of `arctan2`.\nSee also #9913.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9947\n\n",
    "created_at": "2010-09-19T08:26:08Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "output bug in GiNaC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9946",
    "user": "https://github.com/zimmermann6"
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

archive/issue_comments_099012.json:
```json
{
    "body": "add doctest",
    "created_at": "2010-09-24T11:04:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99012",
    "user": "https://github.com/burcin"
}
```

add doctest



---

archive/issue_comments_099013.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-09-24T11:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99013",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_099014.json:
```json
{
    "body": "Changing keywords from \"\" to \"pynac\".",
    "created_at": "2010-09-24T11:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99014",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "" to "pynac".



---

archive/issue_comments_099015.json:
```json
{
    "body": "Changing component from calculus to symbolics.",
    "created_at": "2010-09-24T11:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99015",
    "user": "https://github.com/burcin"
}
```

Changing component from calculus to symbolics.



---

archive/issue_comments_099016.json:
```json
{
    "body": "Attachment [trac_9947-add_eval.patch](tarball://root/attachments/some-uuid/ticket9947/trac_9947-add_eval.patch) by @burcin created at 2010-09-24 11:10:54\n\nThis was fixed in GiNaC by Richard Kreckel. Here is the relevant patch:\n\nhttp://www.ginac.de/ginac.git?p=ginac.git;a=commitdiff;h=e08cda1854bdb82f6706ec269233577690ae00e4\n\nI applied the patch to pynac, so this will be fixed in the next release.",
    "created_at": "2010-09-24T11:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99016",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_9947-add_eval.patch](tarball://root/attachments/some-uuid/ticket9947/trac_9947-add_eval.patch) by @burcin created at 2010-09-24 11:10:54

This was fixed in GiNaC by Richard Kreckel. Here is the relevant patch:

http://www.ginac.de/ginac.git?p=ginac.git;a=commitdiff;h=e08cda1854bdb82f6706ec269233577690ae00e4

I applied the patch to pynac, so this will be fixed in the next release.



---

archive/issue_comments_099017.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-05-09T15:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99017",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099018.json:
```json
{
    "body": "New pynac package with the fix is at #11317.",
    "created_at": "2011-05-09T15:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99018",
    "user": "https://github.com/burcin"
}
```

New pynac package with the fix is at #11317.



---

archive/issue_comments_099019.json:
```json
{
    "body": "Looks ok.  Same comment as at #9891.\n\nFor instance, one could then allow an spkg maintainer to review the upstream fix.  But that's not exactly what we want.",
    "created_at": "2011-05-09T18:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99019",
    "user": "https://github.com/kcrisman"
}
```

Looks ok.  Same comment as at #9891.

For instance, one could then allow an spkg maintainer to review the upstream fix.  But that's not exactly what we want.



---

archive/issue_comments_099020.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-05-09T18:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99020",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099021.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-27T12:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9946#issuecomment-99021",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
