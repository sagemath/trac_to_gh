# Issue 5191: coercion issue of tanh(2) into QQbar

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-06 00:20:10

Assignee: cwitty

CC:  zimmerma

This is a followup to #5023: Paul Zimmermann reports:

```
sage: a=tanh(2)
sage: a._algebraic_(QQbar)
...
TypeError: Unable to coerce e (<class 'sage.functions.constants.E'>) to Rational
```


Carl: If this is invalid just close the ticker as invalid.

Cheers,

Michael


---

Comment by cwitty created at 2009-02-06 03:26:20

QQbar(sinh(2)) fails with the above error message; I believe that sinh(2) is not algebraic, so the conversion must fail, although I suppose the error message could be nicer.

However, QQbar(sinh(log(2))) correctly returns 3/4, so the code does work.  Therefore, I'm marking this invalid.


---

Comment by cwitty created at 2009-02-06 03:26:20

Resolution: invalid
