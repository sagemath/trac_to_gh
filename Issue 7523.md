# Issue 7523: Lightweight Wrapper for Rpy2

archive/issues_007523.json:
```json
{
    "body": "Assignee: amhou\n\nKeywords: rpy, rpy2\n\nCreates an easier to use interface for Rpy2\n\nIssue created by migration from https://trac.sagemath.org/ticket/7523\n\n",
    "created_at": "2009-11-24T06:22:36Z",
    "labels": [
        "statistics",
        "minor",
        "enhancement"
    ],
    "title": "Lightweight Wrapper for Rpy2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7523",
    "user": "amhou"
}
```
Assignee: amhou

Keywords: rpy, rpy2

Creates an easier to use interface for Rpy2

Issue created by migration from https://trac.sagemath.org/ticket/7523





---

archive/issue_comments_063766.json:
```json
{
    "body": "Attachment [trac_7523_patch.patch](tarball://root/attachments/some-uuid/ticket7523/trac_7523_patch.patch) by amhou created at 2009-11-24 06:25:20\n\nMAJORERROR: imports numpy and rpy2 into the global namespace. Not sure how to get past this.",
    "created_at": "2009-11-24T06:25:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7523#issuecomment-63766",
    "user": "amhou"
}
```

Attachment [trac_7523_patch.patch](tarball://root/attachments/some-uuid/ticket7523/trac_7523_patch.patch) by amhou created at 2009-11-24 06:25:20

MAJORERROR: imports numpy and rpy2 into the global namespace. Not sure how to get past this.



---

archive/issue_comments_063767.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-24T06:25:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7523#issuecomment-63767",
    "user": "amhou"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063768.json:
```json
{
    "body": "\n```\nnice\n[10:29pm] amhou:\nnot sure how to get past the importing into global namespace\n[10:29pm] amhou:\nbecause we definitely don't want that\n[10:30pm] amhou:\nbut if I define within the functions, then the stuff called outside of the functions doesn't work\n[10:30pm] amhou:\n:-/\n[10:30pm] williamstein:\nRobert Bradshaw came up with some new clever, clever code to uniformly deal with this problem.\n[10:30pm] williamstein:\nI'll ping him.\n```\n",
    "created_at": "2009-11-24T06:30:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7523#issuecomment-63768",
    "user": "was"
}
```


```
nice
[10:29pm] amhou:
not sure how to get past the importing into global namespace
[10:29pm] amhou:
because we definitely don't want that
[10:30pm] amhou:
but if I define within the functions, then the stuff called outside of the functions doesn't work
[10:30pm] amhou:
:-/
[10:30pm] williamstein:
Robert Bradshaw came up with some new clever, clever code to uniformly deal with this problem.
[10:30pm] williamstein:
I'll ping him.
```




---

archive/issue_comments_063769.json:
```json
{
    "body": "In this case, I think what you want is http://www.python.org/dev/peps/pep-0369/\n\nI'm not sure about using IntVector, as it will silently truncate all non-integer lists...\n\n\n```\nsage: list(rpy2.robjects.IntVector([1,1/2,pi]))\n[1, 0, 3]\n```\n",
    "created_at": "2009-11-24T07:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7523#issuecomment-63769",
    "user": "robertwb"
}
```

In this case, I think what you want is http://www.python.org/dev/peps/pep-0369/

I'm not sure about using IntVector, as it will silently truncate all non-integer lists...


```
sage: list(rpy2.robjects.IntVector([1,1/2,pi]))
[1, 0, 3]
```




---

archive/issue_comments_063770.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-24T07:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7523#issuecomment-63770",
    "user": "robertwb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063771.json:
```json
{
    "body": "Attachment [trac_7523-part2.patch](tarball://root/attachments/some-uuid/ticket7523/trac_7523-part2.patch) by was created at 2009-12-08 01:11:45",
    "created_at": "2009-12-08T01:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7523#issuecomment-63771",
    "user": "was"
}
```

Attachment [trac_7523-part2.patch](tarball://root/attachments/some-uuid/ticket7523/trac_7523-part2.patch) by was created at 2009-12-08 01:11:45



---

archive/issue_comments_063772.json:
```json
{
    "body": "R  has been updated (I've no idea what ticket, but it happened). I suspect these patches might need rebasing at the very least. \n\ndave",
    "created_at": "2010-03-19T22:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7523#issuecomment-63772",
    "user": "drkirkby"
}
```

R  has been updated (I've no idea what ticket, but it happened). I suspect these patches might need rebasing at the very least. 

dave
