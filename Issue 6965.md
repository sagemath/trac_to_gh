# Issue 6965: preventing repository corruption with MANIFEST.in

archive/issues_006965.json:
```json
{
    "body": "Assignee: tba\n\nCC:  jason\n\nFrom [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/61612a7bcca169e7/17f2ab8eb4f63b7f):\n\n```\nI should have posted this question here instead of at #6865, as the\nanswer is probably interesting to many people here.  I'd heard things\nabout MANIFEST.in, but for some reason didn't have a clear idea of what\nit was or what I should do about it.  It would be nice if something was\nadded to the developer's guide... \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6965\n\n",
    "created_at": "2009-09-20T02:56:51Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "preventing repository corruption with MANIFEST.in",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6965",
    "user": "mvngu"
}
```
Assignee: tba

CC:  jason

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/61612a7bcca169e7/17f2ab8eb4f63b7f):

```
I should have posted this question here instead of at #6865, as the
answer is probably interesting to many people here.  I'd heard things
about MANIFEST.in, but for some reason didn't have a clear idea of what
it was or what I should do about it.  It would be nice if something was
added to the developer's guide... 
```


Issue created by migration from https://trac.sagemath.org/ticket/6965





---

archive/issue_comments_057624.json:
```json
{
    "body": "For future reference: see [http://www.python.org/doc/2.6.2/distutils/sourcedist.html#specifying-the-files-to-distribute](http://www.python.org/doc/2.6.2/distutils/sourcedist.html#specifying-the-files-to-distribute) for the relevant part of the Python distribution.",
    "created_at": "2009-09-21T23:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6965#issuecomment-57624",
    "user": "jhpalmieri"
}
```

For future reference: see [http://www.python.org/doc/2.6.2/distutils/sourcedist.html#specifying-the-files-to-distribute](http://www.python.org/doc/2.6.2/distutils/sourcedist.html#specifying-the-files-to-distribute) for the relevant part of the Python distribution.



---

archive/issue_comments_057625.json:
```json
{
    "body": "> For future reference: see http://www.python.org/doc/2.6.2/distutils/sourcedist.html#specifying-the-files-to-distribute for the relevant part of the Python distribution.\n\n(change \"distribution\" to \"documentation\")",
    "created_at": "2009-09-21T23:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6965#issuecomment-57625",
    "user": "jhpalmieri"
}
```

> For future reference: see http://www.python.org/doc/2.6.2/distutils/sourcedist.html#specifying-the-files-to-distribute for the relevant part of the Python distribution.

(change "distribution" to "documentation")



---

archive/issue_comments_057626.json:
```json
{
    "body": "Here's a patch.",
    "created_at": "2009-12-22T00:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6965#issuecomment-57626",
    "user": "jhpalmieri"
}
```

Here's a patch.



---

archive/issue_comments_057627.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-22T00:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6965#issuecomment-57627",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_057628.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-12-22T00:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6965#issuecomment-57628",
    "user": "jhpalmieri"
}
```

Changing priority from major to minor.



---

archive/issue_comments_057629.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-22T08:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6965#issuecomment-57629",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057630.json:
```json
{
    "body": "Looks good. Applied OK against Sage 4.3.rc0. As a side note, the URL for \"Specifying the files to distribute\" could also be \n\nhttp://docs.python.org/distutils/sourcedist.html#specifying-the-files-to-distribute\n\nwhich is usually more up-to-date than the given URL. The given URL is more specific to Python 2.6.2.",
    "created_at": "2009-12-22T08:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6965#issuecomment-57630",
    "user": "mvngu"
}
```

Looks good. Applied OK against Sage 4.3.rc0. As a side note, the URL for "Specifying the files to distribute" could also be 

http://docs.python.org/distutils/sourcedist.html#specifying-the-files-to-distribute

which is usually more up-to-date than the given URL. The given URL is more specific to Python 2.6.2.



---

archive/issue_comments_057631.json:
```json
{
    "body": "Attachment [trac_6965-manifest.patch](tarball://root/attachments/some-uuid/ticket6965/trac_6965-manifest.patch) by jhpalmieri created at 2009-12-22 16:02:30\n\nGood point about the URL.  I've replaced the patch with a new one, changing just the URL to the more permanent one.",
    "created_at": "2009-12-22T16:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6965#issuecomment-57631",
    "user": "jhpalmieri"
}
```

Attachment [trac_6965-manifest.patch](tarball://root/attachments/some-uuid/ticket6965/trac_6965-manifest.patch) by jhpalmieri created at 2009-12-22 16:02:30

Good point about the URL.  I've replaced the patch with a new one, changing just the URL to the more permanent one.



---

archive/issue_comments_057632.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T22:04:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6965#issuecomment-57632",
    "user": "mhansen"
}
```

Resolution: fixed
