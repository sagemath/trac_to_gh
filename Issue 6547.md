# Issue 6547: deprecate the use of all.py instead of __init__.py

Issue created by migration from https://trac.sagemath.org/ticket/6547

Original creator: malb

Original creation time: 2009-07-17 09:51:16

Assignee: cwitty

CC:  kini

For historical reasons, we are using `foo.all.py` instead of `foo.__init__.py`. This is not Pythonic and we should change that (gradually).

Also, the developer's guide needs an update reflecting this change:

http://www.sagemath.org/doc/developer/coding_in_python.html#creating-a-new-directory

This was discussed on [sage-devel]: http://groups.google.com/group/sage-devel/browse_thread/thread/1112fcc8345ecfd2


---

Comment by mhansen created at 2009-07-17 20:20:15

One thing that we need to watch out for is importing an object into `foo/__init__.py` with the same name as a module in `foo/`.  Something like:


```
mike@mike-laptop:~/src/test_init$ ls foo
bar.py  bar.pyc  __init__.py  __init__.pyc
mike@mike-laptop:~/src/test_init$ cat foo/__init__.py
from bar import bar
mike@mike-laptop:~/src/test_init$ cat foo/bar.py
bar = 200
```


Then, things like `foo.bar.bar` won't work.


---

Comment by mhansen created at 2009-10-01 04:57:57

A more specific objection:

Currently in Sage, we have


```
sage: type(sage.plot.plot)
<type 'module'>
sage: type(sage.plot.all.plot)
<type 'function'>
```


If we get rid of `all.py`, what should `sage.plot.plot` be?


---

Comment by malb created at 2009-10-01 07:24:17

`sage.plot.plot.plot` or wherever it is implemented? I don't see the problem.


---

Comment by mhansen created at 2009-10-01 07:37:49

If `plot` the function is imported in `sage/plot/__init__.py`, then `sage.plot.plot` will be the function.  If someone happens to import `sage/plot/plot.py`, then `sage.plot.plot` becomes the module and not the function.  I'm not convinced that this won't cause troubles.


---

Comment by malb created at 2009-10-01 09:34:28

To me the benefits of following the standard outweights the problems. But we should raise the issue on [sage-devel] and see what happens.


---

Comment by kini created at 2011-06-14 19:57:15

Any news here? I'm not sure I fully understand Mike's objection, but can't we treat this as a deprecation, i.e. tell people that the usage `sage.plot.all.whatever` is deprecated?


---

Comment by mkoeppe created at 2021-09-07 07:47:32

After the switch to using native namespace packages (#29705), we cannot use `__init__.py` any more to populate packages. The modularization effort will certainly require us to think what to do with the `sage....all` packages, but moving stuff to `__init__.py` won't be it. So I am proposing to close this ticket as outdated.


---

Comment by mkoeppe created at 2021-09-07 07:47:32

Changing status from new to needs_review.


---

Comment by klee created at 2021-11-15 12:09:16

I agree that the aim of this ticket is not compatible with the modularization effort.


---

Comment by klee created at 2021-11-15 12:09:16

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2021-11-20 23:57:15

Resolution: invalid
