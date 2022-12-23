# Issue 6709: There are many doctest failues on Solaris.

Issue created by migration from https://trac.sagemath.org/ticket/6709

Original creator: drkirkby

Original creation time: 2009-08-09 10:24:07

Assignee: tbd

CC:  david.kirkby@onetel.net dimpase

I'll post a couple of logs later, but thought I'd create a ticket for this. 


---

Comment by drkirkby created at 2009-08-09 18:43:38

Test failues on sage-4.1.1.rc0 with Maxima 5.19.0


---

Attachment

test.log on SPARC after bug fix to ECL 9.8.1


---

Comment by drkirkby created at 2009-08-11 10:01:41

After adding the bug fix to sysfun.lsp which was added by one of ECL developers on the 10th August 2009, here is the output on a SPARC box running Solaris 10 update 7.


---

Comment by drkirkby created at 2011-04-02 12:35:58

I added "32-bit" to the title, as this ticket was created when Sage was only building 64-bit. 

It can be closed as fixed, as all doctests have passed on Solaris or OpenSolaris both SPARC and x86 for a long time.


---

Comment by drkirkby created at 2011-04-02 12:35:58

Changing assignee from tbd to drkirkby.


---

Comment by drkirkby created at 2011-04-02 12:37:16

Replying to [comment:3 drkirkby]:
> I added "32-bit" to the title, as this ticket was created when Sage was only building 64-bit. 

I mean the ticket was opened when Sage was only building 32-bit. Now it will build 64-bit, but does not work very well in 64-bit mode.


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by mjo created at 2020-07-12 19:57:20

Changing status from needs_review to positive_review.


---

Comment by mjo created at 2020-07-12 19:57:20

The goal of these tickets is laudable, but:

* We need at least one user who is able to test.
* The package/OS information on this ticket is outdated beyond usefulness.
* Upstream is a better place to report portability issues these days.


---

Comment by chapoton created at 2020-07-15 07:18:41

Resolution: invalid


---

Comment by chapoton created at 2020-07-15 07:18:41

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.
