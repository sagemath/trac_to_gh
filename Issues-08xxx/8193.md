# Issue 8193: Enumeration of points on plane curves over finite fields is very inefficient

archive/issues_008193.json:
```json
{
    "body": "Assignee: @aghitza\n\nThe title says all!  The code in sage/schemes/plane_curves/projective_curve.py for finding all points on a plane curve over a finite field just enumerates all point in `P^2` and tests every one, which is less than optimal.\n\nA patch to improve this is on its way.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8193\n\n",
    "closed_at": "2010-02-11T15:05:18Z",
    "created_at": "2010-02-05T12:29:54Z",
    "labels": [
        "component: algebraic geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Enumeration of points on plane curves over finite fields is very inefficient",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8193",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @aghitza

The title says all!  The code in sage/schemes/plane_curves/projective_curve.py for finding all points on a plane curve over a finite field just enumerates all point in `P^2` and tests every one, which is less than optimal.

A patch to improve this is on its way.


Issue created by migration from https://trac.sagemath.org/ticket/8193





---

archive/issue_comments_072134.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-05T14:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8193#issuecomment-72134",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072135.json:
```json
{
    "body": "The patch does the enumeration in a more efficient way.",
    "created_at": "2010-02-05T14:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8193#issuecomment-72135",
    "user": "https://github.com/JohnCremona"
}
```

The patch does the enumeration in a more efficient way.



---

archive/issue_comments_072136.json:
```json
{
    "body": "Attachment [trac_8193-enumerate.patch](tarball://root/attachments/some-uuid/ticket8193/trac_8193-enumerate.patch) by @JohnCremona created at 2010-02-07 15:38:44\n\napplies to 4.3.2",
    "created_at": "2010-02-07T15:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8193#issuecomment-72136",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_8193-enumerate.patch](tarball://root/attachments/some-uuid/ticket8193/trac_8193-enumerate.patch) by @JohnCremona created at 2010-02-07 15:38:44

applies to 4.3.2



---

archive/issue_comments_072137.json:
```json
{
    "body": "In view of #8197 I have deleted \"check=False\" twice.  Otherwise unchanged.",
    "created_at": "2010-02-07T15:40:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8193#issuecomment-72137",
    "user": "https://github.com/JohnCremona"
}
```

In view of #8197 I have deleted "check=False" twice.  Otherwise unchanged.



---

archive/issue_comments_072138.json:
```json
{
    "body": "I'm testing now...",
    "created_at": "2010-02-09T22:47:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8193#issuecomment-72138",
    "user": "https://github.com/roed314"
}
```

I'm testing now...



---

archive/issue_comments_072139.json:
```json
{
    "body": "Looks good, passes all doctests.",
    "created_at": "2010-02-11T08:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8193#issuecomment-72139",
    "user": "https://github.com/roed314"
}
```

Looks good, passes all doctests.



---

archive/issue_comments_072140.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-11T08:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8193#issuecomment-72140",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072141.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8193#issuecomment-72141",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_019600.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-02-11T15:05:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8193",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8193#event-19600"
}
```



---

archive/issue_comments_072142.json:
```json
{
    "body": "A bug has been found in this patch - a new ticket #8428 has been opened and a patch to fix this is in progress.",
    "created_at": "2010-03-03T10:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8193#issuecomment-72142",
    "user": "https://trac.sagemath.org/admin/accounts/users/cturner"
}
```

A bug has been found in this patch - a new ticket #8428 has been opened and a patch to fix this is in progress.
