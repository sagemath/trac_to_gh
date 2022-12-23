# Issue 3834: notebook -- massive bug in the notebook -- doing full text search starts a PYthon process for every single worksheet you have!!!

archive/issues_003834.json:
```json
{
    "body": "Assignee: boothby\n\nnotebook -- massive bug in the notebook -- doing full text search starts a PYthon process for every single worksheet you have!!!\n\nThis is a major showstopper bug.\n\nAnd it's either my fault (or Timothy Clemans), but probably me. \n\nThe solution will be to rewrite how full text search works to just look at the filesystem.\nI'm guessing right now it is suddenly doing something really stupid as a result of the \noptimizations I made recently to the notebook.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3834\n\n",
    "created_at": "2008-08-13T06:23:47Z",
    "labels": [
        "notebook",
        "blocker",
        "bug"
    ],
    "title": "notebook -- massive bug in the notebook -- doing full text search starts a PYthon process for every single worksheet you have!!!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3834",
    "user": "was"
}
```
Assignee: boothby

notebook -- massive bug in the notebook -- doing full text search starts a PYthon process for every single worksheet you have!!!

This is a major showstopper bug.

And it's either my fault (or Timothy Clemans), but probably me. 

The solution will be to rewrite how full text search works to just look at the filesystem.
I'm guessing right now it is suddenly doing something really stupid as a result of the 
optimizations I made recently to the notebook.

Issue created by migration from https://trac.sagemath.org/ticket/3834





---

archive/issue_comments_027262.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-13T07:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3834#issuecomment-27262",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_027263.json:
```json
{
    "body": "I am happy with this patch. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-15T09:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3834#issuecomment-27263",
    "user": "mabshoff"
}
```

I am happy with this patch. Positive review.

Cheers,

Michael



---

archive/issue_comments_027264.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-15T09:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3834#issuecomment-27264",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027265.json:
```json
{
    "body": "Merged in Sage 3.1.rc0",
    "created_at": "2008-08-15T09:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3834#issuecomment-27265",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.rc0
