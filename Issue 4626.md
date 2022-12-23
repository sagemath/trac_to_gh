# Issue 4626: error in bessel_J(0,0)

Issue created by migration from https://trac.sagemath.org/ticket/4626

Original creator: zimmerma

Original creation time: 2008-11-26 16:44:35

Assignee: somebody


```
sage: bessel_J(0,0)    
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (284, 0))

---------------------------------------------------------------------------
PariError                                 Traceback (most recent call last)

/users/cacao/zimmerma/.sage/temp/achille.loria.fr/2662/_users_cacao_zimmerma__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/usr/local/sage-3.1.4/sage/local/lib/python2.5/site-packages/sage/functions/special.pyc in bessel_J(nu, z, algorithm, prec)
    522             K = C
    523         K = z.parent()
--> 524         return K(pari(nu).besselj(z, precision=prec))
    525     elif algorithm=="scipy":
    526         if prec != 53:

/usr/local/sage-3.1.4/sage/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:34447)()
   7864 
   7865 
-> 7866 
   7867 
   7868 

PariError:  (8)
```

The other non-default algorithms (maxima and scipy) return the correct answer 1.0000...


---

Comment by rlm created at 2009-01-22 05:53:13

The problem is somewhere between the Pari interface and Pari itself:

```
sage: R = RealField(53)
sage: n = R(0)
sage: z = R(0)
sage: pari(n).besselj(z, precision=53)
BOOM
```



---

Comment by rlm created at 2009-01-22 06:02:51

Aha!:

```
sage: pari('besselj(0,0)')
1.00000000000000
sage: pari('besselj(0.0,0.0)')
---------------------------------------------------------------------------
PariError                                 Traceback (most recent call last)

/Users/rlmill/<ipython console> in <module>()

/Users/rlmill/sage-3.2.2/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38645)()

PariError:  (8)
sage: pari('besselj(0,0.0)')
1.00000000000000
```


The problem is that Pari is expecting an integer:

```
sage: R = RealField(53)
sage: n = Integer(0)
sage: z = R(0)
sage: pari(n).besselj(z, precision=53)
1.00000000000000
```


I'll post a patch once my 3.3.alpha0 builds...


---

Comment by rlm created at 2009-01-22 06:06:22

Changing status from new to assigned.


---

Comment by rlm created at 2009-01-22 06:06:22

Changing assignee from somebody to rlm.


---

Comment by ddrake created at 2009-01-22 07:23:00

Positive review here. It applies cleanly to my 3.3.alpha0 tree and bessel_J(0, 0) works now.


---

Comment by zimmerma created at 2009-01-22 08:43:35

I've reported the problem upstream to Pari.

The patch needs more work since non-integer arguments are no longer allowed:

```
sage: bessel_J(0.1,0)
...
TypeError: Attempt to coerce non-integral RealNumber to Integer
```

This used to work before the patch:

```
sage: bessel_J(0.1,0.1)
0.777264368097005
```



---

Comment by ddrake created at 2009-01-22 09:15:14

Replying to [comment:6 zimmerma]:

Good catch -- thanks for undoing my positive review. Anyone working on this should probably be aware of #3426, which involves other Pari/Bessel problems.


---

Comment by zimmerma created at 2009-01-22 09:17:50

Also, if the doctest did pass with the initial patch, the new one should add a test for say bessel_J(0.1,0.1),
and make clear in the documentation which argument types are allowed.


---

Attachment

Fixed.


---

Comment by zimmerma created at 2009-01-22 21:32:32

The new patch is ok for me.


---

Comment by mabshoff created at 2009-01-23 10:02:13

Resolution: fixed


---

Comment by mabshoff created at 2009-01-23 10:02:13

Merged in Sage 3.3.alpha0

Cheers,

Michael
