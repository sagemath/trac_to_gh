# Issue 2629: Bottom of page problems

Issue created by migration from https://trac.sagemath.org/ticket/2629

Original creator: dunfield

Original creation time: 2008-03-21 16:01:38

Assignee: boothby

CC:  jhpalmieri

When working on a notebook, one tends to end up at the bottom of browser window in the final cell.   However: 

a) If you evaluate this final cell, a new input cell is created, but it is frequently at least partially off-screen and you have to scroll down to get to it.  Currently, window scrolls to accommodate the output of the evaluation, and so should scroll a little more to make the new input cell fully visible.

b) If you do a tab completion or ?-query in the final cell, the output often is partially of screen.   In bad cases, the output is completely off screen and this is very confusing the to user since the program appears to be not responding to their input.   This could be solved either by having the window scroll or having the box appear above the input cell in this instance, though the latter behavior is probably only appropriate for tab completion.  




---

Comment by kcrisman created at 2009-01-21 17:25:20

There is an assessment at #4963 that this issue would largely be resolved by #4963, but this doesn't seem to do it (at least not in the way it is resolved), after testing on Safari and Firefox 2 and 3 on OSX.4 PPC.  

The browser still only shows a little bit; with the proposed fix at #4963, now the browser doesn't have to scroll at all if you are on the last cell and it is at the bottom (not even with a large output), also for tab-completion etc, so the behavior described above is still possible, though perhaps harder because you would have to be unlucky with how you scrolled after your previous computation.

Since this has been dormant for nearly a year, though, moving to minor priority.  If the original reporter disagrees and thinks this should now be closed or stay major, that is okay too, of course!


---

Comment by kcrisman created at 2009-01-21 17:25:20

Changing priority from major to minor.


---

Comment by kcrisman created at 2012-07-07 04:06:12

The second thing is still an issue.  The first does not seem to be any more, upon extremely brief testing.


---

Comment by chapoton created at 2020-03-28 10:10:46

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-03-28 10:10:46

old ticket about deprecated sagenb, can we close ?


---

Comment by dunfield created at 2020-03-28 14:18:32

Changing status from needs_review to positive_review.


---

Comment by dunfield created at 2020-03-28 14:18:32

This ancient ticket should definitely be closed.  Setting positive review.


---

Comment by chapoton created at 2020-03-28 15:21:36

thx


---

Comment by chapoton created at 2020-03-28 15:21:36

Resolution: invalid
