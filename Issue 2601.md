# Issue 2601: problem with change_ring

Issue created by migration from https://trac.sagemath.org/ticket/2601

Original creator: mhampton

Original creation time: 2008-03-19 19:14:33

Assignee: malb

Keywords: ideal, change_ring

The following produces errors:


```
sage: testR.<a,b,c> = PolynomialRing(QQ,3)
sage: id_ringA = ideal([a^2-b,b^2-c,c^2-a])
sage: id_ringB = ideal(id_ringA.gens()).change_ring(PolynomialRing(QQ,'c,b,a')) 
```


although this does not:

```
sage: testR.<a,b,c> = PolynomialRing(QQ,3)
sage: id_ringA = ideal([a^2-b,b^2-c,c^2-a])
sage: id_ringB = ideal(id_ringA.gens()).change_ring(PolynomialRing(QQ,'c,a,b')) 
```



---

Comment by AlexGhitza created at 2008-03-20 01:41:11

I don't know what's happening, but maybe the following simpler example will help someone figure it out:


```
sage: R.<a,b,c> = PolynomialRing(QQ, 3)
sage: P = PolynomialRing(QQ, 'c, b, a')
sage: Q = PolynomialRing(QQ, 'c, a, b')
sage: Q(a)
a
sage: P(a)
...
<type 'exceptions.IndexError'>: list assignment index out of range
```


Note also that out of the 6 permutations of 'a, b, c', only 'c, b, a' and 'b, c, a' throw this exception; the other 4 seem to work properly.


---

Comment by AlexGhitza created at 2008-03-28 00:50:32

I believe the problem is in _mpoly_dict_recursive() in multi_polynomial.pyx:


```
sage: R.<a,b,c> = PolynomialRing(QQ, 3)
sage: a._mpoly_dict_recursive(['c', 'b', 'a'])
---------------------------------------------------------------------------
<type 'exceptions.IndexError'>            Traceback (most recent call last)

/root/<ipython console> in <module>()

/root/multi_polynomial.pyx in sage.rings.polynomial.multi_polynomial.MPolynomial._mpoly_dict_recursive()

<type 'exceptions.IndexError'>: list assignment index out of range
```


This should return {(0, 0, 1): 1}.  I'm having trouble understanding exactly how the code works so I'm giving up on trying to fix this.  Someone familiar with the code should be able to do this properly, and much faster than me.


---

Attachment


---

Comment by AlexGhitza created at 2009-01-27 06:14:59

Looks good to me.


---

Comment by mabshoff created at 2009-01-28 12:59:46

Merged in Sage 3.3.alpha3


---

Comment by mabshoff created at 2009-01-28 12:59:46

Resolution: fixed
