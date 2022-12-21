# Issue 3850: Sage 3.1.alpha2: matrix_space.py doctest failure (OSX only)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-08-14 16:19:07

Assignee: mabshoff


```
********************************************************************* 
File "/Users/palmieri/Desktop/sage-3.1.alpha2/tmp/matrix_space.py", 
line 543: 
    sage: l.index(A) 
Exception raised: 
    Traceback (most recent call last): 
      File "/Users/palmieri/Desktop/sage-3.1.alpha2/local/lib/ 
python2.5/doctest.py", line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_12[7]>", line 1, in <module> 
        l.index(A)###line 543: 
    sage: l.index(A) 
    SystemError: error return without exception set 
********************************************************************** 
File "/Users/palmieri/Desktop/sage-3.1.alpha2/tmp/matrix_space.py", 
line 545: 
    sage: l.index(B) 
Exception raised: 
    Traceback (most recent call last): 
      File "/Users/palmieri/Desktop/sage-3.1.alpha2/local/lib/ 
python2.5/doctest.py", line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_12[8]>", line 1, in <module> 
        l.index(B)###line 545: 
    sage: l.index(B) 
    SystemError: error return without exception set 
********************************************************************** 
File "/Users/palmieri/Desktop/sage-3.1.alpha2/tmp/matrix_space.py", 
line 551: 
    sage: l.index(A) 
Exception raised: 
    Traceback (most recent call last): 
      File "/Users/palmieri/Desktop/sage-3.1.alpha2/local/lib/ 
python2.5/doctest.py", line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_12[9]>", line 1, in <module> 
        l.index(A)###line 551: 
    sage: l.index(A) 
    SystemError: error return without exception set 
********************************************************************** 
File "/Users/palmieri/Desktop/sage-3.1.alpha2/tmp/matrix_space.py", 
line 553: 
    sage: l.index(C) 
Exception raised: 
    Traceback (most recent call last): 
      File "/Users/palmieri/Desktop/sage-3.1.alpha2/local/lib/ 
python2.5/doctest.py", line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_12[10]>", line 1, in <module> 
        l.index(C)###line 553: 
    sage: l.index(C) 
    SystemError: error return without exception set 
********************************************************************** 
1 items had failures: 
   4 of  35 in __main__.example_12 
***Test Failed*** 4 failures. 
For whitespace errors, see the file /Users/palmieri/Desktop/ 
```



---

Comment by mabshoff created at 2008-08-15 08:42:32

From the OSX 10.5 man page:

```
RETURN VALUES
     The memcmp() function returns zero if the two strings are identical, 
otherwise returns the difference between the first two differing bytes 
(treated as unsigned char values, so that `\200' is greater than `\0', 
for example).  Zero-length strings are always identical.
```



---

Attachment

Robert Bradshaw's #3788 caused this (and another failure).    The attached ticket fixes it.


---

Comment by mabshoff created at 2008-08-15 09:38:33

This fixes the problem and also passes doctests. It might be slightly slower, but correctness ought to compensate for that.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-15 09:38:48

Resolution: fixed


---

Comment by mabshoff created at 2008-08-15 09:38:48

Merged in Sage 3.1.rc0
