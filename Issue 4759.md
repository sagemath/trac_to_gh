# Issue 4759: add branch option to sage -upgrade

archive/issues_004759.json:
```json
{
    "body": "Assignee: mabshoff\n\nMerging the sage library with local changes can often break -upgrade. The new behavior would rename the sage-main directory if it wasn't pristine. \n\nSee the end of http://groups.google.com/group/sage-devel/browse_thread/thread/5b566397731862d/e4b19771599e2afd?lnk=gst&q=3.2.2.alpha0#e4b19771599e2afd for the full discussion. \n\n\n```\nOn Dec 8, 2008, at 12:25 PM, William Stein wrote:\n\n> On Mon, Dec 8, 2008 at 12:22 PM, Robert Bradshaw\n> What about an option to the upgrade script, e.g.\n>\n> sage -upgrade [-b branch]\n>\n> which would upgrade specified branch inplace if specified?\n\nThat sounds like a reasonable compromise.\n\n\nWilliam\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4759\n\n",
    "created_at": "2008-12-11T10:34:45Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "add branch option to sage -upgrade",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4759",
    "user": "robertwb"
}
```
Assignee: mabshoff

Merging the sage library with local changes can often break -upgrade. The new behavior would rename the sage-main directory if it wasn't pristine. 

See the end of http://groups.google.com/group/sage-devel/browse_thread/thread/5b566397731862d/e4b19771599e2afd?lnk=gst&q=3.2.2.alpha0#e4b19771599e2afd for the full discussion. 


```
On Dec 8, 2008, at 12:25 PM, William Stein wrote:

> On Mon, Dec 8, 2008 at 12:22 PM, Robert Bradshaw
> What about an option to the upgrade script, e.g.
>
> sage -upgrade [-b branch]
>
> which would upgrade specified branch inplace if specified?

That sounds like a reasonable compromise.


William
```


Issue created by migration from https://trac.sagemath.org/ticket/4759





---

archive/issue_comments_036068.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4759#issuecomment-36068",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_036069.json:
```json
{
    "body": "See also #4833",
    "created_at": "2009-02-21T15:42:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4759#issuecomment-36069",
    "user": "robertwb"
}
```

See also #4833



---

archive/issue_comments_036070.json:
```json
{
    "body": "Probably no longer relevant.",
    "created_at": "2014-02-24T13:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4759#issuecomment-36070",
    "user": "mmezzarobba"
}
```

Probably no longer relevant.



---

archive/issue_comments_036071.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-02-24T13:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4759#issuecomment-36071",
    "user": "mmezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_036072.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-09T22:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4759#issuecomment-36072",
    "user": "aapitzsch"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_036073.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-03-11T14:04:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4759#issuecomment-36073",
    "user": "vbraun"
}
```

Resolution: wontfix
