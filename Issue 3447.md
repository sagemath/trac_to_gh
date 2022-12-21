# Issue 3447: sage -t foo gives wrong path to the file foo in the output

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-06-17 04:46:36

Assignee: failure

CC:  gfurnish mjo


```
D-69-91-136-212:modular was$ sage -t dims.py 
sage -t  devel/sage-main/sage/modular/dims.py               **********************************************************************
File "/Users/was/s/tmp/dims.py", line 1564:
    sage: sturm_bound(Gamma1(13),5)
```


Notice the *tmp* above.  

This is not trivial to fix.  We need to change this:

```
D-69-91-136-212:modular was$ sage -t dims.py 
sage -t  devel/sage-main/sage/modular/dims.py               **********************************************************************
File ".../devel/sage-main/sage/modular/dims.py", line 1564:
    sage: sturm_bound(Gamma1(13),5)
```



---

Comment by mabshoff created at 2008-12-05 05:19:30

Gary, 

any idea about this one?

Cheers,

Michael


---

Comment by mderickx created at 2011-08-24 15:32:54

seems to be fixed a long time ago
right now it works:


```
md:modular maarten$ sage -t dims.py
/Users/maarten/Downloads/sage-4.7.2.alpha2
sage -t  "devel/sage-main/sage/modular/dims.py"             
	 [4.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.9 seconds
```



---

Comment by mderickx created at 2011-08-24 15:32:54

Changing status from new to needs_review.


---

Comment by mjo created at 2011-11-30 23:34:31

It is fixed. The temp file is still mentioned for failures, but is done so separately "For whitespace errors..."


```
$ sage -t dims.py 
sage -t  "devel/sage-new_maxima/sage/modular/dims.py"       
**********************************************************************
File "/home/mjo/src/sage-4.8.alpha2/devel/sage-new_maxima/sage/modular/dims.py", line 110:
    sage: sage.modular.dims.CO_delta(1,5,7,eps^3)
Expected:
    4
Got:
    2
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mjo/.sage//tmp/dims_12113.py
	 [2.9 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage-new_maxima/sage/modular/dims.py"
Total time for all tests: 2.9 seconds
```



---

Comment by jhpalmieri created at 2011-12-01 00:24:42

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-12-09 10:25:09

Resolution: worksforme
