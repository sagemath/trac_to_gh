# Issue 6427: Fix doctest failures in sage-4.1.alpha1

Issue created by migration from https://trac.sagemath.org/ticket/6427

Original creator: boothby

Original creation time: 2009-06-26 18:05:01

Assignee: tba

The following occur in sage-4.1.alpha1:


```
The following tests failed:

        sage -t -long devel/sage/doc/fr/tutorial/programming.rst # 1 doctests failed
        sage -t -long devel/sage/sage/misc/darwin_utilities.pyx # 3 doctests failed
----------------------------------------------------------------------
```


they're both really easy fixes.


---

Attachment


---

Comment by was created at 2009-06-26 18:15:38

The change to module_list.py is wrong.  If you do that, then Sage won't build on OS X 10.4, and will waste time/space on non-OS X.  It's critical to only build that module if we're on OS X >= 10.5, since it isn't implemented for any other platform.  the other part of the patch is fine.


---

Comment by was created at 2009-06-26 18:16:41

I think the right change is to make the doctests in darwin_utilities.pyx marked 

```
# optional - osx
```



---

Comment by mvngu created at 2010-02-02 06:16:15

Resolution: fixed


---

Comment by mvngu created at 2010-02-02 06:16:15

This is fixed in Sage 4.3.2.alpha1:

```
[mvngu@mod sage-4.3.2.alpha1]$ ./sage -t -long devel/sage/doc/fr/tutorial/programming.rst
sage -t -long "devel/sage/doc/fr/tutorial/programming.rst"  
	 [4.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.7 seconds
[mvngu@mod sage-4.3.2.alpha1]$ ./sage -t -long devel/sage/sage/misc/darwin_utilities.pyx
sage -t -long "devel/sage/sage/misc/darwin_utilities.pyx"   
	 [4.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.0 seconds
```

I'm closing this ticket as fixed.
