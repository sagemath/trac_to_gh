# Issue 6555: Twisted produces deprecation warning about using md5 module in Python 2.6

Issue created by migration from https://trac.sagemath.org/ticket/6555

Original creator: jason

Original creation time: 2009-07-18 19:27:35

Assignee: boothby

When I start up the notebook in 4.1, I get:


```
sage: notebook()
The notebook files are stored in: /home/grout/.sage//sage_notebook
**************************************************
*                                                *
* Open your web browser to http://localhost:8000 *
*                                                *
**************************************************
/home/grout/sage/local/lib/python2.6/site-packages/twisted/persisted/sob.py:12: DeprecationWarning: the md5 module is deprecated; use hashlib instead
  import os, md5, sys
```



It looks like this was fixed a while ago in twisted: http://twistedmatrix.com/trac/ticket/2763




---

Comment by jason created at 2009-07-18 19:30:32

It also appears that there is other work for them to be compatible with Python 2.6: http://twistedmatrix.com/trac/query?status=new&status=assigned&status=reopened&milestone=Python-2.6


---

Comment by mhansen created at 2009-11-14 08:50:01

This was fixed by #6676.


---

Comment by mhansen created at 2009-11-14 08:50:01

Resolution: duplicate
