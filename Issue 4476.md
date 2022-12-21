# Issue 4476: [with patch, spkg; needs review] Update to Cython 0.10

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-11-09 06:00:17

Assignee: mabshoff

See http://trac.cython.org/cython_trac/query?group=component&milestone=0.10 (though this is by no means exhaustive). 

Most relevant for us are the optimizations, many bugfixes and the ability to use "cimport *" for types. 


---

Attachment


---

Comment by robertwb created at 2008-11-09 06:02:55

Spkg up at http://sage.math.washington.edu/home/robertwb/cython/cython-0.10.spkg

Sage builds and all tests pass.


---

Comment by mabshoff created at 2008-11-09 09:43:48

Spkg and patch look good to me. The is one tiny reviewer patch for the following failure:

```
sage -t -long devel/sage/sage/interfaces/gap.py             
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc0/devel/sage/sage/interfaces/gap.py", line 262:
    sage: g._next_var_name()
Expected:
    '$sage5'
Got:
    '$sage3'
**********************************************************************
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-11-09 09:46:48

Merged in Sage 3.2.rc0


---

Comment by mabshoff created at 2008-11-09 09:46:48

Resolution: fixed
