# Issue 5368: plot3d is broken when variables not given

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-02-25 04:08:50

Assignee: was

CC:  wcauchois

This gives an infinite loop in the command line or notebook:

```
var('x,y')
plot3d(x*y^2 - sin(x), (-1,1), (-1,1))
```


Pretty bad!!


---

Comment by was created at 2009-02-25 23:03:07

This is (probably) because fast_float isn't being used for some weird reason:

```
sage: var('x,y')
(x, y)
sage: plot3d(x*y^2 - sin(x), (-1,1), (-1,1))
^CControl-C pressed.  Interrupting Maxima. Please wait a few seconds...
Exception exceptions.KeyboardInterrupt: KeyboardInterrupt() in  ignored
^C^CControl-C pressed.  Interrupting Maxima. Please wait a few seconds...
^CControl-C pressed.  Interrupting Maxima. Please wait a few seconds...
^CControl-C pressed.  Interrupting Maxima. Please wait a few seconds...
```



---

Attachment

William's assessment was correct; the function was not being converted into a fast_float form because parametric_plot3d.adapt_to_callable was being invoked incorrectly. I tried to update the documentation of this function according to what I figured out about its workings, so that this mistake might be avoided in the future.


---

Comment by mabshoff created at 2009-03-01 05:23:50

No need to add a complete email address, the account name in trac is sufficient.

Cheers,

Michael


---

Attachment

Merged  trac_5368-rebased.patch in Sage 3.4.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-05 00:45:59

Resolution: fixed
