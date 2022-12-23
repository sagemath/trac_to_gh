# Issue 6518: [with patch, needs review] doctest script uses deprecated signature for showwarning

Issue created by migration from https://trac.sagemath.org/ticket/6518

Original creator: burcin

Original creation time: 2009-07-12 12:18:31

Assignee: tbd

I got this while doctesting a patch with 4.1:


```
sage -t  "devel/sage-s/sage/symbolic/expression_conversions.py"
/home/burcin/sage/sage-4.1/local/lib/python/site-packages/sage/misc/misc.py:1901: DeprecationWarning: functions overriding warnings.showwarning() must support the 'line' argument
  warn(message, DeprecationWarning, stacklevel=3)
```


Apparently showwarning got a new argument in Python 2.6, as stated here:

http://docs.python.org/library/warnings.html#showwarning/show

Attached patch fixes the `sage-doctest` script to use the new call signature. 


---

Attachment

patch for the scripts repository


---

Comment by mhansen created at 2009-07-13 20:14:57

Looks good to me.


---

Comment by mvngu created at 2009-07-17 09:28:43

Resolution: fixed
