# Issue 3853: [with patch, needs review] plot.py improvements part 1: Remove all factories

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-08-14 17:56:23

Assignee: tbd

CC:  anakha jason

I replaced all of the factories with individual functions.


---

Attachment


---

Comment by mhansen created at 2008-08-14 17:57:20

Changing assignee from tbd to was.


---

Comment by mhansen created at 2008-08-14 17:57:20

Changing component from algebra to graphics.


---

Comment by jason created at 2008-08-14 18:21:30

Changing keywords from "" to "jason".


---

Comment by jason created at 2008-08-14 18:21:42

Changing keywords from "jason" to "".


---

Comment by jason created at 2008-08-19 14:54:20

apply instead of trac_3853.patch


---

Attachment

Extra things this patch does:

`line([(0,0,0),(1,1,1)])` no longer produces a 3d line, but a 2d line from the first 2 coordinates.  Use line3d to get a 3d line.

`line(object)` no longer tries object.plot() first, which is a very, very good thing, since it is natural to assume that line(object) will be something like a line, but object.plot() could be *anything*.

`line` no longer has a "coerce" argument; all input data is always coerced to float.  I've changed this to use numpy to convert to float; currently, that's a bit faster, from some tests that wstein ran.  As wstein mentioned on IRC, we should try to replace the float conversion with a snippet of Cython.

`text` used to make 3d text when a 3d point was passed; now it only makes 2d text.  Use the text3d for 3d text.


---

Comment by jason created at 2008-08-19 16:50:32

well, that coerce comment should really be: I changed this to use numpy in one case; the case where we need to separate the x-values and y-values still coerces to float no matter what.  I guess the "line" function, a user-visible function, shouldn't have a coerce=False option; it's too unsafe.


---

Comment by jason created at 2008-08-19 16:54:33

I take that back; I took back out the numpy stuff; we should just make a general cython function that ensures that a list is coerced to float.


---

Comment by jason created at 2008-08-19 16:58:38

That last patch also streamlines a few things and makes a few things more consistent.


---

Comment by jason created at 2008-08-19 17:17:28

Despite the name trac_3880 in the referee patch, it really is the referee patch for this ticket!


---

Comment by jason created at 2008-08-19 19:53:47

referee patch updated to correct documentation and doctests, plus simplify code in xydata... function.


---

Comment by jason created at 2008-08-19 19:54:12

plus throw some errors when trying to do line() or text() and get back a 3d object.


---

Comment by jason created at 2008-08-19 21:04:33

there are still some doctest errors from the referee patch


---

Attachment

updated referee patch to fix some more things.


---

Comment by jason created at 2008-08-21 22:01:07

Positive review for the initial part (mhansen's part).  The referee patch adds enough functionality that it probably ought to be reviewed as well.

So, apply trac_3853-rebased-3.1.1-trac_3880.patch and then the referee patch to review/merge this ticket.


---

Comment by jason created at 2008-08-21 22:03:12

I think now there is one doctest in plot.py that gives a weird error (it's a doctesting error, not a sage error, I think).


---

Comment by mhansen created at 2008-08-26 02:06:20

Apply 

trac_3853-rebased-3.1.1-trac_3880.patch
trac_3880-referee.patch 
trac_3853-fixes.patch 

in order.


---

Comment by jwmerrill created at 2008-08-26 02:38:06

There was a thread about the proposed new behavior of line:

line([(0,0,0),(1,1,1)]) no longer produces a 3d line, but a 2d line from the first 2 coordinates. Use line3d to get a 3d line.

http://groups.google.com/group/sage-devel/browse_thread/thread/6f4b382145c09546

All the comments were negative.  That needs to be addressed, right?

I suspect I may be overstepping my bounds by changing this from positive review to needs work--if so, I'll accept an appropriate wrist slapping.


---

Attachment


---

Comment by mabshoff created at 2008-08-26 03:24:42

This looks good to me, it restores the old behavior. If something else is desired it should be dealt with via a new ticket since this code should go in and would bitrot quickly.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-26 03:44:45

Resolution: fixed


---

Comment by mabshoff created at 2008-08-26 03:44:45

Merged trac_3853-rebased-3.1.1-trac_3880.patch, trac_3880-referee.patch and trac_3853-fixes.2.patch in Sage 3.1.2.alpha1
