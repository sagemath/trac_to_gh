# Issue 1845: [with patch, spkg] list_plot3d should be able to accept lists of points in arbitrary positions

Issue created by migration from https://trac.sagemath.org/ticket/1845

Original creator: jkantor

Original creation time: 2008-01-19 07:46:24

Assignee: was

The following patch adds some improvements to list_plot3d

http://sage.math.washington.edu/home/jkantor/spkgs/list_plot3d.hg

The new code requires an updated scipy_sandbox

http://sage.math.washington.edu/spkgs/scipy_sandbox-20071020.p1.spkg


---

Attachment


---

Comment by cwitty created at 2008-01-27 04:56:02

Code looks good; doctests pass in sage/plot.  I went through all the doctests by hand and they all work and look pretty.  One of the doctests was malformed (syntax error); the attached trac-1845-fix-doctest.patch fixes that.

I did not look at differences between the old and new scipy_sandbox, or check old functionality of that spkg.

To apply: apply list_plot3d.hg, then trac-1845-fix-doctest.patch; and install the new scipy_sandbox spkg.


---

Comment by mabshoff created at 2008-01-27 07:18:31

Merged in Sage 2.10.1.rc1: the bundle and updated scipy_sandbox as well as cwitty's doctest fix patch.


---

Comment by mabshoff created at 2008-01-27 07:18:31

Resolution: fixed
