# Issue 7450: implement is_prime() for ideals

archive/issues_007450.json:
```json
{
    "body": "Assignee: @malb\n\nKeywords: prime ideal\n\nThe attached patch implements a generic primality testing method for ideals.  It is based on the computation of the associated primes of an ideal, and so at the moment will only work for ideals that have this implemented (e.g. ideals in multivariate polynomial rings that Singular can handle).\n\nThere are also a few related methods such as `is_primary()` and `embedded_primes()`.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7450\n\n",
    "created_at": "2009-11-13T12:30:17Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "implement is_prime() for ideals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7450",
    "user": "https://github.com/aghitza"
}
```
Assignee: @malb

Keywords: prime ideal

The attached patch implements a generic primality testing method for ideals.  It is based on the computation of the associated primes of an ideal, and so at the moment will only work for ideals that have this implemented (e.g. ideals in multivariate polynomial rings that Singular can handle).

There are also a few related methods such as `is_primary()` and `embedded_primes()`.


Issue created by migration from https://trac.sagemath.org/ticket/7450





---

archive/issue_comments_062635.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2009-11-13T13:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7450#issuecomment-62635",
    "user": "https://github.com/malb"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_062636.json:
```json
{
    "body": "* patch applies cleanly against 4.2\n  * doctests pass\n  * reference manual builds without reporting any issues\n  * note that there are macros for citations available in ReST: http://sphinx.pocoo.org/rest.html#citations\n\nOther than the last nitpick the patch looks fine.",
    "created_at": "2009-11-13T13:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7450#issuecomment-62636",
    "user": "https://github.com/malb"
}
```

* patch applies cleanly against 4.2
  * doctests pass
  * reference manual builds without reporting any issues
  * note that there are macros for citations available in ReST: http://sphinx.pocoo.org/rest.html#citations

Other than the last nitpick the patch looks fine.



---

archive/issue_comments_062637.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-13T22:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7450#issuecomment-62637",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062638.json:
```json
{
    "body": "Aha!  Thanks for the pointer for citations.  I had looked in the developer guide and there was nothing about this (I'll open a new ticket to fix that).\n\nI have replaced the patch with one that has the proper citation markup.  Having had a look at the html output, I also fixed the markup for `apply_morphism`.",
    "created_at": "2009-11-13T22:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7450#issuecomment-62638",
    "user": "https://github.com/aghitza"
}
```

Aha!  Thanks for the pointer for citations.  I had looked in the developer guide and there was nothing about this (I'll open a new ticket to fix that).

I have replaced the patch with one that has the proper citation markup.  Having had a look at the html output, I also fixed the markup for `apply_morphism`.



---

archive/issue_comments_062639.json:
```json
{
    "body": "Attachment [trac_7450.patch](tarball://root/attachments/some-uuid/ticket7450/trac_7450.patch) by @aghitza created at 2009-11-15 01:01:23\n\nAnd I replaced it once more, having added an optional argument to `is_primary` to check whether an ideal is primary wrt a given prime ideal; also added more doctests borrowed from the Macaulay2 docs.",
    "created_at": "2009-11-15T01:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7450#issuecomment-62639",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_7450.patch](tarball://root/attachments/some-uuid/ticket7450/trac_7450.patch) by @aghitza created at 2009-11-15 01:01:23

And I replaced it once more, having added an optional argument to `is_primary` to check whether an ideal is primary wrt a given prime ideal; also added more doctests borrowed from the Macaulay2 docs.



---

archive/issue_comments_062640.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-16T13:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7450#issuecomment-62640",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062641.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-11-16T13:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7450#issuecomment-62641",
    "user": "https://github.com/malb"
}
```

Looks good.



---

archive/issue_events_007677.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-11-17T05:59:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7450",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7450#event-7677"
}
```



---

archive/issue_comments_062642.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T05:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7450#issuecomment-62642",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
