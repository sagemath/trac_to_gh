# Issue 6435: misformatted docstrings in sage.misc.abstract_method (easy fix)

archive/issues_006435.json:
```json
{
    "body": "Assignee: tba\n\nCC:  nthiery\n\nKeywords: ReST docstring formatting\n\nBuilding the documentation for 4.1.alpha2, there is a warning:\n\n```\nWARNING: /home/david/sage-4.1.alpha2/local/lib/python2.6/site-packages/sage/misc/abstract_method.py:docstring of sage.misc.abstract_method.abstract_method:19: (WARNING/2) Literal block expected; none found.\n```\n\nThis is due to a rogue \"::\" in a docstring introduced by #6097.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6435\n\n",
    "created_at": "2009-06-27T19:03:05Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "misformatted docstrings in sage.misc.abstract_method (easy fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6435",
    "user": "davidloeffler"
}
```
Assignee: tba

CC:  nthiery

Keywords: ReST docstring formatting

Building the documentation for 4.1.alpha2, there is a warning:

```
WARNING: /home/david/sage-4.1.alpha2/local/lib/python2.6/site-packages/sage/misc/abstract_method.py:docstring of sage.misc.abstract_method.abstract_method:19: (WARNING/2) Literal block expected; none found.
```

This is due to a rogue "::" in a docstring introduced by #6097.

Issue created by migration from https://trac.sagemath.org/ticket/6435





---

archive/issue_comments_051662.json:
```json
{
    "body": "Attachment [trac_6435.patch](tarball://root/attachments/some-uuid/ticket6435/trac_6435.patch) by jhpalmieri created at 2009-06-27 20:37:08\n\nHere's a patch.",
    "created_at": "2009-06-27T20:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6435#issuecomment-51662",
    "user": "jhpalmieri"
}
```

Attachment [trac_6435.patch](tarball://root/attachments/some-uuid/ticket6435/trac_6435.patch) by jhpalmieri created at 2009-06-27 20:37:08

Here's a patch.



---

archive/issue_comments_051663.json:
```json
{
    "body": "Oops, sorry for introducing this, and thanks for fixing it! Positive review.",
    "created_at": "2009-06-27T21:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6435#issuecomment-51663",
    "user": "nthiery"
}
```

Oops, sorry for introducing this, and thanks for fixing it! Positive review.



---

archive/issue_comments_051664.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-02T23:43:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6435#issuecomment-51664",
    "user": "rlm"
}
```

Resolution: fixed
