# Issue 8194: SageNB 0.8.x

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-02-05 15:58:45

Assignee: was

CC:  acleone jhpalmieri robert.marik

The trial spkg at

 * 

Has the queue


---

Comment by mpatel created at 2010-02-05 16:39:47

Feel free to ignore a patch (or all of them!).  This is an experiment.


---

Comment by mpatel created at 2010-02-10 18:30:32

Changing status from new to needs_review.


---

Comment by robert.marik created at 2010-02-12 18:31:36

Testing on Sage 4.3.2 I get error


```
sage -t  "local/lib/python2.6/site-packages/sagenb-0.7.5-py2.6.egg/sagenb/misc/sageinspect.py"
**********************************************************************
File "/opt/sage-4.3.2/local/lib/python2.6/site-packages/sagenb-0.7.5-py2.6.egg/sagenb/misc/sageinspect.py", line 75:
    sage: sage_getdoc(Foo)
Expected:
    'docstring\n'
Got:
    'docstring'
**********************************************************************
File "/opt/sage-4.3.2/local/lib/python2.6/site-packages/sagenb-0.7.5-py2.6.egg/sagenb/misc/sageinspect.py", line 459:
    sage: sage_getdoc(identity_matrix)[5:39]
Expected:
    'turn the n x n identity matrix ove'
Got:
    'Return the `n x n` identity matrix'
**********************************************************************
2 items had failures:
   1 of  29 in __main__.example_0
   1 of   4 in __main__.example_8
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/marik/.sage//tmp/.doctest_sageinspect.py

```

Or should be tested on Sage 4.3.3 alpha 0?


---

Comment by mpatel created at 2010-02-13 18:09:45

Thanks for reporting this.  To test with 4.3.2, please apply #8161's latest sage repository patch.  I should have added a note to the description, which I've done now.  I apologize.


---

Comment by robert.marik created at 2010-02-13 18:46:50

Changing status from needs_review to positive_review.


---

Comment by robert.marik created at 2010-02-13 18:46:50

Seems to work fine for me, hanks. Positive review.


---

Comment by jhpalmieri created at 2010-02-13 19:43:28

It seems okay compared to 0.7.4, but it sure would be nice to fix #8231...


---

Comment by mpatel created at 2010-02-14 03:39:30

Resolution: fixed
