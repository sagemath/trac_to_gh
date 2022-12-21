# Issue 9918: Wrap wraps-decorator working around bug when used with non-function callables

Issue created by migration from Trac.

Original creator: jsrn

Original creation time: 2010-09-16 14:07:12

Assignee: jason

Keywords: decorators

The `@`wraps decorator from the Python standard library does not work for non-function callables (e.g. methods) in Python versions older than 3.2. It was fixed as Python bug issue 3445. Until Sage upgrades to such a new version of Python, we should have a small work-around.


---

Comment by jsrn created at 2010-09-23 12:03:10

Changing status from new to needs_review.


---

Comment by jason created at 2010-09-23 12:49:28

I hope I'm not being too picky here, but could also note in the source that this was fixed in Python 3.2 and the Python bug number?  That way, when I'm reading the source (much more often than this ticket!), it's easy to determine when we can remove the work around?

This might be easier to change over on #9089, which I plan to review in conjunction with this ticket.


---

Comment by jsrn created at 2010-09-24 06:52:29

No problem. I have fixed #9907 (which was probably the one you meant) to include such a reference.


---

Comment by rlm created at 2010-11-09 20:21:00

If I apply #6094, #9907, #9919, and #10107 together on top of sage-4.6, all long tests pass. The code looks good.


---

Comment by rlm created at 2010-11-09 20:21:00

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-10 18:59:26

Please change the commit message to include the ticket number (use `hg qrefresh -e` for that)


---

Comment by jdemeyer created at 2010-11-10 18:59:26

Changing status from positive_review to needs_work.


---

Attachment

Fixed the commit message. Changed back to positive review as the code hasn't changed since Robert Miller's review.


---

Comment by jsrn created at 2010-11-11 12:56:58

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2010-11-11 19:37:29

Resolution: fixed
