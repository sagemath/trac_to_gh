# Issue 4563: polar plot does not accept (t, 0, 2*pi) syntax for the interval

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-11-20 08:19:26

Assignee: was

CC:  mhansen

This does not work:


```
sage: polar_plot(x, (x, 0, 1))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/jason/<ipython console> in <module>()

TypeError: polar_plot() takes exactly 3 arguments (2 given)
```


But this does:


```
sage: polar_plot(x,0, 1)
```





---

Comment by jason created at 2008-11-20 08:19:46

Ccing mhansen since he is currently working on plotting code.


---

Attachment


---

Comment by robertwb created at 2009-01-23 04:26:03

Looks good to me. Just a touch of fuzz for against, 3.2.3, but it merged fine.


---

Comment by mabshoff created at 2009-01-23 08:34:36

Resolution: fixed


---

Comment by mabshoff created at 2009-01-23 08:34:36

Merged in Sage 3.3.alpha1
