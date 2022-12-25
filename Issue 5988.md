# Issue 5988: notebook feature request -- make it so non-logged in users are redirected to login page

archive/issues_005988.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @TimDumol\n\nI strongly agree with the following feature request.  I have wanted the same feature myself.\n\n\n```\nIf the sage notebook server is restarted while a logged in user is\nviewing a notebook page, a user attempt to refresh the page results in\na completely blank page titled \"Error | Sage Notebook\".  The user must\nmanually edit the URL to go back to the main server page and login\nagain, presumably because the login credentials have been lost with\nthe server reboot.\n\nBut, it may not be obvious to all users what they need to do to\nrecover from this situation.  Is there some twisted option I can set\nto either redirect the browser back to the login page, or to add\nexplanatory text to the blank page with a link to the login page?  If\nneither of these options is currently possible, I'd like to make a\nfeature request to enhance the server response to an attempt to access\na page when a user is apparently not logged in, to provide the user\nwith a useful page, rather than a completely blank page.\n\nI'm running sage 3.4.2.\n\nThanks,\n--\nKevin Horton\nOttawa, Canada\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5988\n\n",
    "created_at": "2009-05-05T14:22:58Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook feature request -- make it so non-logged in users are redirected to login page",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5988",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

CC:  @TimDumol

I strongly agree with the following feature request.  I have wanted the same feature myself.


```
If the sage notebook server is restarted while a logged in user is
viewing a notebook page, a user attempt to refresh the page results in
a completely blank page titled "Error | Sage Notebook".  The user must
manually edit the URL to go back to the main server page and login
again, presumably because the login credentials have been lost with
the server reboot.

But, it may not be obvious to all users what they need to do to
recover from this situation.  Is there some twisted option I can set
to either redirect the browser back to the login page, or to add
explanatory text to the blank page with a link to the login page?  If
neither of these options is currently possible, I'd like to make a
feature request to enhance the server response to an attempt to access
a page when a user is apparently not logged in, to provide the user
with a useful page, rather than a completely blank page.

I'm running sage 3.4.2.

Thanks,
--
Kevin Horton
Ottawa, Canada

```


Issue created by migration from https://trac.sagemath.org/ticket/5988





---

archive/issue_comments_047496.json:
```json
{
    "body": "See also #6069.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-18T13:19:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5988#issuecomment-47496",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

See also #6069.

Cheers,

Michael



---

archive/issue_comments_047497.json:
```json
{
    "body": "I think this is no longer a problem, at least with SageNB 0.7 (#8051) and maybe even with SageNB 0.6.  If I try to reload the home page or an opened worksheet, I get redirected to the login page or to a page with a message, e.g.,\n\n  You are not logged in or do not have access to the worksheet 'XXX'. Continue\n\nClicking \"Continue\" takes me to the login page.  But clicking on \"Log,\" \"Settings,\" or \"Help\" returns `404 Not Found`, instead of redirecting to the login page.",
    "created_at": "2010-01-25T15:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5988#issuecomment-47497",
    "user": "https://github.com/qed777"
}
```

I think this is no longer a problem, at least with SageNB 0.7 (#8051) and maybe even with SageNB 0.6.  If I try to reload the home page or an opened worksheet, I get redirected to the login page or to a page with a message, e.g.,

  You are not logged in or do not have access to the worksheet 'XXX'. Continue

Clicking "Continue" takes me to the login page.  But clicking on "Log," "Settings," or "Help" returns `404 Not Found`, instead of redirecting to the login page.



---

archive/issue_comments_047498.json:
```json
{
    "body": "Actually, this may still be a problem in WebKit browsers.",
    "created_at": "2010-01-25T16:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5988#issuecomment-47498",
    "user": "https://github.com/qed777"
}
```

Actually, this may still be a problem in WebKit browsers.



---

archive/issue_comments_047499.json:
```json
{
    "body": "I cannot replicate this in Safari, Chrome, or FF on Mac.  The \"searching for Sage server\" takes care of most instances, and I don't see the page mentioned above.  Presumably the flask transition?",
    "created_at": "2014-12-10T18:57:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5988#issuecomment-47499",
    "user": "https://github.com/kcrisman"
}
```

I cannot replicate this in Safari, Chrome, or FF on Mac.  The "searching for Sage server" takes care of most instances, and I don't see the page mentioned above.  Presumably the flask transition?



---

archive/issue_comments_047500.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-12-10T18:57:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5988#issuecomment-47500",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_047501.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-10T18:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5988#issuecomment-47501",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_047502.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2014-12-11T18:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5988#issuecomment-47502",
    "user": "https://github.com/vbraun"
}
```

Resolution: worksforme



---

archive/issue_events_006243.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2014-12-11T18:37:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5988",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5988#event-6243"
}
```
