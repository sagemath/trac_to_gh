# Issue 1141: Number Field elements arithmetic speed

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2007-11-10 20:55:02

Assignee: somebody

This patch just makes a few minor adjustments which gain a bit of speed with number field elements.  It's barely worth talking about for absolute fields, but its quite nice for relative number fields.

The main work of the patch is to place a pointer to the defining polynomial into the number field element.  This possibly introduces more maintenance, but the alternative is to move the number field parent class to cython.

original:

```
sage: L.<a> = CyclotomicField(3).extension(x^3 - 2)
sage: timeit a^6
100 loops, best of 3: 2.89 ms per loop
sage: K.<a> = NumberField(x^3-2*x^2+12)
sage: timeit a^4
10000 loops, best of 3: 44.3 Âµs per loop
sage: O.<a,b> = EquationOrder([x^2+1, x^2+2])
sage: timeit a*b
1000 loops, best of 3: 770 Âµs per loop
```


patched:

```
sage: L.<a> = CyclotomicField(3).extension(x^3 - 2)
sage: timeit a^6
10000 loops, best of 3: 92.7 Âµs per loop
sage: K.<a> = NumberField(x^3-2*x^2+12)
sage: timeit a^4
10000 loops, best of 3: 30.6 Âµs per loop
sage: O.<a,b> = EquationOrder([x^2+1, x^2+2])
sage: timeit a*b
100000 loops, best of 3: 19 Âµs per loop
```




---

Comment by jbmohler created at 2007-11-10 20:55:19

the patch!


---

Attachment


---

Comment by jbmohler created at 2007-11-10 20:55:54

Changing type from defect to enhancement.


---

Comment by cwitty created at 2007-12-01 03:23:40

I applied the patch, verified the promised performance improvements, and checked that doctests in sage/rings/numberfield/* still pass.

I do think that moving the number field parent class to cython may be a better strategy long-term, if only to avoid the extra memory footprint of two more pointers per number field element (although that's probably a silly thing to worry about, given how big number field elements are anyway).  But regardless, this patch should be applied for now.

I approve.


---

Comment by mabshoff created at 2007-12-01 11:38:07

Merged in 2.8.15.alpha0


---

Comment by mabshoff created at 2007-12-01 11:39:35

Merged in 2.8.15.alpha0


---

Comment by mabshoff created at 2007-12-02 07:30:50

Resolution: fixed


---

Comment by mabshoff created at 2007-12-02 07:30:50

Merged in 2.8.15.alpha0 - 3rd time's the charm!
