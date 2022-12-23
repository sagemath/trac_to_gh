# Issue 9200: Add left and right directions to limits

Issue created by migration from https://trac.sagemath.org/ticket/9200

Original creator: DanaErnst

Original creation time: 2010-06-10 02:26:53

Assignee: burcin

CC:  jason rbeezer

1. Add `from_left` and `from_right` for `dir` keyword.

2. Improve error message `dir` keyword.

3. Add doctests and tests.


---

Attachment


---

Comment by DanaErnst created at 2010-06-10 02:53:02

Patch passes tests in `sage/calculus`.  Need to test full Sage library.


---

Comment by DanaErnst created at 2010-07-22 19:40:22

stand alone patch


---

Attachment

Rebased for version 4.5.1, apply only v2 patch.


---

Comment by DanaErnst created at 2010-07-23 12:54:51

Changing status from new to needs_review.


---

Comment by DanaErnst created at 2010-07-23 12:54:51

* All tests passed on version 4.5.1 (running OSX 10.6)
 * HTML & PDF reference built without problem


---

Comment by rbeezer created at 2010-07-24 00:13:07

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2010-07-24 00:13:07

Applies, builds, passes all tests, and docs look fine; on 4.5.2.alpha0.  So this is a positive review.

Nice job on your first contribution!


---

Comment by burcin created at 2010-07-24 21:24:10

Do we really need new keywords for this? And if we do, should it be `from_{right,left}`?

I think a user interface decision like this needs more input from other developers. I'll post to sage-devel with this question.


---

Comment by burcin created at 2010-07-24 21:24:10

Changing status from positive_review to needs_info.


---

Comment by DanaErnst created at 2010-07-25 02:35:50

The idea for this came up during one of the online sessions for the MAA PREP Workshop for Sage (organized by Rob Beezer, Jason Grout, and Karl-Dieter Crisman) that I am currently enrolled in.  While we were discussing calculus during one of our workshop sessions, one of the participants remarked that most students learn one-sided limits as "from the left" and "from the right."  Rob, Jason, and Karl-Dieter knew that I was interested in getting involved in Sage development and remarked that I could add that this terminology to Sage if I was interested.  I figured that it was an easy way to get my feet wet.

I have been using Sage for almost a year, so I would consider myself a newbie.  I'm not personally attached to this patch and if others feel that it is unnecessary bloat, then my feelings won't be hurt.


---

Attachment

add deprecation warnings


---

Comment by burcin created at 2010-09-08 21:19:25

This was discussed in the thread:

http://groups.google.com/group/sage-devel/t/9dd6dfe26f09be93

The resulting decision was to deprecate 'above' and 'below' and add support for '+', '-', 'right', and 'left'.

attachment:trac_9200-deprecation.patch makes the necessary changes, on top of Dana's patch.

Patches to be applied in this order:
 * attachment:trac_9200-left-right-limits-v2.patch
 * attachment:trac_9200-deprecation.patch


---

Comment by burcin created at 2010-09-08 21:19:25

Changing status from needs_info to needs_review.


---

Comment by DanaErnst created at 2010-09-09 00:00:58

Burcin,

Thanks for picking up the ball on this.  I was planning on attacking this in a few weeks after the initial craziness of my semester settled down.  Now, I get to cross something off my todo list:)

Dana


---

Attachment


---

Comment by rbeezer created at 2010-09-09 06:02:03

I noticed while reviewing this that there are two "TEST" headers in the docstring for limit().  So I removed the second one and uploaded a new version of the "documentation" patch - only change is the removal of the header (still has Burcin's name on it too).

I'm running tests overnight and then plan to give this a positive review.  

Burcin - I'll wait for you to check-off on the one change to your patch.

Rob


---

Comment by burcin created at 2010-09-09 07:31:38

Thanks for taking care of the `TEST` headers Rob. I'm ok with your change. Looking forward to that positive review. :)


---

Comment by rbeezer created at 2010-09-09 20:45:43

Thanks, Burcin, for the go-ahead and for prompting the discussion on this one.  Builds (on 4.5.2), docs look good, passes all tests (sage -testall) and is consistent with discussion on sage-devel.  Positive review.

Congrats to Dana Ernst on his first contribution.  Next one will probably engender less discussion.  ;-)

## Release Manager

 Patches to be applied in this order:
  * attachment:trac_9200-left-right-limits-v2.patch
  * attachment:trac_9200-deprecation-v2.patch

Dana Ernst is first-time contributor (for release notes).


---

Comment by rbeezer created at 2010-09-09 20:45:43

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-15 11:13:39

Resolution: fixed
