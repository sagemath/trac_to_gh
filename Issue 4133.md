# Issue 4133: sage.math - sage 3.1.2.rc4 doctest failure in interfaces/maxima.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-09-16 05:26:28

Assignee: mabshoff


```
********************************************************************** 
File "/home/was/build/sage-3.1.2.rc4/tmp/maxima.py", line 791: 
    sage: 'gcd' in t 
Expected: 
    True 
Got: 
    False 
********************************************************************** 
File "/home/was/build/sage-3.1.2.rc4/tmp/maxima.py", line 1849: 
    sage: 'gcd' in m.trait_names() 
Expected: 
    True 
Got: 
    False 
********************************************************************** 
```



---

Comment by mhansen created at 2008-09-17 00:43:16

This is due to a stale maxima_commandlist_cache.sobj in the DOT_SAGE directory.  It was fixed by doing

rm ~/.sage/maxima_commandlist_cache.sobj


---

Comment by mabshoff created at 2008-09-17 01:02:37

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-09-17 01:02:37

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc5/maxima-5.16.2.p0.spkg

fixes the problem.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-17 01:17:59

Merged in Sage 3.1.2.rc5


---

Comment by mabshoff created at 2008-09-17 01:17:59

Resolution: fixed
