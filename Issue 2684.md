# Issue 2684: vertices should not default to  red

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-03-27 14:25:42

Assignee: rlm

A student has brought up that having vertices default to red makes the number labels very difficult to read, especially for visually-impaired people.


---

Comment by jason created at 2008-03-27 14:27:48

The student said that yellow or even pale pink would work much better.


---

Comment by jason created at 2008-04-06 03:59:06

See the extensive discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/87cc5791e7014de8/bf77357d2e33f0a5 for feedback.


---

Attachment


---

Comment by jason created at 2008-05-10 15:43:57

Based on the mailing list conversation, of the two visually-impaired people that looked at the colors, there was:

 * Pink: 1 positive and 1 neutral vote
 * Blue: 1 positive and 1 neutral vote
 * Yellow: 1 positive and 1 negative

I made the default pink and the boundary vertices default to blue.


---

Comment by rlm created at 2008-05-10 18:22:10

No new doctests, but I don't see how to do that for this patch anyway. Apply.


---

Comment by mabshoff created at 2008-05-11 09:21:44

Resolution: fixed


---

Comment by mabshoff created at 2008-05-11 09:21:44

Merged in Sage 3.0.2.alpha0
