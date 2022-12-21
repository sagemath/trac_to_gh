# Issue 1865: notebook -- after restart output of first evaluation is not displayed

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-20 16:44:36

Assignee: boothby

Try this in the notebook:

1. Click restart worksheet in the action menu.

2. Evaluate the contents of a cell.

You'll find nothing happens.   More precisely, the first cell does get evaluated (as you can see by assigning a variable there), but the output of this evaluation is never displayed in the notebook. 


---

Comment by boothby created at 2008-03-16 19:04:47

I can't reproduce this.  Invalid?


---

Comment by was created at 2008-03-16 20:32:46

> I can't reproduce this. Invalid?

I reproduce this every day and it drives me nuts.  This is a serious problem.


---

Comment by boothby created at 2008-03-16 21:26:16

Shoot.  What browser?


---

Comment by was created at 2008-05-11 06:13:13

I fixed this when doing all the work improving the javascript documentation a few weeks ago.


---

Comment by was created at 2008-05-11 06:13:13

Resolution: fixed
