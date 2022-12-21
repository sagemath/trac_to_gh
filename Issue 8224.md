# Issue 8224: help(w) is broken for infinite word w defined by a callable

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2010-02-09 22:51:52

Assignee: slabbe

CC:  jhpalmieri mpatel

Keywords: help

The following works :


```
sage: w = Word(range(10))
sage: help(w)
```


but this one :


```
sage: w = Word(lambda n:n)
sage: w
word: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,...
sage: help(w)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/slabbe/Applications/sage-4.3.2/devel/sage-combinat/sage/combinat/words/<ipython console> in <module>()

/Users/slabbe/Applications/sage-4.3.2/local/lib/python2.6/site-packages/sage/misc/sagedoc.pyc in help(module)
   1202         Welcome to Sage ...
   1203     """    
-> 1204     if module:
   1205         python_help(module)
   1206     else:

TypeError: an integer is required
```


neither the following :


```
sage: from itertools import repeat
sage: w = Word(repeat(4))
sage: w
word: 4444444444444444444444444444444444444444...
sage: help(w)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/slabbe/Applications/sage-4.3.2/devel/sage-combinat/sage/combinat/words/<ipython console> in <module>()

/Users/slabbe/Applications/sage-4.3.2/local/lib/python2.6/site-packages/sage/misc/sagedoc.pyc in help(module)
   1202         Welcome to Sage ...
   1203     """    
-> 1204     if module:
   1205         python_help(module)
   1206     else:

TypeError: an integer is required
```



---

Attachment


---

Comment by slabbe created at 2010-02-10 00:00:32

Changing status from new to needs_review.


---

Comment by slabbe created at 2010-02-14 22:55:56

Dear Mitesh Patel,

I am adding you in cc to this ticket since you were involved in #6820, you might want to review this ticket.

Thank you,

Sébastien


---

Comment by mpatel created at 2010-02-15 05:54:34

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-15 05:54:34

The patch looks good, and it works for me.  I've added Dr. Palmieri to the CC: list, in case I've missed something.


---

Comment by mvngu created at 2010-02-17 00:11:08

I have merged [trac_8224_help_fix-sl.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8224/trac_8224_help_fix-sl.patch) with a sensible commit message containing the ticket number.


---

Comment by mvngu created at 2010-02-17 00:11:08

Resolution: fixed
