# Issue 5636: [with patch; needs review] jsmath is broken in sage-3.4

archive/issues_005636.json:
```json
{
    "body": "Assignee: cwitty\n\n\n```\nOn Sun, Mar 29, 2009 at 3:39 PM, John H Palmieri wrote:\n>\n> 1. In sage-3.4, it looks like %jsmath is broken.  Can anyone reproduce\n> this?\n>\n> Since I haven't seen anyone mention this, either I missed it or no one\n> uses %jsmath any more.  So is it worth fixing, or should we scrap it\n> (and just use tinyMCE, %html, %latex, etc.)?\n\nI just fixed it.  It took me 1 minute (since it was my fault it was broken in the first place -- I broke this in 3.3).\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5636\n\n",
    "created_at": "2009-03-29T23:22:53Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch; needs review] jsmath is broken in sage-3.4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5636",
    "user": "was"
}
```
Assignee: cwitty


```
On Sun, Mar 29, 2009 at 3:39 PM, John H Palmieri wrote:
>
> 1. In sage-3.4, it looks like %jsmath is broken.  Can anyone reproduce
> this?
>
> Since I haven't seen anyone mention this, either I missed it or no one
> uses %jsmath any more.  So is it worth fixing, or should we scrap it
> (and just use tinyMCE, %html, %latex, etc.)?

I just fixed it.  It took me 1 minute (since it was my fault it was broken in the first place -- I broke this in 3.3).
```


Issue created by migration from https://trac.sagemath.org/ticket/5636





---

archive/issue_comments_044017.json:
```json
{
    "body": "Attachment [trac_5636.patch](tarball://root/attachments/some-uuid/ticket5636/trac_5636.patch) by was created at 2009-03-29 23:23:58",
    "created_at": "2009-03-29T23:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5636#issuecomment-44017",
    "user": "was"
}
```

Attachment [trac_5636.patch](tarball://root/attachments/some-uuid/ticket5636/trac_5636.patch) by was created at 2009-03-29 23:23:58



---

archive/issue_comments_044018.json:
```json
{
    "body": "Fixes the problem, simple code, all tests pass.  Positive review.",
    "created_at": "2009-03-30T00:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5636#issuecomment-44018",
    "user": "jhpalmieri"
}
```

Fixes the problem, simple code, all tests pass.  Positive review.



---

archive/issue_comments_044019.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-31T08:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5636#issuecomment-44019",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc0.

Cheers,

Michael



---

archive/issue_comments_044020.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-31T08:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5636#issuecomment-44020",
    "user": "mabshoff"
}
```

Resolution: fixed
