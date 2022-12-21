# Issue 9837: Bugfix in WeylCharacterRing __call__ method

Issue created by migration from Trac.

Original creator: bump

Original creation time: 2010-08-29 19:03:03

Assignee: AlexGhitza

CC:  sage-combinat

This addresses a bug that was reported here:

http://groups.google.com/group/sage-combinat-devel/msg/252fd7fa0e297214

The `__call__` method of a Weyl Character ring, when `style="coroots"` is specified, tries to interpret the arguments as the coroots of a weight; that weight
is then the actual argument. However this is not appropriate if the argument is
not a tuple. Therefore this should be tested.

The patch implements the test.


---

Comment by bump created at 2010-08-29 19:08:17

Changing assignee from AlexGhitza to bump.


---

Comment by bump created at 2010-08-29 19:08:34

Changing status from new to needs_review.


---

Comment by bump created at 2010-08-29 19:10:16

Changing component from algebra to group_theory.


---

Comment by aschilling created at 2010-10-19 06:31:31

Replying to [comment:3 bump]:

This is a bug fix. All tests pass!


---

Comment by aschilling created at 2010-10-19 06:31:31

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-10-26 13:34:43

Please change the commit message of the patch trac_9838.patch (use `hg qrefresh -e` for that).


---

Comment by jdemeyer created at 2010-10-26 13:34:43

Changing status from positive_review to needs_work.


---

Comment by bump created at 2010-10-26 15:19:11

> Please change the commit message of the patch trac_9838.patch (use hg qrefresh -e for that).

Done. -Dan


---

Comment by bump created at 2010-10-26 15:19:11

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2010-10-27 08:52:20

Replying to [comment:7 bump]:
> Done. -Dan

Sorry, the ticket number should also be in the first line of the commit message.


---

Comment by jdemeyer created at 2010-10-27 08:52:20

Changing status from positive_review to needs_work.


---

Attachment

#9838: bugfix in WeylCharac terRing call method


---

Comment by bump created at 2010-10-27 16:26:11

Changing status from needs_work to positive_review.


---

Comment by bump created at 2010-10-27 16:26:11

> Sorry, the ticket number should also be in the first line of the commit message. 

Done.


---

Comment by jdemeyer created at 2010-11-01 10:11:20

Resolution: fixed


---

Comment by jdemeyer created at 2010-11-02 15:34:34

Changing status from closed to needs_work.


---

Comment by jdemeyer created at 2010-11-02 15:35:17

Due to a mistake by me (confusing #9838 with #9893), this ticket did not get merged in sage-4.6.1.alpha0.


---

Comment by jdemeyer created at 2010-11-02 15:35:17

Changing status from needs_work to positive_review.


---

Comment by bump created at 2010-11-02 23:36:18

The ticket is still described as resolved:fixed.

I don't think I can revert the fixed status: trac admin has to do that.
(It doesn't matter if this won't cause the release manager to
forget the patch.)


---

Comment by mvngu created at 2010-11-04 11:43:42

Changing status from closed to new.


---

Comment by mvngu created at 2010-11-04 11:43:42

Resolution changed from fixed to 


---

Comment by mvngu created at 2010-11-04 11:43:57

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-11-04 11:44:04

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-11-04 11:45:07

Replying to [comment:13 bump]:
> I don't think I can revert the fixed status: trac admin has to do that.

Done.


---

Comment by jdemeyer created at 2010-11-10 22:20:13

Resolution: fixed
