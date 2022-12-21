# Issue 8652: load uses "strip" on non-strings

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-06 05:25:31

Assignee: was

CC:  leif

I got this bug/traceback today by making a file grader.py and a file grader.sage (their content doesn't matter).  


```
sage: import grader
sage: load grader.sage
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/Users/wstein/edu/2010/480/grading/<ipython console> in <module>()

/Users/wstein/sage/build/sage/local/lib/python2.6/site-packages/sage/misc/preparser.pyc in load(filename, globals, attach)
   1487             return
   1488         
-> 1489     filename = filename.strip()
   1490     
   1491     if filename.lower().startswith('http://'):

AttributeError: 'module' object has no attribute 'strip'
sage: 
```


The above bug is the fault of the rewrite *I* did of load and attach, so is my fault. 


---

Comment by leif created at 2010-04-07 17:04:47

Did I miss something?

If I create both files `foo.py` and `foo.sage`, then


```
sage: import foo
I am foo.py
sage: load foo.sage
I am foo.sage
```


doesn't give an error (in 4.3.5).


---

Comment by ddrake created at 2010-04-28 03:39:35

I'm using 4.3.4 and I see the same thing as leif -- worksforme. Perhaps the content of grader.py and grader.sage does matter?


---

Comment by ddrake created at 2012-05-28 22:32:04

Changing keywords from "" to "sd40.5".


---

Comment by ddrake created at 2012-05-28 22:32:04

This still works properly on 5.1.beta0. In two years no one has reported or reproduced this bug; I propose we close it.


---

Comment by mmezzarobba created at 2014-03-15 18:47:15

Changing status from new to needs_review.


---

Comment by mmezzarobba created at 2014-03-15 18:47:21

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-03-19 04:36:53

Resolution: invalid
