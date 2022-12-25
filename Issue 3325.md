# Issue 3325: [with patch, needs review] small error in argument to dvipng in latex.py

archive/issues_003325.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: %latex, dvipng\n\n%latex calls dvipng if it is available.  Its arguments include '-q*', and my shell tries to expand the *, thus causing %latex to bomb whenever I use it.  In fact, the argument should just be '-q'.  (See the dvipng man page: at one point it says\n\n```\n-q* Run quietly.  Don't chatter about pages converted, etc. to standard output;\n    report no warnings (only errors) to standard error.\n```\nBut earlier it says\n\n```\nMany of the parameterless options listed here can be turned off by suffixing the\noption with a zero (0); for instance, to turn off page reversal, use -r0.  Such\noptions are marked with a trailing *.\n```\nSo the * is not actually part of the argument.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/3325\n\n",
    "created_at": "2008-05-28T19:50:11Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "[with patch, needs review] small error in argument to dvipng in latex.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3325",
    "user": "https://github.com/jhpalmieri"
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

archive/issue_comments_023013.json:
```json
{
    "body": "remove extraneous * in argument to dvipng",
    "created_at": "2008-05-28T19:50:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3325#issuecomment-23013",
    "user": "https://github.com/jhpalmieri"
}
```

remove extraneous * in argument to dvipng



---

archive/issue_comments_023014.json:
```json
{
    "body": "Attachment [dvipng.patch](tarball://root/attachments/some-uuid/ticket3325/dvipng.patch) by mabshoff created at 2008-05-28 23:37:47\n\nPatch looks good to me. Positive review. \n\nNice catch John.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-28T23:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3325#issuecomment-23014",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [dvipng.patch](tarball://root/attachments/some-uuid/ticket3325/dvipng.patch) by mabshoff created at 2008-05-28 23:37:47

Patch looks good to me. Positive review. 

Nice catch John.

Cheers,

Michael



---

archive/issue_events_007459.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-29T01:10:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3325",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3325#event-7459"
}
```



---

archive/issue_comments_023015.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-29T01:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3325#issuecomment-23015",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023016.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha1",
    "created_at": "2008-05-29T01:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3325#issuecomment-23016",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.3.alpha1
