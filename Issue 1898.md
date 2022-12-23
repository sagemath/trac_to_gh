# Issue 1898: Sage 2.10: numerical doctest failure for polynomial_element.pyx on Linux/Itanium

Issue created by migration from https://trac.sagemath.org/ticket/1898

Original creator: mabshoff

Original creation time: 2008-01-23 21:15:57

Assignee: mabshoff


```
sage -t  devel/sage-main/sage/rings/polynomial/
polynomial_element.pyx**********************************************************************
File "polynomial_element.pyx", line 2669:
    sage: p.roots(ring=CIF)
Expected:
    [([-1.4142135623730952 .. -1.4142135623730949], 1),
([1.4142135623730949 ..
1.4142135623730952], 1), ([-1.2146389322441827 .. -1.2146389322441821]
- [0.1414250525823937... .. 0.1414250525823939...]*I, 2),
([-0.141425052582393... .. -0.1414250525823937...] +
[1.2146389322441821 .. 1.2146389322441827]*I, 2),
([0.141425052582393... .. 0.141425052582393...] -
[1.2146389322441821 .. 1.2146389322441827]*I, 2),
([1.2146389322441821 .. 1.2146389322441827] + [0.14142505258239376 ..
0.14142505258239399]*I, 2)]
Got:
    [([-1.4142135623730952 .. -1.4142135623730949], 1),
([1.4142135623730949 ..
1.4142135623730952], 1), ([-1.2146389322441827 .. -1.2146389322441821]
- [0.14142505258239371 .. 0.14142505258239397]*I, 2),
([-0.14142505258239397 .. -0.14142505258239376] +
[1.2146389322441821 .. 1.2146389322441829]*I, 2),
([0.14142505258239373 .. 0.14142505258239394] - [1.2146389322441821 ..
1.2146389322441829]*I, 2), ([1.2146389322441821 .. 1.2146389322441827]
+ [0.14142505258239376 .. 0.14142505258239399]*I, 2)]
**********************************************************************
```



---

Attachment


---

Attachment

apply the other patch then this one.


---

Comment by mabshoff created at 2008-01-24 20:48:03

Kate confirmed in https://groups.google.com/group/sage-support/t/d489d89ec68b6706 that William's patch now fixes it.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-24 20:48:19

Resolution: fixed


---

Comment by mabshoff created at 2008-01-24 20:48:19

Merged in Sage 2.10.1.alpha2
