# Issue 3550: notebook -- make saving and loading state of the notebook vastly faster and scale better

archive/issues_003550.json:
```json
{
    "body": "Assignee: boothby\n\nThis is an alternative to #3456.  It takes the view that the notebook is more like a web page -- lots of pages as text files -- than a database.    \n\nThis is a simple solution that is completely implemented in this patch.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3550\n\n",
    "created_at": "2008-07-04T09:01:50Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- make saving and loading state of the notebook vastly faster and scale better",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3550",
    "user": "was"
}
```
Assignee: boothby

This is an alternative to #3456.  It takes the view that the notebook is more like a web page -- lots of pages as text files -- than a database.    

This is a simple solution that is completely implemented in this patch.

Issue created by migration from https://trac.sagemath.org/ticket/3550





---

archive/issue_comments_025105.json:
```json
{
    "body": "Attachment [sage-3550-part1.patch](tarball://root/attachments/some-uuid/ticket3550/sage-3550-part1.patch) by was created at 2008-07-04 09:02:44\n\nfirst patch -- does everything but needs more testing and documentation",
    "created_at": "2008-07-04T09:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3550#issuecomment-25105",
    "user": "was"
}
```

Attachment [sage-3550-part1.patch](tarball://root/attachments/some-uuid/ticket3550/sage-3550-part1.patch) by was created at 2008-07-04 09:02:44

first patch -- does everything but needs more testing and documentation



---

archive/issue_comments_025106.json:
```json
{
    "body": "\n```\nBEFORE: \n  TIME: Several *minutes* to store.\n  SPACE: 310MB.\n\nAFTER THIS PATCH, which automigrates the sage notebook:\n  TIME: 6.7 seconds to save (on sage.math)\n  SPACE: 8.8MB.\n```\n\n\nSo basically everything is about 30 times faster / smaller. \n\nThe main problem is that I might have introduced bugs, and of course 7 seconds\nis a lot longer than nothing.  But this seems like a worthwhile payback for\n3 hours of work.\n\nNOTE: There are no doctests yet, since those are very strange to write for the notebook.",
    "created_at": "2008-07-04T11:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3550#issuecomment-25106",
    "user": "was"
}
```


```
BEFORE: 
  TIME: Several *minutes* to store.
  SPACE: 310MB.

AFTER THIS PATCH, which automigrates the sage notebook:
  TIME: 6.7 seconds to save (on sage.math)
  SPACE: 8.8MB.
```


So basically everything is about 30 times faster / smaller. 

The main problem is that I might have introduced bugs, and of course 7 seconds
is a lot longer than nothing.  But this seems like a worthwhile payback for
3 hours of work.

NOTE: There are no doctests yet, since those are very strange to write for the notebook.



---

archive/issue_comments_025107.json:
```json
{
    "body": "this should do it (modulo doctests)",
    "created_at": "2008-07-04T11:25:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3550#issuecomment-25107",
    "user": "was"
}
```

this should do it (modulo doctests)



---

archive/issue_comments_025108.json:
```json
{
    "body": "Attachment [sage-3550-part2.patch](tarball://root/attachments/some-uuid/ticket3550/sage-3550-part2.patch) by was created at 2008-07-04 11:25:54",
    "created_at": "2008-07-04T11:25:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3550#issuecomment-25108",
    "user": "was"
}
```

Attachment [sage-3550-part2.patch](tarball://root/attachments/some-uuid/ticket3550/sage-3550-part2.patch) by was created at 2008-07-04 11:25:54



---

archive/issue_comments_025109.json:
```json
{
    "body": "add doctests and made sure all existing tests pass",
    "created_at": "2008-07-05T17:57:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3550#issuecomment-25109",
    "user": "was"
}
```

add doctests and made sure all existing tests pass



---

archive/issue_comments_025110.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_wstein\".",
    "created_at": "2008-07-05T17:58:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3550#issuecomment-25110",
    "user": "was"
}
```

Changing keywords from "" to "editor_wstein".



---

archive/issue_comments_025111.json:
```json
{
    "body": "Attachment [sage-3550-part3.patch](tarball://root/attachments/some-uuid/ticket3550/sage-3550-part3.patch) by was created at 2008-07-05 17:58:13\n\nThis is now fully ready for review.",
    "created_at": "2008-07-05T17:58:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3550#issuecomment-25111",
    "user": "was"
}
```

Attachment [sage-3550-part3.patch](tarball://root/attachments/some-uuid/ticket3550/sage-3550-part3.patch) by was created at 2008-07-05 17:58:13

This is now fully ready for review.



---

archive/issue_comments_025112.json:
```json
{
    "body": "This code has gone live on sagenb.org, so it seems to work. William has also merged a bundle into my Sage 3.0.4.alpha2 tree since there was a conflict with one of Timothy's patches.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T00:06:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3550#issuecomment-25112",
    "user": "mabshoff"
}
```

This code has gone live on sagenb.org, so it seems to work. William has also merged a bundle into my Sage 3.0.4.alpha2 tree since there was a conflict with one of Timothy's patches.

Cheers,

Michael



---

archive/issue_comments_025113.json:
```json
{
    "body": "Attachment [sage-3550-part4.patch](tarball://root/attachments/some-uuid/ticket3550/sage-3550-part4.patch) by mabshoff created at 2008-07-06 17:54:59\n\nMerged sage-3550-part1.patch to sage-3550-part4.patch in Sage 3.0.4.alpha2\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T17:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3550#issuecomment-25113",
    "user": "mabshoff"
}
```

Attachment [sage-3550-part4.patch](tarball://root/attachments/some-uuid/ticket3550/sage-3550-part4.patch) by mabshoff created at 2008-07-06 17:54:59

Merged sage-3550-part1.patch to sage-3550-part4.patch in Sage 3.0.4.alpha2

Cheers,

Michael



---

archive/issue_comments_025114.json:
```json
{
    "body": "excellent!",
    "created_at": "2008-07-06T20:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3550#issuecomment-25114",
    "user": "boothby"
}
```

excellent!



---

archive/issue_comments_025115.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-06T20:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3550#issuecomment-25115",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025116.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-06T20:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3550#issuecomment-25116",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha2
