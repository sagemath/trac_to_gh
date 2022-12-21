# Issue 3371: bug in uniformiSer for p-adic rings

Issue created by migration from Trac.

Original creator: wuthrich

Original creation time: 2008-06-05 14:01:32

Assignee: malb


Uniformi Z er


```
sage : A = Zp(7,10)
sage : B.<t> = A.ext(x^2+7)
sage : B.uniformizer()
t + O(t^21)
```


versus Uniformi S er


```
sage : B.uniformiser()
6*t^2 + t^4 + O(t^22)
```


which is NOT a uniformiser.



---

Attachment


---

Comment by fwclarke created at 2008-06-05 17:14:50

The attached patch solves the problem [and also eliminates a stray tab].


---

Comment by craigcitro created at 2008-06-15 21:51:45

Changing keywords from "" to "editor_craigcitro".


---

Comment by craigcitro created at 2008-06-18 08:46:50

extra touch-ups


---

Attachment

I approve of the changes in this ticket.


---

Attachment

add a doctest


---

Comment by mabshoff created at 2008-06-23 07:06:40

Resolution: fixed


---

Comment by mabshoff created at 2008-06-23 07:06:40

Merged all three patches in Sage 3.0.4.alpha0
