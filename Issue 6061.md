# Issue 6061: [with patch; needs review] refresh the pickle jar

archive/issues_006061.json:
```json
{
    "body": "Assignee: mabshoff\n\nSage-4.0 has tons  (nearly 100) of objects with doctests that create pickles, which aren't in the pickle jar right now (in sage-3.4.2).  \nThe attached new pickle *adds* all these 100 pickles to the existing pickle jar, and deletes a few from calculus that are no longer supported.  This depends on the pynac switch for the new symbolic pickles to work.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6061\n\n",
    "created_at": "2009-05-18T04:00:25Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch; needs review] refresh the pickle jar",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6061",
    "user": "was"
}
```
Assignee: mabshoff

Sage-4.0 has tons  (nearly 100) of objects with doctests that create pickles, which aren't in the pickle jar right now (in sage-3.4.2).  
The attached new pickle *adds* all these 100 pickles to the existing pickle jar, and deletes a few from calculus that are no longer supported.  This depends on the pynac switch for the new symbolic pickles to work.

Issue created by migration from https://trac.sagemath.org/ticket/6061





---

archive/issue_comments_048250.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-20T23:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6061#issuecomment-48250",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_048251.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-20T23:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6061#issuecomment-48251",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_048252.json:
```json
{
    "body": "Oh, positive review obviously.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-20T23:40:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6061#issuecomment-48252",
    "user": "mabshoff"
}
```

Oh, positive review obviously.

Cheers,

Michael
