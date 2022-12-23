# Issue 1038: bad interaction between numpy and in-place operations

archive/issues_001038.json:
```json
{
    "body": "Assignee: somebody\n\nThe problem was reported in this thread: http://groups.google.com/group/sage-support/browse_thread/thread/96a5f3d336285146#\n\nHere's the test case:\n\n```\nimport numpy as npy\n# With sage.rings.integer.Integer:\nx = npy.array([1])\nprint x\n  # [1]\nnpy.dot(x, npy.array([0]))\nprint x\n  # [0]\n```\n\n\nwhere we see that multiplying a matrix has modified its elements.\n\nThis is from Robert Bradshaw's arithmetic optimization that mutates normally-immutable values if no other references are held.  The optimization makes certain assumptions about the way the Python API is used that are true of normal Python bytecode and of Cython-generated code (with the appropriate command-line arguments, which we use); but these assumptions are not true of C extension code in general, and in particular are not followed by the C code in numpy.\n\nSee http://groups.google.com/group/sage-devel/browse_thread/thread/175e1796069fd33c#, where a discussion has just started on this topic.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1038\n\n",
    "created_at": "2007-10-31T02:55:14Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "bad interaction between numpy and in-place operations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1038",
    "user": "cwitty"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/1038





---

archive/issue_comments_006336.json:
```json
{
    "body": "workaround applied to 2.8.11.rc2.",
    "created_at": "2007-11-02T19:26:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1038#issuecomment-6336",
    "user": "mabshoff"
}
```

workaround applied to 2.8.11.rc2.



---

archive/issue_comments_006337.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-02T19:26:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1038#issuecomment-6337",
    "user": "mabshoff"
}
```

Resolution: fixed
