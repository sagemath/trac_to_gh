# Issue 5593: [with patch; needs review or throwing away] CremonaDB.conductor_range does not give a Python style range

archive/issues_005593.json:
```json
{
    "body": "Assignee: nbruin\n\nCremonaDB().conductor_range() gives an inclusive upper bound, so that\nsrange(*CremonaDB().conductor_range()) may miss a conductor.\n\nFix attached\n\nIssue created by migration from https://trac.sagemath.org/ticket/5593\n\n",
    "created_at": "2009-03-23T19:02:14Z",
    "labels": [
        "modular forms",
        "minor",
        "bug"
    ],
    "title": "[with patch; needs review or throwing away] CremonaDB.conductor_range does not give a Python style range",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5593",
    "user": "nbruin"
}
```
Assignee: nbruin

CremonaDB().conductor_range() gives an inclusive upper bound, so that
srange(*CremonaDB().conductor_range()) may miss a conductor.

Fix attached

Issue created by migration from https://trac.sagemath.org/ticket/5593





---

archive/issue_comments_043565.json:
```json
{
    "body": "Patch",
    "created_at": "2009-03-23T19:03:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5593#issuecomment-43565",
    "user": "nbruin"
}
```

Patch



---

archive/issue_comments_043566.json:
```json
{
    "body": "Attachment\n\nYes, this looks like the right thing to do.",
    "created_at": "2009-03-23T19:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5593#issuecomment-43566",
    "user": "robertwb"
}
```

Attachment

Yes, this looks like the right thing to do.



---

archive/issue_comments_043567.json:
```json
{
    "body": "Looks good to me too.",
    "created_at": "2009-03-23T20:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5593#issuecomment-43567",
    "user": "cremona"
}
```

Looks good to me too.



---

archive/issue_comments_043568.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-23T21:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5593#issuecomment-43568",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_043569.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-23T21:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5593#issuecomment-43569",
    "user": "mabshoff"
}
```

Resolution: fixed
