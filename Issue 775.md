# Issue 775: filename misreported in tracebacks for .pyx files

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2007-10-01 21:04:24

Assignee: was

In tracebacks the filenames get misreported. As you see below, sometimes the filename gets prefixed by the current directory.

```
sage: os.system("pwd")
/tmp
0
sage: sage.misc.sageinspect.sage_getfile(matrix)
'/usr/local/sage/default/local/lib/python2.5/site-packages/sage/matrix/constructor.py'
sage: M=matrix([This is the Trac macro *1,1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1,1-macro))
sage: M*M
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/tmp/<ipython console> in <module>()

/tmp/element.pyx in element.Matrix.__mul__()

/tmp/element.pyx in element.Matrix._matrix_times_matrix_c()

<type 'exceptions.TypeError'>: incompatible dimensions
```



---

Comment by mabshoff created at 2007-10-02 00:41:10

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-10-02 00:41:10

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-10-02 00:41:31

Changing assignee from mabshoff to was.


---

Comment by mabshoff created at 2007-10-02 00:41:31

Changing status from assigned to new.


---

Comment by rlm created at 2009-01-23 02:53:34

Resolution: invalid


---

Comment by rlm created at 2009-01-23 02:53:34

This no longer happens. The traceback could be more useful, but the paths pointed to are now correct.
