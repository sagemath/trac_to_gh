# Issue 3922: [with patch, needs review] Make nice arrows

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-08-21 22:41:37

Assignee: was

We've been having lots of trouble with arrows looking nice.  In this patch, there is a new matplotlib class that puts an arrow at the end of a line, using the same sort of things they do to put markers on lines.  This way, the arrows:

1. don't depend on the aspect ratio of the plot

2. don't depend on the scale of the plot.

They always look pretty :).

It would be nice to eventually upstream this functionality into the matplotlib Line2D class.


---

Comment by jason created at 2008-08-21 22:43:43

Oh, the patch also updates the sage "arrow" class.  This patch is made for after applying the patch at #3853, but it might be possible to apply it before.


---

Comment by jason created at 2008-08-21 23:42:12

It looks like a few doctests fail when they try to do `from sage.all_cmdline import *` or something.  I'm not sure exactly what this issue is here.  The error is that, in arrow_line.py, `import matplotlib` throws an error that there is no module named matplotlib.


---

Comment by jason created at 2008-08-27 13:47:04

Updated patch to correct some of the drawing code and added documentation.


---

Comment by jason created at 2008-08-27 13:57:44

The patch applies cleanly to sage 3.1.2alpha1.  All doctests pass with the patch applied on sage.math.


---

Comment by mhansen created at 2008-08-27 20:41:08

The arrow_line.py should probably be moved to the matplotlib spkg.


---

Attachment


---

Comment by jason created at 2008-09-03 23:55:12

Patch is updated to remove the arrow_line.py file and put it in the matplotlib spkg as a patch.  The updated matplotlib spkg is at: http://sage.math.washington.edu/home/jason/matplotlib-0.98.3.p1.spkg


---

Comment by mhansen created at 2008-09-04 00:37:46

Looks good to me.


---

Comment by mabshoff created at 2008-09-04 00:45:30

Positive review on the spkg. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-04 01:10:51

Resolution: fixed


---

Comment by mabshoff created at 2008-09-04 01:10:51

Merged patch and spkg in Sage 3.1.2.rc0
