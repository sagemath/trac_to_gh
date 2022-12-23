# Issue 5518: Improve efficiency of multiplcative_order() for number field elements

Issue created by migration from https://trac.sagemath.org/ticket/5518

Original creator: cremona

Original creation time: 2009-03-14 18:53:55

Assignee: was

Keywords: number field multiplicative order

The attached patch vastly improves the efficiency of the multiplicative_order() function for number field elements.  Before, this example:

```
 sage: x = polygen(QQ)
            sage: K.<a>=NumberField(x^40 - x^20 + 4)
            sage: u = 1/4*a^30 + 1/4*a^10 + 1/2
            sage: u.multiplicative_order()
            6
            sage: a.multiplicative_order()
            +Infinity
```

would have required raising a to the power 2**40 (I'm serious).  Now it just works (fast).


---

Attachment


---

Comment by cremona created at 2009-03-14 20:35:19

Changing priority from major to minor.


---

Comment by fwclarke created at 2009-03-17 20:22:30

This is excellent.  A great speed up, and it gives the right answer!  

I would suggest adding the doctest

```
sage: K.<a, b> = NumberField([x^2 + x + 1, x^2 - 3])
sage: z = (a - 1)*b/3
sage: z.multiplicative_order()
12
```

because sage-3.4 says the order is `+infinity`.


---

Comment by fwclarke created at 2009-03-17 20:22:30

Changing priority from minor to major.


---

Attachment

I added a small patch with the additional doctest as suggested.


---

Comment by mabshoff created at 2009-03-25 09:24:51

Resolution: fixed


---

Comment by mabshoff created at 2009-03-25 09:24:51

Merged both patches in Sage 3.4.1.alpha0.

Cheers,

Michael
