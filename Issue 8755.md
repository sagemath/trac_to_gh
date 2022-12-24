# Issue 8755: modify sagenb-*/src/sagenb/spkg-dist to produce valid spkg's

archive/issues_008755.json:
```json
{
    "body": "Assignee: jason, was\n\nThe spkg format for Sage requires that:\n\n   (1) the sagenb-*/ directory (that contains spkg-install, SPKG.txt, etc.) has its own hg report, which has spkg-install and SPKG.txt checked in.\n\n   (2) SPKG.txt gets regularly updated with a log message for each new spkg release.\n\nThe goal of this ticket it to change the file src/sagenb/spkg-dist, so that when it it run to create a new spkg, the resulting spkg is *valid* as explained above.  That's it. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8755\n\n",
    "created_at": "2010-04-24T21:38:40Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "modify sagenb-*/src/sagenb/spkg-dist to produce valid spkg's",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8755",
    "user": "was"
}
```
Assignee: jason, was

The spkg format for Sage requires that:

   (1) the sagenb-*/ directory (that contains spkg-install, SPKG.txt, etc.) has its own hg report, which has spkg-install and SPKG.txt checked in.

   (2) SPKG.txt gets regularly updated with a log message for each new spkg release.

The goal of this ticket it to change the file src/sagenb/spkg-dist, so that when it it run to create a new spkg, the resulting spkg is *valid* as explained above.  That's it. 

Issue created by migration from https://trac.sagemath.org/ticket/8755





---

archive/issue_comments_080092.json:
```json
{
    "body": "This is no longer valid given all the changes in how sagenb is incorporated in Sage.",
    "created_at": "2014-09-17T02:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8755#issuecomment-80092",
    "user": "kcrisman"
}
```

This is no longer valid given all the changes in how sagenb is incorporated in Sage.



---

archive/issue_comments_080093.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-09-17T02:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8755#issuecomment-80093",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080094.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-09-17T02:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8755#issuecomment-80094",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080095.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2014-09-18T17:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8755#issuecomment-80095",
    "user": "vbraun"
}
```

Resolution: invalid
