# Issue 6907: implicit_plot reports deprecation warning

Issue created by migration from https://trac.sagemath.org/ticket/6907

Original creator: john_perry

Original creation time: 2009-09-09 02:42:38

Assignee: was

Keywords: implicit_plot

In sage 4.1.1, a call to implicit_plot() draws a perfectly fine graph, but also pops up a warning,

```
/usr/local/share/sage-4.1.1/local/lib/python2.6/site-packages/sage/plot/\
plot.py:2876: DeprecationWarning: Substitution using function-call
syntax and unnamed arguments is deprecated and will be removed from a
future release of Sage; you can use named arguments instead, like
EXPR(x=..., y=...)
  k, _ = adapt_to_callable([f], 2)
```



---

Comment by jason created at 2010-01-20 07:16:43

Changing status from new to needs_info.


---

Comment by jason created at 2010-01-20 07:16:43

Can you give us the command you used?  It's likely that the command you used is deprecated, which means that it still works, but will be removed in a future version of Sage, so you should get used to calling implicit_plot differently.


---

Comment by john_perry created at 2010-01-20 14:04:40

Replying to [comment:1 jason]:
> Can you give us the command you used?

At the time, every implicit_plot() command was doing this for me.

To be honest I had forgotten about this. It looks like it was an internal command that hadn't yet been brought up to the new format, because it works fine now. The ticket should be closed.


---

Comment by john_perry created at 2010-01-20 14:05:50

Replying to [comment:2 john_perry]:
> ...it works fine now. The ticket should be closed.

That's weird. I'm still using 4.1.1 and not getting the problem. I'm sorry; I can't reproduce it now.


---

Comment by jason created at 2010-01-20 14:07:36

Resolution: invalid


---

Comment by jason created at 2010-01-20 14:07:36

Closing per request.  If this comes up again, let us know.
