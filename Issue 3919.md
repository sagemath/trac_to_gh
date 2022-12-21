# Issue 3919: Selector - do not inset a lone button

Issue created by migration from Trac.

Original creator: itolkov

Original creation time: 2008-08-21 00:20:15

Assignee: itolkov

If there is only one button in a selector, such as

```
r=["Reload"]
```

it is not pressed in, as are selected buttons when there is more than one.


---

Attachment


---

Comment by was created at 2008-08-21 00:49:59

PERFECT!


---

Comment by mabshoff created at 2008-08-21 21:57:26

Resolution: fixed


---

Comment by mabshoff created at 2008-08-21 21:57:26

Merged in Sage 3.1.2.alpha0
