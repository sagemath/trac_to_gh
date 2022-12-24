# Issue 9821: Cookies are still causing problems in SageNB (Safari)

archive/issues_009821.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  jason kcrisman mpatel boothby\n\nc.f. http://groups.google.com/group/sage-support/msg/2fd79e5ccfceb728 and http://groups.google.com/group/sage-support/msg/10a3d906b6a0e675\n\nIssue created by migration from https://trac.sagemath.org/ticket/9822\n\n",
    "created_at": "2010-08-27T15:29:01Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Cookies are still causing problems in SageNB (Safari)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9821",
    "user": "timdumol"
}
```
Assignee: jason, was

CC:  jason kcrisman mpatel boothby

c.f. http://groups.google.com/group/sage-support/msg/2fd79e5ccfceb728 and http://groups.google.com/group/sage-support/msg/10a3d906b6a0e675

Issue created by migration from https://trac.sagemath.org/ticket/9822





---

archive/issue_comments_096838.json:
```json
{
    "body": "Attachment [trac_9822-cookie-path-fix.patch](tarball://root/attachments/some-uuid/ticket9822/trac_9822-cookie-path-fix.patch) by timdumol created at 2010-08-27 15:30:01\n\nSageNB. Attempted fix for Safari (setting cookie path to '/')",
    "created_at": "2010-08-27T15:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96838",
    "user": "timdumol"
}
```

Attachment [trac_9822-cookie-path-fix.patch](tarball://root/attachments/some-uuid/ticket9822/trac_9822-cookie-path-fix.patch) by timdumol created at 2010-08-27 15:30:01

SageNB. Attempted fix for Safari (setting cookie path to '/')



---

archive/issue_comments_096839.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-27T15:32:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96839",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096840.json:
```json
{
    "body": "I have no Safari (on Linux), so it would be helpful if someone with Safari could test if this fixes the issue.",
    "created_at": "2010-08-27T15:32:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96840",
    "user": "timdumol"
}
```

I have no Safari (on Linux), so it would be helpful if someone with Safari could test if this fixes the issue.



---

archive/issue_comments_096841.json:
```json
{
    "body": "I'd like to test it, but have no way to apply it to a server where this is a problem for me :(",
    "created_at": "2010-08-27T17:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96841",
    "user": "kcrisman"
}
```

I'd like to test it, but have no way to apply it to a server where this is a problem for me :(



---

archive/issue_comments_096842.json:
```json
{
    "body": "I'll test it.  I had 3-4 students today who complained about the issue.",
    "created_at": "2010-08-27T18:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96842",
    "user": "jason"
}
```

I'll test it.  I had 3-4 students today who complained about the issue.



---

archive/issue_comments_096843.json:
```json
{
    "body": "Let me say again that it would be *really* nice if the sagenb repository was located somewhere in the sage repository, so that it was easy to apply patches and make fixes (without having to hunt down the spkg, read the instructions again, untar it, etc).  Maybe the sage spkg could by default do the equivalent of extracting in sage/devel/sagenb/ and doing the developer install (so the source and repository would be in sage/devel/sagenb/",
    "created_at": "2010-08-27T18:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96843",
    "user": "jason"
}
```

Let me say again that it would be *really* nice if the sagenb repository was located somewhere in the sage repository, so that it was easy to apply patches and make fixes (without having to hunt down the spkg, read the instructions again, untar it, etc).  Maybe the sage spkg could by default do the equivalent of extracting in sage/devel/sagenb/ and doing the developer install (so the source and repository would be in sage/devel/sagenb/



---

archive/issue_comments_096844.json:
```json
{
    "body": "Thanks for testing!  I hope to start using it a little on the side next week.\n> Let me say again that it would be *really* nice if the sagenb repository was located somewhere in the sage repository, so that it was easy to apply patches and make fixes (without having to hunt down the spkg, read the instructions again, untar it, etc).  Maybe the sage spkg could by default do the equivalent of extracting in sage/devel/sagenb/ and doing the developer install (so the source and repository would be in sage/devel/sagenb/\n\nI have asked about this a lot too, though of course I also haven't stepped up and tried to figure out how to use python setup or whatever to create `hg_sagenb` or something.  Same with Pynac - it's just dumb that these things which (currently) are only used in Sage can't be easily modified.",
    "created_at": "2010-08-28T00:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96844",
    "user": "kcrisman"
}
```

Thanks for testing!  I hope to start using it a little on the side next week.
> Let me say again that it would be *really* nice if the sagenb repository was located somewhere in the sage repository, so that it was easy to apply patches and make fixes (without having to hunt down the spkg, read the instructions again, untar it, etc).  Maybe the sage spkg could by default do the equivalent of extracting in sage/devel/sagenb/ and doing the developer install (so the source and repository would be in sage/devel/sagenb/

I have asked about this a lot too, though of course I also haven't stepped up and tried to figure out how to use python setup or whatever to create `hg_sagenb` or something.  Same with Pynac - it's just dumb that these things which (currently) are only used in Sage can't be easily modified.



---

archive/issue_comments_096845.json:
```json
{
    "body": "Jason Grout has [posted a fix on sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/dbe2e0a64e9ccc38).",
    "created_at": "2010-09-01T23:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96845",
    "user": "mpatel"
}
```

Jason Grout has [posted a fix on sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/dbe2e0a64e9ccc38).



---

archive/issue_comments_096846.json:
```json
{
    "body": "Replaces all others. Includes Jason Grout's fix ( http://groups.google.com/group/sage-notebook/browse_thread/thread/dbe2e0a64e9ccc38).",
    "created_at": "2010-09-10T04:19:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96846",
    "user": "timdumol"
}
```

Replaces all others. Includes Jason Grout's fix ( http://groups.google.com/group/sage-notebook/browse_thread/thread/dbe2e0a64e9ccc38).



---

archive/issue_comments_096847.json:
```json
{
    "body": "Attachment [trac_9822-cookie-fix.patch](tarball://root/attachments/some-uuid/ticket9822/trac_9822-cookie-fix.patch) by timdumol created at 2010-09-10 04:20:23",
    "created_at": "2010-09-10T04:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96847",
    "user": "timdumol"
}
```

Attachment [trac_9822-cookie-fix.patch](tarball://root/attachments/some-uuid/ticket9822/trac_9822-cookie-fix.patch) by timdumol created at 2010-09-10 04:20:23



---

archive/issue_comments_096848.json:
```json
{
    "body": "Setting the port for the cookie worries me.  How does that play with using a proxy server (where Sage thinks it is running on a certain port, like 8000, but the web browser thinks it is running on port 80)?",
    "created_at": "2010-09-10T04:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96848",
    "user": "jason"
}
```

Setting the port for the cookie worries me.  How does that play with using a proxy server (where Sage thinks it is running on a certain port, like 8000, but the web browser thinks it is running on port 80)?



---

archive/issue_comments_096849.json:
```json
{
    "body": "Gets the port number from the HTTP header instead (this fixes the issue given by Jason)",
    "created_at": "2010-09-10T04:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96849",
    "user": "timdumol"
}
```

Gets the port number from the HTTP header instead (this fixes the issue given by Jason)



---

archive/issue_comments_096850.json:
```json
{
    "body": "Attachment [trac_9822-cookie-fix.2.patch](tarball://root/attachments/some-uuid/ticket9822/trac_9822-cookie-fix.2.patch) by timdumol created at 2010-09-10 04:41:55\n\nReplying to [comment:8 jason]:\n> Setting the port for the cookie worries me.  How does that play with using a proxy server (where Sage thinks it is running on a certain port, like 8000, but the web browser thinks it is running on port 80)?\n\nGood point. I've added a new patch that fixes that issue.",
    "created_at": "2010-09-10T04:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96850",
    "user": "timdumol"
}
```

Attachment [trac_9822-cookie-fix.2.patch](tarball://root/attachments/some-uuid/ticket9822/trac_9822-cookie-fix.2.patch) by timdumol created at 2010-09-10 04:41:55

Replying to [comment:8 jason]:
> Setting the port for the cookie worries me.  How does that play with using a proxy server (where Sage thinks it is running on a certain port, like 8000, but the web browser thinks it is running on port 80)?

Good point. I've added a new patch that fixes that issue.



---

archive/issue_comments_096851.json:
```json
{
    "body": "What if the connection is over https?  Can you assume that if you don't see a port number, then the port number is 80?  Why can't we just not set the port number (like before)?  (Disclaimer: I don't know much about this, so if someone that does thinks everything is all right, well, okay).\n\nAlso, I notice you use hasHeader.  Should my part of the patch be changed to have:\n\n\n```\nif request.headers.hasHeader('cookie'):\n```\n",
    "created_at": "2010-09-10T06:29:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96851",
    "user": "jason"
}
```

What if the connection is over https?  Can you assume that if you don't see a port number, then the port number is 80?  Why can't we just not set the port number (like before)?  (Disclaimer: I don't know much about this, so if someone that does thinks everything is all right, well, okay).

Also, I notice you use hasHeader.  Should my part of the patch be changed to have:


```
if request.headers.hasHeader('cookie'):
```




---

archive/issue_comments_096852.json:
```json
{
    "body": "Attachment [trac_9822-cookie-fix.3.patch](tarball://root/attachments/some-uuid/ticket9822/trac_9822-cookie-fix.3.patch) by timdumol created at 2010-09-10 10:49:53\n\nMakes the default port 443 if the connection is HTTPS.",
    "created_at": "2010-09-10T10:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96852",
    "user": "timdumol"
}
```

Attachment [trac_9822-cookie-fix.3.patch](tarball://root/attachments/some-uuid/ticket9822/trac_9822-cookie-fix.3.patch) by timdumol created at 2010-09-10 10:49:53

Makes the default port 443 if the connection is HTTPS.



---

archive/issue_comments_096853.json:
```json
{
    "body": "It is insecure to let any site under the domain to access the cookie (cross-site scripting). I've made the port 443 if the notebook is secure. It also poses a problem if (in the admittedly rare case) the user decides to forward several ports to one notebook server.\n\n`getHeader()` returns None if the header is not found, so it works either way.",
    "created_at": "2010-09-10T10:56:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96853",
    "user": "timdumol"
}
```

It is insecure to let any site under the domain to access the cookie (cross-site scripting). I've made the port 443 if the notebook is secure. It also poses a problem if (in the admittedly rare case) the user decides to forward several ports to one notebook server.

`getHeader()` returns None if the header is not found, so it works either way.



---

archive/issue_comments_096854.json:
```json
{
    "body": "Attachment [trac_9822-cookie-fix.4.patch](tarball://root/attachments/some-uuid/ticket9822/trac_9822-cookie-fix.4.patch) by timdumol created at 2010-09-16 17:00:53\n\nFixes a bug.",
    "created_at": "2010-09-16T17:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96854",
    "user": "timdumol"
}
```

Attachment [trac_9822-cookie-fix.4.patch](tarball://root/attachments/some-uuid/ticket9822/trac_9822-cookie-fix.4.patch) by timdumol created at 2010-09-16 17:00:53

Fixes a bug.



---

archive/issue_comments_096855.json:
```json
{
    "body": "Bug fixed in latest patch.",
    "created_at": "2010-09-16T17:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96855",
    "user": "timdumol"
}
```

Bug fixed in latest patch.



---

archive/issue_comments_096856.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-09-28T20:44:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96856",
    "user": "jason"
}
```

