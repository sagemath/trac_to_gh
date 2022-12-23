# Issue 2509: [with patch, needs review] showstopper in xgcd(f, 0)

Issue created by migration from https://trac.sagemath.org/ticket/2509

Original creator: ncalexan

Original creation time: 2008-03-13 20:25:55

Assignee: somebody

CC:  ncalexan

This is an absolute showstopper, but it's a little tricky to hit the right piece of code.


```
sage: x = GF(37**4, 'a')['x'].gen()
sage: x.xgcd
<built-in method xgcd of Polynomial_generic_dense_field object at 0xca59298>
sage: x.xgcd(0)
(1, 0, x)
sage: 0.xgcd(x)
(x, 0, 1)
sage: x.xgcd(x)
(x, 0, 1)
```


Observe that the first `xgcd` has the outputs in the wrong order.  This cost me hours of debugging the Cantor reduction algorithms in the hyperelliptic curves code.


---

Attachment


---

Comment by dmharvey created at 2008-03-13 20:55:49

I am reviewing this right now and expect to give a positive review as soon as the doctests are finished...


---

Comment by dmharvey created at 2008-03-13 22:16:04

Well, there are two doctest failures. One was easy to fix (a broken doctest in `polynomial_integer_dense_ntl.pyx`), I have attached a patch.

The other one is really weird. In `sage/structure/factorization.py`, we have the following doctest:


```
        We create a polynomial over the real double field and factor it:                       
            sage: x = polygen(RDF, 'x')                                                        
            sage: F = factor(-2*x^2 - 1); F                                                    
            (-2.0) * (1.0*x^2 - 1.82173070032e-16*x + 0.5) * (1.0*x^2 + 0.5)    # 32-bit       
            (-2.0) * (1.0*x^2 - 2.22044604925e-16*x + 0.5) * (1.0*x^2 + 0.5)    # 64-bit       
```


The 32-bit example gets a little changed with Nick's patch.

BUT... look more closely at that doctest. WTF? 2 + 2 = 2?


---

Attachment


---

Comment by ncalexan created at 2008-03-13 22:39:10

The fact that another doctest broke shows that the doctest is not testing the correct code... or there is another bug there.  However, on closer inspection, everything looks okay to me.

The bug you are reporting about numerical noise is well-known and there is a fix that will be applied in 2.10.4.  It's independent of this patch.

Thanks!
Nick


---

Comment by dmharvey created at 2008-03-14 00:28:28

nick: yes ok I agree. The stuff in `polynomial_integer_dense` is happening because it's a special case that's falling back on generic code. (Possibly it shouldn't be doing that, but that's for another day.)

I'll take your word for it that the factoring thing is unrelated.

Thumbs up for this patch.


---

Comment by mabshoff created at 2008-03-14 01:46:37

Resolution: fixed


---

Comment by mabshoff created at 2008-03-14 01:46:37

Both patches merged in Sage 2.10.4.alpha0
