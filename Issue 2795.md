# Issue 2795: [with patch,needs review] QuotientRing -> Magma

Issue created by migration from https://trac.sagemath.org/ticket/2795

Original creator: malb

Original creation time: 2008-04-04 11:21:03

Assignee: malb

Keywords: magma


```
sage: P.<x,y> = PolynomialRing(GF(2))
sage: Q = P.quotient(sage.rings.ideal.FieldIdeal(P))
sage: xbar, ybar = Q.gens()
sage: xbar._magma_() # optional requires magma
x
```



---

Attachment

Looks good to me.


---

Comment by mabshoff created at 2008-04-04 20:07:36

Resolution: fixed


---

Comment by mabshoff created at 2008-04-04 20:07:36

Merged in Sage 3.0.alpha1


---

Comment by was created at 2008-04-05 20:26:10

I'm changing this from closed -- positive review to "opened, negative review", since the given doctest doesn't even work if you *do* have Magma:


```
teragon:~ was$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: referee
sage: sage: P.<x,y> = PolynomialRing(GF(2))
sage:  sage: Q = P.quotient(sage.rings.ideal.FieldIdeal(P))
sage:  sage: xbar, ybar = Q.gens()
sage:  sage: xbar._magma_() 
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)
| SAGE Version sage-2.11, Release Date: 2008-03-30                   |
| Type notebook() for the GUI, and license() for information.        |
/Users/was/<ipython console> in <module>()

/Users/was/sage_object.pyx in sage.structure.sage_object.SageObject._magma_()

/Users/was/sage_object.pyx in sage.structure.sage_object.SageObject._interface_()

/Users/was/build/sage-2.10.4/local/lib/python2.5/site-packages/sage/interfaces/magma.py in __call__(self, x, gens)
    332             if isinstance(x, bool):
    333                 return Expect.__call__(self, str(x).lower())
--> 334             return Expect.__call__(self, x)
    335         return self.objgens(x, gens)
    336         

/Users/was/build/sage-2.10.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)
    736             return x
    737         if isinstance(x, basestring):
--> 738             return cls(self, x)
    739         try:
    740             return self._coerce_from_special_method(x)

/Users/was/build/sage-2.10.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __init__(self, parent, value, is_name)
   1005             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1006                 self._session_number = -1
-> 1007                 raise TypeError, x
   1008         self._session_number = parent._session_number
   1009 

<type 'exceptions.TypeError'>: Error evaluation Magma code.
IN:_sage_[1] := xbar;
OUT:
>> _sage_[1] := xbar;
                ^
User error: Identifier 'xbar' has not been declared or assigned
sage: 
```



---

Comment by was created at 2008-04-05 20:26:10

Changing status from closed to reopened.


---

Comment by was created at 2008-04-05 20:26:10

Resolution changed from fixed to 


---

Comment by was created at 2008-04-05 20:28:24

Never mind:

```
13:27 < wstein> Ah, I think I mistunderstood what the ticket is about.
13:27 < wstein> Oops.
13:27 < wstein> I'll change it back.
13:28 < wstein> The problem was that the ticket description was a little vague.
13:28 < wstein> Sorry
```



---

Comment by was created at 2008-04-05 20:28:24

Resolution: fixed
