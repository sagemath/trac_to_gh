# Issue 4098: "T1 =  M1.hecke_operator(13^9)" blows up on 32 bit builds

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-09-10 20:55:18

Assignee: craigcitro

Raouf reports in http://groups.google.com/group/sage-support/browse_thread/thread/cf22177234f605a4

```
varro:~/sage-3.1.2.rc1 mabshoff$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.2.rc1, Release Date: 2008-09-08                   |
| Type notebook() for the GUI, and license() for information.        |
sage: M1 =  ModularSymbols(21,2)
sage: T1 =  M1.hecke_operator(13^8)
sage: trace1=T1.trace()
sage: print trace1
2651076189
sage: M1 =  ModularSymbols(21,2) 
sage: T1 =  M1.hecke_operator(13^9) 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/mabshoff/sage-3.1.2.rc1/<ipython console> in <module>()

/Users/mabshoff/sage-3.1.2.rc1/local/lib/python2.5/site-packages/sage/modular/hecke/module.py in hecke_operator(self, n)
    858            int n -- an integer at least 1.
    859         """
--> 860         return self.hecke_algebra().hecke_operator(n)
    861 
    862     def T(self, n):

/Users/mabshoff/sage-3.1.2.rc1/local/lib/python2.5/site-packages/sage/modular/hecke/algebra.py in hecke_operator(self, n)
    184             pass
    185         n = int(n)
--> 186         T = hecke_operator.HeckeOperator(self, n)
    187         self.__hecke_operator[n] = T 
    188         return T

/Users/mabshoff/sage-3.1.2.rc1/local/lib/python2.5/site-packages/sage/modular/hecke/hecke_operator.py in __init__(self, parent, n)
    360         HeckeAlgebraElement.__init__(self, parent)
    361         if not isinstance(n, int):
--> 362             raise TypeError, "n must be an int"
    363         self.__n = n
    364 
```



---

Attachment


---

Comment by mabshoff created at 2008-09-10 21:22:43

Nice and quick fix. Doctests pass on 32 bits, positive review.

Cheers,

Michael


---

Comment by cremona created at 2008-09-10 21:25:04

You got there before me but I agree.


---

Comment by mabshoff created at 2008-09-10 21:25:54

Resolution: fixed


---

Comment by mabshoff created at 2008-09-10 21:25:54

Merged in Sage 3.1.2.rc2
