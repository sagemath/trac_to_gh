# Issue 1833: [with patch; needs review] plot3d and parametric_plot3d can be very slow on some inputs

Issue created by migration from https://trac.sagemath.org/ticket/1833

Original creator: was

Original creation time: 2008-01-18 16:22:22

Assignee: was


```
sage: x,y = var('x,y')
sage: plot3d(x*y, (x,-1,1), (y,-1,1))
```

is fast, but 

```
sage: x,y = var('x,y')
sage: plot3d(x*y, (-1,1), (-1,1))
```

is shockingly slow (and similar remarks for parametric plots).   The attached patch fixes this problem. 

This also fixes trac #1737.


---

Comment by was created at 2008-01-18 16:22:30

Changing component from algebraic geometry to graphics.


---

Comment by was created at 2008-01-18 16:23:29

This patch also moves plot3d_adaptive into plot3d (i.e., as an option), and deprecates globally exposing plot3d_adaptive.   This is natural to do in the context of this patch.


---

Attachment


---

Comment by mhansen created at 2008-01-21 03:32:32

Looks good to me.


---

Comment by mabshoff created at 2008-01-21 04:13:28

Merged in Sage 2.10.1.alpha1


---

Comment by mabshoff created at 2008-01-21 04:13:28

Resolution: fixed
