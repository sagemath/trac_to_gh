# Issue 1223: doctest timeouts in sage/plot/plot.py on slow systems

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-20 22:53:11

Assignee: mabshoff

On my trusty OSX 10.4 PPC 1.4GHz iBook I get the following timeout:

```
michael-abshoffs-ibook-g4:~/Desktop/sage-2.8.13.rc0 mabshoff$ ./sage -
t  devel/sage-main/sage/plot/plot.py
sage -t  devel/sage-main/sage/plot/plot.py                  *** ***
Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [269.9 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:

        sage -t  devel/sage-main/sage/plot/plot.py
Total time for all tests: 269.9 seconds
```

I have seen similar issues on slower Linux boxen, so maybe we should raise the timeout value.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-20 22:53:18

Changing status from new to assigned.


---

Attachment

this optimizes the plot doctests some


---

Comment by mabshoff created at 2007-11-21 13:25:53

trac1223.patch has been applied and doctesting plot.py drops from 51 seconds on sage.math to 35 seconds.

Cheers,

Michael


---

Attachment

speed ups for graph generators and database doctests


---

Comment by mabshoff created at 2007-11-21 13:42:20

Resolution: fixed


---

Comment by mabshoff created at 2007-11-21 13:42:20

Merged in 2.8.13.rc2.
