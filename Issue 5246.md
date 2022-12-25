# Issue 5246: installing R package in r.console() doesn't work

archive/issues_005246.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @mwhansen\n\nfrom [public \"report a problem\" bugtracker in the notebook](http://spreadsheets.google.com/ver?key=pCwvGVwSMxTzT6E2xNdo5fA&t=1234453264894000&pt=1234453244894000&diffWidget=true&s=AJVazbUgzUp_UbQ1kyziS_LZuaCZwUhLGA)\n\nInstalling CRAN packages with `r.console()` and then `install.packages()` fails with the error: \n\n\"Can't open /home/was/build/sage-3.1.4/local/lib/R/share/sh/dcf.sh\". **Strange enough, as the Sage version is 3.2.3, not 3.1.4.** This can be \"fixed\" by creating a symlink from /home/was/build/sage-3.1.4 to the real Sage installation, but it would be better if it worked out of the box. R without CRAN is not very useful.\n\n---\n\nNote by me: seems like there is something linked absolutely!\n\nIssue created by migration from https://trac.sagemath.org/ticket/5246\n\n",
    "closed_at": "2010-01-25T23:24:49Z",
    "created_at": "2009-02-12T15:59:42Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "installing R package in r.console() doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5246",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: mabshoff

CC:  @mwhansen

from [public "report a problem" bugtracker in the notebook](http://spreadsheets.google.com/ver?key=pCwvGVwSMxTzT6E2xNdo5fA&t=1234453264894000&pt=1234453244894000&diffWidget=true&s=AJVazbUgzUp_UbQ1kyziS_LZuaCZwUhLGA)

Installing CRAN packages with `r.console()` and then `install.packages()` fails with the error: 

"Can't open /home/was/build/sage-3.1.4/local/lib/R/share/sh/dcf.sh". **Strange enough, as the Sage version is 3.2.3, not 3.1.4.** This can be "fixed" by creating a symlink from /home/was/build/sage-3.1.4 to the real Sage installation, but it would be better if it worked out of the box. R without CRAN is not very useful.

---

Note by me: seems like there is something linked absolutely!

Issue created by migration from https://trac.sagemath.org/ticket/5246





---

archive/issue_comments_040138.json:
```json
{
    "body": "This is from a binary not build by that person that seems to have been upgraded in place. I am not sure this is reproducible, so unless someone can either reproduce this or get the original reporter to give additional info this is \"invalid\" for me.\n\nR in general does stupid things like ignore RHOME and R_HOME when using cran, so this might very well be an upstream bug.\n\nIn general bugs reported via \"report a problem\" should go to the groups first before anyone opens a ticket.\n\nAnd this certainly isn't critical.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-12T16:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5246#issuecomment-40138",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is from a binary not build by that person that seems to have been upgraded in place. I am not sure this is reproducible, so unless someone can either reproduce this or get the original reporter to give additional info this is "invalid" for me.

R in general does stupid things like ignore RHOME and R_HOME when using cran, so this might very well be an upstream bug.

In general bugs reported via "report a problem" should go to the groups first before anyone opens a ticket.

And this certainly isn't critical.

Cheers,

Michael



---

archive/issue_comments_040139.json:
```json
{
    "body": "To release manager: I recommend this be closed, as it seems to be a duplicate of #4959.",
    "created_at": "2009-12-11T20:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5246#issuecomment-40139",
    "user": "https://github.com/kcrisman"
}
```

To release manager: I recommend this be closed, as it seems to be a duplicate of #4959.



---

archive/issue_comments_040140.json:
```json
{
    "body": "This is apparently fixed by #6532.",
    "created_at": "2010-01-25T19:17:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5246#issuecomment-40140",
    "user": "https://github.com/kcrisman"
}
```

This is apparently fixed by #6532.



---

archive/issue_events_012187.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-25T23:24:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5246",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5246#event-12187"
}
```



---

archive/issue_comments_040141.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-25T23:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5246#issuecomment-40141",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: duplicate



---

archive/issue_comments_040142.json:
```json
{
    "body": "Close as duplicate of #4959.",
    "created_at": "2010-01-25T23:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5246#issuecomment-40142",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Close as duplicate of #4959.



---

archive/issue_events_012188.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-25T23:24:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5246",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5246#event-12188"
}
```
