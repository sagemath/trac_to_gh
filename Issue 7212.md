# Issue 7212: [with patch, needs review] steenrod algebra multiplication bug

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-10-14 19:12:43

Assignee: tbd

From sage-support:

```
I have Sage 4.1.1 install on a server, and I run the following code, 
which outputs the following error: 
sage: A3=SteenrodAlgebra(3) 
sage: A3.P(36,6)*A3.P(27,9,81) 
--------------------------------------------------------------------------- 
KeyError                                  Traceback (most recent call 
last) 
/home/user_bob/<ipython console> in <module>() 
/usr/local/sage-4.1.1/local/lib/python2.6/site-packages/sage/structure/ 
element.so in sage.structure.element.RingElement.__mul__ (sage/ 
structure/element.c:9956)() 
/usr/local/sage-4.1.1/local/lib/python2.6/site-packages/sage/structure/ 
element.so in sage.structure.element.RingElement._mul_ (sage/structure/ 
element.c:10021)() 
/usr/local/sage-4.1.1/local/lib/python2.6/site-packages/sage/algebras/ 
steenrod_algebra_element.pyc in _mul_(self, other) 
    925                         new_dict = milnor_multiplication 
(mono1, mono2) 
    926                     else: 
--> 927                         new_dict = milnor_multiplication_odd 
(mono1, mono2, p=p) 
    928                     for new_mono in new_dict: 
    929                         if result.has_key(new_mono): 
/usr/local/sage-4.1.1/local/lib/python2.6/site-packages/sage/algebras/ 
steenrod_milnor_multiplication_odd.pyc in milnor_multiplication_odd 
(m1, m2, p) 
    225                     t = tuple(diagonal[:i+1]) 
    226                     if result.has_key((e,t)): 
--> 227                         result[(e,t)] = F(coeff + result[t]) 
    228                     else: 
    229                         result[(e,t)] = F(coeff) 
KeyError: (26, 8, 86) 
```

This is because of a simple bug: instead of `result[t]`, it should be `result[(e,t)]`.



---

Comment by jason created at 2009-10-14 21:20:35

Changing status from new to needs_review.


---

Attachment


---

Comment by was created at 2009-10-14 21:50:04

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-15 08:52:13

Resolution: fixed
