# Issue 2195: Givaro-related crash in finite fields

Issue created by migration from https://trac.sagemath.org/ticket/2195

Original creator: cwitty

Original creation time: 2008-02-17 18:57:35

Assignee: somebody

John Cremona reported this crash:

```
sage:  E=EllipticCurve(GF(5),[1,1])
sage:  E1=E.base_extend(GF(125,'a'))
sage:  E2=E1.base_extend(GF(125^2,'b'))

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------ 
```


I got a backtrace for the crash, which looks like this:

```
Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0xb7dfb8c0 (LWP 15819)]
0xb5443782 in
__pyx_f_4sage_5rings_19finite_field_givaro_25FiniteField_givaroElement__add_c_impl
(__pyx_v_self=0x9e10d74, __pyx_v_right=0x9e10f7c)
    at /home/cwitty/sage/local//include/givaro/givgfq.inl:292
292     { _GIVARO_GFQ_ADD(r, a, b, GFqDom<TT>::_qm1,
GFqDom<TT>::_plus1) ; return r; }
(gdb) bt
#0  0xb5443782 in
__pyx_f_4sage_5rings_19finite_field_givaro_25FiniteField_givaroElement__add_c_impl
(__pyx_v_self=0x9e10d74, __pyx_v_right=0x9e10f7c)
    at /home/cwitty/sage/local//include/givaro/givgfq.inl:292
#1  0xb71eac7f in
__pyx_pf_4sage_9structure_7element_13ModuleElement___add__ (
    __pyx_v_left=0x9e10d74, __pyx_v_right=0x9e10f7c)
    at sage/structure/element.c:15976
#2  0x0805ce33 in binary_op1 (v=0x9e10d74, w=0xbfb53d64, op_slot=0)
    at Objects/abstract.c:398
#3  0x0805d310 in PyNumber_Add (v=0x9e10d74, w=0x9e10f7c)
    at Objects/abstract.c:638 
```




---

Comment by mabshoff created at 2008-02-17 19:07:07

Note that on sage.math the crash does not happen, instead we get an exception thrown by python complaining about:

```
sage: E=EllipticCurve(GF(5),[1,1])
sage: E1=E.base_extend(GF(125,'a'))
sage: E2=E1.base_extend(GF(125^2,'b'))
---------------------------------------------------------------------------
<type 'exceptions.ArithmeticError'>       Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in base_extend(self, R)
    756         Elliptic Curve defined by y^2  = x^3 + x + (4*b^3+4*b^2+4*b+3) over Finite Field in b of size 5^4
    757         """
--> 758         return constructor.EllipticCurve([R(a) for a in self.a_invariants()])
    759
    760     def base_ring(self):

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/constructor.py in EllipticCurve(x, y)
    159
    160     elif isinstance(x[0], rings.FiniteFieldElement) or rings.is_IntegerMod(x[0]):
--> 161         return ell_finite_field.EllipticCurve_finite_field(x, y)
    162
    163     else:

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py in __init__(self, x, y)
     73             raise TypeError
     74
---> 75         EllipticCurve_field.__init__(self, ainvs)
     76
     77         self._point_class = ell_point.EllipticCurvePoint_finite_field

/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in __init__(self, ainvs, extra)
    135         if self.discriminant() == 0:
    136             raise ArithmeticError, \
--> 137                   "Invariants %s define a singular curve."%ainvs
    138         PP = projective_space.ProjectiveSpace(2, K, names='xyz');
    139         x, y, z = PP.coordinate_ring().gens()

<type 'exceptions.ArithmeticError'>: Invariants [0, 0, 0, 0, 0] define a singular curve.
```

I ran the same code under valgrind and there are no leads from that end. It is probably some bug that is only triggered with certain compilers.

Cheers,

Michael


---

Attachment

I've attached a valgrind record from my laptop.  (Actually, this is only the beginning of the valgrind record... I cut out the memory leak reports at the end.)

I wonder if it could be a 32-bit vs. 64-bit issue?  My laptop is 32-bit.


---

Comment by cremona created at 2008-02-17 20:24:48

Replying to [comment:2 cwitty]:
> I've attached a valgrind record from my laptop.  (Actually, this is only the beginning of the valgrind record... I cut out the memory leak reports at the end.)
> 
> I wonder if it could be a 32-bit vs. 64-bit issue?  My laptop is 32-bit.

I'm pretty sure that my original report was from a 32-bit machine.


---

Comment by wdj created at 2008-03-01 13:04:00

I think these are related bugs:


```
sage: version()
'SAGE Version 2.10.3.alpha0, Release Date: 2008-02-25'

sage: FF.<z> = GF(3^2,"z")
sage: b = GF(3,"zz").random_element()
sage: FF(b)
2
```

This works fine. Now try a bigger field:

```
sage: FF.<z> = GF(13^9,"z")
sage: b = GF(13**3,"zz").random_element()
sage: FF(b)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

...

<type 'exceptions.TypeError'>: unable to coerce element to an integer
no coercion defined
```

