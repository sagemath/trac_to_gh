# Issue 6675: doctest failure in sage/sage/misc/sagedoc.py

Issue created by migration from https://trac.sagemath.org/ticket/6675

Original creator: mvngu

Original creation time: 2009-08-05 12:32:47

Assignee: tbd

Keywords: sagedoc.py


```
Built from scratch on

Linux cartan 2.6.28-15-generic #48-Ubuntu SMP Wed Jul 29 08:53:35 UTC
2009 x86_64 GNU/Linux

(MacBook running 64-bit Ubuntu).

Running make test gave one failing doctest, which is repeatable:

[ghitza@cartan sage-4.1.1.rc1]$ ./sage -t devel/sage/sage/misc/sagedoc.py
sage -t  "devel/sage/sage/misc/sagedoc.py"
**********************************************************************
File "/opt/sage-4.1.1.rc1/devel/sage/sage/misc/sagedoc.py", line 360:
   sage: 'abvar/homology' in _search_src_or_doc('doc', 'homology',
'variety', interact=False)
Expected:
   True
Got:
   False
**********************************************************************
1 items had failures:
  1 of   6 in __main__.example_5
***Test Failed*** 1 failures.
For whitespace errors, see the file /opt/sage-4.1.1.rc1/tmp/.doctest_sagedoc.py
        [5.6 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


       sage -t  "devel/sage/sage/misc/sagedoc.py"
Total time for all tests: 5.6 seconds
```

This was reported in [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/37d851338ed69c6a/289094b891882b2e).


---

Comment by AlexGhitza created at 2009-08-05 12:36:20

The same problem occurs on 


```
Linux artin 2.6.30-ARCH #1 SMP PREEMPT Fri Jul 31 18:10:38 UTC 2009 i686 Intel(R) Core(TM)2 Duo CPU T9300 @ 2.50GHz GenuineIntel GNU/Linux
```


a Dell laptop running 32-bit Archlinux.


---

Comment by jhpalmieri created at 2009-08-05 21:37:35

I believe that this is fixed by #6674.  That is, the failure here is because the reference manual didn't build during the 'make' process, and it didn't build because of the issue discussed and solved at #6674.  Since the reference manual didn't build, searching the docs produced no results, hence the doctest failure here.  If someone can confirm this, I think we can close this ticket.


---

Comment by mvngu created at 2009-08-12 15:40:51

This has been fixed by #6674.


---

Comment by mvngu created at 2009-08-12 15:40:51

Resolution: fixed
