# Issue 4985: Expand documentation for list_plot to point out the utility of zip

Issue created by migration from https://trac.sagemath.org/ticket/4985

Original creator: jason

Original creation time: 2009-01-16 02:50:47

Assignee: was

CC:  jhpalmieri

We should expand the documentation for list_plot so that questions like on the latter half of this thread don't happen:

http://groups.google.com/group/sage-support/browse_thread/thread/e523b8ade175746c

Basically, we should explain how to use zip like thus:

list_plot(zip(list of x-coords, list of y-coords))

so that people from Matlab don't get confused by the very unhelpful error message.  Maybe the error message ought to be changed too.


---

Comment by wdj created at 2009-01-16 02:55:09

Good idea, IMHO. 
I wonder if it also a good idea to add plot_list as an alias to the namespace so people who hunt for plot commands (and the documentation for them) using tab completion can find this more easily?


---

Comment by jhpalmieri created at 2009-03-22 23:51:17

Changing priority from major to minor.


---

Comment by jhpalmieri created at 2009-03-22 23:51:17

Here's a patch, adding to the list_plot docstring.  I feel neutral, or maybe a little negative, about the suggestion to add plot_list as an alias.  Would we then need to do the same for list_plot3d?  Anyway, that can be dealt with as a separate ticket.

By the way, I wasn't sure what "the very unhelpful error message" is. We might consider testing whether the second argument to list_plot (which is "plotjoined", should be boolean) is a list or tuple, and then print a warning, because perhaps someone ran "list_plot([list1], [list2])" without meaning to.  Opinions?


---

Attachment

Nice!  Positive review.


---

Comment by jason created at 2009-03-23 21:20:26

(applies cleanly to 3.4, doctests in plot.py pass, and the plot looks right).


---

Comment by jason created at 2009-03-23 21:23:13

#5594 is for the suggestion by jhpalmieri above.


---

Comment by mabshoff created at 2009-03-25 06:08:13

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-25 06:08:13

Resolution: fixed
