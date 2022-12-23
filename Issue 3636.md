# Issue 3636: Text control, no label

Issue created by migration from https://trac.sagemath.org/ticket/3636

Original creator: itolkov

Original creation time: 2008-07-10 21:07:58

Assignee: itolkov

Allows adding text among the controls:


```
@interact
def _(t1=text_control("Factors an integer."), n="1"):
    print factor(Integer(n))
```


Additionally, the way labels are displayed is changed. If an empty label ('') is specified, the input block is aligned with the left edge of the table, rather than the rest of the controls. This is useful for controls that should not have a label, such as text. However, if label=' ' (space) is set, the input is aligned with the rest of the inputs with no label showing.



---

Attachment


---

Comment by jason created at 2008-07-21 22:21:26

Can you please put an example of using the control in the documentation for interact()?  The above example would work great.


---

Comment by mabshoff created at 2008-07-21 22:29:47

Please remember to assign a milestone.

Cheers,

Michael


---

Attachment


---

Comment by itolkov created at 2008-07-22 20:03:06

Done.


---

Comment by mabshoff created at 2008-07-30 23:40:46

Merged both patches in Sage 3.1.alpha0


---

Comment by mabshoff created at 2008-07-30 23:40:46

Resolution: fixed
