# Issue 5260: document the requirement for a compiler better for f2py/weave/ctypes and error out with a sensible error message when no compiler is present

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-13 22:14:35

Assignee: cwitty

This is motivated by http://groups.google.com/group/sage-devel/browse_thread/thread/ef0eecd9f3473215

```
Hi everyone, 
being a new Sage user under Mac OS X, I spent a whole day trying to 
get the examples for using compiled code from 
http://www.math.washington.edu/~jkantor/Numerical_Sage/node10.html to 
work. Trying to make sense of the error messages and googling for 
fixes, I did not realise the most simple explanation - until I ran 
"which gcc" in the terminal and got no result. I simply didn't have 
gcc installed! Unless I'm blind, there is no hint to check if gcc is 
installed in an obvious place on website or in the documentation. Of 
course, the problem was fixed easily by installing XcodeTools. 
I think it would be very helpful for new users to have a remark in the 
readme or on the download page, that sage does not include gcc, but 
requires it for certain features. Maybe this is so obvious, that 
nobody thought of it before. 
Otherwise, Sage seems to be a great piece of Software, keep on the 
great Work 
Felix 
```



---

Comment by mabshoff created at 2009-02-13 22:30:02

Changing component from misc to documentation.


---

Comment by mabshoff created at 2009-02-13 22:30:02

D'oh, this is probably better assigned to component "documentation".

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-13 22:30:02

Changing assignee from cwitty to tba.


---

Comment by jdemeyer created at 2015-09-07 19:05:58

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-09-07 19:05:58

`gcc` is included with Sage now.


---

Comment by jdemeyer created at 2015-09-07 19:06:02

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-09-12 13:57:41

Resolution: fixed
