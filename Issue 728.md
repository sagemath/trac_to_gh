# Issue 728: sage_inspect broken

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-09-21 13:38:10

Assignee: was

This is SAGE 2.8.5:


```
sage: A = random_matrix(ZZ,3,3)
sage: A.lll?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
 ... File "/usr/local/sage-2.8.1/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 252, in sage_getargspec
    args, varargs, varkw = inspect.getargs(func_obj.func_code)
UnboundLocalError: local variable 'func_obj' referenced before assignment
sage: e = 1
sage: e.additive_order?

  File "<stdin>", line 1, in <module>
 ... File "/usr/local/sage-2.8.1/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 252, in sage_getargspec
    args, varargs, varkw = inspect.getargs(func_obj.func_code)
UnboundLocalError: local variable 'func_obj' referenced before assignment
```



---

Comment by mhansen created at 2007-09-26 20:31:57

What platform do these errors occur on?

Both of the examples work fine for me on 64-bit Linux.


---

Comment by was created at 2007-10-04 18:44:20

Resolution: fixed


---

Comment by was created at 2007-10-04 18:44:20

I fixed this; it happened on os x.
