# Issue 9126: Symbolic arguments() method

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-06-03 05:11:07

Assignee: burcin

Right now, the following works:

```
sage: a=(x+y)
sage: a.arguments()
(x, y)
```

However, we deprecated the following a long time ago:

```
sage: a(1,2)
/Users/grout/sage/local/lib/python2.6/site-packages/IPython/iplib.py:2073:
DeprecationWarning: Substitution using function-call syntax and unnamed
arguments is deprecated and will be removed from a future release of
Sage; you can use named arguments instead, like EXPR(x=..., y=...)
   exec code_obj in self.user_global_ns, self.user_ns
3
```

I propose that a.arguments() should return a deprecation warning:

```
sage: a.arguments()
/Users/grout/sage/local/lib/python2.6/site-packages/IPython/iplib.py:2073:
DeprecationWarning: (Since Sage version 4.4.2) symbolic expressions do
not have default callable arguments.  Please use the variables() method
   exec code_obj in self.user_global_ns, self.user_ns
(x, y)
```

This will impact other things as well, since apparently things have been
using .arguments() when they should have been using .variables().  I can
post a patch for this.  Here, I'm just calling for comment, especially
from those that think this will mess everything up in some way.

Note that callable functions will still have sensible return values:

```
sage: f(x,y)=x+y
sage: f.arguments()
(x, y) 
```



---

Attachment


---

Comment by jason created at 2010-06-03 05:13:00

I've attached a rough patch which needs work to finish fixing the ramifications of this change.


---

Comment by jason created at 2010-06-03 05:13:00

Changing status from new to needs_work.


---

Comment by mkoeppe created at 2021-09-06 05:39:53

dup of #32227, can close


---

Comment by mkoeppe created at 2021-09-06 05:39:53

Changing status from needs_work to needs_review.


---

Comment by mjo created at 2021-11-20 21:19:40

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2021-11-20 23:57:15

Resolution: invalid
