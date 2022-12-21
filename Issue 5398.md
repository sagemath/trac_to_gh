# Issue 5398: clone is broken in Sage 3.4.alpha0 due to non-7 bit ASCII characters in docstrings

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-27 21:32:52

Assignee: cwitty

CC:  cremona

John Cremona reported in http://groups.google.com/group/sage-devel/browse_thread/thread/dc34f1b1f5fc4251

```
From my newly built 3.4.alpha0 I made a clone but it will not run, 
complaining about things like this: 

SyntaxError: Non-ASCII character '\xc3' in file 
/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages
/sage/combinat/sloane_functions.py 

on line 6381, but no encoding declared; see 
http://www.python.org/peps/pep-0263.html for details 
(sloane_functions.py, line 6380) 

That one is Mobius, spelled Mo"bius (with an o-umlaut character). 
And before that I had a problem with Gro"bner in interfaces/singular.py.
 
Is this somehow caused by the ReST/Sphinx stuff?  It is hard to 
review  patches when clones don't run... 

John 
```



---

Attachment


---

Comment by mabshoff created at 2009-03-01 01:55:37

Changing assignee from cwitty to mabshoff.


---

Comment by mabshoff created at 2009-03-01 01:55:37

Changing status from new to assigned.


---

Comment by justin created at 2009-03-01 01:59:54

The patch is excellent!


---

Comment by mabshoff created at 2009-03-01 02:05:12

Resolution: fixed


---

Comment by mabshoff created at 2009-03-01 02:05:12

Merged in Sage 3.4.rc0.

Cheers,

Michael
