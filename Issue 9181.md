# Issue 9181: Update dev-guide : __hash__ return a long

archive/issues_009181.json:
```json
{
    "body": "Assignee: @hivert\n\nKeywords: __hash__\n\nFrom [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/f68986cb2d436554)\n\n```\n> 1. I think we should update the devguide, or is there something I don't get ?\n\nNo, we should update the developers guide. Despite this sentence, the (c)\nreturn type of \"hash\" has been a long since Python 2.3 at least, so I think\nthis wasn't ever correct for 64-bit long machines. (What was required is\nthat it fit into a Python int.)\n\n> 2. I'm writing a Cython class which caches the hash value. Which type\n> should I\n>   use for the attribute ? int doesn't work since when trying to store the\n>   hash of None in an int I get\n>\n>      OverflowError: value too large to convert to int\n>\n>   Is long ok and portable (it is was is used in a few place in sage) ?\n> Should\n>   we write it in the doc ?\n\nYes, we should be using C longs here. Under the hood\n\nPython int = C long != C int\nPython float = C double  != C float\n\nand Python longs have no (native) C equivalent.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9181\n\n",
    "closed_at": "2011-04-21T19:35:21Z",
    "created_at": "2010-06-07T23:00:08Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "Update dev-guide : __hash__ return a long",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9181",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

Keywords: __hash__

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/f68986cb2d436554)

```
> 1. I think we should update the devguide, or is there something I don't get ?

No, we should update the developers guide. Despite this sentence, the (c)
return type of "hash" has been a long since Python 2.3 at least, so I think
this wasn't ever correct for 64-bit long machines. (What was required is
that it fit into a Python int.)

> 2. I'm writing a Cython class which caches the hash value. Which type
> should I
>   use for the attribute ? int doesn't work since when trying to store the
>   hash of None in an int I get
>
>      OverflowError: value too large to convert to int
>
>   Is long ok and portable (it is was is used in a few place in sage) ?
> Should
>   we write it in the doc ?

Yes, we should be using C longs here. Under the hood

Python int = C long != C int
Python float = C double  != C float

and Python longs have no (native) C equivalent.
```

Issue created by migration from https://trac.sagemath.org/ticket/9181





---

archive/issue_comments_085754.json:
```json
{
    "body": "Changing assignee from mvngu to @hivert.",
    "created_at": "2010-06-07T23:01:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9181#issuecomment-85754",
    "user": "https://github.com/hivert"
}
```

Changing assignee from mvngu to @hivert.



---

archive/issue_comments_085755.json:
```json
{
    "body": "Attachment [trac_9181-hash_devel_doc_fix-fh.patch](tarball://root/attachments/some-uuid/ticket9181/trac_9181-hash_devel_doc_fix-fh.patch) by @hivert created at 2011-01-18 15:18:08",
    "created_at": "2011-01-18T15:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9181#issuecomment-85755",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_9181-hash_devel_doc_fix-fh.patch](tarball://root/attachments/some-uuid/ticket9181/trac_9181-hash_devel_doc_fix-fh.patch) by @hivert created at 2011-01-18 15:18:08



---

archive/issue_comments_085756.json:
```json
{
    "body": "Changing keywords from \"\" to \"__hash__\".",
    "created_at": "2011-01-18T15:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9181#issuecomment-85756",
    "user": "https://github.com/hivert"
}
```

Changing keywords from "" to "__hash__".



---

archive/issue_comments_085757.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-18T15:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9181#issuecomment-85757",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085758.json:
```json
{
    "body": "Any chance to get this ticket reviewed ?",
    "created_at": "2011-04-04T15:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9181#issuecomment-85758",
    "user": "https://github.com/hivert"
}
```

Any chance to get this ticket reviewed ?



---

archive/issue_comments_085759.json:
```json
{
    "body": "Sounds good and harmless to me, assuming the patch applies (it should since the file did not change in the last year). Positive review!",
    "created_at": "2011-04-21T01:34:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9181#issuecomment-85759",
    "user": "https://github.com/nthiery"
}
```

Sounds good and harmless to me, assuming the patch applies (it should since the file did not change in the last year). Positive review!



---

archive/issue_comments_085760.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-21T01:34:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9181#issuecomment-85760",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085761.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-21T19:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9181#issuecomment-85761",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_022576.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-04-21T19:35:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9181",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9181#event-22576"
}
```
