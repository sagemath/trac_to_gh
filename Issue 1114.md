# Issue 1114: Delete a file to fix an example involving the sage latex mode

archive/issues_001114.json:
```json
{
    "body": "Assignee: tba\n\n\n```\n\nThis is for a 2.8.10 installation so apologies if it has been fixed.\n\nThe file examples/latex_embed/E2.sobj contains bad cached data so that\nwhen you run \"sage example.sage\" you get a run-time error, even though\nexample.tex is correct!   The clue came from looking at the backup\nfile #example.tex#.   Since the script cleverly only does a long\ncomputation when the result has not been stored, it keeps on using the\nbad data (just an array subscript out of range).  The solution is to\ndelete file E2.sobj .\n\nI didn't think this was worth a trac ticket...\n```\n\n\nYes it is, or it will be lost...\n\nIssue created by migration from https://trac.sagemath.org/ticket/1114\n\n",
    "created_at": "2007-11-06T16:25:11Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "Delete a file to fix an example involving the sage latex mode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1114",
    "user": "was"
}
```
Assignee: tba


```

This is for a 2.8.10 installation so apologies if it has been fixed.

The file examples/latex_embed/E2.sobj contains bad cached data so that
when you run "sage example.sage" you get a run-time error, even though
example.tex is correct!   The clue came from looking at the backup
file #example.tex#.   Since the script cleverly only does a long
computation when the result has not been stored, it keeps on using the
bad data (just an array subscript out of range).  The solution is to
delete file E2.sobj .

I didn't think this was worth a trac ticket...
```


Yes it is, or it will be lost...

Issue created by migration from https://trac.sagemath.org/ticket/1114





---

archive/issue_comments_006728.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-07T05:22:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1114#issuecomment-6728",
    "user": "was"
}
```

Resolution: fixed
