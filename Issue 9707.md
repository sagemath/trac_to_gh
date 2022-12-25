# Issue 9707: Add a "signless" option to laplacian

archive/issues_009707.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  @nathanncohen @rlmill @dcoudert\n\nWe should have an option to g.laplacian() to return the signless Laplacian, which is attracting attention these days, and which is calculated by `D+A` instead of `D-A` (see p. 12 of http://www.doiserbia.nb.rs/ft.aspx?id=0350-13020795011C, for example).\n\nThanks to Steve Butler for the feature request.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9707\n\n",
    "created_at": "2010-08-08T00:40:24Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.7",
    "title": "Add a \"signless\" option to laplacian",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9707",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jason, ncohen, rlm

CC:  @nathanncohen @rlmill @dcoudert

We should have an option to g.laplacian() to return the signless Laplacian, which is attracting attention these days, and which is calculated by `D+A` instead of `D-A` (see p. 12 of http://www.doiserbia.nb.rs/ft.aspx?id=0350-13020795011C, for example).

Thanks to Steve Butler for the feature request.

Issue created by migration from https://trac.sagemath.org/ticket/9707





---

archive/issue_events_024267.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9707",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9707#event-24267"
}
```



---

archive/issue_events_024268.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9707",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9707#event-24268"
}
```



---

archive/issue_events_024269.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9707",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9707#event-24269"
}
```



---

archive/issue_events_024270.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9707",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9707#event-24270"
}
```



---

archive/issue_events_024271.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9707",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9707#event-24271"
}
```



---

archive/issue_events_024272.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9707",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9707#event-24272"
}
```



---

archive/issue_events_024273.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9707",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9707#event-24273"
}
```



---

archive/issue_comments_094454.json:
```json
{
    "body": "Signless laplacian is indeed gaining popularity as evident in the papers below.\nSo can I add the option to the current Laplacian Matrix method to return signless laplacian matrix?\n\nhttps://arxiv.org/pdf/1803.06135.pdf\n\nhttp://elib.mi.sanu.ac.rs/files/journals/publ/101/n095p011.pdf\n\nhttps://ac.els-cdn.com/S0024379507000316/1-s2.0-S0024379507000316-main.pdf?_tid=59a3915e-dd7a-4dea-87a7-1892bc82cdca&acdnat=1552416165_1a56db5226e8357d8b7c9879a5dc3973",
    "created_at": "2019-03-12T18:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9707#issuecomment-94454",
    "user": "https://github.com/rajat1433"
}
```

Signless laplacian is indeed gaining popularity as evident in the papers below.
So can I add the option to the current Laplacian Matrix method to return signless laplacian matrix?

https://arxiv.org/pdf/1803.06135.pdf

http://elib.mi.sanu.ac.rs/files/journals/publ/101/n095p011.pdf

https://ac.els-cdn.com/S0024379507000316/1-s2.0-S0024379507000316-main.pdf?_tid=59a3915e-dd7a-4dea-87a7-1892bc82cdca&acdnat=1552416165_1a56db5226e8357d8b7c9879a5dc3973



---

archive/issue_comments_094455.json:
```json
{
    "body": "A quick search effectively returns a significant number of recent publications.",
    "created_at": "2019-03-13T10:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9707#issuecomment-94455",
    "user": "https://github.com/dcoudert"
}
```

A quick search effectively returns a significant number of recent publications.



---

archive/issue_comments_094456.json:
```json
{
    "body": "Changing assignee from jason, ncohen, rlm to @rajat1433.",
    "created_at": "2019-03-13T14:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9707#issuecomment-94456",
    "user": "https://github.com/rajat1433"
}
```

Changing assignee from jason, ncohen, rlm to @rajat1433.



---

archive/issue_events_024274.json:
```json
{
    "actor": "https://github.com/rajat1433",
    "created_at": "2019-03-13T14:25:00Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9707",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9707#event-24274"
}
```



---

archive/issue_events_024275.json:
```json
{
    "actor": "https://github.com/rajat1433",
    "created_at": "2019-03-13T14:25:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9707",
    "milestone": "sage-8.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9707#event-24275"
}
```



---

archive/issue_comments_094457.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2019-03-13T15:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9707#issuecomment-94457",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_094458.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2019-03-13T15:07:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9707#issuecomment-94458",
    "user": "https://github.com/rajat1433"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094459.json:
```json
{
    "body": "Do i need to include this ticket number somewhere in the code?",
    "created_at": "2019-03-13T15:07:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9707#issuecomment-94459",
    "user": "https://github.com/rajat1433"
}
```

Do i need to include this ticket number somewhere in the code?



---

archive/issue_comments_094460.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2019-03-13T17:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9707#issuecomment-94460",
    "user": "https://github.com/dcoudert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094461.json:
```json
{
    "body": "We usually add ticket number when we fix a bug. So it's not needed here.\n\nLGTM.",
    "created_at": "2019-03-13T17:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9707#issuecomment-94461",
    "user": "https://github.com/dcoudert"
}
```

We usually add ticket number when we fix a bug. So it's not needed here.

LGTM.



---

archive/issue_events_024276.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2019-03-14T18:14:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9707",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9707#event-24276"
}
```



---

archive/issue_comments_094462.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2019-03-14T18:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9707#issuecomment-94462",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
