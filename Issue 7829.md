# Issue 7829: implement hex for real numbers

archive/issues_007829.json:
```json
{
    "body": "Assignee: @aghitza\n\n\n```\nsage: float(e).hex()\n'0x1.5bf0a8b145769p+1'\nsage: RR(e).hex()\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\nAttributeError: 'sage.rings.real_mpfr.RealNumber' object has no attribute 'hex'\n```\n\n\nThere should probably be a __hex__ method as well, so hex(2.3) works. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7829\n\n",
    "created_at": "2010-01-03T05:37:30Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.3",
    "title": "implement hex for real numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7829",
    "user": "@robertwb"
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

archive/issue_comments_067790.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-05-29T07:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67790",
    "user": "@mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067791.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-05-29T07:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67791",
    "user": "@mezzarobba"
}
```

New commits:



---

archive/issue_comments_067792.json:
```json
{
    "body": "Changing component from algebra to basic arithmetic.",
    "created_at": "2014-05-29T07:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67792",
    "user": "@mezzarobba"
}
```

Changing component from algebra to basic arithmetic.



---

archive/issue_comments_067793.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-29T07:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67793",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_067794.json:
```json
{
    "body": "Does the C string need to be freed in the error case as well? In that case you could use a finally clause (and just \"return s\")\n\nCould you add a test showing that hex(RR(x)) works too?",
    "created_at": "2014-05-29T16:14:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67794",
    "user": "@robertwb"
}
```

Does the C string need to be freed in the error case as well? In that case you could use a finally clause (and just "return s")

Could you add a test showing that hex(RR(x)) works too?



---

archive/issue_comments_067795.json:
```json
{
    "body": "Just a short comment: I think the new syntax for exceptions should be used, i.e. `raise RuntimeError(\"...\")`.",
    "created_at": "2014-05-29T18:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67795",
    "user": "jkeitel"
}
```

Just a short comment: I think the new syntax for exceptions should be used, i.e. `raise RuntimeError("...")`.



---

archive/issue_comments_067796.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2014-05-30T07:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67796",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_067797.json:
```json
{
    "body": "Replying to [comment:3 robertwb]:\n> Does the C string need to be freed in the error case as well?\n\nAs far as I understand, no, it doesn't.\n\n> Could you add a test showing that hex(RR(x)) works too?\n\nDone.\n\n\nReplying to [comment:4 jkeitel]:\n> I think the new syntax for exceptions should be used, i.e. raise RuntimeError(\"...\").\n\nFixed, thanks!",
    "created_at": "2014-05-30T07:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67797",
    "user": "@mezzarobba"
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

archive/issue_comments_067798.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-06-04T07:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67798",
    "user": "@robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067799.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-06-04T14:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7829#issuecomment-67799",
    "user": "@vbraun"
}
```

Resolution: fixed
