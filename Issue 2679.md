# Issue 2679: sage docs -- get rid of aux, etc., files when packaging up for distribution

archive/issues_002679.json:
```json
{
    "body": "Assignee: tba\n\n\n```\n> 3. removing the .aux and .toc cache files from the documentation area\n> solved the pdf/html problems.\n\nok, we ought to make sure that we remove all those temp files before\npackaging the documentation.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2679\n\n",
    "created_at": "2008-03-26T18:36:16Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "sage docs -- get rid of aux, etc., files when packaging up for distribution",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2679",
    "user": "@williamstein"
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

archive/issue_comments_018424.json:
```json
{
    "body": "The file to change is \n\n```\n   doc/scripts/spkg-dist\n```\n\n\nSee also #2675, which is the same problem.",
    "created_at": "2008-03-26T18:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2679#issuecomment-18424",
    "user": "@williamstein"
}
```

The file to change is 

```
   doc/scripts/spkg-dist
```


See also #2675, which is the same problem.



---

archive/issue_comments_018425.json:
```json
{
    "body": "This can be closed now, right?",
    "created_at": "2009-02-26T17:09:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2679#issuecomment-18425",
    "user": "@jhpalmieri"
}
```

This can be closed now, right?



---

archive/issue_comments_018426.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-26T17:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2679#issuecomment-18426",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018427.json:
```json
{
    "body": "Close in Sage 3.4.alpha0 due to the switch to ReST.\n\nThanks for catching this.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-26T17:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2679#issuecomment-18427",
    "user": "mabshoff"
}
```

Close in Sage 3.4.alpha0 due to the switch to ReST.

Thanks for catching this.

Cheers,

Michael
