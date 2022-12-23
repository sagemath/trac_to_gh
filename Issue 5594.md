# Issue 5594: better error message for list_plot

Issue created by migration from https://trac.sagemath.org/ticket/5594

Original creator: jason

Original creation time: 2009-03-23 21:22:32

Assignee: was

CC:  jhpalmieri

We might consider testing whether the second argument to list_plot (which is "plotjoined", should be boolean) is a list or tuple, and then print a warning, because perhaps someone ran "list_plot([list1], [list2])" without meaning to.


---

Comment by jhpalmieri created at 2009-06-10 22:34:19

This patch raises a `TypeError` if plotjoined is a list or a tuple.


---

Attachment


---

Comment by ncalexan created at 2009-06-15 19:22:28

Fine by me.


---

Comment by rlm created at 2009-06-24 10:06:43

Resolution: fixed
