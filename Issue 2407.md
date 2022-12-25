# Issue 2407: Notebook fails without explanation when cookies are disabled

archive/issues_002407.json:
```json
{
    "body": "Assignee: boothby\n\nThis may be more of enhancement, but it would be nice to throw up an error message in the notebook if cookies are disabled in the browser.  \n\nFor example, I jumped on sagenb.org to try things out.  After logging in I started with nothing.  I clicked on \"New Worksheet\" to get started, and I get a \"404 Not Found\" error for the page /new_worksheet.  This seems an easy and natural place to tell the user they need to enable cookies in their browser.  Even better would be to check for the expected cookie in the \"just logged in\" page generation logic.\n\nFor completeness, most of the other links on the \"just logged in\" page just ask me to log in again.  (This is when I figured out the problem.  Originally I assumed the notebook must be broken.)  The \"Upload\" link gives me a corresponding 404 page, and \"Log\" and \"Help\" just open new, empty pages.  (Not particularly helpful when I tried it.)  I am using Firefox 2.0.0.12 on FreeBSD 6.3.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2407\n\n",
    "created_at": "2008-03-06T17:19:30Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "Notebook fails without explanation when cookies are disabled",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2407",
    "user": "https://github.com/rhinton"
}
```
Assignee: boothby

This may be more of enhancement, but it would be nice to throw up an error message in the notebook if cookies are disabled in the browser.  

For example, I jumped on sagenb.org to try things out.  After logging in I started with nothing.  I clicked on "New Worksheet" to get started, and I get a "404 Not Found" error for the page /new_worksheet.  This seems an easy and natural place to tell the user they need to enable cookies in their browser.  Even better would be to check for the expected cookie in the "just logged in" page generation logic.

For completeness, most of the other links on the "just logged in" page just ask me to log in again.  (This is when I figured out the problem.  Originally I assumed the notebook must be broken.)  The "Upload" link gives me a corresponding 404 page, and "Log" and "Help" just open new, empty pages.  (Not particularly helpful when I tried it.)  I am using Firefox 2.0.0.12 on FreeBSD 6.3.

Issue created by migration from https://trac.sagemath.org/ticket/2407





---

archive/issue_comments_016217.json:
```json
{
    "body": "Attachment [sage-2407_1.patch](tarball://root/attachments/some-uuid/ticket2407/sage-2407_1.patch) by TimothyClemans created at 2008-09-29 18:48:38",
    "created_at": "2008-09-29T18:48:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2407#issuecomment-16217",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-2407_1.patch](tarball://root/attachments/some-uuid/ticket2407/sage-2407_1.patch) by TimothyClemans created at 2008-09-29 18:48:38



---

archive/issue_comments_016218.json:
```json
{
    "body": "Attachment [sage-2407_2.patch](tarball://root/attachments/some-uuid/ticket2407/sage-2407_2.patch) by TimothyClemans created at 2008-09-29 18:48:57",
    "created_at": "2008-09-29T18:48:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2407#issuecomment-16218",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-2407_2.patch](tarball://root/attachments/some-uuid/ticket2407/sage-2407_2.patch) by TimothyClemans created at 2008-09-29 18:48:57



---

archive/issue_comments_016219.json:
```json
{
    "body": "Attachment [sage-2407_3.patch](tarball://root/attachments/some-uuid/ticket2407/sage-2407_3.patch) by TimothyClemans created at 2008-09-29 18:49:49\n\nTicket has been rebased. Apply all 3 patches.",
    "created_at": "2008-09-29T18:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2407#issuecomment-16219",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-2407_3.patch](tarball://root/attachments/some-uuid/ticket2407/sage-2407_3.patch) by TimothyClemans created at 2008-09-29 18:49:49

Ticket has been rebased. Apply all 3 patches.



---

archive/issue_comments_016220.json:
```json
{
    "body": "\n```\n13:43 < jason-> okay, after getting the error, I reenabled cookies, but I still\n                get the error.\n13:44 < tclemans> refresh the homepage?\n13:44 < tclemans> *login page\n13:44 < jason-> ah, works now.\n13:45 < jason-> huh, so I disable cookies after logging in\n13:45 < jason-> and get a \"You are not logged in or do not have access to the\n                worksheet '104'.\"\n13:45 < jason-> not a cookie message\n13:46 < tclemans> ok well I never meant to fix that issue basically on the\n                  login page we set a test cookie and while login is being\n                  processed we look for that cookie\n13:46 < jason-> okay\n13:46 < tclemans> and then that cookie is deleted after succesful login\n```\n",
    "created_at": "2008-09-29T20:50:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2407#issuecomment-16220",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```


```
13:43 < jason-> okay, after getting the error, I reenabled cookies, but I still
                get the error.
13:44 < tclemans> refresh the homepage?
13:44 < tclemans> *login page
13:44 < jason-> ah, works now.
13:45 < jason-> huh, so I disable cookies after logging in
13:45 < jason-> and get a "You are not logged in or do not have access to the
                worksheet '104'."
13:45 < jason-> not a cookie message
13:46 < tclemans> ok well I never meant to fix that issue basically on the
                  login page we set a test cookie and while login is being
                  processed we look for that cookie
13:46 < jason-> okay
13:46 < tclemans> and then that cookie is deleted after succesful login
```




---

archive/issue_comments_016221.json:
```json
{
    "body": "I applied all three patches to 3.1.3alpha1 and verified that the intended error message pops up trying to log in without cookies enabled.  I looked at the code and it looks like it might be reasonable, but I am not familiar with this specific section of the code base, so I might have missed something.\n\nTentative positive review, in that I verified from the user's standpoint the bug is fixed.",
    "created_at": "2008-09-29T20:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2407#issuecomment-16221",
    "user": "https://github.com/jasongrout"
}
```

I applied all three patches to 3.1.3alpha1 and verified that the intended error message pops up trying to log in without cookies enabled.  I looked at the code and it looks like it might be reasonable, but I am not familiar with this specific section of the code base, so I might have missed something.

Tentative positive review, in that I verified from the user's standpoint the bug is fixed.



---

archive/issue_comments_016222.json:
```json
{
    "body": "Jason, \n\nplease stick with the agreed upon labels.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-29T22:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2407#issuecomment-16222",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Jason, 

please stick with the agreed upon labels.

Cheers,

Michael



---

archive/issue_comments_016223.json:
```json
{
    "body": "I'm with jason: I applied the three patches 3.1.3alpha1 and now get an error message when trying to log in with no cookies, but I don't know the Twisted code much and can't really comment on that. So consider this another positive user-experience review.",
    "created_at": "2008-09-30T01:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2407#issuecomment-16223",
    "user": "https://github.com/dandrake"
}
```

I'm with jason: I applied the three patches 3.1.3alpha1 and now get an error message when trying to log in with no cookies, but I don't know the Twisted code much and can't really comment on that. So consider this another positive user-experience review.



---

archive/issue_comments_016224.json:
```json
{
    "body": "I think we can merge this.",
    "created_at": "2008-09-30T11:54:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2407#issuecomment-16224",
    "user": "https://github.com/mwhansen"
}
```

I think we can merge this.



---

archive/issue_comments_016225.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-30T11:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2407#issuecomment-16225",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002583.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-30T11:59:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2407",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2407#event-2583"
}
```



---

archive/issue_comments_016226.json:
```json
{
    "body": "Merged all three patches in Sage 3.1.3.alpha2",
    "created_at": "2008-09-30T11:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2407#issuecomment-16226",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 3.1.3.alpha2
