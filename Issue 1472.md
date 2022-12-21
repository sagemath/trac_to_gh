# Issue 1472: [with optional spkg] gnuplotpy optional package doesn' t work with numpy

Issue created by migration from Trac.

Original creator: jkantor

Original creation time: 2007-12-12 10:00:35

Assignee: was

The optional gnuplotpy package doesn't work with numpy (requires Numeric). Luckily this is fixed by doing a global search an replace of Numeric with numpy. Having done that 

http://sage.math.washington.edu/home/jkantor/spkgs/gnuplotpy-1.7.p3.spkg

now works. 




---

Comment by cwitty created at 2007-12-15 04:19:43

For the sake of the reviewer, could you give an example of a command sequence that fails with the current gnuplotpy package and works with the new one?


---

Comment by cwitty created at 2007-12-15 05:14:02

Looks good to me.  Tested using sample code from http://www.math.washington.edu/~jkantor/Numerical_Sage/node13.html .


---

Comment by mabshoff created at 2007-12-15 05:45:47

The optional spkg has been added to sagemath.org.


---

Comment by mabshoff created at 2007-12-15 05:45:47

Resolution: fixed
