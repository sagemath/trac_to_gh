# Issue 6405: Typesetting of imaginary 'I' in new Symbolics is not proper

Issue created by migration from Trac.

Original creator: gmhossain

Original creation time: 2009-06-25 14:30:01

CC:  robertwb

In new symbolics, imaginary 'I' is typeset as 'I' which is not "textbook style". This is a regression compared to Sage 3.4


```
sage: latex( exp(i*x))
e^{I \, x}
```


Lower case letter 'i' should be used in the typeset version.



---

Comment by burcin created at 2009-08-01 02:43:00

Complex I in new symbolics is nothing but a quadratic number field element.

Robert, any thoughts on how to handle this?


---

Comment by robertwb created at 2010-05-22 15:56:43

See #9017


---

Comment by burcin created at 2010-07-11 16:00:20

This was fixed by #9017. attachment:9017-latex-sqrt-neg1.patch:ticket:9017 changes a doctest in `sage.symbolic.pynac.pyx` to test this change.

I'm closing this as a duplicate.


---

Comment by burcin created at 2010-07-11 16:00:20

Resolution: duplicate
