# Issue 7780: latex problems from underscores in docstrings

archive/issues_007780.json:
```json
{
    "body": "Assignee: mvngu\n\nKeywords: latex\n\nBuilding docs in 4.3, there are some latex errors:\n\n```\nWARNING: display latex u'\\\\mbox{min_bound} \\\\leq \\\\mbox{linear_function} \\\\leq \\\\mbox{max_bound}': latex exited with error:\n```\n\ncaused by the underscores in min_bound, max_bound and linear_function.  These come from numerical/mip.pyx.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7780\n\n",
    "created_at": "2009-12-28T16:38:16Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "latex problems from underscores in docstrings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7780",
    "user": "cremona"
}
```
Assignee: mvngu

Keywords: latex

Building docs in 4.3, there are some latex errors:

```
WARNING: display latex u'\\mbox{min_bound} \\leq \\mbox{linear_function} \\leq \\mbox{max_bound}': latex exited with error:
```

caused by the underscores in min_bound, max_bound and linear_function.  These come from numerical/mip.pyx.


Issue created by migration from https://trac.sagemath.org/ticket/7780





---

archive/issue_comments_067081.json:
```json
{
    "body": "Applies to 4.3",
    "created_at": "2009-12-28T16:57:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7780#issuecomment-67081",
    "user": "cremona"
}
```

Applies to 4.3



---

archive/issue_comments_067082.json:
```json
{
    "body": "Attachment [trac_7780-docstring.patch](tarball://root/attachments/some-uuid/ticket7780/trac_7780-docstring.patch) by cremona created at 2009-12-28 16:58:31\n\nPatch attached.  Review is trivial but requires waiting for docs to rebuild...",
    "created_at": "2009-12-28T16:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7780#issuecomment-67082",
    "user": "cremona"
}
```

Attachment [trac_7780-docstring.patch](tarball://root/attachments/some-uuid/ticket7780/trac_7780-docstring.patch) by cremona created at 2009-12-28 16:58:31

Patch attached.  Review is trivial but requires waiting for docs to rebuild...



---

archive/issue_comments_067083.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-28T16:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7780#issuecomment-67083",
    "user": "cremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067084.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-12-28T17:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7780#issuecomment-67084",
    "user": "mvngu"
}
```

Resolution: duplicate



---

archive/issue_comments_067085.json:
```json
{
    "body": "This is a duplicate of #7768. The latter has already received positive review.",
    "created_at": "2009-12-28T17:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7780#issuecomment-67085",
    "user": "mvngu"
}
```

This is a duplicate of #7768. The latter has already received positive review.



---

archive/issue_comments_067086.json:
```json
{
    "body": "Replying to [comment:2 mvngu]:\n> This is a duplicate of #7768. The latter has already received positive review.\n\nFair enough, I wasted your (and my) time, sorry.  I did look for a ticket on this but obviously not well enough.",
    "created_at": "2009-12-28T17:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7780#issuecomment-67086",
    "user": "cremona"
}
```

Replying to [comment:2 mvngu]:
> This is a duplicate of #7768. The latter has already received positive review.

Fair enough, I wasted your (and my) time, sorry.  I did look for a ticket on this but obviously not well enough.
