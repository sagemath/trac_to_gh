# Issue 6740: upgrade mpmath to 0.13

Issue created by migration from https://trac.sagemath.org/ticket/6740

Original creator: mvngu

Original creation time: 2009-08-13 19:24:19

Assignee: mabshoff

CC:  fredrik.johansson

The latest version of mpmath is now 0.13. Upgrade Sage to use that latest version.


---

Attachment


---

Comment by fredrik.johansson created at 2009-08-14 00:36:45

I took the 0.12 spkg and updated the files in it. Let's see if this works!


---

Comment by mhansen created at 2009-09-01 23:11:11

I just removed a temporary file from the spkg and checked in Fredrik's update to SPKG.txt into the hg repo.  Other than that, looks good.

Use the spkg at http://sage.math.washington.edu/home/mhansen/mpmath-0.13.spkg


---

Comment by mvngu created at 2009-09-02 09:44:53

Merged `mpmath-0.13.spkg` in the standard packages repository. Running the test suite results in the following failures:

```
sage -t -long devel/sage-main/sage/server/simple/twist.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/server/simple/twist.py", line 51:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))
Expected:
    {
    "status": "done",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    4
Got:
    {
    "status": "computing",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    <BLANKLINE>
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/server/simple/twist.py", line 95:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=%s' % (port, session, urllib.quote(code)))
Expected:
    {
    "status": "done",
    "files": ["a.txt"],
    "cell_id": 3
    }
    ___S_A_G_E___
Got:
    {
    "status": "done",
    "files": [],
    "cell_id": 3
    }
    ___S_A_G_E___
    <BLANKLINE>
    Traceback (most recent call last):    h = open('a.txt', 'w'); h.write('test'); h.close()
    NameError: name 'os' is not defined
    THERE WAS AN ERROR LOADING THE SAGE LIBRARIES.  Try starting Sage from the command line to see what the error is.
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/server/simple/twist.py", line 103:
    sage: print get_url('http://localhost:%s/simple/file?session=%s&cell=3&file=a.txt' % (port, session))
Expected:
    test
Got:
    No such file a.txt in cell 3.
**********************************************************************
1 items had failures:
   3 of  24 in __main__.example_0
***Test Failed*** 3 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_twist.py
	 [23.3 s]
```

These have nothing to do to with the updated mpmath spkg. They are known failures and have been reported in Sage 4.1.1.


---

Comment by mvngu created at 2009-09-02 09:44:53

Resolution: fixed
