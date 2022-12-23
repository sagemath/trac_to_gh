# Issue 3325: [with patch, needs review] small error in argument to dvipng in latex.py

archive/issues_003325.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: %latex, dvipng\n\n%latex calls dvipng if it is available.  Its arguments include '-q*', and my shell tries to expand the *, thus causing %latex to bomb whenever I use it.  In fact, the argument should just be '-q'.  (See the dvipng man page: at one point it says\n\n```\n-q* Run quietly.  Don't chatter about pages converted, etc. to standard output;\n    report no warnings (only errors) to standard error.\n```\n\nBut earlier it says\n\n```\nMany of the parameterless options listed here can be turned off by suffixing the\noption with a zero (0); for instance, to turn off page reversal, use -r0.  Such\noptions are marked with a trailing *.\n```\n\nSo the * is not actually part of the argument.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/3325\n\n",
    "created_at": "2008-05-28T19:50:11Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] small error in argument to dvipng in latex.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3325",
    "user": "jhpalmieri"
}
```
Assignee: somebody

Keywords: %latex, dvipng

%latex calls dvipng if it is available.  Its arguments include '-q*', and my shell tries to expand the *, thus causing %latex to bomb whenever I use it.  In fact, the argument should just be '-q'.  (See the dvipng man page: at one point it says

```
-q* Run quietly.  Don't chatter about pages converted, etc. to standard output;
    report no warnings (only errors) to standard error.
```

But earlier it says

```
Many of the parameterless options listed here can be turned off by suffixing the
option with a zero (0); for instance, to turn off page reversal, use -r0.  Such
options are marked with a trailing *.
```

So the * is not actually part of the argument.)

Issue created by migration from https://trac.sagemath.org/ticket/3325





---

archive/issue_comments_023061.json:
```json
{
    "body": "remove extraneous * in argument to dvipng",
    "created_at": "2008-05-28T19:50:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3325#issuecomment-23061",
    "user": "jhpalmieri"
}
```

remove extraneous * in argument to dvipng



---

archive/issue_comments_023062.json:
```json
{
    "body": "Attachment\n\nPatch looks good to me. Positive review. \n\nNice catch John.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-28T23:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3325#issuecomment-23062",
    "user": "mabshoff"
}
```

Attachment

Patch looks good to me. Positive review. 

Nice catch John.

Cheers,

Michael



---

archive/issue_comments_023063.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-29T01:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3325#issuecomment-23063",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023064.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha1",
    "created_at": "2008-05-29T01:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3325#issuecomment-23064",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.alpha1
