# Issue 1345: I is sometimes wrapped in SymbolicConstant, sometimes not

Issue created by migration from https://trac.sagemath.org/ticket/1345

Original creator: cwitty

Original creation time: 2007-11-30 22:20:45

Assignee: mhansen

This behavior seems strange:

```
 sage: foo = I+I
 sage: foo._operands
 [I, I]
 sage: [type(i) for i in foo._operands]
 [<class 'sage.calculus.calculus.SymbolicConstant'>,
  <class 'sage.functions.constants.I_class'>]
```

And here's another strange thing (probably the same bug):

```
 sage: is_SymbolicExpression(SR(I))
 False
```



---

Attachment


---

Comment by mhansen created at 2007-11-30 22:56:53

Changing status from new to assigned.


---

Comment by mhansen created at 2007-11-30 23:03:32

This should be applied after #847.


---

Comment by cwitty created at 2007-12-01 02:05:13

The code looks good and the doctests in the affected files pass.  I approve.


---

Comment by mabshoff created at 2007-12-01 11:14:47

Merged in 2.8.15.alpha0.


---

Comment by mabshoff created at 2007-12-01 11:14:47

Resolution: fixed
