# Issue 2642: doctest failure in polynomial_modn_dense_ntl.pyx: .small_roots()

archive/issues_002642.json:
```json
{
    "body": "Assignee: @malb\n\nThe doctest for .small_roots() randomly fails in 2.11.alpha0.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2642\n\n",
    "created_at": "2008-03-22T01:44:36Z",
    "labels": [
        "component: commutative algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "doctest failure in polynomial_modn_dense_ntl.pyx: .small_roots()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2642",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @malb

The doctest for .small_roots() randomly fails in 2.11.alpha0.

Issue created by migration from https://trac.sagemath.org/ticket/2642





---

archive/issue_comments_018114.json:
```json
{
    "body": "Attachment [trac2642-small-roots.patch](tarball://root/attachments/some-uuid/ticket2642/trac2642-small-roots.patch) by cwitty created at 2008-03-22 01:46:49",
    "created_at": "2008-03-22T01:46:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2642#issuecomment-18114",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac2642-small-roots.patch](tarball://root/attachments/some-uuid/ticket2642/trac2642-small-roots.patch) by cwitty created at 2008-03-22 01:46:49



---

archive/issue_comments_018115.json:
```json
{
    "body": "I've attached a patch with one possible fix for the .small_roots() problem.\n\nEvidently the current algorithm can return roots much larger than X, which breaks the doctest.  Under the assumption that more roots==good, I left that behavior (and documented it), and fixed the doctest to search for the root it wants.  Another possible fix would be to filter the roots and discard roots larger than X.",
    "created_at": "2008-03-22T01:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2642#issuecomment-18115",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I've attached a patch with one possible fix for the .small_roots() problem.

Evidently the current algorithm can return roots much larger than X, which breaks the doctest.  Under the assumption that more roots==good, I left that behavior (and documented it), and fixed the doctest to search for the root it wants.  Another possible fix would be to filter the roots and discard roots larger than X.



---

archive/issue_comments_018116.json:
```json
{
    "body": "What exactly is the failure? The code shouldn't return any roots larger than X afaik iff you take into account that e.g. -1 === (N -1). Probably the representation of finite field elements for which the concept of small makes sense should be clarified in the docstring.",
    "created_at": "2008-03-22T14:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2642#issuecomment-18116",
    "user": "https://github.com/malb"
}
```

What exactly is the failure? The code shouldn't return any roots larger than X afaik iff you take into account that e.g. -1 === (N -1). Probably the representation of finite field elements for which the concept of small makes sense should be clarified in the docstring.



---

archive/issue_comments_018117.json:
```json
{
    "body": "This does not answer the outstanding question, but while looking at this code (and I did not get past the docstring, this is really not something I am familiar with) I found the following:\n\n```\nsage: N=10001\nsage: p,q = map(lambda (r,m): r, N.factor())\n```\n\nwhich is so opaque that I could not ignore it.  Pleasr replace that last line with\n\n```\nsage: p,q = N.prime_divisors()\n```\n\n!!!",
    "created_at": "2008-03-23T17:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2642#issuecomment-18117",
    "user": "https://github.com/JohnCremona"
}
```

This does not answer the outstanding question, but while looking at this code (and I did not get past the docstring, this is really not something I am familiar with) I found the following:

```
sage: N=10001
sage: p,q = map(lambda (r,m): r, N.factor())
```

which is so opaque that I could not ignore it.  Pleasr replace that last line with

```
sage: p,q = N.prime_divisors()
```

!!!



---

archive/issue_comments_018118.json:
```json
{
    "body": "Attachment [small_roots_fix.patch](tarball://root/attachments/some-uuid/ticket2642/small_roots_fix.patch) by @malb created at 2008-03-24 00:49:57",
    "created_at": "2008-03-24T00:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2642#issuecomment-18118",
    "user": "https://github.com/malb"
}
```

Attachment [small_roots_fix.patch](tarball://root/attachments/some-uuid/ticket2642/small_roots_fix.patch) by @malb created at 2008-03-24 00:49:57



---

archive/issue_comments_018119.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-24T00:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2642#issuecomment-18119",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_018120.json:
```json
{
    "body": "The attached patch\n* replaces the opaque doctest line with `N.prime_divisors()`\n* enforces roots <= X\n\nThis should fix the issue (it does for me on sage.math).",
    "created_at": "2008-03-24T00:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2642#issuecomment-18120",
    "user": "https://github.com/malb"
}
```

The attached patch
* replaces the opaque doctest line with `N.prime_divisors()`
* enforces roots <= X

This should fix the issue (it does for me on sage.math).



---

archive/issue_comments_018121.json:
```json
{
    "body": "To be precise this patch is a replacement for Carl's patch because I don't think it is correct.",
    "created_at": "2008-03-24T00:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2642#issuecomment-18121",
    "user": "https://github.com/malb"
}
```

To be precise this patch is a replacement for Carl's patch because I don't think it is correct.



---

archive/issue_comments_018122.json:
```json
{
    "body": "REVIEW:\n\nLooks good (though I don't understand/know this LLL algorithm).  One thing -- cwitty's patch fixed some latexing/formating issues around line 320, and your patch doesn't fix those same issue.  You should remake your patch so that it fixes those formatting issues too, though this isn't at all critical.",
    "created_at": "2008-03-28T07:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2642#issuecomment-18122",
    "user": "https://github.com/williamstein"
}
```

REVIEW:

Looks good (though I don't understand/know this LLL algorithm).  One thing -- cwitty's patch fixed some latexing/formating issues around line 320, and your patch doesn't fix those same issue.  You should remake your patch so that it fixes those formatting issues too, though this isn't at all critical.



---

archive/issue_comments_018123.json:
```json
{
    "body": "Applied small_roots_fix.patch and the \"latex only\" portion from trac2642-small-roots.patch to Sage 2.11.alpha2",
    "created_at": "2008-03-28T07:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2642#issuecomment-18123",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Applied small_roots_fix.patch and the "latex only" portion from trac2642-small-roots.patch to Sage 2.11.alpha2



---

archive/issue_comments_018124.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-28T07:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2642#issuecomment-18124",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002833.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-28T07:43:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2642",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2642#event-2833"
}
```
