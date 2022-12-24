# Issue 9005: Derangements

archive/issues_009005.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  @nathanncohen @ppurka\n\nKeywords: derangements\n\nThe current implementation in Sage for derangements is a wrapper for the GAP \"derangements\" and \"number_of_derangements\" which is very restrictive.  For example, it doesn't allow derangements of arbitrary lists or strings.  The documentation observes \n\n\"Warning - Wraps GAP - hence mset must be a list of objects that have string representations that can be interpreted by the GAP interpreter. If mset consists of at all complicated Sage objects, this function does not do what you expect. A proper function should be written! (TODO!)\" \n\nThis file is an attempt to provide that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9005\n\n",
    "created_at": "2010-05-21T10:20:57Z",
    "labels": [
        "combinatorics",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.10",
    "title": "Derangements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9005",
    "user": "amca01"
}
```
Assignee: sage-combinat

CC:  @nathanncohen @ppurka

Keywords: derangements

The current implementation in Sage for derangements is a wrapper for the GAP "derangements" and "number_of_derangements" which is very restrictive.  For example, it doesn't allow derangements of arbitrary lists or strings.  The documentation observes 

"Warning - Wraps GAP - hence mset must be a list of objects that have string representations that can be interpreted by the GAP interpreter. If mset consists of at all complicated Sage objects, this function does not do what you expect. A proper function should be written! (TODO!)" 

This file is an attempt to provide that.

Issue created by migration from https://trac.sagemath.org/ticket/9005





---

archive/issue_comments_083300.json:
```json
{
    "body": "Attachment [derangements.sage](tarball://root/attachments/some-uuid/ticket9005/derangements.sage) by amca01 created at 2010-05-29 06:00:16",
    "created_at": "2010-05-29T06:00:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9005#issuecomment-83300",
    "user": "amca01"
}
```

Attachment [derangements.sage](tarball://root/attachments/some-uuid/ticket9005/derangements.sage) by amca01 created at 2010-05-29 06:00:16



---

archive/issue_comments_083301.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-04-01T19:40:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9005#issuecomment-83301",
    "user": "@tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083302.json:
```json
{
    "body": "Converted the sage file into a patch and brought it up to our current standards. Ready for review.",
    "created_at": "2013-04-01T19:40:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9005#issuecomment-83302",
    "user": "@tscrim"
}
```

Converted the sage file into a patch and brought it up to our current standards. Ready for review.



---

archive/issue_comments_083303.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-04-18T17:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9005#issuecomment-83303",
    "user": "@bsalisbury1"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083304.json:
```json
{
    "body": "The patch is not a proper patch file, patches should be generated using `hg export tip`.",
    "created_at": "2013-04-23T13:18:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9005#issuecomment-83304",
    "user": "@jdemeyer"
}
```

The patch is not a proper patch file, patches should be generated using `hg export tip`.



---

archive/issue_comments_083305.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-04-23T13:18:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9005#issuecomment-83305",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_083306.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-04-23T15:16:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9005#issuecomment-83306",
    "user": "@tscrim"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_083307.json:
```json
{
    "body": "Attachment [trac_9005-derangements-ts.patch](tarball://root/attachments/some-uuid/ticket9005/trac_9005-derangements-ts.patch) by @tscrim created at 2013-04-23 15:16:47\n\nSorry about that. Fixed.",
    "created_at": "2013-04-23T15:16:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9005#issuecomment-83307",
    "user": "@tscrim"
}
```

Attachment [trac_9005-derangements-ts.patch](tarball://root/attachments/some-uuid/ticket9005/trac_9005-derangements-ts.patch) by @tscrim created at 2013-04-23 15:16:47

Sorry about that. Fixed.



---

archive/issue_comments_083308.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-04-28T10:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9005#issuecomment-83308",
    "user": "@jdemeyer"
}
```

Resolution: fixed
