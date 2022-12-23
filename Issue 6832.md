# Issue 6832: [with patch, needs review] bug in inverse_mod for number field elements

Issue created by migration from https://trac.sagemath.org/ticket/6832

Original creator: mtaranes

Original creation time: 2009-08-27 12:50:26

Assignee: somebody

CC:  cremona

Keywords: number fields

In the documentation for inverse_mod for (integral) elements of a number field says that the input may be "an ideal, or an element or list of elements generating a nonzero ideal" which is not true right now.


```
sage: k.<a> = NumberField(x^2 + 23)
sage: d = a + 3
sage: d.inverse_mod(a)
Traceback (most recent call last)
...
AttributeError: ...
```


I fixed that and added an example in the doctest (patch based on 4.1.1) 


---

Attachment


---

Comment by mvngu created at 2009-09-23 04:08:35

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 09:48:08

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
