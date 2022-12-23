# Issue 5725: [with patch; needs review] sequences -- bring coverage to 100%; don't allow hashing of mutable sequences

archive/issues_005725.json:
```json
{
    "body": "Assignee: cwitty\n\nBring up the coverage of sequence.py from 59% to 100%.  Also, sequences allowed hashing even when they are mutable which *breaks* all the Python algorithms that rely on hashing!  This was because I didn't understand this fast about Python when I implemented Sequences.  \n\nIf there is any fallout as a result of eliminating hashing, then that other code must be fixed, because it would surely exhibit subtle bugs. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5725\n\n",
    "created_at": "2009-04-09T08:34:53Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] sequences -- bring coverage to 100%; don't allow hashing of mutable sequences",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5725",
    "user": "was"
}
```
Assignee: cwitty

Bring up the coverage of sequence.py from 59% to 100%.  Also, sequences allowed hashing even when they are mutable which *breaks* all the Python algorithms that rely on hashing!  This was because I didn't understand this fast about Python when I implemented Sequences.  

If there is any fallout as a result of eliminating hashing, then that other code must be fixed, because it would surely exhibit subtle bugs. 

Issue created by migration from https://trac.sagemath.org/ticket/5725





---

archive/issue_comments_044740.json:
```json
{
    "body": "Attachment\n\nFYI: I ran long doctests and all of the tests pass.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T08:54:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5725#issuecomment-44740",
    "user": "mabshoff"
}
```

Attachment

FYI: I ran long doctests and all of the tests pass.

Cheers,

Michael



---

archive/issue_comments_044741.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-04-09T08:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5725#issuecomment-44741",
    "user": "robertwb"
}
```

Looks good to me.



---

archive/issue_comments_044742.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T09:10:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5725#issuecomment-44742",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc2.

Cheers,

Michael



---

archive/issue_comments_044743.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-09T09:10:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5725#issuecomment-44743",
    "user": "mabshoff"
}
```

Resolution: fixed