Unless my brain cells are mis-firing, GF(13**3) is a subfield of GF(13**9).

Here is the smallest example I found:

```
sage: FF.<z> = GF(5^8,"z")
sage: b = GF(5^4,"zz").random_element()
sage: FF(b)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)
....
```


(If you replace 5**8 -> 5**6 and 5**4 -> 5**3, it works okay.)

Also:

```
sage: FF.<z> = GF(5^6,"z")
sage: b = GF(5^3,"zz")(0); b; FF(b)
0
2*z^3 + 4*z^2 + 4*z
sage: b = GF(5^3,"zz")(1); b; FF(b)
1
2*z^3 + 4*z^2 + 4*z
```

It doesn't give a traceback for some reason, though it is clearly wrong.


---

Comment by mabshoff created at 2008-03-15 02:28:33

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-03-15 02:43:52

I ran this under 2.10.4.alpha0 with the updated givaro.spkg from #2525 and the valgrind log is clean. I guess time will tell if the problem is gone when cwitty will hopefully test this in the morning on a 32 bit setup.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-16 01:47:39

Changing component from basic arithmetic to givaro.


---

Comment by mabshoff created at 2008-03-16 01:47:39

Changing assignee from somebody to cpernet.


---

Comment by mabshoff created at 2008-03-16 01:47:39

This is still a problem with the updated Givaro.spkg from #2524. Assigning to Clement so he can hopefully hunt this down.

Cheers,

Michael


---

Comment by wjp created at 2008-04-14 20:52:23

After #2916 this should now always throw an exception instead of producing undefined behaviour. As wdj pointed out, casts between finite fields could give weird results.


---

Comment by mabshoff created at 2008-04-14 20:53:54

Resolution: fixed


---

Comment by mabshoff created at 2008-04-14 20:53:54

After applying wjp's patch from #2916 I get the following now:

```
sage: sage:  E=EllipticCurve(GF(5),[1,1])
sage: sage:  E1=E.base_extend(GF(125,'a'))
sage: sage:  E2=E1.base_extend(GF(125^2,'b'))
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-3.0.alpha5/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in base_extend(self, R)
    849         Elliptic Curve defined by y^2  = x^3 + x + (4*b^3+4*b^2+4*b+3) over Finite Field in b of size 5^4
    850         """
--> 851         return constructor.EllipticCurve([R(a) for a in self.a_invariants()])
    852
    853     def base_ring(self):

/scratch/mabshoff/release-cycle/sage-3.0.alpha5/finite_field_givaro.pyx in sage.rings.finite_field_givaro.FiniteField_givaro.__call__ (sage/rings/finite_field_givaro.cpp:3264)()

<type 'exceptions.TypeError'>: unable to coerce from a finite field other than the prime subfield
sage:
```

wjp confirmed that the issue is also fixed on his computer, so I am closing this.

John: once you have 3.0.alpha5 or final can you please check that this is also fixed for you or otherwise reopen?

Great work wjp.

Cheers,

Michael


---

Comment by cremona created at 2008-04-15 16:15:58

Replying to [comment:9 mabshoff]:
> After applying wjp's patch from #2916 I get the following now:
> {{{
> sage: sage:  E=EllipticCurve(GF(5),[1,1])
> sage: sage:  E1=E.base_extend(GF(125,'a'))
> sage: sage:  E2=E1.base_extend(GF(125^2,'b'))
> ---------------------------------------------------------------------------
> <type 'exceptions.TypeError'>             Traceback (most recent call last)
> 
> /scratch/mabshoff/release-cycle/sage-3.0.alpha5/<ipython console> in <module>()
> 
> /scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in base_extend(self, R)
>     849         Elliptic Curve defined by y^2  = x^3 + x + (4*b<sup>3+4*b</sup>2+4*b+3) over Finite Field in b of size 5^4
>     850         """
> --> 851         return constructor.EllipticCurve([R(a) for a in self.a_invariants()])
>     852
>     853     def base_ring(self):
> 
> /scratch/mabshoff/release-cycle/sage-3.0.alpha5/finite_field_givaro.pyx in sage.rings.finite_field_givaro.FiniteField_givaro.__call__ (sage/rings/finite_field_givaro.cpp:3264)()
> 
> <type 'exceptions.TypeError'>: unable to coerce from a finite field other than the prime subfield
> sage:
> }}}
> wjp confirmed that the issue is also fixed on his computer, so I am closing this.
> 
> John: once you have 3.0.alpha5 or final can you please check that this is also fixed for you or otherwise reopen?

OK, I'll do that in the next day or so (I'm at a conference with no evening internet access).

John

> 
> Great work wjp.
> 
> Cheers,
> 
> Michael


---

Comment by cremona created at 2008-04-16 12:16:54

The issue is resolved (in 3.0.alpha5) in the sense that it throws an exception rather than crashing.

To get anything better than that we will have to do serious work on the finite field implementationa (as in previous discussions which referred to the Cannon-Bosma-Steele paper describing how Magma does it).

John
