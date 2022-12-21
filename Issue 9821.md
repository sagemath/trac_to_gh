# Issue 9821: Cookies are still causing problems in SageNB (Safari)

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2010-08-27 15:29:01

Assignee: jason, was

CC:  jason kcrisman mpatel boothby

c.f. http://groups.google.com/group/sage-support/msg/2fd79e5ccfceb728 and http://groups.google.com/group/sage-support/msg/10a3d906b6a0e675


---

Attachment

SageNB. Attempted fix for Safari (setting cookie path to '/')


---

Comment by timdumol created at 2010-08-27 15:32:38

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-08-27 15:32:38

I have no Safari (on Linux), so it would be helpful if someone with Safari could test if this fixes the issue.


---

Comment by kcrisman created at 2010-08-27 17:41:41

I'd like to test it, but have no way to apply it to a server where this is a problem for me :(


---

Comment by jason created at 2010-08-27 18:09:15

I'll test it.  I had 3-4 students today who complained about the issue.


---

Comment by jason created at 2010-08-27 18:17:20

Let me say again that it would be *really* nice if the sagenb repository was located somewhere in the sage repository, so that it was easy to apply patches and make fixes (without having to hunt down the spkg, read the instructions again, untar it, etc).  Maybe the sage spkg could by default do the equivalent of extracting in sage/devel/sagenb/ and doing the developer install (so the source and repository would be in sage/devel/sagenb/


---

Comment by kcrisman created at 2010-08-28 00:46:58

Thanks for testing!  I hope to start using it a little on the side next week.
> Let me say again that it would be *really* nice if the sagenb repository was located somewhere in the sage repository, so that it was easy to apply patches and make fixes (without having to hunt down the spkg, read the instructions again, untar it, etc).  Maybe the sage spkg could by default do the equivalent of extracting in sage/devel/sagenb/ and doing the developer install (so the source and repository would be in sage/devel/sagenb/

I have asked about this a lot too, though of course I also haven't stepped up and tried to figure out how to use python setup or whatever to create `hg_sagenb` or something.  Same with Pynac - it's just dumb that these things which (currently) are only used in Sage can't be easily modified.


---

Comment by mpatel created at 2010-09-01 23:07:11

Jason Grout has [posted a fix on sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/dbe2e0a64e9ccc38).


---

Comment by timdumol created at 2010-09-10 04:19:34

Replaces all others. Includes Jason Grout's fix ( http://groups.google.com/group/sage-notebook/browse_thread/thread/dbe2e0a64e9ccc38).


---

Attachment


---

Comment by jason created at 2010-09-10 04:30:19

Setting the port for the cookie worries me.  How does that play with using a proxy server (where Sage thinks it is running on a certain port, like 8000, but the web browser thinks it is running on port 80)?


---

Comment by timdumol created at 2010-09-10 04:41:29

Gets the port number from the HTTP header instead (this fixes the issue given by Jason)


---

Attachment

Replying to [comment:8 jason]:
> Setting the port for the cookie worries me.  How does that play with using a proxy server (where Sage thinks it is running on a certain port, like 8000, but the web browser thinks it is running on port 80)?

Good point. I've added a new patch that fixes that issue.


---

Comment by jason created at 2010-09-10 06:29:26

What if the connection is over https?  Can you assume that if you don't see a port number, then the port number is 80?  Why can't we just not set the port number (like before)?  (Disclaimer: I don't know much about this, so if someone that does thinks everything is all right, well, okay).

Also, I notice you use hasHeader.  Should my part of the patch be changed to have:


```
if request.headers.hasHeader('cookie'):
```



---

Attachment

Makes the default port 443 if the connection is HTTPS.


---

Comment by timdumol created at 2010-09-10 10:56:22

It is insecure to let any site under the domain to access the cookie (cross-site scripting). I've made the port 443 if the notebook is secure. It also poses a problem if (in the admittedly rare case) the user decides to forward several ports to one notebook server.

`getHeader()` returns None if the header is not found, so it works either way.


---

Attachment

Fixes a bug.


---

Comment by timdumol created at 2010-09-16 17:01:20

Bug fixed in latest patch.


---

Comment by jason created at 2010-09-28 20:44:09

Changing priority from major to critical.


---

Comment by jason created at 2010-09-28 20:44:09

The cookie issue preventing logins makes this critical, I think.  I'm confident about that part of this patch.  I'm not confident about the other stuff done on cookies in this patch (just because I'm not familiar with them very much anymore).

Mitesh or Tom: you are some of the resident web experts.  Can you look at this patch?


---

Comment by jason created at 2010-09-28 22:42:28

I installed this on my server (4.5.2) where I have apache forwarding port 80 (outside) to port 8000 (the local sage server).  On logging in, I get a browser message: "Please enable cookies or delete all Sage cookies and localhost cookies in your browser and try again."  In Firebug, I see I have two cookies: cookie_test_80, and nb_session_8000.  That looks wrong, doesn't it?

When I delete all of my cookies from that server, I still can't log in (same error).  After the error page comes up, and I click "Continue", I see the cookie_test_80 cookie show up in FireCookies.

Can we split this ticket into two tickets?  A very high priority one that fixes the bug I found (my fix has been working for the past couple of months for me), and another ticket which takes care of the other issues?  That way the checking-only-last-cookie error can be taken care of right away.


---

Comment by jason created at 2010-09-28 22:42:28

Changing status from needs_review to needs_work.


---

Comment by jason created at 2010-09-28 22:48:31

With just my part of the patch, I see a cookie_test_8000 and a nb_session_8000 cookie.  So apparently the problem is that after the patch above, we have a cookie_test_80 cookie.


---

Comment by kcrisman created at 2010-09-29 00:35:18

> Can we split this ticket into two tickets?  A very high priority one that fixes the bug I found (my fix has been working for the past couple of months for me), and another ticket which takes care of the other issues?  That way the checking-only-last-cookie error can be taken care of right away.

Yes, please!  I've been avoiding using Sage this semester (other than for me personally) some because the cookie issue just seems to have gotten worse...


---

Comment by jason created at 2010-09-29 01:01:01

I've split Tim's changes to cookies out to #10029, since they don't seem to be quite ready yet.


---

Attachment

apply instead of previous patches


---

Comment by jason created at 2010-09-29 01:06:53

Apply only 9822-multiple-cookies.patch.  The rest of the work on this ticket has been moved to #10029.


---

Comment by jason created at 2010-09-29 01:06:53

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-09-29 11:09:21

I think we should get this and the currently positively reviewed SageNB tickets at {32} into a new SageNB 0.8.3.

But I can't work on this now, as I'm a bit busy with getting 4.6.alpha2 ready to release and working on #3524.  That will put the 4.6 cycle in feature freeze, so it's likely that the new Cython, NumPy, Pynac, SageNB, and SciPy packages will have to wait for 4.6.1.


---

Comment by kcrisman created at 2010-09-29 12:21:18

> But I can't work on this now, as I'm a bit busy with getting 4.6.alpha2 ready to release and working on #3524.  That will put the 4.6 cycle in feature freeze, so it's likely that the new Cython, NumPy, Pynac, SageNB, and SciPy packages will have to wait for 4.6.1.

Not to reopen the whole numbering issue, but it seems weird that major upgrades to big pieces of Sage would be 4.6.1 - and possibly wait weeks.  Is it possible to keep the 4.6 cycle going, or would it make more sense to wait on all these?  I realize you're doing the work - just a query.  (Partly this is the fear that 4.6.1 might not happen for a while, since I expect you to take a break after this release! You certainly deserve it.)


---

Comment by mpatel created at 2010-09-29 21:23:19

Replying to [comment:21 mpatel]:
> I think we should get this and the currently positively reviewed SageNB tickets at {32} into a new SageNB 0.8.3.

I've opened #10036 for this.


---

Comment by mpatel created at 2010-09-29 21:41:29

Replying to [comment:22 kcrisman]:
> > But I can't work on this now, as I'm a bit busy with getting 4.6.alpha2 ready to release and working on #3524.  That will put the 4.6 cycle in feature freeze, so it's likely that the new Cython, NumPy, Pynac, SageNB, and SciPy packages will have to wait for 4.6.1.
> 
> Not to reopen the whole numbering issue, but it seems weird that major upgrades to big pieces of Sage would be 4.6.1 - and possibly wait weeks.  Is it possible to keep the 4.6 cycle going, or would it make more sense to wait on all these?  I realize you're doing the work - just a query.  (Partly this is the fear that 4.6.1 might not happen for a while, since I expect you to take a break after this release! You certainly deserve it.)

Thanks!  I may well take a break after 4.6 is out.

I'll try to reply soon on sage-devel about the possibility of waiting longer for 4.6.alpha2 or adding an alpha3.

Right now, I need to investigate a potential problem with current trial alpha2.  The current merge script is [here](http://sage.math.washington.edu/home/release/sage-4.6.alpha2/merger-4.6.alpha2).


---

Comment by mpatel created at 2010-10-03 09:42:31

Replying to [comment:18 jason]:
> Apply only 9822-multiple-cookies.patch.  The rest of the work on this ticket has been moved to #10029.

Tim, does this patch look good to you?


---

Comment by timdumol created at 2010-10-03 09:45:14

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-10-03 09:45:14

Looks good to me.


---

Comment by mpatel created at 2010-10-04 01:34:54

Resolution: fixed
