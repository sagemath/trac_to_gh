# Issue 4708: sage -tp doesn't test absolute file names nor does it ignore non-existent files

Issue created by migration from https://trac.sagemath.org/ticket/4708

Original creator: ncalexan

Original creation time: 2008-12-05 04:47:56

Assignee: mabshoff

Keywords: ptest parallel test absolute filename


```
-*- mode: sage-test; default-directory: "~/sage-3.2.1.alpha1/devel/sage-nca/sage/modules/" -*-
sage-test started at Thu Dec  4 20:43:38

/Users/ncalexan/bin/sage -b >/dev/null && /Users/ncalexan/bin/sage -tp 2 /Users/ncalexan/sage-3.2.1.alpha1/devel/sage-nca/sage/modules/free_module.py

real	0m1.413s
user	0m0.875s
sys	0m0.426s
Global iterations: 1
File iterations: 1
TeX files: 0
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 0.0 seconds

sage-test finished (all test passed) at Thu Dec  4 20:43:40
```


Also:


```
-*- mode: sage-test; default-directory: "~/sage-3.2.1.alpha1/devel/sage-nca/sage/modules/" -*-
sage-test started at Thu Dec  4 20:44:39

/Users/ncalexan/bin/sage -b >/dev/null && /Users/ncalexan/bin/sage -t /Users/ncalexan/sage-3.2.1.alpha1/devel/sage-nca/sage/modules/free_module.py2

real	0m1.311s
user	0m0.872s
sys	0m0.416s
ERROR: File .//Users/ncalexan/sage-3.2.1.alpha1/devel/sage-nca/sage/modules/free_module.py2 is missing
exit code: 1
 
----------------------------------------------------------------------
The following tests failed:


	.//Users/ncalexan/sage-3.2.1.alpha1/devel/sage-nca/sage/modules/free_module.py2
Total time for all tests: 0.0 seconds

sage-test finished (all test passed) at Thu Dec  4 20:44:40
```



---

Attachment


---

Comment by gfurnish created at 2008-12-05 04:56:28

Trivial fix attached.


---

Comment by gfurnish created at 2008-12-05 04:56:28

Changing assignee from mabshoff to gfurnish.


---

Comment by gfurnish created at 2008-12-05 04:56:28

Changing status from new to assigned.


---

Attachment

Apply only 4708_bin-2.patch, all credit to gfurnish.


---

Comment by mabshoff created at 2008-12-05 06:38:32

Merged 4708_bin-2.patch in Sage 3.2.2.alpha0


---

Comment by mabshoff created at 2008-12-05 06:38:32

Resolution: fixed
