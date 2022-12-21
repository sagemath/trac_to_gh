# Issue 3632: [with patch, needs review] small bug in p-adic heights

Issue created by migration from Trac.

Original creator: wuthrich

Original creation time: 2008-07-10 13:11:05

Assignee: was


```
sage: E = EllipticCurve([37,0])
sage: E.padic_regulator(5)
```


gives a Assertion Error.

The included patch corrects this.


---

Attachment


---

Comment by dmharvey created at 2008-07-10 23:27:48

I hate to do this.... it's obviously a perfectly good patch.... but the documentation needs to be updated too, and the loop in the doctests needs to test the m = 1 case, and somewhere you need to add a doctest showing the correct behaviour for the example you gave in the ticket description!


---

Attachment

Ok. I added an additional patch (applied after the first) with some docstring. I hope that it is enough.


---

Attachment

hi, I've added yet a third patch, with minor changes to your patch, plus cleaning up some existing nearby doctests which didn't make sense to me. Assuming you are happy with these changes, I think this patch is good to go.

(all three patches should be applied)


---

Comment by wuthrich created at 2008-07-14 09:39:02

Yop, that is fine with me. I guess I am allowed to change the 'summary'.


---

Comment by mabshoff created at 2008-07-16 01:33:52

Resolution: fixed


---

Comment by mabshoff created at 2008-07-16 01:33:52

Merged in Sage 3.0.6.alpha0
