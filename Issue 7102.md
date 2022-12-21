# Issue 7102: R.py doctest fails for non-english locale

Issue created by migration from Trac.

Original creator: GeorgSWeber

Original creation time: 2009-10-03 19:14:40

Assignee: tbd

Testing Sage-4.1.2-alpha4, I saw that the old failure from #6379 somehow was resurrected (probably by using some new version of the R package that has changed its internationalized warning messages). To reproduce the failure, do something (or nothing, see also #6379) like

```
export LANG=de_DE.UTF-8
```

from a (sage -sh) shell and then you'll get:

```
sage -t -long "devel/sage/sage/interfaces/r.py"             
**********************************************************************
File "/Users/Shared/sage/sage-4.1.2.alpha4/devel/sage/sage/interfaces/r.py", line 549:
    sage: r.library('foobar')
Expected:
    Traceback (most recent call last):
    ...
    ImportError: ...
Got nothing
**********************************************************************
File "/Users/Shared/sage/sage-4.1.2.alpha4/devel/sage/sage/interfaces/r.py", line 839:
    sage: r.completions('tes')
Expected:
    ['testInheritedMethods', 'testPlatformEquivalence', 'testVirtual']
Got:
    ['testInheritedMethods', 'testInheritedMethods', 'testPlatformEquivalence', 'testPlatformEquivalence', 'testVirtual', 'testVirtual']
**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_17
   1 of   4 in __main__.example_34
***Test Failed*** 2 failures.
For whitespace errors, see the file /Users/georgweber/.sage//tmp/.doctest_r.py
         [7.3 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage/sage/interfaces/r.py"
```

Fortunately, I fiddled around with this file and this bug more than once (see also #6594, #6646), so I knew where to look. Hopefully, this zombie is put down to rest ... 


---

Comment by GeorgSWeber created at 2009-10-03 19:17:26

tested against 4.1.2.alpha4


---

Comment by GeorgSWeber created at 2009-10-03 19:19:29

Changing assignee from tbd to GeorgSWeber.


---

Comment by GeorgSWeber created at 2009-10-03 19:19:29

Changing status from new to assigned.


---

Attachment


---

Comment by was created at 2009-10-05 03:00:57

Resolution: fixed


---

Comment by was created at 2009-10-05 03:00:57

merged in sage-4.1.2.rc1...
