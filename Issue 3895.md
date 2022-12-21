# Issue 3895: sage-notebook-insecure ImportError

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-08-19 03:48:07

Assignee: boothby

If called from $SAGE_ROOT, everything goes fine, but if called from somewhere else:


```
rank4:sage-main rlmill$ ../../sage -inotebook
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.1, Release Date: 2008-08-17                       |
| Type notebook() for the GUI, and license() for information.        |
Please wait while the SAGE Notebook server starts...
Traceback (most recent call last):
  File "/Users/rlmill/sage-3.1.1/local/bin/sage-notebook-insecure", line 9, in <module>
    from sage.server.notebook.all import notebook
  File "/Users/rlmill/sage-3.1.1/devel/sage-main/sage/server/notebook/all.py", line 13, in <module>
    from notebook_object import notebook, inotebook
  File "/Users/rlmill/sage-3.1.1/devel/sage-main/sage/server/notebook/notebook_object.py", line 19, in <module>
    import notebook as _notebook
  File "/Users/rlmill/sage-3.1.1/devel/sage-main/sage/server/notebook/notebook.py", line 22, in <module>
    from   sage.structure.sage_object import SageObject, load
ImportError: No module named sage_object
rank4:sage-main rlmill$ cd ../..
rank4:sage-3.1.1 rlmill$ ./sage -inotebook
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.1, Release Date: 2008-08-17                       |
| Type notebook() for the GUI, and license() for information.        |
Please wait while the SAGE Notebook server starts...
...
The notebook files are stored in: /Users/rlmill/.sage//sage_notebook
**************************************************
*                                                *
* Open your web browser to http://localhost:8000 *
*                                                *
**************************************************
<goes swimmingly>
```



---

Comment by malb created at 2009-01-25 19:01:07

Changing status from new to assigned.


---

Comment by malb created at 2009-01-25 19:01:07

Changing assignee from boothby to malb.


---

Comment by malb created at 2009-08-25 19:25:09

This is fixed (at least) in 4.1.1.


---

Comment by malb created at 2009-08-25 19:25:09

Resolution: fixed
