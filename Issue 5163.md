# Issue 5163: jsmath extensions for published webpages

archive/issues_005163.json:
```json
{
    "body": "Assignee: boothby\n\nThe extensions enabled in #5021 don't work for published web pages, I think because js.py isn't loaded.\n\nWe could move the extensions to be invoked right after jsmath is loaded.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5163\n\n",
    "created_at": "2009-02-03T04:55:31Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "jsmath extensions for published webpages",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5163",
    "user": "jason"
}
```
Assignee: boothby

The extensions enabled in #5021 don't work for published web pages, I think because js.py isn't loaded.

We could move the extensions to be invoked right after jsmath is loaded.

Issue created by migration from https://trac.sagemath.org/ticket/5163





---

archive/issue_comments_039568.json:
```json
{
    "body": "Attachment [trac_5163-jsmath-extensions-published.patch](tarball://root/attachments/some-uuid/ticket5163/trac_5163-jsmath-extensions-published.patch) by jason created at 2009-02-03 05:10:45",
    "created_at": "2009-02-03T05:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5163#issuecomment-39568",
    "user": "jason"
}
```

Attachment [trac_5163-jsmath-extensions-published.patch](tarball://root/attachments/some-uuid/ticket5163/trac_5163-jsmath-extensions-published.patch) by jason created at 2009-02-03 05:10:45



---

archive/issue_comments_039569.json:
```json
{
    "body": "Changing assignee from boothby to jason.",
    "created_at": "2009-02-03T09:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5163#issuecomment-39569",
    "user": "jason"
}
```

Changing assignee from boothby to jason.



---

archive/issue_comments_039570.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-03T09:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5163#issuecomment-39570",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039571.json:
```json
{
    "body": "Looks good to me.  I was wondering if there was a better place to put these extensions when I wrote the patch for #5021...",
    "created_at": "2009-02-04T21:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5163#issuecomment-39571",
    "user": "jhpalmieri"
}
```

Looks good to me.  I was wondering if there was a better place to put these extensions when I wrote the patch for #5021...



---

archive/issue_comments_039572.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-05T10:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5163#issuecomment-39572",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael



---

archive/issue_comments_039573.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-05T10:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5163#issuecomment-39573",
    "user": "mabshoff"
}
```

Resolution: fixed
