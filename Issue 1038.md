# Issue 1038: bad interaction between numpy and in-place operations

Issue created by migration from https://trac.sagemath.org/ticket/1038

Original creator: cwitty

Original creation time: 2007-10-31 02:55:14

Assignee: somebody

The problem was reported in this thread: http://groups.google.com/group/sage-support/browse_thread/thread/96a5f3d336285146#

Here's the test case:

```
import numpy as npy
# With sage.rings.integer.Integer:
x = npy.array([1])
print x
  # [1]
npy.dot(x, npy.array([0]))
print x
  # [0]
```


where we see that multiplying a matrix has modified its elements.

This is from Robert Bradshaw's arithmetic optimization that mutates normally-immutable values if no other references are held.  The optimization makes certain assumptions about the way the Python API is used that are true of normal Python bytecode and of Cython-generated code (with the appropriate command-line arguments, which we use); but these assumptions are not true of C extension code in general, and in particular are not followed by the C code in numpy.

See http://groups.google.com/group/sage-devel/browse_thread/thread/175e1796069fd33c#, where a discussion has just started on this topic.


---

Comment by mabshoff created at 2007-11-02 19:26:17

workaround applied to 2.8.11.rc2.


---

Comment by mabshoff created at 2007-11-02 19:26:17

Resolution: fixed
