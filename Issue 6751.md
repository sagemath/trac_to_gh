# Issue 6751: implement ternary quadratic forms associated to orders in rational quaternion algebras

archive/issues_006751.json:
```json
{
    "body": "Assignee: tbd\n\nThis patch could possibly depend on #6745.\n\nThe goal of this patch is to implement computation of the ternary quadratic form associated to an order in a rational quaternion algebra.  These are useful, e.g, in computing with Heegner points, in decided whether quaternion orders have embeddings from orders in quadratic imaginary fields, and in computing elements of the Kohnen + subspace of modular forms of weight 3/2. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6751\n\n",
    "created_at": "2009-08-15T01:18:30Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "implement ternary quadratic forms associated to orders in rational quaternion algebras",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6751",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

This patch could possibly depend on #6745.

The goal of this patch is to implement computation of the ternary quadratic form associated to an order in a rational quaternion algebra.  These are useful, e.g, in computing with Heegner points, in decided whether quaternion orders have embeddings from orders in quadratic imaginary fields, and in computing elements of the Kohnen + subspace of modular forms of weight 3/2. 

Issue created by migration from https://trac.sagemath.org/ticket/6751





---

archive/issue_comments_055491.json:
```json
{
    "body": "Attachment [trac_6751.patch](tarball://root/attachments/some-uuid/ticket6751/trac_6751.patch) by @williamstein created at 2009-08-15 01:42:38",
    "created_at": "2009-08-15T01:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6751#issuecomment-55491",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_6751.patch](tarball://root/attachments/some-uuid/ticket6751/trac_6751.patch) by @williamstein created at 2009-08-15 01:42:38



---

archive/issue_comments_055492.json:
```json
{
    "body": "Apply after previous",
    "created_at": "2009-08-23T16:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6751#issuecomment-55492",
    "user": "https://github.com/JohnCremona"
}
```

Apply after previous



---

archive/issue_comments_055493.json:
```json
{
    "body": "Attachment [trac_6751-review.patch](tarball://root/attachments/some-uuid/ticket6751/trac_6751-review.patch) by @JohnCremona created at 2009-08-23 16:08:23\n\nLooks good to me:  applies fine to 4.1.1, tests pass, some examples I tried looked correct (as does the code).\n\nThere's one small typo (\"had\" for \"has\" in the docstring) which I put into a second patch (overkill perhaps!)",
    "created_at": "2009-08-23T16:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6751#issuecomment-55493",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_6751-review.patch](tarball://root/attachments/some-uuid/ticket6751/trac_6751-review.patch) by @JohnCremona created at 2009-08-23 16:08:23

Looks good to me:  applies fine to 4.1.1, tests pass, some examples I tried looked correct (as does the code).

There's one small typo ("had" for "has" in the docstring) which I put into a second patch (overkill perhaps!)



---

archive/issue_comments_055494.json:
```json
{
    "body": "Merged both patches. The patch `trac_6751.patch` applies OK, but with fuzz:\n\n```\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6751/trac_6751.patch && hg qpush\nadding trac_6751.patch to series file\napplying trac_6751.patch\npatching file sage/algebras/quatalg/quaternion_algebra_element.pyx\nHunk #1 succeeded at 537 with fuzz 2 (offset -76 lines).\nNow at: trac_6751.patch\n```\n",
    "created_at": "2009-08-30T09:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6751#issuecomment-55494",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged both patches. The patch `trac_6751.patch` applies OK, but with fuzz:

```
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6751/trac_6751.patch && hg qpush
adding trac_6751.patch to series file
applying trac_6751.patch
patching file sage/algebras/quatalg/quaternion_algebra_element.pyx
Hunk #1 succeeded at 537 with fuzz 2 (offset -76 lines).
Now at: trac_6751.patch
```




---

archive/issue_events_015918.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-30T09:29:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6751",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6751#event-15918"
}
```



---

archive/issue_comments_055495.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-30T09:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6751#issuecomment-55495",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_055496.json:
```json
{
    "body": "See #6846 for a follow up to this ticket.",
    "created_at": "2009-08-30T09:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6751#issuecomment-55496",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See #6846 for a follow up to this ticket.
