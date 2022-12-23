# Issue 5323: "./sage -t" gives misleading error message when doctesting non-existing file with absolute patch

Issue created by migration from https://trac.sagemath.org/ticket/5323

Original creator: mabshoff

Original creation time: 2009-02-20 15:49:37

Assignee: mabshoff

CC:  mjo

The `./` should not be here:

```
mabshoff@sage:/scratch/mabshoff/sage-3.3.rc3$ ./sage -t /scratch/mabshoff/sage-3.3.rc3/devel/sage/sage/plot/plotg.py 
ERROR: File .//scratch/mabshoff/sage-3.3.rc3/devel/sage/sage/plot/plotg.py is missing
```


Cheers,

Michael


---

Comment by mjo created at 2012-01-05 00:31:00

Fixed in 4.8.alpha6:


```
$ ./sage -t /scratch/mabshoff/sage-3.3.rc3/devel/sage/sage/plot/plotg.py 
ERROR: File /scratch/mabshoff/sage-3.3.rc3/devel/sage/sage/plot/plotg.py is missing
 
----------------------------------------------------------------------
The following tests failed:


	/scratch/mabshoff/sage-3.3.rc3/devel/sage/sage/plot/plotg.py # File not found
Total time for all tests: 0.0 seconds
```



---

Comment by mjo created at 2012-01-05 00:31:00

Changing status from new to needs_review.


---

Comment by mjo created at 2012-01-05 00:31:57

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-01-05 13:37:37

Resolution: worksforme
