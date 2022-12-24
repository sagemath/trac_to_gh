# Issue 3667: [with patch; needs (easy) review] notebook -- if user history can't be loaded from disk make it blank (much better than making entire notebook not work at all)

archive/issues_003667.json:
```json
{
    "body": "Assignee: boothby\n\nIf the user's command log for some reason can't be loaded from disk, currently the notebook\nsimply fails to ever work for them again.  This is not ideal behavior.  This 1-line patches fixes\nthis problem by making the history log empty in this case. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3667\n\n",
    "created_at": "2008-07-16T07:44:35Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "[with patch; needs (easy) review] notebook -- if user history can't be loaded from disk make it blank (much better than making entire notebook not work at all)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3667",
    "user": "@williamstein"
}
```
Assignee: boothby

If the user's command log for some reason can't be loaded from disk, currently the notebook
simply fails to ever work for them again.  This is not ideal behavior.  This 1-line patches fixes
this problem by making the history log empty in this case. 

Issue created by migration from https://trac.sagemath.org/ticket/3667





---

archive/issue_comments_025919.json:
```json
{
    "body": "Attachment [sage-3667.patch](tarball://root/attachments/some-uuid/ticket3667/sage-3667.patch) by mabshoff created at 2008-07-16 18:25:52\n\nAs is this is next to impossible to doctest. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-16T18:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3667#issuecomment-25919",
    "user": "mabshoff"
}
```

Attachment [sage-3667.patch](tarball://root/attachments/some-uuid/ticket3667/sage-3667.patch) by mabshoff created at 2008-07-16 18:25:52

As is this is next to impossible to doctest. Positive review.

Cheers,

Michael



---

archive/issue_comments_025920.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-16T18:27:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3667#issuecomment-25920",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025921.json:
```json
{
    "body": "Merged in Sage 3.0.6.alpha0",
    "created_at": "2008-07-16T18:27:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3667#issuecomment-25921",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.6.alpha0
