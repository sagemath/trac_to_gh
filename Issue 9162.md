# Issue 9162: cygwin:

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-07 03:57:50

Assignee: tbd

CC:  snark

This is a followup to #8847, which was supposed to fix this, but simply didn't. 


```

sage -t  "devel/sage/sage/functions/other.py"               
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/functions/other.py", line 475:
    sage: gamma1(float(6))
Expected:
    120.0
Got:
    119.99999999999997
**********************************************************************
1 items had failures:
   1 of  29 in __main__.example_12
```


See #8847 for more details.


---

Comment by mhansen created at 2010-06-07 08:58:14

I don't think that #8847 was supposed to fix this.  #8847 was to make it so that we get 120.0 instead of 119.99999999999997 on Linux.  Cygwin has always given 119.9999...


---

Comment by kcrisman created at 2011-08-02 02:31:10

Somewhat miraculously, this passes tests on a recent build of mine on XP.  Perhaps due to using mpmath now or something?


---

Comment by kcrisman created at 2011-08-19 14:18:11

Changing priority from critical to major.


---

Comment by kcrisman created at 2011-08-19 14:47:46

But this, once again, does _not_ pass when done by hand.  What is going on?


---

Comment by dimpase created at 2012-01-17 03:49:26

exactly the same problem also pops up on ARM running Ubuntu 11.10.


---

Comment by burcin created at 2012-02-13 11:10:09

Changing status from new to needs_review.


---

Comment by burcin created at 2012-02-13 11:10:09

#12449 contains a patch to fix. We should close this as a duplicate.


---

Comment by dimpase created at 2012-02-13 11:13:08

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-02-16 21:32:51

Resolution: duplicate
