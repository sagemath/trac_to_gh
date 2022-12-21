# Issue 1565: RealDoubleField documentation missing

Issue created by migration from Trac.

Original creator: phatsphere

Original creation time: 2007-12-19 10:50:37

Assignee: tba

Somewhere I read that missing documentation should be considered as a bug:
sage version 2.9

```
RealDoubleField?
```


```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/server4/sage_notebook/worksheets/phatsphere/0/code/11.py", line 4, in <module>
    print _support_.docstring("RealDoubleField", globals())
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/server/support.py", line 142, in docstring
    s += 'Definition:  %s\n'%sageinspect.sage_getdef(obj, obj_name)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 276, in sage_getdef
    spec = sage_getargspec(obj)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 249, in sage_getargspec
    return _sage_getargspec_cython(source)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 201, in _sage_getargspec_cython
    raise ValueError, "Could not parse cython argspec"
ValueError: Could not parse cython argspec
```



---

Comment by mabshoff created at 2007-12-19 11:04:24

I cannot reproduce this with either Sage 2.9.1.alpha1 compiled from source as well as 2.9 on sage.math:

```
mabshoff`@`sage:/tmp/Work-mabshoff/sage-2.9.1.alpha1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.9.1.alpha1, Release Date: 2007-12-18                |
| Type notebook() for the GUI, and license() for information.        |
sage: RealDoubleField?
Type:           builtin_function_or_method
Base Class:     <type 'builtin_function_or_method'>
String Form:    <built-in function RealDoubleField>
Namespace:      Interactive

sage: RealDoubleField??
Type:           builtin_function_or_method
Base Class:     <type 'builtin_function_or_method'>
String Form:    <built-in function RealDoubleField>
Namespace:      Interactive
Source:
def RealDoubleField():
    global _RDF
    return _RDF
sage:
Exiting SAGE (CPU time 0m0.02s, Wall time 0m38.13s).
mabshoff`@`sage:/tmp/Work-mabshoff/sage-2.9.1.alpha1$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.9, Release Date: 2007-12-16                         |
| Type notebook() for the GUI, and license() for information.        |
sage: RealDoubleField?
Type:           builtin_function_or_method
Base Class:     <type 'builtin_function_or_method'>
String Form:    <built-in function RealDoubleField>
Namespace:      Interactive

sage: RealDoubleField??
Type:           builtin_function_or_method
Base Class:     <type 'builtin_function_or_method'>
String Form:    <built-in function RealDoubleField>
Namespace:      Interactive
Source:
def RealDoubleField():
    global _RDF
    return _RDF
sage:
```


Cheers,

Michael


---

Comment by malb created at 2007-12-19 12:00:14

Replying to [comment:1 mabshoff]:
> I cannot reproduce this with either Sage 2.9.1.alpha1 compiled from source as well as 2.9 on sage.math:

```
sage: RealDoubleField?
Type:           builtin_function_or_method
Base Class:     <type 'builtin_function_or_method'>
String Form:    <built-in function RealDoubleField>
Namespace:      Interactive
```


Actually, you just reproduced it: There is no documentation.


---

Comment by mabshoff created at 2007-12-22 15:18:23

The patch for #1459 might also fix this issue.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-26 03:30:09

This wasn't fixed in 2.9.1.

Cheers,

Michael


---

Comment by gfurnish created at 2008-06-15 23:29:05

This is fixed as of 3.0.3.alpha2.  Please close


---

Comment by mabshoff created at 2008-06-16 19:05:30

Closed since it is fixed :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-16 19:05:30

Resolution: fixed
