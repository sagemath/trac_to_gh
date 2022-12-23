# Issue 1736: sturm_bound() not working on spaces of cusp forms

Issue created by migration from https://trac.sagemath.org/ticket/1736

Original creator: AlexGhitza

Original creation time: 2008-01-09 12:40:32

Assignee: AlexGhitza

This was part of #1612: the sturm_bound() method seems not to work


```
sage: S37=CuspForms(37,2)
sage: S37.sturm_bound()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/opt/sage-2.9.3/devel/sage-alex/sage/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/modular/modform/space.py in sturm_bound(self, M)
    919         if M != None:
    920             raise NotImplementedError
--> 921         if self.__sturm_bound == None:
    922             # the +1 below is because O(q^prec) has precision prec.
    923             self.__sturm_bound = int(\

<type 'exceptions.AttributeError'>: 'CuspidalSubmodule_g0_Q' object has no attribute '_ModularFormsSpace__sturm_bound'
```




---

Attachment


---

Comment by AlexGhitza created at 2008-01-09 13:02:13

Trivial fix; in fact, I changed the method sturm_bound() so that it uses the function sturm_bound(level, weight) from dims.py.


---

Comment by was created at 2008-01-16 17:58:15

Looks good to me.


---

Comment by mabshoff created at 2008-01-16 18:02:22

Merged in Sage 2.10.alpha4


---

Comment by mabshoff created at 2008-01-16 18:02:22

Resolution: fixed
