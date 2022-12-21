# Issue 3592: please update sympy

Issue created by migration from Trac.

Original creator: certik

Original creation time: 2008-07-07 22:06:16

Assignee: gfurnish

1) Put there the attached sympy-0.6.0.spkg. 

2) Then apply the attached patch to Sage and rebuild Sage with "sage -b"

3) make sure the test_sympy.py test works, this should be the outcome:



```
$ ./sage -t devel/sage/sage/calculus/test_sympy.py
sage -t  3.0.3-debian-opteron64-x86_64-Linux/devel/sage/sage/calculus/test_sympy.py
	 [5.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 5.2 seconds
```


4) make sure all tests work. The result of:

$ ./sage -tp 6 devel/sage/sage &> test.log

is attached.


---

Attachment

The category of this ticket is packages and please also assign a milestone per default.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-07 22:17:06

Changing assignee from gfurnish to ondrej.


---

Comment by mabshoff created at 2008-07-07 22:17:06

Changing component from calculus to packages.


---

Comment by mabshoff created at 2008-07-07 22:17:37

And do *not* attach spkgs, link them.

Cheers,

Michael


---

Comment by certik created at 2008-07-07 22:33:35

Test log:

http://sage.math.washington.edu/home/ondrej/ext/sage/test.log

as you can see, there is one test failing, but I think it is not related. Should I check if all tests run without the patch for me?

Here is the link to the spkg:

http://sage.math.washington.edu/home/ondrej/ext/sage/ondrej/sympy-0.6.0.spkg


---

Comment by mabshoff created at 2008-07-08 00:08:20

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-07-08 00:08:20

I am making this a blocker since it fixes one more important import time patch that is worth >0.1 seconds.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-08 00:09:48

The test failure seems to be another rpy is moved and hence broken failure. This ought to be put on its own ticket and fixed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-16 02:12:41

Positive review. The attached patch is a diff and not a proper mercurial patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-16 02:46:29

Resolution: fixed


---

Comment by mabshoff created at 2008-07-16 02:46:29

Merged in Sage 3.0.6.alpha0. I committed the patch in Ondrej's name.

Cheers,

Michael
