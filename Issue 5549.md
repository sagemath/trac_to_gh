# Issue 5549: ?? help in notebook is broken for functions defined in C

Issue created by migration from https://trac.sagemath.org/ticket/5549

Original creator: cwitty

Original creation time: 2009-03-17 14:44:44

Assignee: tba

At the command line,

```
import scipy
scipy.sin??
```

falls back to just giving the docstring (like `scipy.sin?`), plus an additional notation that says `[source file open failed]`.  In the notebook, the same thing only gives 

```
No object scipy.sin
```

The notebook should fall back to ? help when ?? help fails, like the command line does.


---

Comment by kcrisman created at 2014-05-21 13:27:52

Confirmed.  This is reported "upstream" at [this issue](https://github.com/sagemath/sagenb/issues/207).


---

Comment by kcrisman created at 2014-08-06 03:47:58

Proposed easier solution is at [this pull request](https://github.com/sagemath/sagenb/pull/209).


---

Comment by embray created at 2018-08-10 09:37:11

FWIW this appears to be fixed.  I don't know since when, but it's probably been fixed in IPython for a while.  Indeed `??` now falls back on `?` if it can't get the source code of an object.


---

Comment by embray created at 2018-08-10 09:37:11

Resolution: worksforme
