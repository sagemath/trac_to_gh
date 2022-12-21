# Issue 2163: .show?? pops up the graphics item as well as the help page

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-02-14 23:00:03

Assignee: was

At the command line:


```
sage: a=plot(x^2,(x,-1,1))
sage: a.show??
sage: a.show?
```


In either of the last two commands, the plot pops up on my Ubuntu 7.10 box (as well as the help).



---

Comment by mabshoff created at 2008-02-14 23:03:20

Changing component from algebraic geometry to graphics.


---

Comment by mhansen created at 2008-02-15 01:51:20

Changing status from new to assigned.


---

Comment by mhansen created at 2008-02-15 01:51:20

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2008-02-15 01:51:20

This is due to the following:


```
String Form:    <bound method Graphics.show of >
```


whereas after show_default(False), we get:


```
String Form:    <bound method Graphics.show of Graphics object consisting of 1 graphics primitive>
```



---

Comment by mhansen created at 2008-02-15 02:11:23

This can be fixed if we can tell IPython to set show_default(False) when doing things like repr(a.show)


---

Comment by mhansen created at 2008-09-03 00:54:09

Resolution: fixed


---

Comment by mhansen created at 2008-09-03 00:54:23

Resolution changed from fixed to 


---

Comment by mhansen created at 2008-09-03 00:54:23

Changing status from closed to reopened.


---

Attachment

I had already fixed some problems caused by removing the 'nodoctest' at the top before realizing there's no good way to test the function which I added.

The thing which addresses this ticket is the last hunk at the bottom of the patch.


---

Comment by jason created at 2008-12-05 08:49:01

This fixes the problem.  Tests pass in interpreter.py as well (thanks for fixing all those too!)

Positive review.


---

Comment by mabshoff created at 2008-12-05 09:37:33

Resolution: fixed


---

Comment by mabshoff created at 2008-12-05 09:37:33

Merged in Sage 3.2.2.alpha0
