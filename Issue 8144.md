# Issue 8144: SageTeX is not actually installed under SAGE_LOCAL

archive/issues_008144.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @dandrake\n\nKeywords: sagetex\n\nTicket #7617 adds SageTeX as a standard spkg. However, despite modifying the spkg dependency rules in `SAGE_ROOT/spkg/install` and `SAGE_ROOT/spkg/standard/deps` to account for this new package, SageTeX isn't actually installed at all in Sage 4.3.2.alpha1. This was reported on [sage-devel](http://groups.google.com/group/sage-devel/msg/fa6ed48cba5037e0).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8144\n\n",
    "created_at": "2010-02-01T18:14:12Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "SageTeX is not actually installed under SAGE_LOCAL",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8144",
    "user": "mvngu"
}
```
Assignee: tbd

CC:  @dandrake

Keywords: sagetex

Ticket #7617 adds SageTeX as a standard spkg. However, despite modifying the spkg dependency rules in `SAGE_ROOT/spkg/install` and `SAGE_ROOT/spkg/standard/deps` to account for this new package, SageTeX isn't actually installed at all in Sage 4.3.2.alpha1. This was reported on [sage-devel](http://groups.google.com/group/sage-devel/msg/fa6ed48cba5037e0).

Issue created by migration from https://trac.sagemath.org/ticket/8144





---

archive/issue_comments_071596.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-02-01T22:43:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8144#issuecomment-71596",
    "user": "@jhpalmieri"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_071597.json:
```json
{
    "body": "I think you just need to add a line for sagetex to the \"all\" section of deps.  See the attached patch and new version of deps.",
    "created_at": "2010-02-01T22:43:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8144#issuecomment-71597",
    "user": "@jhpalmieri"
}
```

I think you just need to add a line for sagetex to the "all" section of deps.  See the attached patch and new version of deps.



---

archive/issue_comments_071598.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-01T22:43:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8144#issuecomment-71598",
    "user": "@jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071599.json:
```json
{
    "body": "Attachment [deps.patch](tarball://root/attachments/some-uuid/ticket8144/deps.patch) by @jhpalmieri created at 2010-02-01 22:44:09",
    "created_at": "2010-02-01T22:44:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8144#issuecomment-71599",
    "user": "@jhpalmieri"
}
```

Attachment [deps.patch](tarball://root/attachments/some-uuid/ticket8144/deps.patch) by @jhpalmieri created at 2010-02-01 22:44:09



---

archive/issue_comments_071600.json:
```json
{
    "body": "That does the trick. Positive review.",
    "created_at": "2010-02-01T23:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8144#issuecomment-71600",
    "user": "@dandrake"
}
```

That does the trick. Positive review.



---

archive/issue_comments_071601.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-01T23:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8144#issuecomment-71601",
    "user": "@dandrake"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071602.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-02T20:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8144#issuecomment-71602",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_071603.json:
```json
{
    "body": "Copied [deps](http://trac.sagemath.org/sage_trac/attachment/ticket/8144/deps) to `SAGE_ROOT/spkg/standard` and replaced the previous version of `deps` with this one.",
    "created_at": "2010-02-02T20:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8144#issuecomment-71603",
    "user": "mvngu"
}
```

Copied [deps](http://trac.sagemath.org/sage_trac/attachment/ticket/8144/deps) to `SAGE_ROOT/spkg/standard` and replaced the previous version of `deps` with this one.
