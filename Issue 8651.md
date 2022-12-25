# Issue 8651: binomial(n,k) evaluates to zero when 0 is subsituted for k

archive/issues_008651.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @jasongrout\n\nKeywords: symbolic, binomial\n\nWe all know binomial(n,0) should be 1.  But we're not getting that answer in the following case.\n\n```\nsage: var('n, k')\n(n, k)\nsage: binomial(n, 0)  # this is OK\n1\nsage: binomial(n, k).subs(k=0)  # this is a problem!\n0\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8651\n\n",
    "created_at": "2010-04-05T12:31:30Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "binomial(n,k) evaluates to zero when 0 is subsituted for k",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8651",
    "user": "https://github.com/rhinton"
}
```
Assignee: @burcin

CC:  @jasongrout

Keywords: symbolic, binomial

We all know binomial(n,0) should be 1.  But we're not getting that answer in the following case.

```
sage: var('n, k')
(n, k)
sage: binomial(n, 0)  # this is OK
1
sage: binomial(n, k).subs(k=0)  # this is a problem!
0
```


Issue created by migration from https://trac.sagemath.org/ticket/8651





---

archive/issue_comments_078364.json:
```json
{
    "body": "Good catch! I recall this being fixed in `GiNaC` recently. I'll import the relevant patch into pynac and make an updated package.",
    "created_at": "2010-04-05T12:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8651#issuecomment-78364",
    "user": "https://github.com/burcin"
}
```

Good catch! I recall this being fixed in `GiNaC` recently. I'll import the relevant patch into pynac and make an updated package.



---

archive/issue_comments_078365.json:
```json
{
    "body": "Changing keywords from \"symbolic, binomial\" to \"pynac, binomial\".",
    "created_at": "2010-04-05T12:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8651#issuecomment-78365",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "symbolic, binomial" to "pynac, binomial".



---

archive/issue_comments_078366.json:
```json
{
    "body": "add doctests",
    "created_at": "2010-05-05T19:12:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8651#issuecomment-78366",
    "user": "https://github.com/burcin"
}
```

add doctests



---

archive/issue_comments_078367.json:
```json
{
    "body": "Attachment [trac_8651-binomial.patch](tarball://root/attachments/some-uuid/ticket8651/trac_8651-binomial.patch) by @burcin created at 2010-05-05 19:13:53\n\nI uploaded a patch with the doctest, new pynac package with the fix coming soon.",
    "created_at": "2010-05-05T19:13:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8651#issuecomment-78367",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_8651-binomial.patch](tarball://root/attachments/some-uuid/ticket8651/trac_8651-binomial.patch) by @burcin created at 2010-05-05 19:13:53

I uploaded a patch with the doctest, new pynac package with the fix coming soon.



---

archive/issue_comments_078368.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-06T04:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8651#issuecomment-78368",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078369.json:
```json
{
    "body": "Corresponding pynac package is available at #8903. Note that the new package also contains fixes for #8542, #8688, #8775. Patches from these tickets should be applied before running doctests.",
    "created_at": "2010-05-06T04:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8651#issuecomment-78369",
    "user": "https://github.com/burcin"
}
```

Corresponding pynac package is available at #8903. Note that the new package also contains fixes for #8542, #8688, #8775. Patches from these tickets should be applied before running doctests.



---

archive/issue_comments_078370.json:
```json
{
    "body": "Looks good to me.  This can be merged now.",
    "created_at": "2010-05-26T04:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8651#issuecomment-78370",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  This can be merged now.



---

archive/issue_comments_078371.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-26T04:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8651#issuecomment-78371",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078372.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T07:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8651#issuecomment-78372",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_020936.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-06T07:37:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8651",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8651#event-20936"
}
```
