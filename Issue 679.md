# Issue 679: print statistics about the number of failed doctests and exact nature of failures

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-17 05:46:44

Assignee: mhansen

Currently we print something like:

```
failures:

        sage -t  calculus/calculus.py
        sage -t  functions/constants.py
<SNIP>
```

It would be nice if we get more precise failure reports, something like:

```
failures:

        sage -t  calculus/calculus.py: 1 out of 27 tests failed
        sage -t  functions/constants.py: segfault
        sage -t  server/notebook/twist.py: CTRL-C invoked
```



---

Comment by gfurnish created at 2008-03-20 11:17:25

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-03-20 11:17:25

Changing assignee from mhansen to gfurnish.


---

Comment by gfurnish created at 2008-03-20 23:02:02

This also fixes the segfault hang bug and the keyboard interrupt functionality of sage-ptest


---

Attachment


---

Comment by mabshoff created at 2008-03-21 00:20:35

Patch looks good to me. Excellent work.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-21 00:20:50

Merged in Sage 2.11.alpha1


---

Comment by mabshoff created at 2008-03-21 00:20:50

Resolution: fixed


---

Comment by mabshoff created at 2008-03-21 00:52:24

After the patch some small trouble left:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha1$ ./sage -tp 1 -long devel/sage/sage/plot/plot.py
Global iterations: 1
File iterations: 1
TeX files: 0

----------------------------------------------------------------------
sage -t -long devel/sage/sage/plot/plot.py
**********************************************************************
File "plot.py", line 3506:
    sage: plot(x^(1/3), (x,-1,1))
Expected nothing
Got:
    WARNING: When plotting, failed to evaluate function at 100 points.
    Last error message: 'negative number cannot be raised to a fractional power'
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of  28 in __main__.example_111
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_plot.py

         [71.8 s]

The following tests failed:

        sage -t -long devel/sage/sage/plot/plot.py: 0 doctests failed
----------------------------------------------------------------------
```


Cheers,

Michael


---

Attachment

Fix for plot.py bug


---

Comment by mabshoff created at 2008-03-21 01:01:22

Also merged trac_679n2.patch in Sage 2.11.alpha1


---

Comment by mabshoff created at 2008-03-21 12:19:45

More trouble with pexpect exceptions:

```
sage -t -long devel/sage-main/sage/interfaces/rubik.py      **********************************************************************
File "rubik.py", line 243:
    sage: DikSolver().solve(C.facets())
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[2]>", line 1, in <module>
        DikSolver().solve(C.facets())###line 243:
    sage: DikSolver().solve(C.facets())
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/rubik.py", line 253, in solve
        child = pexpect.spawn(self.__cmd+" -p")
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/pexpect.py", line 328, in __init__
        raise ExceptionPexpect ('The command was not found or was not executable: %s.' % self.command)
    ExceptionPexpect: The command was not found or was not executable: cube.
**********************************************************************
File "rubik.py", line 246:
    sage: DikSolver().solve(C.facets())
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[4]>", line 1, in <module>
        DikSolver().solve(C.facets())###line 246:
    sage: DikSolver().solve(C.facets())
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/rubik.py", line 253, in solve
        child = pexpect.spawn(self.__cmd+" -p")
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/pexpect.py", line 328, in __init__
        raise ExceptionPexpect ('The command was not found or was not executable: %s.' % self.command)
    ExceptionPexpect: The command was not found or was not executable: cube.
**********************************************************************
File "rubik.py", line 249:
    sage: DikSolver().solve(C.facets())
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[6]>", line 1, in <module>
        DikSolver().solve(C.facets())###line 249:
    sage: DikSolver().solve(C.facets())
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/rubik.py", line 253, in solve
        child = pexpect.spawn(self.__cmd+" -p")
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/pexpect.py", line 328, in __init__
        raise ExceptionPexpect ('The command was not found or was not executable: %s.' % self.command)
    ExceptionPexpect: The command was not found or was not executable: cube.
**********************************************************************
1 items had failures:
   3 of   7 in __main__.example_5
***Test Failed*** 3 failures.
For whitespace errors, see the file .doctest_rubik.py
         [59.8 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:
```



---

Attachment

The patch trac_679-case-3.patch fixes the above issue.

Cheers,

Michael
