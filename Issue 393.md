# Issue 393: Very strange behavior of QQ -> RealField() conversion.

Issue created by migration from Trac.

Original creator: jonhanke

Original creation time: 2007-06-28 15:20:44

Assignee: somebody

Keywords: real, rational, coerce

There is something very wrong with this behavior of this code, which tries to convert 1/2 to a 2x2 matrix.  The problem seems not to be in the matrix code, but since it's hard to reproduce it appears in that form.


---

Attachment

Here is the output of the attached routine, which essentially does the same thing 3 times and gets 3 different answers!


```
jonhanke`@`[~/Documents/sage-2.6/devel/sage-qfdevel/sage/quadratic_forms]: sage -br

----------------------------------------------------------
sage: Building and installing modified SAGE library files.

running install
running build
running build_py
copying sage/quadratic_forms/sage_errors__matrix_test.py -> build/lib.macosx-10.3-i386-2.5/sage/quadratic_forms
running build_ext
running build_scripts
running install_lib
copying build/lib.macosx-10.3-i386-2.5/sage/quadratic_forms/sage_errors__matrix_test.py -> /Users/jonhanke/Documents/sage-2.6/local/lib/python2.5/site-packag

sage: MatrixTest()
False
[0.000000000000000 0.000000000000000]
[0.000000000000000 0.000000000000000]
[0.500000000000000 0.000000000000000]
[0.000000000000000 0.500000000000000]

m1 is 
[0.000000000000000 0.000000000000000]
[0.000000000000000 0.000000000000000]

m2 is 
[0.000000000000000 0.000000000000000]
[0.000000000000000 0.000000000000000]
False


m1 is 
[0.500000000000000 0.000000000000000]
[0.000000000000000 0.500000000000000]

m2 is 
[0.500000000000000 0.000000000000000]
[0.000000000000000 0.500000000000000]
False
```



---

Comment by mhansen created at 2007-08-18 21:40:13

This is just due to the difference between SAGE and Python.  When run from the command line or in a .sage file, SAGE will preprocess the file and change 1/2 to Integer(1)/Integer(2) to (correctly) form the rational 1/2.  When included or run form a .py file, it will remain as 1/2 which Python evaluates to 0.

There is also a typo in the second section of the attached file (m1 is printed twice).


---

Comment by mhansen created at 2007-08-18 21:40:13

Resolution: invalid
