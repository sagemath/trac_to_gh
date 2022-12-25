# Issue 8755: modify sagenb-*/src/sagenb/spkg-dist to produce valid spkg's

archive/issues_008755.json:
```json
{
    "body": "Assignee: jason, was\n\nThe spkg format for Sage requires that:\n\n   (1) the sagenb-*/ directory (that contains spkg-install, SPKG.txt, etc.) has its own hg report, which has spkg-install and SPKG.txt checked in.\n\n   (2) SPKG.txt gets regularly updated with a log message for each new spkg release.\n\nThe goal of this ticket it to change the file src/sagenb/spkg-dist, so that when it it run to create a new spkg, the resulting spkg is *valid* as explained above.  That's it. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8755\n\n",
    "created_at": "2010-04-24T21:38:40Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "modify sagenb-*/src/sagenb/spkg-dist to produce valid spkg's",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8755",
    "user": "https://github.com/williamstein"
}
```
Assignee: jason, was

The spkg format for Sage requires that:

   (1) the sagenb-*/ directory (that contains spkg-install, SPKG.txt, etc.) has its own hg report, which has spkg-install and SPKG.txt checked in.

   (2) SPKG.txt gets regularly updated with a log message for each new spkg release.

The goal of this ticket it to change the file src/sagenb/spkg-dist, so that when it it run to create a new spkg, the resulting spkg is *valid* as explained above.  That's it. 

Issue created by migration from https://trac.sagemath.org/ticket/8755





---

archive/issue_comments_079962.json:
```json
{
    "body": "This is no longer valid given all the changes in how sagenb is incorporated in Sage.",
    "created_at": "2014-09-17T02:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8755#issuecomment-79962",
    "user": "https://github.com/kcrisman"
}
```

This is no longer valid given all the changes in how sagenb is incorporated in Sage.



---

archive/issue_comments_079963.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-09-17T02:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8755#issuecomment-79963",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079964.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-09-17T02:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8755#issuecomment-79964",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008923.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2014-09-18T17:59:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8755",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8755#event-8923"
}
```



---

archive/issue_comments_079965.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2014-09-18T17:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8755#issuecomment-79965",
    "user": "https://github.com/vbraun"
}
```

Resolution: invalid
