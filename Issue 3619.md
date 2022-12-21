# Issue 3619: notebook -- record date & time each user logs in

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-07-08 23:33:58

Assignee: boothby




---

Comment by TimothyClemans created at 2008-07-08 23:34:06

Changing assignee from boothby to TimothyClemans.


---

Comment by TimothyClemans created at 2008-07-08 23:34:06

Changing status from new to assigned.


---

Comment by TimothyClemans created at 2008-07-10 13:58:25

I couldn't seem to figure out how to get AdminToplevel to be the toplevel for admins.


---

Comment by ncalexan created at 2008-08-10 23:24:15

I don't understand what the final comment, about AdminToplevel, is about.

I worry that we will hang on to thousands of login times with this, which could be memory/disk intensive.  Could we agree on the last fifty login times, or the first time ever and then the next 100 or something similar?

Also, there is no way to view this information.  Why are we keeping it?


---

Comment by TimothyClemans created at 2008-08-11 04:37:49

Replying to [comment:3 ncalexan]:
> I don't understand what the final comment, about AdminToplevel, is about.

Somehow the user account type for the user admin was getting changed to 'user'. This is no longer a problem because a patch was merged which has account_type returning 'admin' for user admin no matter what.

> I worry that we will hang on to thousands of login times with this, which could be memory/disk intensive.  Could we agree on the last fifty login times, or the first time ever and then the next 100 or something similar?
> 

We could, but I am very interested in being able to look up all login times for a given user. 

> Also, there is no way to view this information.  Why are we keeping it?

There will be. I just didn't do it because at the time I couldn't figure out the AdminToplevel problem.

I'll get back to this ticket after thinking more about it. Thanks for reviewing.


---

Comment by TimothyClemans created at 2008-08-12 21:37:41

How I test this:

(1) I login and then go to sage.math.washington.edu:8999/users # Table of users with two links next to each of them if login recording is on. 

(2) I click on "Access" in third column to see login times. The page should be blank if no login times have been recorded.

Login recording is turned off by default. In order to turn it on I do:

```
*** WARNING: Notebook must not be running! ***

sage: nb = load('.sage/sage_notebook/nb.sobj', compress=False)
sage: nb.conf()['record_logins'] = True
sage: nb.save(filename='/home/tclemans/.sage/sage_notebook/nb.sobj')
```



---

Comment by TimothyClemans created at 2008-08-13 02:22:06

Depends on #3776


---

Attachment


---

Attachment

new patch against sagenb that simply adds calls to log.msg in a few places, which will properly log user login attempts using the standard twisted loging facility


---

Comment by was created at 2009-11-19 22:44:03

I've attached a new patch against sagenb that simply adds calls to log.msg in a few places, which will properly log user login attempts using the standard twisted loging facility.  I also deleted some cruft from guard.py that wasn't used.


---

Comment by was created at 2009-11-19 22:44:03

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2009-12-06 11:51:00

Applied and the patch works perfectly. I wonder though whether a configuration setting should be added?


---

Comment by timdumol created at 2009-12-06 11:51:00

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-07 17:36:33

> Applied and the patch works perfectly. I wonder though whether a 
> configuration setting should be added? 

Yes, definitely.  However, I don't think that has to be done in this patch.  Little steps are best.


---

Comment by was created at 2009-12-07 17:38:02

Resolution: fixed
