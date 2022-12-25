# Issue 2679: sage docs -- get rid of aux, etc., files when packaging up for distribution

archive/issues_002679.json:
```json
{
    "body": "Assignee: tba\n\n```\n> 3. removing the .aux and .toc cache files from the documentation area\n> solved the pdf/html problems.\n\nok, we ought to make sure that we remove all those temp files before\npackaging the documentation.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2679\n\n",
    "created_at": "2008-03-26T18:36:16Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "sage docs -- get rid of aux, etc., files when packaging up for distribution",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2679",
    "user": "https://github.com/williamstein"
}
```
Assignee: tba

```
> 3. removing the .aux and .toc cache files from the documentation area
> solved the pdf/html problems.

ok, we ought to make sure that we remove all those temp files before
packaging the documentation.
```

Issue created by migration from https://trac.sagemath.org/ticket/2679





---

archive/issue_comments_018385.json:
```json
{
    "body": "The file to change is \n\n```\n   doc/scripts/spkg-dist\n```\n\nSee also #2675, which is the same problem.",
    "created_at": "2008-03-26T18:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2679#issuecomment-18385",
    "user": "https://github.com/williamstein"
}
```

The file to change is 

```
   doc/scripts/spkg-dist
```

See also #2675, which is the same problem.



---

archive/issue_comments_018386.json:
```json
{
    "body": "This can be closed now, right?",
    "created_at": "2009-02-26T17:09:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2679#issuecomment-18386",
    "user": "https://github.com/jhpalmieri"
}
```

This can be closed now, right?



---

archive/issue_comments_018387.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-26T17:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2679#issuecomment-18387",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006253.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-26T17:27:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2679",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2679#event-6253"
}
```



---

archive/issue_comments_018388.json:
```json
{
    "body": "Close in Sage 3.4.alpha0 due to the switch to ReST.\n\nThanks for catching this.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-26T17:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2679#issuecomment-18388",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Close in Sage 3.4.alpha0 due to the switch to ReST.

Thanks for catching this.

Cheers,

Michael



---

archive/issue_events_006254.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-26T17:27:05Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2679",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2679#event-6254"
}
```
