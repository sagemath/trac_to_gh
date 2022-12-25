# Issue 8045: add elliptic integrals to the reference manual

archive/issues_008045.json:
```json
{
    "body": "Assignee: mvngu\n\nThe documentation strings for classes like `elliptic_ec` are contained in their `__init__` methods, and so doesn't show up in the reference manual.  This patch fixes that by moving the documentation to the class definition.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8045\n\n",
    "created_at": "2010-01-23T17:19:12Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "add elliptic integrals to the reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8045",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: mvngu

The documentation strings for classes like `elliptic_ec` are contained in their `__init__` methods, and so doesn't show up in the reference manual.  This patch fixes that by moving the documentation to the class definition.


Issue created by migration from https://trac.sagemath.org/ticket/8045





---

archive/issue_comments_070193.json:
```json
{
    "body": "Attachment [trac_8045-elliptic.patch](tarball://root/attachments/some-uuid/ticket8045/trac_8045-elliptic.patch) by @jhpalmieri created at 2010-01-23 17:19:43",
    "created_at": "2010-01-23T17:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8045#issuecomment-70193",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8045-elliptic.patch](tarball://root/attachments/some-uuid/ticket8045/trac_8045-elliptic.patch) by @jhpalmieri created at 2010-01-23 17:19:43



---

archive/issue_comments_070194.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-23T17:19:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8045#issuecomment-70194",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070195.json:
```json
{
    "body": "Some cleanups.  Replaces previous.",
    "created_at": "2010-01-31T01:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8045#issuecomment-70195",
    "user": "https://github.com/qed777"
}
```

Some cleanups.  Replaces previous.



---

archive/issue_comments_070196.json:
```json
{
    "body": "Attachment [trac_8045-elliptic.2.patch](tarball://root/attachments/some-uuid/ticket8045/trac_8045-elliptic.2.patch) by @qed777 created at 2010-01-31 01:26:27\n\nV2 makes the docstrings more consistent and fixes a mistake (I think) in `elliptic_pi`'s docstring.  For comparison, see [Maxima's documentation](http://maxima.sourceforge.net/docs/manual/en/maxima_17.html#SEC68) and [MathWorld](http://mathworld.wolfram.com/EllipticIntegraloftheThirdKind.html).\n\nPositive review, if my changes are OK.",
    "created_at": "2010-01-31T01:26:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8045#issuecomment-70196",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8045-elliptic.2.patch](tarball://root/attachments/some-uuid/ticket8045/trac_8045-elliptic.2.patch) by @qed777 created at 2010-01-31 01:26:27

V2 makes the docstrings more consistent and fixes a mistake (I think) in `elliptic_pi`'s docstring.  For comparison, see [Maxima's documentation](http://maxima.sourceforge.net/docs/manual/en/maxima_17.html#SEC68) and [MathWorld](http://mathworld.wolfram.com/EllipticIntegraloftheThirdKind.html).

Positive review, if my changes are OK.



---

archive/issue_comments_070197.json:
```json
{
    "body": "We both missed two typos.  Here's version 3, plus a delta patch to see the (essentially trivial) differences.",
    "created_at": "2010-01-31T03:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8045#issuecomment-70197",
    "user": "https://github.com/jhpalmieri"
}
```

We both missed two typos.  Here's version 3, plus a delta patch to see the (essentially trivial) differences.



---

archive/issue_comments_070198.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T03:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8045#issuecomment-70198",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070199.json:
```json
{
    "body": "Attachment [trac_8045-elliptic-v3.patch](tarball://root/attachments/some-uuid/ticket8045/trac_8045-elliptic-v3.patch) by @jhpalmieri created at 2010-01-31 03:09:35\n\nreplaces all previous patches",
    "created_at": "2010-01-31T03:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8045#issuecomment-70199",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8045-elliptic-v3.patch](tarball://root/attachments/some-uuid/ticket8045/trac_8045-elliptic-v3.patch) by @jhpalmieri created at 2010-01-31 03:09:35

replaces all previous patches



---

archive/issue_comments_070200.json:
```json
{
    "body": "Attachment [trac_8045-delta.patch](tarball://root/attachments/some-uuid/ticket8045/trac_8045-delta.patch) by @jhpalmieri created at 2010-01-31 03:13:59\n\ndifference between versions 2 and 3, for reference purposes only. don't merge.",
    "created_at": "2010-01-31T03:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8045#issuecomment-70200",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8045-delta.patch](tarball://root/attachments/some-uuid/ticket8045/trac_8045-delta.patch) by @jhpalmieri created at 2010-01-31 03:13:59

difference between versions 2 and 3, for reference purposes only. don't merge.



---

archive/issue_comments_070201.json:
```json
{
    "body": "Oops.  Thanks for catching the typos.",
    "created_at": "2010-01-31T03:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8045#issuecomment-70201",
    "user": "https://github.com/qed777"
}
```

Oops.  Thanks for catching the typos.



---

archive/issue_comments_070202.json:
```json
{
    "body": "Merged [trac_8045-elliptic-v3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8045/trac_8045-elliptic-v3.patch).",
    "created_at": "2010-02-02T03:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8045#issuecomment-70202",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [trac_8045-elliptic-v3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8045/trac_8045-elliptic-v3.patch).



---

archive/issue_comments_070203.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-02T03:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8045#issuecomment-70203",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_008255.json:
```json
{
    "actor": "mvngu",
    "created_at": "2010-02-02T03:23:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8045",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8045#event-8255"
}
```
