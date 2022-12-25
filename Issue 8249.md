# Issue 8249: sagenb: notebook cookies

archive/issues_008249.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  acleone @qed777 mhampton\n\nThis is a followup to #6353.   That ticket improved cookie naming a bit.  However, it appears to be not enough.  \n\n\n```\nOn Thu, Feb 11, 2010 at 7:21 PM, Marshall Hampton <> wrote:\n> Just for the record, this has happened to me quite a bit recently.\n>\n> I use a lot of different sage servers, often running different\n> versions, so I don't usually report this kind of stuff since I think I\n> am something of an extreme case.  But most of the servers I use are\n> now running 4.3.2 and I am pretty sure I have seen the cookie message\n> more than before.\n>\n\nHere's the relevant ticket I was remembering:\n\n     http://trac.sagemath.org/sage_trac/ticket/6353\n\nIt is definitely in sage-4.3.2 (since it is merged into sagenb-0.7.4).   \n\nLooking at that patch show that:\n\n  (1) it addresses a related issue,\n\n  (2) it might not solve the issue we're discussing, since it merely includes the *port* in the cookie name -- some unique id for the notebook (e.g., the URL or something else) is maybe also needed to fix the problem we're discussing.\n\nSo somebody should look at ticket 6353, see if a small modification of it would give a real fix, and make said modification.      Alex Leone: this would be a good project for you, if you're looking for something to do on the notebook. \n\n -- William\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8249\n\n",
    "created_at": "2010-02-12T12:12:00Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "sagenb: notebook cookies",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8249",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  acleone @qed777 mhampton

This is a followup to #6353.   That ticket improved cookie naming a bit.  However, it appears to be not enough.  


```
On Thu, Feb 11, 2010 at 7:21 PM, Marshall Hampton <> wrote:
> Just for the record, this has happened to me quite a bit recently.
>
> I use a lot of different sage servers, often running different
> versions, so I don't usually report this kind of stuff since I think I
> am something of an extreme case.  But most of the servers I use are
> now running 4.3.2 and I am pretty sure I have seen the cookie message
> more than before.
>

Here's the relevant ticket I was remembering:

     http://trac.sagemath.org/sage_trac/ticket/6353

It is definitely in sage-4.3.2 (since it is merged into sagenb-0.7.4).   

Looking at that patch show that:

  (1) it addresses a related issue,

  (2) it might not solve the issue we're discussing, since it merely includes the *port* in the cookie name -- some unique id for the notebook (e.g., the URL or something else) is maybe also needed to fix the problem we're discussing.

So somebody should look at ticket 6353, see if a small modification of it would give a real fix, and make said modification.      Alex Leone: this would be a good project for you, if you're looking for something to do on the notebook. 

 -- William
```


Issue created by migration from https://trac.sagemath.org/ticket/8249





---

