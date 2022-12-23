# Issue 6893: [with patch, needs work] Plotting code improvements

Issue created by migration from https://trac.sagemath.org/ticket/6893

Original creator: jason

Original creation time: 2009-09-05 09:06:37

Assignee: was

The patch on this ticket was originally posted by Mike Hansen to #5448.  This patch was replaced with a different patch on that ticket.  However, there are still good bits in this patch that simplify the plotting code.  These good bits should be taken and incorporated into the plotting code.


---

Comment by jason created at 2010-03-17 05:20:39

Changing type from defect to enhancement.


---

Attachment


---

Comment by kcrisman created at 2010-07-27 17:34:15

What pieces of this patch are the relevant ones?  Most of this does look related to switching to mpl axes.


---

Comment by jason created at 2010-07-27 23:39:39

The options stuff looked potentially interesting, and possibly the architecture for constructing a matplotlib image.
