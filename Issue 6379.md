# Issue 6379: #2513 made R.py doctest fail for non-english locale

Issue created by migration from https://trac.sagemath.org/ticket/6379

Original creator: GeorgSWeber

Original creation time: 2009-06-21 21:49:20

Assignee: was

In ticket #276, the LANG environment variable was set in sage-env (to en_US.UTF-8) and in ticket #2513, this was undone. On my box, the following doctest failure was a consequence:

```
sage -t -long "devel/sage/sage/interfaces/r.py"             
**********************************************************************
File "/Users/Shared/sage/sage-4.0.2/devel/sage/sage/interfaces/r.py", line 554:
    sage: r.library('foobar')
Expected:
    Traceback (most recent call last):
    ...
    ImportError: there is no package called 'foobar'
Got nothing
**********************************************************************
File "/Users/Shared/sage/sage-4.0.2/devel/sage/sage/interfaces/r.py", line 840:
    sage: r.completions('tes')
Expected:
    ['testPlatformEquivalence', 'testVirtual']
Got:
    ['testPlatformEquivalence', 'testPlatformEquivalence', 'testVirtual', 'testVirtual']
**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_17
   1 of   3 in __main__.example_34
***Test Failed*** 2 failures.
For whitespace errors, see the file /Users/Shared/sage/sage-4.0.2/tmp/.doctest_r.py
         [6.3 s]
```

I have *none* of the usual "locale" variables set (LANG, LC_ALL, ...) but nevertheless R is clever enough to detect that I might want read its messages in german. (It's using some Mac OS feature, I think.) But unfortunately the Sage code did parse for english key-words in the R messages. 
Anyway, the above doctest failure could be triggered by anyone by issuing e.g. "export LANG=de_DE.UTF-8" just before running the doctest.


---

Comment by GeorgSWeber created at 2009-06-21 21:49:45

Changing status from new to assigned.


---

Comment by GeorgSWeber created at 2009-06-21 21:49:45

Changing assignee from was to GeorgSWeber.


---

Attachment

tested against 4.0.2


---

Comment by mvngu created at 2009-07-13 22:08:12

All tests passed in Sage 4.1.


---

Comment by mvngu created at 2009-07-14 10:36:37

While testing out this patch, I came across an incidental problem. It's reported at this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/f8da7ca9d81b506b) thread. OK, so the patch fixes a locale problem. But then comes a problem with the R interface command `r.library()`. By the way, this has nothing to do with Georg's patch.


---

Comment by mvngu created at 2009-07-16 10:25:00

Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(


---

Comment by mvngu created at 2009-07-16 21:29:55

Resolution: fixed
