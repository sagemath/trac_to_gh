# Issue 8353: Adding height() and width() functions to square grid paths

Issue created by migration from Trac.

Original creator: abmasse

Original creation time: 2010-02-24 22:34:23

Assignee: sage-combinat

CC:  slabbe sage-combinat

Keywords: paths, height, width

When dealing with word paths on the square grid, it is very useful to know their height and their width.

In particular, one can compute a bounding box for display purposes. This small ticket adds those two functionalities.


---

Comment by abmasse created at 2010-02-25 10:45:48

Changing status from new to needs_review.


---

Comment by abmasse created at 2010-02-25 10:45:48

Needs review !


---

Comment by slabbe created at 2010-03-01 11:56:01

I would suggest that the value be converted to RR before taking the max or min. You could add a comment explaining the reason of the conversion and that this bug is trac at a ticket number that you give.

The description of this ticket is not really the good place to put your comment. You can put it in a comment of the ticket instead or on sage-devel. I asked the question on sage-devel :
http://groups.google.com/group/sage-devel/browse_thread/thread/2557a48ad695b42e


---

Comment by slabbe created at 2010-03-01 11:56:01

Changing status from needs_review to needs_work.


---

Comment by abmasse created at 2010-03-01 15:36:10

Thanks for your comments !

I found an almost-clean solution for the problem raised by the triangular grid paths. Instead of computing directly the `height()` and `width()` functions, I introduced the `xmin()`, `xmax()`, `ymin()` and `ymax()` functions we talked about. They are called by the two first functions. To solve the problem for the triangular grid paths, I just redefined them by coercing the x- and y-coordinates to real values, so that the `max` and `min` functions be well-defined.

I'll upload another patch in a few minutes. Needs review !


---

Comment by abmasse created at 2010-03-01 15:36:10

Changing assignee from sage-combinat to abmasse.


---

Comment by abmasse created at 2010-03-01 15:36:51

New patch -- adds functions xmin(), xmax(), etc.


---

Comment by abmasse created at 2010-03-01 15:37:23

Changing status from needs_work to needs_review.


---

Attachment


---

Attachment

Applies over the precedent patch


---

Comment by slabbe created at 2010-03-03 17:49:39

All tests passed in sage/combinat/words. Documentation builds fine. The issue discussed above is fixed. I am giving a positive review to Alex's changes.

I added a small patch fixing some documentation. If Alexandre agrees with the changes I did, I allow him to change the status of the ticket to positive review.


---

Comment by abmasse created at 2010-03-03 19:36:45

I agree with Sébastien's changes. I retested it just to make sure, and I looked at the documentation, which is still fine. I'll set this ticket to "positive review".


---

Comment by abmasse created at 2010-03-03 19:36:45

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-03-06 09:16:42

Resolution: fixed
