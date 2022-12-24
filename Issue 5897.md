# Issue 5897: add some javascript to make jsmath happier (very easy ticket to close, probably)

archive/issues_005897.json:
```json
{
    "body": "Assignee: boothby\n\nThis was on sage-support on April 25.  \n\n```\nThanks for posting the new example.  I have found that the problem is\ndue to the fact that Sage puts the output inside a <PRE> block, and\nIE7 gets confused about some of its measurements in that case.  It can\nbe fixed by including\n\n span.typeset {\n    white-space: normal;\n }\n\nin the css/main.css file for sage.  I will add this to jsMath in the\nnext release.\n\nDavide\n```\n\n\nWe should add this to sage, since who knows when it'll go into jsmath and get into sage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5897\n\n",
    "created_at": "2009-04-26T02:05:09Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "add some javascript to make jsmath happier (very easy ticket to close, probably)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5897",
    "user": "was"
}
```
Assignee: boothby

This was on sage-support on April 25.  

```
Thanks for posting the new example.  I have found that the problem is
due to the fact that Sage puts the output inside a <PRE> block, and
IE7 gets confused about some of its measurements in that case.  It can
be fixed by including

 span.typeset {
    white-space: normal;
 }

in the css/main.css file for sage.  I will add this to jsMath in the
next release.

Davide
```


We should add this to sage, since who knows when it'll go into jsmath and get into sage.

Issue created by migration from https://trac.sagemath.org/ticket/5897





---

archive/issue_comments_046628.json:
```json
{
    "body": "This is in the version of jsMath included with SageNB.  Should we close this ticket?",
    "created_at": "2009-11-14T05:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5897#issuecomment-46628",
    "user": "mpatel"
}
```

This is in the version of jsMath included with SageNB.  Should we close this ticket?



---

archive/issue_comments_046629.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-11-15T14:17:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5897#issuecomment-46629",
    "user": "mhansen"
}
```

Resolution: invalid
