# Issue 6755: sage-4.1.1 -- twist.py tests are seriously broken on OS X 10.5 PPC

Issue created by migration from https://trac.sagemath.org/ticket/6755

Original creator: was

Original creation time: 2009-08-15 16:37:47

Assignee: boothby


```

pdlc424:sage-4.1.1 wstein$ ./sage -t devel/sage/sage/server/simple/twist.py
sage -t  "devel/sage/sage/server/simple/twist.py"           
**********************************************************************
File "/Users/wstein/build/sage-4.1.1/devel/sage/sage/server/simple/twist.py", line 51:
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
File "/Users/wstein/build/sage-4.1.1/devel/sage/sage/server/simple/twist.py", line 95:
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
File "/Users/wstein/build/sage-4.1.1/devel/sage/sage/server/simple/twist.py", line 103:
    sage: print get_url('http://localhost:%s/simple/file?session=%s&cell=3&file=a.txt' % (port, session))
Expected:
    test
Got:
    No such file a.txt in cell 3.
**********************************************************************
1 items had failures:
   3 of  24 in __main__.example_0
***Test Failed*** 3 failures.
For whitespace errors, see the file /Users/wstein/build/sage-4.1.1/tmp/.doctest_twist.py

```



---

Comment by was created at 2009-10-02 16:18:34

Resolution: fixed