archive/issue_comments_072834.json:
```json
{
    "body": "I couldn't reproduce his by signing in/out of sagenb.org and demo.sagenb.org.  Cookies are stored by domain (sagenb.org and demo.sagenb.org are two seperate sites), so differentiating by port should be all that's necessary.\n\nI made sure all instances of 'cookie' in twist.py were updated from #6353 (they were), so I really have no idea what is causing this.  It could be a subtle bug in the 'cookie_test' cookie.",
    "created_at": "2010-02-12T21:00:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8249#issuecomment-72834",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

I couldn't reproduce his by signing in/out of sagenb.org and demo.sagenb.org.  Cookies are stored by domain (sagenb.org and demo.sagenb.org are two seperate sites), so differentiating by port should be all that's necessary.

I made sure all instances of 'cookie' in twist.py were updated from #6353 (they were), so I really have no idea what is causing this.  It could be a subtle bug in the 'cookie_test' cookie.



---

archive/issue_comments_072835.json:
```json
{
    "body": "Has anyone been able to reproduce the problem reliably?  It would help greatly to have specific instructions.",
    "created_at": "2010-02-14T03:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8249#issuecomment-72835",
    "user": "https://github.com/qed777"
}
```

Has anyone been able to reproduce the problem reliably?  It would help greatly to have specific instructions.



---

archive/issue_comments_072836.json:
```json
{
    "body": "Expire cookies on logout.  sagenb repo.",
    "created_at": "2010-02-14T04:38:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8249#issuecomment-72836",
    "user": "https://github.com/qed777"
}
```

Expire cookies on logout.  sagenb repo.



---

archive/issue_comments_072837.json:
```json
{
    "body": "Attachment [trac_8249-notebook_cookies.patch](tarball://root/attachments/some-uuid/ticket8249/trac_8249-notebook_cookies.patch) by @qed777 created at 2010-02-14 04:44:12\n\nI've attached a patch that should delete both the test and notebook session cookies, when a user logs out.",
    "created_at": "2010-02-14T04:44:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8249#issuecomment-72837",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8249-notebook_cookies.patch](tarball://root/attachments/some-uuid/ticket8249/trac_8249-notebook_cookies.patch) by @qed777 created at 2010-02-14 04:44:12

I've attached a patch that should delete both the test and notebook session cookies, when a user logs out.



---

archive/issue_comments_072838.json:
```json
{
    "body": "The patch may depend weakly on #6069.",
    "created_at": "2010-02-14T04:44:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8249#issuecomment-72838",
    "user": "https://github.com/qed777"
}
```

The patch may depend weakly on #6069.



---

archive/issue_comments_072839.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-14T04:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8249#issuecomment-72839",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072840.json:
```json
{
    "body": "LGTM: I can't produce any cookie errors through normal use.\n\nHowever, selenium errors when logging out - I'm working on a new patch to fix the tests.  (See attached for log)",
    "created_at": "2010-02-14T06:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8249#issuecomment-72840",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

LGTM: I can't produce any cookie errors through normal use.

However, selenium errors when logging out - I'm working on a new patch to fix the tests.  (See attached for log)



---

archive/issue_comments_072841.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-14T06:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8249#issuecomment-72841",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072842.json:
```json
{
    "body": "Selenium errors with patch.  Same errors when the patch for #6069 -missing_pub_ws.3 is applied.",
    "created_at": "2010-02-14T06:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8249#issuecomment-72842",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Selenium errors with patch.  Same errors when the patch for #6069 -missing_pub_ws.3 is applied.



---

archive/issue_comments_072843.json:
```json
{
    "body": "Attachment [trac_8249-notebook_cookies-selenium_errors.log](tarball://root/attachments/some-uuid/ticket8249/trac_8249-notebook_cookies-selenium_errors.log) by @qed777 created at 2010-02-14 06:55:39\n\nThanks for catching the Se test errors.  I should have checked.\n\nThe patch fixes for me the one cookie-related problem I could reproduce reliably:  Logging out in Chrom* displays a browser error page:\n\n\n```\nThis webpage has a redirect loop.\n\nThe webpage at http://localhost:8000/home/admin/ has resulted in too many redirects. Clearing your cookies for this site or allowing third-party cookies may fix the problem. If not, it is possibly a server configuration issue and not a problem with your computer.\n```\n\nBut with the patch, clicking on \"Sign Out\" just returns me to the login page.  I'm not sure if it helps with the reported problems, but making the cookies expire on logout seems logical.",
    "created_at": "2010-02-14T06:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8249#issuecomment-72843",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8249-notebook_cookies-selenium_errors.log](tarball://root/attachments/some-uuid/ticket8249/trac_8249-notebook_cookies-selenium_errors.log) by @qed777 created at 2010-02-14 06:55:39

Thanks for catching the Se test errors.  I should have checked.

The patch fixes for me the one cookie-related problem I could reproduce reliably:  Logging out in Chrom* displays a browser error page:


```
This webpage has a redirect loop.

The webpage at http://localhost:8000/home/admin/ has resulted in too many redirects. Clearing your cookies for this site or allowing third-party cookies may fix the problem. If not, it is possibly a server configuration issue and not a problem with your computer.
```

But with the patch, clicking on "Sign Out" just returns me to the login page.  I'm not sure if it helps with the reported problems, but making the cookies expire on logout seems logical.



---

archive/issue_comments_072844.json:
```json
{
    "body": "For some reason Selenium doesn't like HTTP redirect responses.  I keep getting this 'Problem loading page' error (in firefox):\n\n```\nThe page isn't redirecting properly\n      \nFirefox has detected that the server is redirecting the request for this address in a way that will never complete.\n\n    *   This problem can sometimes be caused by disabling or refusing to accept\n          cookies.\n```\n\n\nThis always happens when the selenium gets the redirect HTTP response.  Perhaps we should change it back to a dedicated logout page, but add a `<meta http-equiv=\"Refresh\"` tag so the page redirects after a second.",
    "created_at": "2010-02-15T04:57:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8249#issuecomment-72844",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

For some reason Selenium doesn't like HTTP redirect responses.  I keep getting this 'Problem loading page' error (in firefox):

```
The page isn't redirecting properly
      
Firefox has detected that the server is redirecting the request for this address in a way that will never complete.

    *   This problem can sometimes be caused by disabling or refusing to accept
          cookies.
```


This always happens when the selenium gets the redirect HTTP response.  Perhaps we should change it back to a dedicated logout page, but add a `<meta http-equiv="Refresh"` tag so the page redirects after a second.



---

archive/issue_comments_072845.json:
```json
{
    "body": "Adjust `close_callback` to make Se tests pass.  Apply only this patch.",
    "created_at": "2010-02-15T07:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8249#issuecomment-72845",
    "user": "https://github.com/qed777"
}
```

Adjust `close_callback` to make Se tests pass.  Apply only this patch.



---

archive/issue_comments_072846.json:
```json
{
    "body": "Attachment [trac_8249-notebook_cookies.2.patch](tarball://root/attachments/some-uuid/ticket8249/trac_8249-notebook_cookies.2.patch) by @qed777 created at 2010-02-15 07:45:54\n\nV2 replaces `'/'` with `'/home/' + user_name` in `notebook_lib.js`'s `close_callback`.  Strangely, this seems to work.",
    "created_at": "2010-02-15T07:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8249#issuecomment-72846",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8249-notebook_cookies.2.patch](tarball://root/attachments/some-uuid/ticket8249/trac_8249-notebook_cookies.2.patch) by @qed777 created at 2010-02-15 07:45:54

V2 replaces `'/'` with `'/home/' + user_name` in `notebook_lib.js`'s `close_callback`.  Strangely, this seems to work.



---

archive/issue_comments_072847.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-16T02:01:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8249#issuecomment-72847",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072848.json:
```json
{
    "body": "I'm signing this off since it's a good idea, and may help. I'm unable to replicate the cookie issue though, with or without this patch, but it may be related to the performance issues of the sagenb server.",
    "created_at": "2010-03-19T08:21:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8249#issuecomment-72848",
    "user": "https://github.com/TimDumol"
}
```

I'm signing this off since it's a good idea, and may help. I'm unable to replicate the cookie issue though, with or without this patch, but it may be related to the performance issues of the sagenb server.



---

archive/issue_comments_072849.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-19T08:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8249#issuecomment-72849",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072850.json:
```json
{
    "body": "Woops. Forgot to add Alex.",
    "created_at": "2010-03-19T08:21:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8249#issuecomment-72850",
    "user": "https://github.com/TimDumol"
}
```

Woops. Forgot to add Alex.



---

archive/issue_comments_072851.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-04T04:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8249#issuecomment-72851",
    "user": "https://github.com/TimDumol"
}
```

Resolution: fixed



---

archive/issue_events_008450.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-05-04T04:44:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8249",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8249#event-8450"
}
```
