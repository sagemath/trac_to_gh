# Issue 2803: notebook -- the confirmation email after creating a new account is marked as spam

archive/issues_002803.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\n----BEGIN PGP SIGNED MESSAGE-----\nHash: SHA1\n\nProfessor Stein:\nAfter registering for the sage notebook, I noticed that my confirmation\nemail was tagged as spam. looking at the headers I saw\nmath.sage.washington.edu (more accurately its IP 128.208.160.191) was\nblacklisted by XBL:\nhttp://www.spamhaus.org/xbl/\nChecking XBL, I found that the IP was included since it was included in\nanother blacklist, CBL:\nhttp://cbl.abuseat.org/lookup.cgi?ip=128.208.160.191\n\nCBL lists the server for non-RFC2821 compliant HELO host names. Checking\nthe header of the notebook registration confirmed this.\n\nReceived: from localhost.localdomain (sage.math.washington.edu\n[128.208.160.191])\nby mail.erkert.com with SMTP id 97F2E2CB077\nfor <>; Fri,  4 Apr 2008 04:37:23 -0700 (PDT)\n\nTo remove the server from the blacklists CBL&XBL, it should be a pretty\neasy fix and is discussed for numerous MTAs on:\nhttp://cbl.abuseat.org/namingproblems.html\n\n- --Nick Erkert\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2803\n\n",
    "created_at": "2008-04-05T02:23:27Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook -- the confirmation email after creating a new account is marked as spam",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2803",
    "user": "@williamstein"
}
```
Assignee: boothby


```
----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA1

Professor Stein:
After registering for the sage notebook, I noticed that my confirmation
email was tagged as spam. looking at the headers I saw
math.sage.washington.edu (more accurately its IP 128.208.160.191) was
blacklisted by XBL:
http://www.spamhaus.org/xbl/
Checking XBL, I found that the IP was included since it was included in
another blacklist, CBL:
http://cbl.abuseat.org/lookup.cgi?ip=128.208.160.191

CBL lists the server for non-RFC2821 compliant HELO host names. Checking
the header of the notebook registration confirmed this.

Received: from localhost.localdomain (sage.math.washington.edu
[128.208.160.191])
by mail.erkert.com with SMTP id 97F2E2CB077
for <>; Fri,  4 Apr 2008 04:37:23 -0700 (PDT)

To remove the server from the blacklists CBL&XBL, it should be a pretty
easy fix and is discussed for numerous MTAs on:
http://cbl.abuseat.org/namingproblems.html

- --Nick Erkert

```


Issue created by migration from https://trac.sagemath.org/ticket/2803





---

archive/issue_comments_019241.json:
```json
{
    "body": "Changing type from defect to task.",
    "created_at": "2009-11-15T17:21:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2803#issuecomment-19241",
    "user": "@TimDumol"
}
```

Changing type from defect to task.



---

archive/issue_comments_019242.json:
```json
{
    "body": "Given that this IP is still relevant to Sage, but according to the link above:\n\n```\nIP Address 128.208.160.191 is not listed in the CBL.\n```\n\nI think we can close this.",
    "created_at": "2013-06-14T20:31:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2803#issuecomment-19242",
    "user": "@kcrisman"
}
```

Given that this IP is still relevant to Sage, but according to the link above:

```
IP Address 128.208.160.191 is not listed in the CBL.
```

I think we can close this.



---

archive/issue_comments_019243.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-06-14T20:31:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2803#issuecomment-19243",
    "user": "@kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_019244.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-14T20:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2803#issuecomment-19244",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_019245.json:
```json
{
    "body": "Neither is 128.208.160.198, sagenb.org, so I think we're set.",
    "created_at": "2013-06-14T20:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2803#issuecomment-19245",
    "user": "@kcrisman"
}
```

Neither is 128.208.160.198, sagenb.org, so I think we're set.



---

archive/issue_comments_019246.json:
```json
{
    "body": "Changing component from notebook to website/wiki.",
    "created_at": "2013-06-19T12:19:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2803#issuecomment-19246",
    "user": "@jdemeyer"
}
```

Changing component from notebook to website/wiki.



---

archive/issue_comments_019247.json:
```json
{
    "body": "In any case, this is not a Sage ticket.",
    "created_at": "2013-06-19T12:19:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2803#issuecomment-19247",
    "user": "@jdemeyer"
}
```

In any case, this is not a Sage ticket.



---

archive/issue_comments_019248.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-06-19T12:19:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2803#issuecomment-19248",
    "user": "@jdemeyer"
}
```

Resolution: invalid
