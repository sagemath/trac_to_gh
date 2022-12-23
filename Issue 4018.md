# Issue 4018: casting of non t_INT pari integers

Issue created by migration from https://trac.sagemath.org/ticket/4018

Original creator: robertwb

Original creation time: 2008-08-31 08:28:22

Assignee: robertwb


```
sage: t = pari(0*ZZ[x].0); t
 0

sage: ZZ(t)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/robertwb/<ipython console> in <module>()

/home/robertwb/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.__call__ (sage/rings/integer_ring.c:4902)()

/home/robertwb/integer.pyx in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:5812)()

/home/robertwb/gen.pyx in sage.libs.pari.gen.gen.__hex__ (sage/libs/pari/gen.c:5840)()

TypeError: gen must be of PARI type t_INT
```



---

Attachment


---

Comment by AlexGhitza created at 2008-09-01 10:33:22

Looks good to me (tested it against 3.1.1).


---

Comment by mabshoff created at 2008-09-01 13:00:44

Line 358 in the patch needs to be changed to 

```
sage: t = pari(0*ZZ[x].0 + 3)
```

With that change the doctests for integer.pyx actually pass :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-01 13:02:04

Resolution: fixed


---

Comment by mabshoff created at 2008-09-01 13:02:04

Merged in sage 3.1.2.alpha4
