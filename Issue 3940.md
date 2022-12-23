# Issue 3940: Add a warnings framework to Sage

Issue created by migration from https://trac.sagemath.org/ticket/3940

Original creator: jason

Original creation time: 2008-08-24 00:09:30

Assignee: cwitty

The builtin python warnings framework allows filtering on subclasses of warnings.  This would be useful to make a sage warnings framework, with different types of sage-specific warnings.

Here, I've added a directory and a basic file with a NumericalPrecisionWarning class that could be triggered, for example, in the eigenvalue computations.


---

Attachment

Jason,

now that #3873 has been merged can you check how much of this patch is still useful/applies?

Cheers,

Michael


---

Comment by jason created at 2008-08-25 14:29:57

Changing type from defect to enhancement.


---

Comment by jason created at 2008-08-25 14:29:57

It is useful and it still applies; the application is still sitting in my queue, though.

Basically, there are some situations where computing eigenvalues/vectors should throw a warning.  Also, the plotting code should throw a warning when some situations come up (when the function can't be evaluated at certain points).  The point of this patch is that: 

1. It makes it so that sage-related warnings are always shown by default.

2. It makes it very easy to do something with all sage-related warnings (e.g., throw exceptions or ignore them and don't print them out, etc.)

If you want to wait until I post a patch that uses this, that's fine.


---

Comment by jason created at 2008-08-25 14:30:38

BTW, one question I had was whether to make a warnings directory or to just put this under the misc directory.


---

Comment by cwitty created at 2008-08-25 15:46:43

IMHO if the warnings framework is expected to stay as one file, then it should be in the misc directory; if you expect the warnings framework to expand to multiple files then maybe a new directory would be more appropriate.


---

Comment by mabshoff created at 2009-04-16 21:48:31

What is the status here? Not having a proper summary subject makes files fall through the cracks. 

Either this code is useful in which case it should be applied or not. It seems that cwitty's has some pointers, so what's going on here? :)

Cheers,

Michael


---

Comment by jason created at 2009-04-16 22:30:26

I agree with cwitty:

Work that needs to be done on this patch to get it ready for review:

 * Make it one file in the misc directory

If warnings become a more important part of Sage, then later we can break things into a different directory.


---

Attachment


---

Comment by mraum created at 2010-01-18 21:55:15

I uploaded sagewarnings.py which derives from Jason's patch.
This extension addresses the lack of use cases by providing some warning classes adapted to particular things I've got in mind. This file is for discussion; See the thread on sage-devel.

I renamed the file warning.py to sagewarnings.py. This seems more consistent with python's warnings module to me.


---

Comment by mkoeppe created at 2021-08-26 03:45:59

outdated, should close


---

Comment by mkoeppe created at 2021-08-26 03:45:59

Changing status from needs_work to needs_review.


---

Comment by mjo created at 2021-10-04 22:56:34

Changing status from needs_review to positive_review.


---

Comment by mjo created at 2021-10-04 22:56:34

I think the motivation behind this is still valid. But to proceed today, we'd have to look through `git grep 'warn('` and come up with a set of warnings that map nicely to the existing uses in the tree. (And the names themselves are just asking for a bikeshed thread on sage-devel.) The patches on the ticket are far out-of-date in that respect.

That said, I could sit down for five minutes and easily come up with a hundred "wishlist" items that would be nice to have and that would involve a lot of work that no one is willing to do. So I think after so many years, the small benefit of closing a "dead" ticket outweighs whatever we'd gain from keeping this on the wishlist.


---

Comment by mkoeppe created at 2021-10-04 23:44:13

Resolution: invalid
