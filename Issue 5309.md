# Issue 5309: mark some doctests in misc/package.py #optional - internet

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-02-18 19:06:11

Assignee: mabshoff


```
sage -t -long "devel/sage/sage/misc/package.py"
**********************************************************************
File "/Users/wstein/build/build/sage-3.3.rc2/devel/sage/sage/misc/package.py", line 50:
    sage: sage.misc.package.install_all_optional_packages(dry_run=True)
Expected:
    Installing ...
    []
Got:
    Using SAGE Server http://www.sagemath.org//packages
    http://www.sagemath.org//packages/optional/list --> /Users/wstein/build/build/sage-3.3.rc2/tmp/list
    [Errno socket error] (8, 'nodename nor servname provided, or not known')

SOLUTION: This was caused by the networking being down during this test.   These tests should be marked # optional, since doctesting sage *must* not require an external network connection.  
```



---

Attachment


---

Comment by mabshoff created at 2009-02-20 05:36:33

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 05:55:28

Resolution: fixed


---

Comment by mabshoff created at 2009-02-20 05:55:28

Merged in Sage 3.3.rc3.

Cheers,

Michael
