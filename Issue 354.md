# Issue 354: Introspection broken for SageX'd files from notebook.

Issue created by migration from https://trac.sagemath.org/ticket/354

Original creator: boothby

Original creation time: 2007-04-22 18:23:52

Assignee: boothby

Keywords: introspection

Offending code:


```
F = ZZ.quo(2*ZZ)
R.<x> = F['x']
p = x^2-1
p.root_field?
```


Traceback:


```
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/home/boothby/sage_notebook/worksheets/hw4/code/4.py", line 4, in &lt;module&gt;
    print _support_.docstring("p.root_field", globals())
  File "/home/boothby/sage/local/lib/python2.5/site-packages/sage/server/support.py", line 131, in docstring
    s += 'Definition:  %s\n'%sageinspect.sage_getdef(obj, obj_name)
  File "/home/boothby/sage/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 264, in sage_getdef
    spec = sage_getargspec(obj)
  File "/home/boothby/sage/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 246, in sage_getargspec
    return _sage_getargspec_sagex(source)
  File "/home/boothby/sage/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 200, in _sage_getargspec_sagex
    raise ValueError, "Could not parse sagex argspec"
ValueError: Could not parse sagex argspec
```


This is using a freshly upgraded SAGE.  Cannot reproduce on the public notebook.


---

Comment by boothby created at 2007-04-22 18:25:02

Introspection works fine from the commandline.


---

Comment by ncalexan created at 2007-06-27 05:54:13

Changing assignee from boothby to ncalexan.


---

Comment by ncalexan created at 2007-06-27 05:54:13

Given the flux of the new notebook, and the fact that this works well for me, I'm going to close this.  If it can be duplicated with newer code, I'll address the issue.


---

Comment by mabshoff created at 2007-08-29 15:21:25

Works for me:

```
[mabshoff@m940 sage-2.8.3.alpha2]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.3.alpha2, Release Date: 2007-08-29                |
| Type notebook() for the GUI, and license() for information.        |
sage: F = ZZ.quo(2*ZZ)
sage: R.<x> = F['x']
sage: p = x^2-1
sage: p.root_field?
sage:
sage:   
```


Retagged for 2.9.

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-31 22:09:50

The problem is in the notebook, not the console application. So this is not resolved and should be fixed.

Cheers,

Michael


---

Comment by was created at 2007-09-05 04:39:20

Resolution: fixed
