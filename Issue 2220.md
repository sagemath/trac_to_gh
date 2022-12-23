# Issue 2220: irreducibility testing in relative extensions seems to be messed up

Issue created by migration from https://trac.sagemath.org/ticket/2220

Original creator: jason

Original creation time: 2008-02-20 03:54:04

Assignee: was

CC:  ncalexan ccitro mjo

See http://groups.google.com/group/sage-devel/browse_thread/thread/32fe12de12d5f6a5/c91753b5e65fe7b9#c91753b5e65fe7b9



```
> Is the following output for b.gens() correct?

> sage: NumberField([x,x^2-3],'a')
> Number Field in a0 with defining polynomial x over its base field
> sage: b=NumberField([x,x^2-3],'a')
> sage: b.gens()
> (0, 0)

> To contrast:

> sage: c=NumberField([x^2-3, x^2-2],'a')
> sage: c.gens()
> (a0, a1)

> Also, this blows up:

> sage: c=NumberField([x^2-3, x],'a')

The problem here is that x is triggering a an error in the
irreducibility test, which is a little bizarre since of course x is
irreducible.

So the real issue is: why is x allowed to determine an absolute number
field (base Q) but not a relative one?  My guess is that this is a
side-effect of the differing code being used to test irreducibility in
the two cases,

Personally, I think that trivial extensions should be allowed and
treated just as non-trivial ones.  I have recently had to define
extensions of the ring ZZ, and find this awkward:

sage: R=ZZ.extension(x^2+5,'a')
sage: R.gens()
[1, a]
sage: S=ZZ.extension(x+5,'b')
sage: S.gens()
[1]

In the latter case I need S to remember the polynomial used to
generaite it and would expect its gens() to include (in this case) -5.

On the same topic, R and S above have no defining_polynomial() method.
 I'll try to fix that if it looks easy. 
```




---

Comment by cremona created at 2008-02-20 09:20:12

As was pointed out (by was I think), the gens() for an extension of ZZ are ZZ-module generators, n in number for an extension of degree n.  For example:


```
sage: R.<a>=ZZ.extension(x^3-2)
sage: R
Order in Number Field in a with defining polynomial x^3 - 2
sage: R.gens()
[1, a, a^2]
```


This is quite clear in the docstring "returns module generators of this order" and so requires no action.

For examples such as this, I said that the following would be convenient to access more directly:

```
sage: R.fraction_field().gen()
a
sage: R.fraction_field().defining_polynomial()
x^3 - 2
```


However, objects of the type or R here <class 'sage.rings.number_field.order.AbsoluteOrder'>  might be created in more complicated ways so that they do not have one natural defining polynomial or (ring) generator.  In fact one immediately finds this:

```
sage: R.ring_generators()
[a]
```

and the docstring for ring_generators() gives an example for which more than one generator is needed (remember that not every order is of the form Z[a] for some a), so it makes no sense at all, in general, to define methods gen() or ring_gen() or defining_polynomial() for general orders.

All this leaves from the original post is to work out why the specific polynomial x is not handled consistently.  The rest is perfect as it is.  Well done to the authors (was and robertb) for doing a good job, well documented!


---

Comment by mhansen created at 2009-06-04 21:32:51

Note that this part now works:


```
sage: c=NumberField([x^2-3, x],'a')
sage: 
sage: c.gens()
(a0, 0)
```



---

Comment by davidloeffler created at 2009-07-20 19:57:57

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-20 19:57:57

Changing assignee from was to davidloeffler.


---

Comment by fwclarke created at 2011-03-01 12:08:32

The other part works too now:


```
sage: b = NumberField([x, x^2 - 3], 'a')
sage: b.gens()
(0, a1)
```



---

Attachment

Add doctest for a trivial extension


---

Comment by mjo created at 2011-12-17 20:38:29

Changing status from new to needs_review.


---

Comment by mjo created at 2011-12-17 20:38:29

I'm pretty sure this is fixed, so I've added a doctest.


---

Comment by cpauderis created at 2011-12-17 21:27:29

Changing status from needs_review to positive_review.


---

Comment by cpauderis created at 2011-12-17 21:27:29

This appears to work exactly as advertised.  Positive review.


---

Comment by jdemeyer created at 2011-12-22 13:06:33

Resolution: fixed
