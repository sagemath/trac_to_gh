# Issue 5158: [with patch, needs review] bug in symbolic factorial

Issue created by migration from Trac.

Original creator: whuss

Original creation time: 2009-02-02 13:52:16

Assignee: whuss


```
sage: factorial(x)^2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

...

TypeError: unable to make sense of Maxima expression 'x!^2' in Sage
```


The attached patch fixes this.

Cheers,

Wilfried


---

Attachment


---

Comment by cwitty created at 2009-02-05 06:54:58

Code looks good; doctests pass.

Positive review.


---

Comment by mabshoff created at 2009-02-05 11:09:52

Resolution: fixed


---

Comment by mabshoff created at 2009-02-05 11:09:52

Merged in Sage 3.3.alpha6.

Cheers,

Michael
