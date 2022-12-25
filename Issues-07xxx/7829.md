# Issue 7829: implement hex for real numbers

archive/issues_007829.json:
```json
{
    "body": "Assignee: @aghitza\n\n```\nsage: float(e).hex()\n'0x1.5bf0a8b145769p+1'\nsage: RR(e).hex()\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\nAttributeError: 'sage.rings.real_mpfr.RealNumber' object has no attribute 'hex'\n```\n\nThere should probably be a __hex__ method as well, so hex(2.3) works. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7829\n\n",
    "closed_at": "2014-06-04T14:48:09Z",
    "created_at": "2010-01-03T05:37:30Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.3",
    "title": "implement hex for real numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7829",
    "user": "https://github.com/robertwb"
}
```
Assignee: @aghitza

```
sage: float(e).hex()
'0x1.5bf0a8b145769p+1'
sage: RR(e).hex()
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
AttributeError: 'sage.rings.real_mpfr.RealNumber' object has no attribute 'hex'
```

There should probably be a __hex__ method as well, so hex(2.3) works. 

Issue created by migration from https://trac.sagemath.org/ticket/7829





---

archive/issue_comments_067673.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-05-29T07:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67673",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067674.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-05-29T07:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67674",
    "user": "https://github.com/mezzarobba"
}
```

New commits:



---

archive/issue_comments_067675.json:
```json
{
    "body": "Changing component from algebra to basic arithmetic.",
    "created_at": "2014-05-29T07:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67675",
    "user": "https://github.com/mezzarobba"
}
```

Changing component from algebra to basic arithmetic.



---

archive/issue_events_018727.json:
```json
{
    "actor": "https://github.com/mezzarobba",
    "created_at": "2014-05-29T07:07:43Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7829#event-18727"
}
```



---

archive/issue_comments_067676.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-29T07:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67676",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_067677.json:
```json
{
    "body": "Does the C string need to be freed in the error case as well? In that case you could use a finally clause (and just \"return s\")\n\nCould you add a test showing that hex(RR(x)) works too?",
    "created_at": "2014-05-29T16:14:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67677",
    "user": "https://github.com/robertwb"
}
```

Does the C string need to be freed in the error case as well? In that case you could use a finally clause (and just "return s")

Could you add a test showing that hex(RR(x)) works too?



---

archive/issue_comments_067678.json:
```json
{
    "body": "Just a short comment: I think the new syntax for exceptions should be used, i.e. `raise RuntimeError(\"...\")`.",
    "created_at": "2014-05-29T18:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67678",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkeitel"
}
```

Just a short comment: I think the new syntax for exceptions should be used, i.e. `raise RuntimeError("...")`.



---

archive/issue_comments_067679.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2014-05-30T07:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67679",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_067680.json:
```json
{
    "body": "Replying to [comment:3 robertwb]:\n> Does the C string need to be freed in the error case as well?\n\n\nAs far as I understand, no, it doesn't.\n\n> Could you add a test showing that hex(RR(x)) works too?\n\n\nDone.\n\n\nReplying to [comment:4 jkeitel]:\n> I think the new syntax for exceptions should be used, i.e. raise RuntimeError(\"...\").\n\n\nFixed, thanks!",
    "created_at": "2014-05-30T07:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67680",
    "user": "https://github.com/mezzarobba"
}
```

Replying to [comment:3 robertwb]:
> Does the C string need to be freed in the error case as well?


As far as I understand, no, it doesn't.

> Could you add a test showing that hex(RR(x)) works too?


Done.


Replying to [comment:4 jkeitel]:
> I think the new syntax for exceptions should be used, i.e. raise RuntimeError("...").


Fixed, thanks!



---

archive/issue_comments_067681.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-06-04T07:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67681",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067682.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-06-04T14:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67682",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_018728.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-06-04T14:48:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7829#event-18728"
}
```
