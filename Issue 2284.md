# Issue 2284: CallableSymbolicExpression._latex_() has some odd behavior

Issue created by migration from Trac.

Original creator: moretti

Original creation time: 2008-02-24 00:01:19

Assignee: was


```
sage: f(x,y,z) = 2*x + 3*z^3 - sin(y)
sage: f._latex_()
'\\left((x, y, z) \\right)\\ {\\mapsto}\\ {3 {z}^{3} } - \\sin \\left( y
\\right) + {2 x}'
```

(note the extra parens on the left of the arrow)


---

Comment by moretti created at 2008-02-24 00:07:00

Also note that _latex_() does not TeX the variable names on the left:
{{{ 	
sage: f(omega) = omega
sage: f._latex_()
'omega \\ {\\mapsto}\\ {2 \\omega}'
}}}

'omega' should be '\\omega'.


---

Comment by moretti created at 2008-02-24 00:35:13

latex fix


---

Attachment

Okay, submitted a fix; need a review.


---

Comment by mhansen created at 2008-02-27 23:06:11

Applies cleanly to 2.10.3.alpha0 and passes tests for me.


---

Comment by mabshoff created at 2008-02-28 06:50:17

Resolution: fixed


---

Comment by mabshoff created at 2008-02-28 06:50:17

Merged in Sage 2.10.3.rc0