Changing priority from major to critical.



---

archive/issue_comments_096857.json:
```json
{
    "body": "The cookie issue preventing logins makes this critical, I think.  I'm confident about that part of this patch.  I'm not confident about the other stuff done on cookies in this patch (just because I'm not familiar with them very much anymore).\n\nMitesh or Tom: you are some of the resident web experts.  Can you look at this patch?",
    "created_at": "2010-09-28T20:44:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96857",
    "user": "jason"
}
```

The cookie issue preventing logins makes this critical, I think.  I'm confident about that part of this patch.  I'm not confident about the other stuff done on cookies in this patch (just because I'm not familiar with them very much anymore).

Mitesh or Tom: you are some of the resident web experts.  Can you look at this patch?



---

archive/issue_comments_096858.json:
```json
{
    "body": "I installed this on my server (4.5.2) where I have apache forwarding port 80 (outside) to port 8000 (the local sage server).  On logging in, I get a browser message: \"Please enable cookies or delete all Sage cookies and localhost cookies in your browser and try again.\"  In Firebug, I see I have two cookies: cookie_test_80, and nb_session_8000.  That looks wrong, doesn't it?\n\nWhen I delete all of my cookies from that server, I still can't log in (same error).  After the error page comes up, and I click \"Continue\", I see the cookie_test_80 cookie show up in FireCookies.\n\nCan we split this ticket into two tickets?  A very high priority one that fixes the bug I found (my fix has been working for the past couple of months for me), and another ticket which takes care of the other issues?  That way the checking-only-last-cookie error can be taken care of right away.",
    "created_at": "2010-09-28T22:42:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96858",
    "user": "jason"
}
```

I installed this on my server (4.5.2) where I have apache forwarding port 80 (outside) to port 8000 (the local sage server).  On logging in, I get a browser message: "Please enable cookies or delete all Sage cookies and localhost cookies in your browser and try again."  In Firebug, I see I have two cookies: cookie_test_80, and nb_session_8000.  That looks wrong, doesn't it?

When I delete all of my cookies from that server, I still can't log in (same error).  After the error page comes up, and I click "Continue", I see the cookie_test_80 cookie show up in FireCookies.

Can we split this ticket into two tickets?  A very high priority one that fixes the bug I found (my fix has been working for the past couple of months for me), and another ticket which takes care of the other issues?  That way the checking-only-last-cookie error can be taken care of right away.



---

archive/issue_comments_096859.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-28T22:42:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96859",
    "user": "jason"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_096860.json:
```json
{
    "body": "With just my part of the patch, I see a cookie_test_8000 and a nb_session_8000 cookie.  So apparently the problem is that after the patch above, we have a cookie_test_80 cookie.",
    "created_at": "2010-09-28T22:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96860",
    "user": "jason"
}
```

With just my part of the patch, I see a cookie_test_8000 and a nb_session_8000 cookie.  So apparently the problem is that after the patch above, we have a cookie_test_80 cookie.



---

archive/issue_comments_096861.json:
```json
{
    "body": "> Can we split this ticket into two tickets?  A very high priority one that fixes the bug I found (my fix has been working for the past couple of months for me), and another ticket which takes care of the other issues?  That way the checking-only-last-cookie error can be taken care of right away.\n\nYes, please!  I've been avoiding using Sage this semester (other than for me personally) some because the cookie issue just seems to have gotten worse...",
    "created_at": "2010-09-29T00:35:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96861",
    "user": "kcrisman"
}
```

> Can we split this ticket into two tickets?  A very high priority one that fixes the bug I found (my fix has been working for the past couple of months for me), and another ticket which takes care of the other issues?  That way the checking-only-last-cookie error can be taken care of right away.

Yes, please!  I've been avoiding using Sage this semester (other than for me personally) some because the cookie issue just seems to have gotten worse...



---

archive/issue_comments_096862.json:
```json
{
    "body": "I've split Tim's changes to cookies out to #10029, since they don't seem to be quite ready yet.",
    "created_at": "2010-09-29T01:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96862",
    "user": "jason"
}
```

I've split Tim's changes to cookies out to #10029, since they don't seem to be quite ready yet.



---

archive/issue_comments_096863.json:
```json
{
    "body": "Attachment [9822-multiple-cookies.patch](tarball://root/attachments/some-uuid/ticket9822/9822-multiple-cookies.patch) by jason created at 2010-09-29 01:06:00\n\napply instead of previous patches",
    "created_at": "2010-09-29T01:06:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96863",
    "user": "jason"
}
```

Attachment [9822-multiple-cookies.patch](tarball://root/attachments/some-uuid/ticket9822/9822-multiple-cookies.patch) by jason created at 2010-09-29 01:06:00

apply instead of previous patches



---

archive/issue_comments_096864.json:
```json
{
    "body": "Apply only 9822-multiple-cookies.patch.  The rest of the work on this ticket has been moved to #10029.",
    "created_at": "2010-09-29T01:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96864",
    "user": "jason"
}
```

Apply only 9822-multiple-cookies.patch.  The rest of the work on this ticket has been moved to #10029.



---

archive/issue_comments_096865.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-29T01:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96865",
    "user": "jason"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_096866.json:
```json
{
    "body": "I think we should get this and the currently positively reviewed SageNB tickets at {32} into a new SageNB 0.8.3.\n\nBut I can't work on this now, as I'm a bit busy with getting 4.6.alpha2 ready to release and working on #3524.  That will put the 4.6 cycle in feature freeze, so it's likely that the new Cython, NumPy, Pynac, SageNB, and SciPy packages will have to wait for 4.6.1.",
    "created_at": "2010-09-29T11:09:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96866",
    "user": "mpatel"
}
```

I think we should get this and the currently positively reviewed SageNB tickets at {32} into a new SageNB 0.8.3.

But I can't work on this now, as I'm a bit busy with getting 4.6.alpha2 ready to release and working on #3524.  That will put the 4.6 cycle in feature freeze, so it's likely that the new Cython, NumPy, Pynac, SageNB, and SciPy packages will have to wait for 4.6.1.



---

archive/issue_comments_096867.json:
```json
{
    "body": "> But I can't work on this now, as I'm a bit busy with getting 4.6.alpha2 ready to release and working on #3524.  That will put the 4.6 cycle in feature freeze, so it's likely that the new Cython, NumPy, Pynac, SageNB, and SciPy packages will have to wait for 4.6.1.\n\nNot to reopen the whole numbering issue, but it seems weird that major upgrades to big pieces of Sage would be 4.6.1 - and possibly wait weeks.  Is it possible to keep the 4.6 cycle going, or would it make more sense to wait on all these?  I realize you're doing the work - just a query.  (Partly this is the fear that 4.6.1 might not happen for a while, since I expect you to take a break after this release! You certainly deserve it.)",
    "created_at": "2010-09-29T12:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96867",
    "user": "kcrisman"
}
```

> But I can't work on this now, as I'm a bit busy with getting 4.6.alpha2 ready to release and working on #3524.  That will put the 4.6 cycle in feature freeze, so it's likely that the new Cython, NumPy, Pynac, SageNB, and SciPy packages will have to wait for 4.6.1.

Not to reopen the whole numbering issue, but it seems weird that major upgrades to big pieces of Sage would be 4.6.1 - and possibly wait weeks.  Is it possible to keep the 4.6 cycle going, or would it make more sense to wait on all these?  I realize you're doing the work - just a query.  (Partly this is the fear that 4.6.1 might not happen for a while, since I expect you to take a break after this release! You certainly deserve it.)



---

archive/issue_comments_096868.json:
```json
{
    "body": "Replying to [comment:21 mpatel]:\n> I think we should get this and the currently positively reviewed SageNB tickets at {32} into a new SageNB 0.8.3.\n\nI've opened #10036 for this.",
    "created_at": "2010-09-29T21:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96868",
    "user": "mpatel"
}
```

Replying to [comment:21 mpatel]:
> I think we should get this and the currently positively reviewed SageNB tickets at {32} into a new SageNB 0.8.3.

I've opened #10036 for this.



---

archive/issue_comments_096869.json:
```json
{
    "body": "Replying to [comment:22 kcrisman]:\n> > But I can't work on this now, as I'm a bit busy with getting 4.6.alpha2 ready to release and working on #3524.  That will put the 4.6 cycle in feature freeze, so it's likely that the new Cython, NumPy, Pynac, SageNB, and SciPy packages will have to wait for 4.6.1.\n> \n> Not to reopen the whole numbering issue, but it seems weird that major upgrades to big pieces of Sage would be 4.6.1 - and possibly wait weeks.  Is it possible to keep the 4.6 cycle going, or would it make more sense to wait on all these?  I realize you're doing the work - just a query.  (Partly this is the fear that 4.6.1 might not happen for a while, since I expect you to take a break after this release! You certainly deserve it.)\n\nThanks!  I may well take a break after 4.6 is out.\n\nI'll try to reply soon on sage-devel about the possibility of waiting longer for 4.6.alpha2 or adding an alpha3.\n\nRight now, I need to investigate a potential problem with current trial alpha2.  The current merge script is [here](http://sage.math.washington.edu/home/release/sage-4.6.alpha2/merger-4.6.alpha2).",
    "created_at": "2010-09-29T21:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96869",
    "user": "mpatel"
}
```

Replying to [comment:22 kcrisman]:
> > But I can't work on this now, as I'm a bit busy with getting 4.6.alpha2 ready to release and working on #3524.  That will put the 4.6 cycle in feature freeze, so it's likely that the new Cython, NumPy, Pynac, SageNB, and SciPy packages will have to wait for 4.6.1.
> 
> Not to reopen the whole numbering issue, but it seems weird that major upgrades to big pieces of Sage would be 4.6.1 - and possibly wait weeks.  Is it possible to keep the 4.6 cycle going, or would it make more sense to wait on all these?  I realize you're doing the work - just a query.  (Partly this is the fear that 4.6.1 might not happen for a while, since I expect you to take a break after this release! You certainly deserve it.)

Thanks!  I may well take a break after 4.6 is out.

I'll try to reply soon on sage-devel about the possibility of waiting longer for 4.6.alpha2 or adding an alpha3.

Right now, I need to investigate a potential problem with current trial alpha2.  The current merge script is [here](http://sage.math.washington.edu/home/release/sage-4.6.alpha2/merger-4.6.alpha2).



---

archive/issue_comments_096870.json:
```json
{
    "body": "Replying to [comment:18 jason]:\n> Apply only 9822-multiple-cookies.patch.  The rest of the work on this ticket has been moved to #10029.\n\nTim, does this patch look good to you?",
    "created_at": "2010-10-03T09:42:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96870",
    "user": "mpatel"
}
```

Replying to [comment:18 jason]:
> Apply only 9822-multiple-cookies.patch.  The rest of the work on this ticket has been moved to #10029.

Tim, does this patch look good to you?



---

archive/issue_comments_096871.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-03T09:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96871",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096872.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-10-03T09:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96872",
    "user": "timdumol"
}
```

Looks good to me.



---

archive/issue_comments_096873.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-04T01:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9821#issuecomment-96873",
    "user": "mpatel"
}
```

Resolution: fixed
